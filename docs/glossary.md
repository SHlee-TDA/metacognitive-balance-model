# 용어집 — 수학자를 위한 심리학 개념 사전

> **버전 v1.** 2026-07-07 원문 16면 전체 정독으로 전 항목 검증 완료
> (감사 근거: [audit/claim-model-alignment.md](audit/claim-model-alignment.md)).
> 각 항목의 "번역 손실" 열은 수학적 대응물이 심리학 개념을 **어디까지만**
> 포착하는지 명시한다 — 이 열이 Han과의 디스커션에서 가장 중요한 부분.
>
> 표기: ✅ 검증됨(원문 재확인 완료) / 🔶 시드(검증 대기)

| 용어 | 심리학적 정의 (원문 기준) | 수학적 대응물 (모델 내) | 번역 손실 / 주의점 | 상태 |
|---|---|---|---|---|
| metacognition (메타인지) | "생각에 대한 생각" — 자신의 사고·감정·신체감각을 타인의 의도, 사회 규범, 상황 단서에 비추어 통합·해석하고 반응을 조절하는 능력 (p.1) | 믿음 `L`에 작용하는 제어 법칙 `dL/dt = M(...)` 전체 | 심리학에서는 능력(capacity)이자 과정 — 모델은 과정만 포착, 개인차는 파라미터로 환원 | ✅ |
| metacognitive regulation | 메타인지의 실행 측면: 멈추고(stop), 점검하고(check), 전략을 바꾸는(strategy shift) 제어 (p.3, Proust) | 제어 입력 `u(t)` + leak `kappa` | — | ✅ |
| procedural metacognition (Proust) | 비개념적·경험적 시스템: confidence, fluency, effort 같은 **메타인지적 느낌**으로 진행 중인 인지를 감시·교정 (p.3) | 읽기 가능한 스칼라 신호 `c = \|2b − 1\|` (confidence) | 원개념은 다차원(fluency, effort 포함); 모델은 confidence 1차원만 구현 | ✅ |
| explicit metacognition (Proust) | 언어적 반성, 증거 대조, 타인 관점 채택에 의존하는 표상적 시스템 (p.3) | pivot 규칙·재평가(leak)의 이산적 개입 | 언어적/개념적 내용은 모델 밖 | ✅ |
| self-awareness (자기인식) | 자신의 생각·감정·의도를 구별하고 인지적 함정(자동적 걱정, 반추 등)을 메타 수준에서 관찰·탈동조화하는 능력 (p.2) | self 채널 `lambda_S(L) = aS + r·sigmoid(L)`에 대한 접근 | 심리학의 self-awareness는 **질적 통찰** 포함 — 모델은 채널 가중치로만 표현 | ✅ |
| context/other-awareness | 타인의 관점과 사회적·상황적 단서를 통합해 다관점 해석을 하는 능력 (p.2) | context 채널 `lambda_C(t) = aC + xi(t)` | 사회 인지의 내용(ToM 추론 등)은 노이즈 있는 외생 신호로 추상화됨 | ✅ |
| metacognitive balance (균형) | self-와 context-awareness의 **동시적 공동조절**(concurrent co-regulation); 두 축의 "mutual constraint and cooperation" (abstract, p.8). Han의 작업명: **Metacognitive Balance Theory** (p.7) | `alpha` dial의 동역학 + corridor attractor | ★원문 Fig. 2에서 두 축은 **독립**이며 corridor는 대각선 y = x — 둘 다 높은 상태(80,80)도 균형. 모델의 `alpha`/`1−alpha`는 **zero-sum**이라 tilt 성분만 포착 (감사 F1, Han Q1) | ✅ |
| over-internalization (과잉 내재화) | 과도한 자기초점·반추로의 표류; "원인을 자기 안에서 찾음" (p.4–5) | `alpha → 1` 영역 + rumination 양성 피드백 `r·sigmoid(L)` | — | ✅ |
| over-externalization (과잉 외재화) | 타인의 반응·상황 단서·소문에 과의존; hyper-suspiciousness, 외재화/개인화 귀인의 **강화**, hyper-mentalizing, 반응 불안정 (p.5, 7) | `alpha → 0` 영역: 믿음이 OU 노이즈 `xi(t)`를 추적 | ★모델은 "끌려다님"만 포착 — 외부 단서가 위협 해석을 **강화**하는 경로(편집증적 과잉추론)는 `aC ≤ 0` 가정상 생성 불가 (감사 F3, Han Q3) | ✅ |
| rumination (반추) | 자동적·반복적 부정 사고; 인지적 함정의 대표 (p.2) | 양성 피드백 항 `r·sigmoid(L)` | 반추의 **내용**(과거지향적 자기비판 등)은 없음; 구조(자기강화 루프)만 | ✅ |
| jumping to conclusions (JTC) | 재평가 전에 "느낌 = 사실"로 성급히 종결하는 편향 (p.1, 5) | 낮은 증거량에서 confidence가 commit 임계 초과 (Exp. 2) | ★원문은 JTC를 **over-externalization 문단**(p.5, p.8, Table 2)에 배치 — Exp. 2의 고`alpha0` 구현과 긴장 (감사 F2, Han Q2). 실증 JTC는 beads task 문헌[3,4]과 Phase 2 대조 | ✅ |
| theory of mind (ToM) | 타인의 정신 상태(믿음·의도)를 추론하는 능력 | 명시적 대응물 **없음** — context 채널에 흡수 | 의도적 단순화; Proust는 메타인지가 ToM과 부분 독립이라 주장 (p.3) — 모델과 정합 | ✅ |
| confidence calibration | 주관적 확신이 사후 증거/정확도와 정렬되도록 판단 규칙을 조정하는 과정 (p.3 fn.1) | Exp. 5의 confidence–outcome congruence, ECE | ECE는 LLM 문헌과 **공용 언어** — Phase 4의 핵심 교량 | ✅ |
| tolerance of ambiguity | 모르는 상태(not-knowing)에 머무를 수 있는 시간/능력 (p.4 Table 1) | 모호 자극에서 confidence가 commit 수준을 넘기까지의 시간 (Exp. 5) | — | ✅ |
| pivot (Pivot A / B) | 불균형 감지 시 self-work ↔ context-work 규칙 세트를 전환해 재중심화하는 개입 (p.4 Table 1, fn) | 히스테리시스 제어기 `PivotLatch` (Schmitt trigger) | 히스테리시스(engage/release 임계 분리)는 **모델 측 추가** — chattering 방지 목적, 원문에 없음 (EXTRAPOLATED 후보) | ✅ |
| adaptive corridor | self(x)·context(y) 관여 평면에서 **대각선 y = x 주변의 띠** — 균형적 공동조절 영역; pivot은 좌상(→self-work)·우하(→context-work) 모서리에서 발동 (p.7–8 Fig. 2) | 벡터장의 attractor 띠 (Exp. 4) | 원문 Fig. 2는 개념도("conceptual map") — attractor 해석은 INTERPRETIVE. 두 축 독립성 문제는 감사 F1 참조 | ✅ |
| MCI-S | Metacognitive Intervention for Schizophrenia: self-awareness 먼저, context-awareness 나중의 순차 2단계 개입 (p.2) | Exp. 6의 "sequential policy" (`alpha0(t)` 게이트, 피드백 없음) | 실제 MCI-S는 임상 프로토콜 — "피드백 없는 게이트"로의 환원은 비교를 위한 캐리커처일 수 있음 (Phase 2 검증) | ✅ |
| insight (병식) | 자신의 상태에 대한 인식 — MCI-S에서 개선이 제한적이었던 변수 (p.2) | 명시적 대응물 없음 | 모델 확장 후보 | ✅ |
| schizophrenia 맥락 | 망상·환각 + 사회기능 저하; 본 모델의 임상 배경 | "they laughed at me" 시나리오의 threat 해석 `h2` | 모델은 단일 해석 사건만 다룸 — 질병 전체가 아님 | ✅ |

