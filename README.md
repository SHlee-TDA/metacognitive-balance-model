# Metacognitive Balance — a computational realization

A minimal, runnable **control-theoretic model** of the *balance-oriented perspective*
on metacognition in schizophrenia proposed by **Han & Gu (2025)**. The model treats
interpretation as a probabilistic belief, metacognition as a control law acting on
that belief, and the self-vs-context *cognitive referencing system* as a coupled dial.
A single two-hypothesis scenario ("they laughed at me") reproduces four clinical
phenomena the chapter describes and turns its two "minimal indices" and its
sequence-vs-balance argument into measurable quantities.

> This repository is a scholarly **interpretation** of Han & Gu (2025), not a competing
> theory. Every modeling choice in the manuscript is anchored to the specific sentence
> in the chapter that motivated it.

Source chapter (CC-BY 4.0):
Han, M., & Gu, H. (2025). *Toward Metacognitive Balance: A Framework for Cognitive and
Social Functioning in Schizophrenia.* IntechOpen. https://doi.org/10.5772/intechopen.1012821

---

## The model in one screen

State: log-odds of the threat reading `L` (belief `b = sigmoid(L)`) and self-weight `alpha`.

```
dL/dt     = alpha * (aS + r*sigmoid(L))  +  (1-alpha) * (aC + xi(t))  -  kappa*L   [+ perturbation]
dalpha/dt = -gamma * (alpha - alpha0(t))  +  u(t)
```

- `r*sigmoid(L)` — ruminative self-amplification ("finding the cause within"): a positive
  feedback loop that, with the dial turned inward, consolidates a threat belief.
- `xi(t)` — Ornstein–Uhlenbeck ambiguity noise on the external channel.
- `-kappa*L` — leak toward equipoise (controlled re-appraisal / calibration).
- `u(t)` — the pivot / micro-cycle, a **hysteretic** feedback controller (Pivot A / Pivot B).

See [`docs/model.md`](docs/model.md) for the equations and the sentence-by-sentence
provenance table, and [`docs/experiments.md`](docs/experiments.md) for the studies.

---

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .          # installs the `mcbalance` package + deps (numpy, matplotlib)
```

## Reproduce every figure

```bash
python scripts/run_all.py --outdir figures
# or, after install:
mcbalance-figures --outdir figures
```

## Use as a library

```python
from mcbalance import Params, simulate, tolerance_of_ambiguity

# an over-internalizing patient
r = simulate(Params(alpha0=0.85), T=40, seed=7)
print(r["b"][-1])                 # consolidated threat belief ~0.98

# the paper's ambiguity-tolerance index for a balanced person
print(tolerance_of_ambiguity(Params(alpha0=0.50)))
```

---

## Experiments

| # | Claim tested (chapter) | Figure |
|---|------------------------|--------|
| 1 | internal/external tilt drives distortion (p.7) | `figures/exp1_regimes.png` |
| 2 | "feeling = fact" → JTC (p.5) | `figures/exp2_jtc.png` |
| 3 | pivots recenter within the corridor (p.6) | `figures/exp3_pivot.png` |
| 4 | the adaptive corridor (Fig. 2, p.7) | `figures/exp4_corridor.png` |
| 5 | the two minimal indices are diagnostic (p.6) | `figures/exp5_indices.png` |
| 6 | concurrency beats a gated sequence (Table 1) | `figures/exp6_policy.png` |

Representative Experiment 6 output: corridor dwell-fraction **0.84 (balanced)** vs
**0.12 (sequential)**; post-perturbation recovery **3.5** vs **5.9**.

---

## Repository layout

```
metacognitive-balance-model/
├── README.md
├── LICENSE                  # MIT (code); source chapter is CC-BY, see LICENSE note
├── pyproject.toml           # installable package (src-layout)
├── requirements.txt
├── src/mcbalance/
│   ├── model.py             # core dynamics: Params, simulate(), PivotLatch (hysteresis)
│   ├── metrics.py           # minimal indices + corridor/recovery measures (reusable)
│   └── experiments.py       # exp1..exp6, each returns a figure path
├── scripts/run_all.py       # regenerate all figures + print exp-5/6 numbers
├── figures/                 # generated PNGs
├── paper/
│   ├── main.tex             # the manuscript (provenance quotes + plain-language boxes)
│   ├── references.bib
│   ├── model_listing.py     # ASCII copy of model.py used by the appendix listing
│   └── figs/                # figures embedded in the PDF
└── docs/
    ├── model.md
    └── experiments.md
```

## Build the manuscript

```bash
cd paper
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

## Citing

If you build on this, please cite the source chapter (see `paper/references.bib`).
This code is released under the MIT License.
