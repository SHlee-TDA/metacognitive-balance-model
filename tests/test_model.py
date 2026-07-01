"""Smoke + behavioral tests for the mcbalance model."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mcbalance import Params, simulate, sigmoid, confidence  # noqa: E402
from mcbalance import tolerance_of_ambiguity, congruence_ensemble, calibration_curve  # noqa: E402


def test_sigmoid_confidence_ranges():
    assert abs(sigmoid(0.0) - 0.5) < 1e-9
    assert 0.0 <= confidence(0.0) <= 1e-9
    assert confidence(10.0) > 0.99


def test_simulate_shapes_and_bounds():
    r = simulate(Params(alpha0=0.5), T=10, dt=0.02, seed=1)
    n = int(round(10 / 0.02))
    for key in ("t", "L", "alpha", "b", "conf", "xi", "u"):
        assert r[key].shape == (n,)
    assert np.all((r["b"] >= 0) & (r["b"] <= 1))
    assert np.all((r["alpha"] >= 0) & (r["alpha"] <= 1))


def test_regime_ordering():
    """Over-internalizing ends more threat-committed than balanced than over-external."""
    b_int = simulate(Params(alpha0=0.85), T=40, seed=7)["b"][-1]
    b_bal = simulate(Params(alpha0=0.50), T=40, seed=7)["b"][-1]
    b_ext = simulate(Params(alpha0=0.15), T=40, seed=7)["b"][-1]
    assert b_int > b_bal > b_ext


def test_pivot_reduces_consolidation():
    """The pivot should keep the final belief below the un-intervened case."""
    off = simulate(Params(alpha0=0.85, pivot=False), T=40, seed=3)["b"][-1]
    on = simulate(Params(alpha0=0.85, pivot=True), T=40, seed=3)["b"][-1]
    assert on < off


def test_balanced_better_calibrated_than_internalizer():
    ece_bal = calibration_curve(**{k: congruence_ensemble(Params(alpha0=0.50), n_trials=200)[k]
                                   for k in ("conf", "correct")})["ece"]
    ece_int = calibration_curve(**{k: congruence_ensemble(Params(alpha0=0.85, kappa=0.20), n_trials=200)[k]
                                   for k in ("conf", "correct")})["ece"]
    assert ece_bal < ece_int


def test_tolerance_positive():
    assert tolerance_of_ambiguity(Params(alpha0=0.5), n_trials=50) > 0
