# The six experiments

Each `exp*` function in `mcbalance/experiments.py` writes one figure and tests one
claim from Han & Gu (2025). All use the "they laughed at me" scenario
(`h1` benign, `h2` threat/self-referential).

### Experiment 1 — three regimes from one set-point
Vary only the personality set-point `alpha0 ∈ {0.85, 0.5, 0.15}`. Over-internalization
consolidates the threat belief (≈0.98) with high confidence; balance stays near
equipoise; over-externalization is low but erratic (tracks cue noise). One trait
parameter reproduces all three clinical pictures. → `exp1_regimes.png`

### Experiment 2 — jumping to conclusions
A high confidence-gain agent (small leak `kappa`, high `alpha0`) crosses the decision
threshold after very little evidence; a cautious agent never over-commits. JTC =
confidence outrunning evidence. → `exp2_jtc.png`

### Experiment 3 — pivot rescue
The over-internalizing patient of Exp. 1 with the hysteretic pivot on vs off (same
noise seed). Without it, the belief locks near 0.97; with it, Pivot A engages above
`theta_H_on`, pulls the dial toward context, disconfirming cues re-enter, and the
belief returns toward the corridor. → `exp3_pivot.png`

### Experiment 4 — the adaptive corridor
The self/context engagement plane (cf. the chapter's Fig. 2) rendered as a vector
field: the diagonal corridor is an attractor; trajectories from both risk corners are
drawn back into the band. → `exp4_corridor.png`

### Experiment 5 — the two minimal indices
- **Confidence–outcome congruence.** A truth-balanced ensemble (hidden state threat or
  benign per trial); at commitment we record confidence and correctness and summarize
  calibration by ECE. Balance is best calibrated; the over-internalizer is confidently
  wrong (high ECE).
- **Tolerance of ambiguity.** On a genuinely ambiguous stimulus (internal/external
  evidence cancel, high noise), measure time before confidence crosses a commit level.
  Balance stays with not-knowing longest. → `exp5_indices.png`

### Experiment 6 — sequential vs balanced policy
Same substrate and noise; a burst of threat evidence mid-run. The *sequential* policy
gates `alpha0(t)` (self-work first, then context-work; no feedback); the *balanced*
policy uses the hysteretic pivot. Balance wins on corridor dwell-fraction
(≈0.84 vs 0.12) and recovery time (≈3.5 vs 5.9). → `exp6_policy.png`

## Reusing the metrics

`mcbalance.metrics` exposes the measures independently of the figures:

```python
from mcbalance import Params, congruence_ensemble, calibration_curve

ens = congruence_ensemble(Params(alpha0=0.85))
cal = calibration_curve(ens["conf"], ens["correct"])
print("ECE:", cal["ece"])
```
