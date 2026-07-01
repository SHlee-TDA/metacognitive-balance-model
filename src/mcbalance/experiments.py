"""The six simulation experiments, each producing one figure.

Experiments 1-4 test qualitative claims (regimes, JTC, pivot rescue, corridor).
Experiments 5-6 test the paper's minimal indices and the sequential-vs-balanced
argument. Every ``exp*`` function takes an output directory and returns the path
of the figure it writes. Legends are placed *outside* the plotting area.
"""
from __future__ import annotations

import os
from dataclasses import replace

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from .model import Params, simulate
from .metrics import (
    corridor_dwell_fraction,
    recovery_time,
    tolerance_of_ambiguity,
    congruence_ensemble,
    calibration_curve,
)

# ---- shared palette / style ------------------------------------------------ #
C_INT = "#c0392b"   # over-internalization / threat
C_BAL = "#27ae60"   # balanced
C_EXT = "#2980b9"   # over-externalization
INK = "#222222"


def _style(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(alpha=0.15, lw=0.6)


def _save(fig, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, name)
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return path


# --------------------------------------------------------------------------- #
def exp1_regimes(outdir="figures"):
    """Three metacognitive regimes produced by a single personality set-point."""
    regimes = [("Over-internalizing (a0=0.85)", 0.85, C_INT),
               ("Balanced (a0=0.50)", 0.50, C_BAL),
               ("Over-externalizing (a0=0.15)", 0.15, C_EXT)]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    handles = []
    for label, a0, col in regimes:
        r = simulate(Params(alpha0=a0), T=40, seed=7)
        h, = axes[0].plot(r["t"], r["b"], color=col, lw=2, label=label)
        axes[1].plot(r["t"], r["conf"], color=col, lw=2)
        handles.append(h)
    axes[0].axhline(0.5, color=INK, ls=":", lw=1, alpha=0.6)
    axes[0].set(title="Belief in threat  b(t)=sigmoid(L)", xlabel="time", ylabel="P(threat)", ylim=(0, 1))
    axes[1].set(title="Confidence  |2b-1|", xlabel="time", ylabel="confidence", ylim=(0, 1))
    for ax in axes:
        _style(ax)
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False,
               fontsize=9, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle("Experiment 1 - Three metacognitive regimes from a fixed set-point",
                 fontsize=12, fontweight="bold", color=INK)
    fig.tight_layout(rect=[0, 0.06, 1, 0.95])
    return _save(fig, outdir, "exp1_regimes.png")


# --------------------------------------------------------------------------- #
def exp2_jtc(outdir="figures"):
    """Jumping to conclusions as confidence outrunning evidence."""
    settings = [("High confidence-gain (kappa=0.10, a0=0.80)", Params(kappa=0.10, alpha0=0.80), C_INT),
                ("Cautious (kappa=0.45, a0=0.50)", Params(kappa=0.45, alpha0=0.50), C_BAL)]
    c_star = 0.8
    fig, ax = plt.subplots(figsize=(8.4, 4.6))
    handles = []
    for label, P, col in settings:
        r = simulate(P, T=40, seed=11)
        h, = ax.plot(r["t"], r["conf"], color=col, lw=2.2, label=label)
        handles.append(h)
        idx = int(np.argmax(r["conf"] >= c_star))
        if r["conf"][idx] >= c_star:
            ax.scatter([r["t"][idx]], [r["conf"][idx]], color=col, s=60, zorder=5)
            ax.annotate(f"commit @ t={r['t'][idx]:.1f}", (r["t"][idx], c_star),
                        textcoords="offset points", xytext=(8, -22), fontsize=8, color=col)
    ax.axhline(c_star, color=INK, ls="--", lw=1, alpha=0.7)
    ax.text(0.3, c_star + 0.02, "decision threshold c*", fontsize=8, color=INK)
    ax.set(title="Experiment 2 - Jumping to conclusions = early commitment on little evidence",
           xlabel="time (~ evidence accumulated)", ylabel="confidence", ylim=(0, 1.02))
    _style(ax)
    fig.legend(handles=handles, loc="lower center", ncol=2, frameon=False,
               fontsize=9, bbox_to_anchor=(0.5, -0.04))
    fig.tight_layout(rect=[0, 0.05, 1, 1])
    return _save(fig, outdir, "exp2_jtc.png")


# --------------------------------------------------------------------------- #
def exp3_pivot(outdir="figures"):
    """A hysteretic within-session pivot rescues a consolidating belief."""
    base = dict(alpha0=0.85)
    r_off = simulate(Params(pivot=False, **base), T=40, seed=3)
    r_on = simulate(Params(pivot=True, **base), T=40, seed=3)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))

    axes[0].axhspan(0.25, 0.75, color=C_BAL, alpha=0.10)
    axes[0].text(1, 0.77, "adaptive corridor", fontsize=8, color=C_BAL)
    axes[0].plot(r_off["t"], r_off["b"], color=C_INT, lw=2)
    axes[0].plot(r_on["t"], r_on["b"], color=C_BAL, lw=2)
    axes[0].set(title="Belief in threat", xlabel="time", ylabel="P(threat)", ylim=(0, 1))

    axes[1].plot(r_off["t"], r_off["alpha"], color=C_INT, lw=2)
    axes[1].plot(r_on["t"], r_on["alpha"], color=C_BAL, lw=2)
    fired = r_on["u"] < 0
    axes[1].fill_between(r_on["t"], 0, 1, where=fired, color=C_INT, alpha=0.08, step="mid")
    axes[1].axhline(0.5, color=INK, ls=":", lw=1, alpha=0.6)
    axes[1].set(title="Self-weight  alpha(t)", xlabel="time", ylabel="alpha (self)", ylim=(0, 1))
    for ax in axes:
        _style(ax)

    handles = [plt.Line2D([], [], color=C_INT, lw=2, label="No intervention"),
               plt.Line2D([], [], color=C_BAL, lw=2, label="With pivot (micro-cycle)"),
               Patch(facecolor=C_INT, alpha=0.15, label="Pivot A active")]
    fig.legend(handles=handles, loc="lower center", ncol=3, frameon=False,
               fontsize=9, bbox_to_anchor=(0.5, -0.02))
    fig.suptitle("Experiment 3 - A within-session pivot pulls a consolidating delusion back into balance",
                 fontsize=12, fontweight="bold", color=INK)
    fig.tight_layout(rect=[0, 0.06, 1, 0.95])
    return _save(fig, outdir, "exp3_pivot.png")


