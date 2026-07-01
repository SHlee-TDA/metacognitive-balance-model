# The model, and where each part comes from

This document mirrors the manuscript's core in Markdown. Each modeling decision is
tied to the sentence in Han & Gu (2025) that motivated it. Page numbers refer to the
IntechOpen chapter (doi:10.5772/intechopen.1012821).

## State variables

- `L(t)` — log-odds of the threat / self-referential reading `h2` vs the benign `h1`.
  Belief `b = sigmoid(L)`; `L = 0` is genuine equipoise (50/50).
- `alpha(t)` — self-weight in `[0, 1]`; `alpha_self = alpha`, `alpha_context = 1 - alpha`.
- Confidence `c = |2b - 1|` — a readable procedural (metacognitive) feeling.

## Equations

```
dL/dt     = alpha*lambda_S(L) + (1-alpha)*lambda_C(t) - kappa*L  [+ perturbation]
dalpha/dt = -gamma*(alpha - alpha0(t)) + u(t)
lambda_S(L) = aS + r*sigmoid(L)
lambda_C(t) = aC + xi(t),   dxi = -theta*xi dt + sigC dW
```

## Provenance — sentence → formal object

| Modeling decision | Motivating sentence (paraphrased location) |
|---|---|
| Interpretation = integrate internal + external, then regulate | p.1: metacognitive regulation integrates thoughts/feelings/sensations with others' intentions, norms, cues, and regulates responses |
| Belief is a **probability**, not a verdict; JTC = premature closure | p.5: decisions driven by "feeling = fact" lead to premature closure (JTC) before re-appraisal |
| Metacognition is **control** → a rate law `dL/dt = M(...)` | p.3: "its core is control — stop, check, strategy shift" |
| Confidence as procedural signal | p.2 (Proust): monitors/corrects via feelings such as confidence, fluency, effort |
| Self–context **dial** `alpha` | p.7: a referencing system tilting internal vs external; a dynamic regulator between two axes |
| **Coupled** (concurrent) system | abstract/p.2: coordinates both axes concurrently and interactively |
| Rumination term `r*sigmoid(L)` (positive feedback) | p.4–5: over-internalization = "finding the cause within"; fluency mistaken for validity |
| Over-externalization = cue-tracking (erratic) | p.5: drawn to others' cues, neglecting internal monitoring, responses erratic |
| Pivot `u(t)` as feedback control (Pivot A/B) | p.6 fn.3: on imbalance, switch rule-set between self- and context-work to recenter |
| Four control parameters | p.9: confidence gain, ambiguity threshold, cue weighting, switch sensitivity |
| Set-point `alpha0`, gain `gamma`; personality | p.8: baseline tilt (set-point) and regulatory gain; aligns with Jung intro/extraversion |
| Adaptive corridor (attractor) | p.7: diagonal corridor = balanced co-regulation; pivots at the two corners |
| Minimal indices | p.6: track confidence–outcome congruence and tolerance of ambiguity |

## Mapping the chapter's four control parameters (p.9) onto the code

| Chapter parameter | Code quantity | Meaning |
|---|---|---|
| confidence gain | small `kappa` / fast `|L|` growth | how fast certainty outruns evidence |
| ambiguity threshold | tolerance of `xi` before commit | how long you sit with not-knowing |
| cue weighting | `alpha` | inner-vs-outer allocation (the dial) |
| switch sensitivity | `p_gain`, thresholds `theta_H_on/off`, `theta_L` | how easily a pivot fires |

## Note on the pivot hysteresis

A bare threshold makes the pivot *chatter* near the boundary. `PivotLatch`
(in `model.py`) uses separate engage/release thresholds (a Schmitt trigger), so the
rebalancing move engages decisively and releases only once the imbalance clearly
resolves — both more stable and more clinically realistic.
