"""Core dynamical model of the Metacognitive Balance perspective.

Formalizes Han & Gu (2025), "Toward Metacognitive Balance: A Framework for
Cognitive and Social Functioning in Schizophrenia" (IntechOpen,
doi:10.5772/intechopen.1012821) as a coupled control system.

State
-----
L(t)      : log-odds of the threat / self-referential hypothesis h2 vs benign h1.
            belief b = sigmoid(L) in [0, 1].
alpha(t)  : self-weight in [0, 1]. alpha_self = alpha, alpha_context = 1 - alpha.

Dynamics
--------
    dL/dt     = alpha * lambda_S(L) + (1 - alpha) * lambda_C(t) - kappa * L + P_ext(t)
    dalpha/dt = -gamma * (alpha - alpha0(t)) + u(t)

with
    lambda_S(L) = aS + r * sigmoid(L)     # internal affect + ruminative self-amplification
    lambda_C(t) = aC + xi(t)              # external cues (disconfirming) + OU ambiguity noise
    u(t)                                  # pivot control law, with hysteresis (see PivotLatch)
    P_ext(t)                              # optional external evidence perturbation

Everything is deliberately minimal so the qualitative behaviour can be read off
the equations. See ``experiments.py`` for the studies and ``metrics.py`` for the
paper's two "minimal indices".
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Tuple, Dict

import numpy as np

__all__ = ["Params", "sigmoid", "confidence", "simulate", "PivotLatch"]

DEFAULT_SEED = 20250701


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    """Logistic squashing function mapping log-odds to a probability in [0, 1]."""
    return 1.0 / (1.0 + np.exp(-x))


def confidence(L: np.ndarray | float) -> np.ndarray | float:
    """Metacognitive confidence: distance of the belief from equipoise, in [0, 1]."""
    return np.abs(2.0 * sigmoid(L) - 1.0)


@dataclass
class Params:
    """Model parameters. Field names mirror the symbols used in the manuscript.

    The four control parameters that Han & Gu (2025, p. 9) enumerate map onto
    these fields: confidence gain -> kappa (leak); ambiguity threshold -> how
    long |L| stays small under sigC noise; cue weighting -> alpha; switch
    sensitivity -> p_gain / thresholds.
    """
    # --- evidence channels ---
    aS: float = 0.20        # baseline threat-leaning internal affect
    r: float = 1.20         # ruminative self-amplification gain ("finding the cause within")
    aC: float = -0.70       # external cues disconfirm the threat reading on average
    sigC: float = 0.50      # ambiguity: amplitude of external (OU) noise
    theta_ou: float = 1.0   # OU mean-reversion rate (noise time-correlation)

    # --- integration / regulation ---
    kappa: float = 0.30     # leak toward equipoise (controlled re-appraisal / calibration)
    gamma: float = 0.50     # CRS homeostatic return rate to the set-point
    alpha0: float = 0.50    # personality set-point (baseline tilt); Jung intro/extraversion

    # --- pivot control (with hysteresis) ---
    pivot: bool = False
    p_gain: float = 0.90    # pivot strength (switch sensitivity)
    theta_H_on: float = 0.78    # Pivot A engages when belief b exceeds this
    theta_H_off: float = 0.62   # ... and disengages only when b falls below this (hysteresis)
    theta_L: float = 0.25       # Pivot B considered when alpha below this
    erratic_on: float = 0.9     # Pivot B engages when |db/dt| exceeds this
    erratic_off: float = 0.4    # ... and disengages when |db/dt| falls below this


class PivotLatch:
    """Stateful, hysteretic pivot trigger.

    A bare threshold makes the pivot *chatter* (rapidly toggle) near the
    boundary. Separate on/off thresholds (Schmitt-trigger style) latch the pivot
    so it engages decisively and releases only once the imbalance has clearly
    resolved -- a more clinically realistic "commit to the rebalancing move".
    """

    def __init__(self, P: Params):
        self.P = P
        self.A_on = False   # Pivot A (over-internalization -> context-work)
        self.B_on = False   # Pivot B (over-externalization -> self-work)

    def __call__(self, b: float, dL: float, alpha: float, db: float) -> float:
        P = self.P
        # --- Pivot A: over-internalization -> push knob toward context (alpha down) ---
        if self.A_on:
            if b < P.theta_H_off:
                self.A_on = False
        elif b > P.theta_H_on and dL > 0:
            self.A_on = True

        # --- Pivot B: over-externalization -> push knob toward self (alpha up) ---
        if self.B_on:
            if abs(db) < P.erratic_off:
                self.B_on = False
        elif alpha < P.theta_L and abs(db) > P.erratic_on:
            self.B_on = True

        if self.A_on:
            return -P.p_gain
        if self.B_on:
            return +P.p_gain
        return 0.0


def simulate(
    P: Params,
    T: float = 40.0,
    dt: float = 0.02,
    L0: float = 0.0,
    alpha_init: Optional[float] = None,
    seed: int = DEFAULT_SEED,
    alpha0_fn: Optional[Callable[[float], float]] = None,
    perturb: Optional[Tuple[float, float, float]] = None,
) -> Dict[str, np.ndarray]:
    """Integrate the coupled system with the explicit Euler-Maruyama scheme.

    Parameters
    ----------
    P : Params
        Model parameters.
    T, dt : float
        Total time and step. Time is in the same abstract units as the
        30-180 s micro-cycle discussed by Han & Gu (2025, p. 9).
    L0 : float
        Initial log-odds (0.0 = equipoise).
    alpha_init : float, optional
        Initial self-weight. Defaults to ``P.alpha0`` (or ``alpha0_fn(0)``).
    seed : int
        RNG seed for the external ambiguity noise.
    alpha0_fn : callable, optional
        Time-varying set-point ``alpha0(t)``. Used to express a *scheduled*
        (sequential) policy, e.g. self-work first then context-work. When
        supplied it overrides the constant ``P.alpha0`` in the CRS equation.
    perturb : (t0, t1, mag), optional
        Adds a constant external-evidence rate ``mag`` to dL for ``t in [t0, t1]``
        -- a burst of (dis)confirming evidence used to probe recovery.

    Returns
    -------
    dict of np.ndarray with keys: t, L, alpha, b, conf, xi, u.
    """
    rng = np.random.default_rng(seed)
    n = int(round(T / dt))
    t = np.linspace(0.0, T, n)

    L = np.zeros(n)
    A = np.zeros(n)
    xi = np.zeros(n)
    U = np.zeros(n)

    set_point = (lambda _t: P.alpha0) if alpha0_fn is None else alpha0_fn
    L[0] = L0
    A[0] = set_point(0.0) if alpha_init is None else alpha_init

    latch = PivotLatch(P)
    prev_b = sigmoid(L[0])

    for k in range(n - 1):
        # Ornstein-Uhlenbeck ambiguity noise on the external channel
        xi[k + 1] = xi[k] - P.theta_ou * xi[k] * dt + P.sigC * np.sqrt(dt) * rng.standard_normal()

        lamS = P.aS + P.r * sigmoid(L[k])
        lamC = P.aC + xi[k]
        p_ext = 0.0
        if perturb is not None and perturb[0] <= t[k] < perturb[1]:
            p_ext = perturb[2]

        dL = A[k] * lamS + (1.0 - A[k]) * lamC - P.kappa * L[k] + p_ext

        b = sigmoid(L[k])
        db = (b - prev_b) / dt
        prev_b = b

        u = latch(b, dL, A[k], db) if P.pivot else 0.0
        U[k] = u

        dA = -P.gamma * (A[k] - set_point(t[k])) + u

        L[k + 1] = L[k] + dL * dt
        A[k + 1] = float(np.clip(A[k] + dA * dt, 0.0, 1.0))

    return dict(t=t, L=L, alpha=A, b=sigmoid(L), conf=confidence(L), xi=xi, u=U)
