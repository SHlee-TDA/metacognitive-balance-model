# Daniel, Lovatt & Mason (2014) — Psychotic-Like Experiences Under Short-Term Sensory Deprivation

*Frontiers in Psychiatry 5:106.* 검토: 2026-07-07. 정독: pp.1–4 (서론·방법·주요 결과).

## WHY / HOW / WHAT

- **WHY**: 단기 감각 박탈로 psychotic-like experiences(PLEs)를 안전하게 유도할 수 있는지, 환각 성향(trait)과 상호작용하는지.
- **HOW**: anechoic chamber(빛·소리 완전 차단) 25분. 환각 성향 상·하위 20% 각 18명. 조건 3: baseline / 조용한 사무실(seclusion) / 박탈. PSI·AANEX 측정.
- **WHAT**: **양 집단 모두** 박탈에서 PLE 유의 증가 (조건 주효과). 성향 높은 집단은 perceptual distortions가 추가로 크게 증가 (**state × trait**). 서론의 이론 틀: 환각 성향 = "내부 생성 자극을 외부 출처로 오귀속"하는 경향; Corlett 등의 Bayesian 관점 = "**top-down 시스템이 noisy하고 예측 불가한 bottom-up 신호에 구조를 부과**"할 때 정신증적 증상 발생.

## 모델 구성요소별 판정

| mcbalance 요소 | 판정 | 상세 |
|---|---|---|
| 외부 채널 구조 `(1−alpha)·lambda_C` | **정교화(중요)** | 박탈은 dial(`alpha`)이 아니라 **채널 자체의 가용성**을 조작. 현 모델은 "기울기"와 "채널 가용성"을 곱으로 뭉쳐 놓았는데, 이 실험은 둘을 분리해서 검증 가능하게 함: `aC, sigC → 0` (박탈) vs `alpha → 1` (성향) |
| 예측 재현 가능성 | **지지 — Exp. 7 후보** | 모델 예측: `lambda_C` 소거 시 균형자(`alpha0=0.5`)도 내부 피드백 `r·sigmoid(L)`만 남아 믿음 표류(주효과), `alpha0`·`r` 높은 개체는 더 크게(상호작용). 관찰된 state×trait 패턴과 정확히 동형. **시뮬레이션으로 재현할 것** |
| rumination 항 | 지지 | 외부 교정 입력 부재 시 내부 구조 부과(top-down imposition)가 병리 생성 — 양성 피드백 서사와 합치 |

## Phase 4 함의 (핵심)

박탈 조건 = **closed-book LLM**: 접지(retrieval/context) 없이 생성하면 "균형 잡힌" 모델도 hallucination이 증가하고, self-conditioning이 강한 모델은 더 크게 증가한다는 예측으로 직역됨. 심리학 실험 설계(state×trait)를 LLM 벤치마크 설계(grounding 유무 × 모델 특성)로 이식 가능.

## 백로그

- **[신규 B-11, P1] Exp. 7 — 감각 박탈 시뮬레이션**: `aC=0, sigC→0` 조건에서 `alpha0 × r` 격자 스윕, PLE 대리 지표(임계 초과 빈도)로 state×trait 패턴 재현.
