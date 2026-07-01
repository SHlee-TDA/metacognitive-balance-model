"""mcbalance - a minimal control-theoretic model of the Metacognitive Balance
perspective of Han & Gu (2025).

Public API
----------
    Params, simulate, sigmoid, confidence   (model)
    corridor_dwell_fraction, recovery_time,
    tolerance_of_ambiguity, congruence_ensemble, calibration_curve   (metrics)
    exp1_regimes ... exp6_policy, ALL_EXPERIMENTS   (experiments)
"""
from .model import Params, simulate, sigmoid, confidence, PivotLatch
from .metrics import (
    corridor_dwell_fraction,
    recovery_time,
    tolerance_of_ambiguity,
    congruence_ensemble,
    calibration_curve,
)
from .experiments import (
    exp1_regimes,
    exp2_jtc,
    exp3_pivot,
    exp4_corridor,
    exp5_indices,
    exp6_policy,
    ALL_EXPERIMENTS,
)

__version__ = "0.1.0"
