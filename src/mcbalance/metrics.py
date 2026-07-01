"""Quantitative indices for the metacognitive balance model.

Implements the two "minimal indices" that Han & Gu (2025, p. 6, Table 2)
recommend tracking -- confidence-outcome congruence and tolerance of ambiguity
-- plus two operational measures used to compare policies (corridor dwell-time
and post-perturbation recovery time). All functions are model-agnostic: they
take trajectories or Params and return plain numbers, so they can be reused on
any variant of the model.
"""
from __future__ import annotations

from dataclasses import replace
from typing import Dict, Tuple

import numpy as np

from .model import Params, simulate, sigmoid

__all__ = [
    "corridor_dwell_fraction",
    "recovery_time",
    "tolerance_of_ambiguity",
    "congruence_ensemble",
    "calibration_curve",
]


# --------------------------------------------------------------------------- #
# Corridor-based measures (used by the sequential-vs-balanced comparison)      #
# --------------------------------------------------------------------------- #
def corridor_dwell_fraction(b: np.ndarray, half_width: float = 0.25) -> float:
    """Fraction of time the belief stays inside the adaptive corridor.

    The corridor is the band ``|b - 0.5| <= half_width`` around equipoise.
    """
    return float(np.mean(np.abs(b - 0.5) <= half_width))


def recovery_time(
    t: np.ndarray, b: np.ndarray, t_perturb_end: float, half_width: float = 0.25
) -> float:
    """Time from the end of a perturbation until the belief re-enters the corridor.

    Returns the remaining horizon (a censored value) if it never recovers.
    """
    dt = t[1] - t[0]
    start = int(round(t_perturb_end / dt))
    inside = np.abs(b - 0.5) <= half_width
    for k in range(start, len(t)):
        if inside[k]:
            return float(t[k] - t_perturb_end)
    return float(t[-1] - t_perturb_end)  # censored: no recovery within horizon


# --------------------------------------------------------------------------- #
# Tolerance of ambiguity (minimal index #2)                                    #
# --------------------------------------------------------------------------- #
def tolerance_of_ambiguity(
    P: Params,
    n_trials: int = 200,
    T: float = 40.0,
    dt: float = 0.02,
    commit_conf: float = 0.6,
    ambiguous: Tuple[float, float, float] = (0.40, -0.40, 0.70),
    base_seed: int = 1000,
) -> float:
    """Mean time a person can stay with an ambiguous stimulus before committing.

    A genuinely ambiguous event is created by making the internal and external
    evidence roughly cancel (``ambiguous = (aS, aC, sigC)``) with elevated noise.
    Tolerance is the average time until confidence first exceeds ``commit_conf``;
    if the person never commits, the full horizon ``T`` is used. Higher = more
    tolerant (better able to "stay with not-knowing").
    """
    aS, aC, sigC = ambiguous
    Pa = replace(P, aS=aS, aC=aC, sigC=sigC)
    times = np.empty(n_trials)
    for i in range(n_trials):
        r = simulate(Pa, T=T, dt=dt, seed=base_seed + i)
        crossed = np.flatnonzero(r["conf"] >= commit_conf)
        times[i] = r["t"][crossed[0]] if crossed.size else T
    return float(times.mean())


# --------------------------------------------------------------------------- #
# Confidence-outcome congruence (minimal index #1) via a truth-conditioned     #
# ensemble and a calibration (reliability) analysis                            #
# --------------------------------------------------------------------------- #
def _params_for_truth(P: Params, threat_true: bool) -> Params:
    """Evidence that genuinely points to threat vs benign (agent does not know)."""
    if threat_true:
        return replace(P, aS=0.85, aC=-0.05)   # net evidence favors threat
    return replace(P, aS=0.20, aC=-0.80)        # net evidence favors benign


def congruence_ensemble(
    P: Params,
    n_trials: int = 400,
    T: float = 40.0,
    dt: float = 0.02,
    base_seed: int = 5000,
) -> Dict[str, np.ndarray]:
    """Run a truth-balanced ensemble and collect (confidence, correct) pairs.

    On each trial the (hidden) ground truth is threat or benign with equal
    probability. The agent commits at the final time to the more probable
    reading. We record its confidence and whether the commitment was correct.
    Well-calibrated metacognition => confidence tracks accuracy.
    """
    rng = np.random.default_rng(base_seed)
    conf = np.empty(n_trials)
    correct = np.empty(n_trials, dtype=bool)
    for i in range(n_trials):
        threat_true = bool(rng.integers(0, 2))
        Pt = _params_for_truth(P, threat_true)
        r = simulate(Pt, T=T, dt=dt, seed=base_seed + 1 + i)
        b_final = r["b"][-1]
        commit_threat = b_final > 0.5
        conf[i] = abs(2 * b_final - 1)
        correct[i] = (commit_threat == threat_true)
    return dict(conf=conf, correct=correct)


def calibration_curve(
    conf: np.ndarray, correct: np.ndarray, n_bins: int = 8
) -> Dict[str, np.ndarray | float]:
    """Reliability diagram + Expected Calibration Error (ECE).

    Returns bin centers, empirical accuracy per (occupied) bin, and the scalar
    ECE. ECE is the mean gap between confidence and accuracy, weighted by bin
    occupancy; lower ECE = better congruence between confidence and outcome.
    """
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    centers, accs, ece, n = [], [], 0.0, len(conf)
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (conf >= lo) & (conf < hi if hi < 1.0 else conf <= hi)
        if not np.any(m):
            continue
        acc = float(np.mean(correct[m]))
        cnf = float(np.mean(conf[m]))
        centers.append(0.5 * (lo + hi))
        accs.append(acc)
        ece += (np.sum(m) / n) * abs(acc - cnf)
    return dict(centers=np.array(centers), acc=np.array(accs), ece=float(ece))
