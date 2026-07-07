# Fleming & Daw (2017) — Self-Evaluation of Decision-Making: A General Bayesian Framework for Metacognitive Computation

*Psychological Review 124(1), 91–114. doi:10.1037/rev0000045*
*검토: 2026-07-07. 정독 범위: pp.91–98 (모델 정의·핵심 결과). pp.99–114(추가 시뮬레이션·논의)는 미정독 — 아래 판정은 핵심 구조에 근거.*

## WHY / HOW / WHAT

- **WHY**: confidence와 error detection을 함께 설명하는 통일된 계산 프레임워크가 없었고, 수행–메타인지 **해리**(blindsight, 임상적 자기평가 손상)를 기존 1차 모델은 원리적으로 설명 못 함.
- **HOW**: 3계층 모델 비교. ① **1차(first-order)**: 결정 변수 `X_act`가 행동과 confidence를 **모두** 생성 (`X_conf = X_act`). ② **postdecisional**: `X_conf = X_act + 추가 증거`. ③ **2차(second-order)**: `X_act`, `X_conf`가 상관 ρ를 가진 **구분된 결합 변수** (bivariate Gaussian, Eq. 8–9) — 자기평가란 "자기 안의 다른 행위자(Actor)의 수행을 Confidence-rater가 추론"하는 것. confidence는 자신의 **행동 a까지 조건화**한 `z = P(a = d | X_conf, a, Σ)`.
- **WHAT**: 1차 모델은 error detection(커밋 직후 confidence < 0.5)과 수행–메타인지 해리를 **구조적으로 생성 불가**. 2차 모델은 confidence, error detection, 메타인지 개인차(수행보다 좋거나 나쁜 메타인지)를 단일 구조로 통일. 자기 행동이 이후 confidence를 인과적으로 바꾼다는 반직관적 예측 도출·검증(Siedlecka et al. 2016).

## 모델 구성요소별 판정

| mcbalance 요소 | 판정 | 상세 |
|---|---|---|
| `L` log-odds 믿음 (Eq. belief) | **지지** | 신호검출·베이지안 전통과 완전 연속. F&D의 `P(d\|X)` posterior와 같은 계열 |
| confidence `c = \|2b−1\|` | **반박(구조적)** | 이것은 F&D의 **1차 모델** — confidence가 행동을 만드는 동일 변수의 결정론적 읽기. 따라서 현 모델은 (a) 커밋 직후 "아차" (error detection), (b) **수행과 무관하게 손상되는 자기평가** — 즉 조현병의 insight 결핍 그 자체 — 를 원리적으로 표현할 수 없다 |
| Exp. 5의 ECE 미보정 | **정교화** | 현 모델의 미보정은 전적으로 증거 가중(`alpha` 기울기)에서 나옴. F&D 구분을 적용하면 미보정의 두 원천 — ① 기울기(증거 왜곡) ② 메타인지 채널 자체의 잡음/편향(σ_conf, ρ) — 을 분리 가능. 원문(Han)의 "fluency mistaken for validity = **calibration failure in metacognitive feelings**"(p.5)는 ②를 가리키는 것으로 읽히므로, 현 모델은 이 문장을 실은 ①로 구현한 셈 |
| rumination `r·sigmoid(L)` | **정교화(흥미)** | F&D: "자기 행동이 이후 confidence에 정보로 작용" — 자기 산출물에 조건화하는 것이 2차 계산에서는 **합리적**이기까지 함. 폭주(rumination)와 합리적 자기조건화의 경계가 ρ, σ로 매개된다는 관점 → LLM self-conditioning 논의(Phase 4)의 규범적 기준선 제공 |
| pivot / corridor / OU 노이즈 | 무관 | 본 문헌 범위 밖 |

## 모델 수정 백로그 제안

- **[P1] 2차 확장**: `L_conf` — `L`과 상관 ρ로 결합된 별도 confidence 변수 — 를 추가하면, **ρ가 "insight" 파라미터**가 된다 (ρ→1: 완전한 자기 투명성, 현 모델; ρ 낮음: 수행과 해리된 자기평가). 원문이 "MCI-S에서 insight 개선은 제한적"(p.2)이라 한 바로 그 변수의 자리가 생김. 감사 §6 "uncovered claims"의 insight 항목을 정확히 메운다.
- **[P2] Exp. 5 재해석**: 미보정의 두 원천(기울기 vs 메타인지 잡음)을 분리하는 대조 실험.

## 용어집 추가 후보

first-order vs second-order metacognitive computation, metacognitive sensitivity (vs bias), error detection / error-related negativity, blindsight (해리의 전형).

## Questions for Han (추가분, 2호 브리프 후보)

7. 조현병에서 "수행은 되는데 자기평가가 안 되는" 해리(insight 결핍)와 "증거 처리 자체의 기울기"는 임상적으로 구분되는 두 현상인가요? (F&D의 2차 구조 도입 여부를 가르는 질문 — 도입 시 모델이 insight를 다룰 수 있게 됨)