## Phase 2 문헌에서 추가된 용어 (수학자용)

| 용어 | 정의 (출처) | 수학적/모델 대응 | 상태 |
|---|---|---|---|
| meta-level / object-level | 감시하는 층 / 감시받는 층 (Nelson & Narens 1990, Hilbert 메타수학 유래) | leak·pivot(meta) vs `L` 동역학(object) — **수직** 구분 | ✅ |
| monitoring / control | 정보 흐름 방향: object→meta(갱신) / meta→object(수정) (N&N 1990) | `c(t)` 읽기 / `dL/dt`·`u(t)` | ✅ |
| good regulator theorem | "시스템의 좋은 제어기는 그 시스템의 모델이어야 한다" (Conant & Ashby 1970, N&N 인용) | pivot이 `b`, `dL/dt`를 읽는 것의 필요성 근거; Phase 4 LLM 제어기 설계 정리 | ✅ |
| first- vs second-order metacognition | confidence가 결정 변수와 같은가(1차) 별개 결합 변수인가(2차) (Fleming & Daw 2017) | 현 `c=\|2b−1\|`는 1차; 2차는 상관 ρ의 `L_conf` 추가 | ✅ |
| metacognitive sensitivity vs bias | 정오 구분 능력 vs 전반적 과/저확신 (Fleming & Daw) | ECE의 두 성분 | ✅ |
| insight (병식) — 조작화 | 자기 상태의 정확한 자각; 환각 내용과 **해리** 가능 (Merabet 2004: 환각하되 가짜임을 앎) | 2차 채널 상관 ρ (ρ↓ = insight 결핍) | ✅ |
| S-REF / CAS | Self-Regulatory Executive Function / Cognitive Attentional Syndrome (worry·rumination·threat monitoring) (Wells 2019) | CAS의 threat monitoring = 외부 채널의 위협 확증 모드(F3) | ✅ |
| metacognitive beliefs (declarative/procedural) | 사고에 대한 신념/절차 규칙 (Wells) | `r`, pivot 정책을 결정하는 상위 파라미터 | ✅ |
| rational metareasoning / resource-rational | 유한 자원 하 전략의 비용–편익 최적 선택 (Lieder & Griffiths 2017) | pivot `u(t)`의 규범적 유도; 히스테리시스 정리화 | ✅ |
| value of computation (VOC) | 추가 계산의 기대 가치 (Russell & Wefald) | pivot 발동 임계의 원리적 대체 | ✅ |
| representation vs behavior-control pathology | LLM 실패의 두 부류: hallucination·bias / sycophancy·refusal (Sun 2026 NeuroCogMap) | `L`(표상) 축 / `alpha`·pivot(제어) 축과 대응 | ✅ |
| psychotic-like experiences (PLEs) | 준임상 정신증 유사 경험; state×trait로 유발 (Daniel 2014) | 외부 채널 소거 시 `L` 표류의 대리 지표 | ✅ |

## 미등재 대기열

Phase 2 후반/Phase 4에서 등재 예정: metacognitive feelings (fluency, effort),
externalizing/personalizing attribution, thought suppression, SCT/SCIT/MCT/MERIT
개입 계열, Jung introversion/extraversion (p.8), sycophancy·refusal failure (LLM),
semantic entropy (Farquhar 2024), SAE·residual stream (조건부, 사용자 지시).