# --------------------------------------------------------------------------- #
def exp4_corridor(outdir="figures"):
    """The adaptive corridor rendered as a dynamical attractor (cf. Fig. 2)."""
    def field(x, y):
        d = (y - x)
        return 0.15 * d + 0.05 * (50 - x), -0.15 * d + 0.05 * (50 - y)

    xs = np.linspace(2, 100, 22)
    ys = np.linspace(2, 100, 22)
    X, Y = np.meshgrid(xs, ys)
    U, V = field(X, Y)
    N = np.hypot(U, V)
    N[N == 0] = 1
    fig, ax = plt.subplots(figsize=(6.8, 6.4))
    ax.quiver(X, Y, U / N, V / N, N, cmap="Greys", alpha=0.5, scale=32, width=0.003)
    ax.fill_between([0, 100], [-15, 85], [15, 115], color=C_BAL, alpha=0.12, zorder=0)
    ax.plot([0, 100], [0, 100], color=C_BAL, lw=1.5, ls="--")
    ax.text(58, 70, "Adaptive corridor", rotation=45, color=C_BAL, fontsize=11, fontweight="bold")
    ax.scatter([80], [18], color=C_INT, s=70, zorder=5)
    ax.annotate("over-internalization\n(pivot -> context-work)", (80, 18),
                xytext=(40, 6), fontsize=8, color=C_INT, arrowprops=dict(arrowstyle="->", color=C_INT))
    ax.scatter([18], [80], color=C_EXT, s=70, zorder=5)
    ax.annotate("over-externalization\n(pivot -> self-work)", (18, 80),
                xytext=(20, 92), fontsize=8, color=C_EXT, arrowprops=dict(arrowstyle="->", color=C_EXT))
    for (x0, y0), col in [((80, 18), C_INT), ((18, 80), C_EXT), ((15, 20), INK)]:
        x, y = x0, y0
        xt, yt = [x], [y]
        for _ in range(400):
            fx, fy = field(x, y)
            x += fx * 0.1
            y += fy * 0.1
            xt.append(x)
            yt.append(y)
        ax.plot(xt, yt, color=col, lw=1.8, alpha=0.85)
        ax.scatter([x0], [y0], color=col, s=18)
    ax.set(xlim=(0, 100), ylim=(0, 100), xlabel="Self-awareness (x)", ylabel="Context/other-awareness (y)")
    _style(ax)
    ax.set_title("Experiment 4 - Adaptive corridor as a dynamical attractor (cf. Fig. 2)",
                 fontsize=11, fontweight="bold", color=INK)
    fig.tight_layout()
    return _save(fig, outdir, "exp4_corridor.png")


