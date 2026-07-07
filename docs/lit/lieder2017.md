# Lieder & Griffiths (2017) — Strategy Selection as Rational Metareasoning

*Psychological Review 124(6):762–794 (검토본은 preprint, 68면).*
*검토: 2026-07-07. 정독: pp.1–5 (초록·서론·배경). 모델 세부(SSL 알고리즘)·실험은 미정독 — 필요 시 재방문.*

## WHY / HOW / WHAT

- **WHY**: 마음이 여러 전략(heuristics) 중 **언제 무엇을 쓸지** 어떻게 정하는가 — 전략 선택 문제.
- **HOW**: AI의 **rational metareasoning**(Russell & Wefald 1991)을 심리학에 이식. 각 전략의 성능 예측 모델을 학습해 비용–편익 최적 전략을 선택(metacognitive reinforcement learning). "resource-rational" 관점: 유한한 인지 자원의 최적 사용.
- **WHAT**: 정렬·의사결정·암산 등 고전 현상들의 통일적 설명 + 신규 실험 4건 검증. 핵심 논제: **heuristic 자체는 합리적이지도 비합리적이지도 않다 — 문제와의 적합이 결정하며, 진짜 질문은 "heuristic이 합리적으로 선택되는가"**. 전략 선택 기제는 효율적이어야 하고 "추론에 대한 추론"의 무한 회귀를 피해야 함.

## 모델 구성요소별 판정

| mcbalance 요소 | 판정 | 상세 |
|---|---|---|
| pivot `u(t)` (임계 기반 수제 규칙) | **정교화(승격 경로)** | pivot = self-work/context-work라는 두 "전략" 사이의 선택 → rational metareasoning으로 **원리적 유도** 가능: 전환의 기대 가치(VOC) − 전환 비용 > 0일 때 전환. 현재의 임계·게인은 근사로 재해석됨 |
| PivotLatch 히스테리시스 (EXTRAPOLATED) | **잠재적 격상** | 전환 비용이 있는 메타추론에서는 잦은 왕복이 비합리적 → engage/release 임계 분리가 **자원 합리적 정책으로 유도될 가능성**. 성립하면 히스테리시스는 임의 장치가 아니라 정리(定理)가 됨 — Han Q5의 수학 측 보강 |
| JTC (Exp. 2) | 정교화 | 시간 압박에서 frugal heuristic 선택은 적응적(Payne 1988) — JTC를 "환경에 맞던 전략 선택이 부적합 환경에서 지속되는 것"으로 읽는 제3의 해석(Han Q2의 (c) 갈래에 이론 언어 제공) |
| corridor 유지의 목적함수 | 참고 | balance를 "두 전략의 자원 합리적 혼합"으로 보는 규범적 재정식화 여지 |

## Phase 4 함의

"언제 비싼 계산(retrieval, self-check, abstention)을 발동할 것인가" = value of computation 문제로, LLM의 adaptive computation·tool-use 트리거 설계에 기존 이론 체계가 존재함을 확인. pivot 정책의 LLM 이식은 이 언어로 쓰는 것이 정공법.

## 백로그

- **[신규 B-12, P2] pivot의 메타추론적 유도**: 전환 비용 c_switch 하에서 VOC 기반 최적 정책을 수치적으로 구해 PivotLatch와 비교 — 히스테리시스가 창발하는지 검증.