# --------------------------------------------------------------------------- #
def exp5_indices(outdir="figures"):
    """The two minimal indices: confidence-outcome congruence and ambiguity tolerance."""
    regimes = [("Over-internalizing", Params(alpha0=0.85, kappa=0.20), C_INT),
               ("Balanced", Params(alpha0=0.50, kappa=0.30), C_BAL),
               ("Over-externalizing", Params(alpha0=0.15, kappa=0.30), C_EXT)]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    # (a) reliability diagram + ECE
    axes[0].plot([0, 1], [0, 1], color=INK, ls=":", lw=1, alpha=0.6)
    tol_vals, tol_cols, tol_labels = [], [], []
    for label, P, col in regimes:
        ens = congruence_ensemble(P)
        cal = calibration_curve(ens["conf"], ens["correct"])
        axes[0].plot(cal["centers"], cal["acc"], "-o", color=col, lw=2, ms=4,
                     label=f"{label} (ECE={cal['ece']:.2f})")
        tol_vals.append(tolerance_of_ambiguity(P))
        tol_cols.append(col)
        tol_labels.append(label)
    axes[0].set(title="(a) Confidence-outcome congruence", xlabel="confidence (bin)",
                ylabel="empirical accuracy", xlim=(0, 1), ylim=(0, 1))
    axes[0].text(0.05, 0.9, "perfect calibration", fontsize=7, color=INK, rotation=37)
    _style(axes[0])
    axes[0].legend(fontsize=8, frameon=False, loc="lower right")

    # (b) tolerance of ambiguity
    xpos = np.arange(len(tol_labels))
    axes[1].bar(xpos, tol_vals, color=tol_cols, alpha=0.85, width=0.6)
    for x, v in zip(xpos, tol_vals):
        axes[1].text(x, v + 0.4, f"{v:.1f}", ha="center", fontsize=9, color=INK)
    axes[1].set(title="(b) Tolerance of ambiguity", ylabel="time before committing (higher = more tolerant)")
    axes[1].set_xticks(xpos)
    axes[1].set_xticklabels(["Over-\ninternal.", "Balanced", "Over-\nexternal."], fontsize=9)
    _style(axes[1])

    fig.suptitle("Experiment 5 - The balanced regime scores best on both minimal indices",
                 fontsize=12, fontweight="bold", color=INK)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    return _save(fig, outdir, "exp5_indices.png")


# --------------------------------------------------------------------------- #
def exp6_policy(outdir="figures"):
    """Sequential (gated) vs balanced (concurrent) policy under a perturbation."""
    T, dt = 60.0, 0.02
    t_pert = (36.0, 40.0, 1.6)   # a burst of threat-consistent evidence
    base = Params(alpha0=0.5)

    # Sequential: self-work first (alpha high), then context-work (alpha low); no feedback pivot.
    def seq_setpoint(tt):
        return 0.80 if tt < T / 2 else 0.20
    r_seq = simulate(replace(base, pivot=False), T=T, dt=dt, seed=21,
                     alpha0_fn=seq_setpoint, perturb=t_pert)

    # Balanced: concurrent co-regulation via the hysteretic pivot.
    r_bal = simulate(replace(base, pivot=True), T=T, dt=dt, seed=21, perturb=t_pert)

    dwell_seq = corridor_dwell_fraction(r_seq["b"])
    dwell_bal = corridor_dwell_fraction(r_bal["b"])
    rec_seq = recovery_time(r_seq["t"], r_seq["b"], t_pert[1])
    rec_bal = recovery_time(r_bal["t"], r_bal["b"], t_pert[1])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.7, 1]})

    axes[0].axhspan(0.25, 0.75, color=C_BAL, alpha=0.10)
    axes[0].axvspan(t_pert[0], t_pert[1], color=C_INT, alpha=0.10)
    axes[0].text(t_pert[0], 0.03, "perturbation", fontsize=8, color=C_INT)
    h1, = axes[0].plot(r_seq["t"], r_seq["b"], color=C_INT, lw=2, label="Sequential (gated self->context)")
    h2, = axes[0].plot(r_bal["t"], r_bal["b"], color=C_BAL, lw=2, label="Balanced (concurrent)")
    axes[0].set(title="Belief trajectories", xlabel="time", ylabel="P(threat)", ylim=(0, 1))
    _style(axes[0])
    axes[0].legend(handles=[h1, h2], fontsize=8, frameon=False, loc="upper left")

    metrics = [("Corridor\ndwell (frac.)", dwell_seq, dwell_bal),
               ("Recovery\ntime", rec_seq / 10.0, rec_bal / 10.0)]  # recovery scaled /10 to share axis
    xpos = np.arange(len(metrics))
    w = 0.36
    axes[1].bar(xpos - w / 2, [m[1] for m in metrics], width=w, color=C_INT, alpha=0.85, label="Sequential")
    axes[1].bar(xpos + w / 2, [m[2] for m in metrics], width=w, color=C_BAL, alpha=0.85, label="Balanced")
    axes[1].set_xticks(xpos)
    axes[1].set_xticklabels([m[0] for m in metrics], fontsize=9)
    axes[1].set(title="Policy comparison", ylabel="value (recovery time / 10)")
    _style(axes[1])
    axes[1].legend(fontsize=8, frameon=False, loc="upper right")

    fig.suptitle("Experiment 6 - Concurrent co-regulation beats a gated sequence",
                 fontsize=12, fontweight="bold", color=INK)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    path = _save(fig, outdir, "exp6_policy.png")
    return path, dict(dwell_seq=dwell_seq, dwell_bal=dwell_bal, rec_seq=rec_seq, rec_bal=rec_bal)


ALL_EXPERIMENTS = [exp1_regimes, exp2_jtc, exp3_pivot, exp4_corridor, exp5_indices, exp6_policy]


def _cli():
    """Console-script entry point: regenerate every figure into ./figures."""
    import argparse
    ap = argparse.ArgumentParser(description="Regenerate all mcbalance figures.")
    ap.add_argument("--outdir", default="figures")
    args = ap.parse_args()
    for fn in (exp1_regimes, exp2_jtc, exp3_pivot, exp4_corridor, exp5_indices):
        print("wrote", fn(args.outdir))
    path, stats = exp6_policy(args.outdir)
    print("wrote", path)
    print("exp6:", stats)
