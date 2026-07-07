# Sun et al. (2026) — NeuroCogMap Reveals Cognitive Organization of Large Language Models

*arXiv:2607.00397 (q-bio.NC), 2026-07-01. 82면. **사용자(이성헌)가 직접 추가 — Han 추천 아님.***
*검토: 2026-07-07. 정독: pp.1–4 (초록·서론·Fig 1–2 개념·결과 개요). **방대하여 나머지는 Phase 4에서 정독 예정** (아래 "정독 대기" 참조).*

## 왜 이 논문이 우리 연구의 교량인가 (사용자 직관 확인)

이 논문은 우리가 Phase 4에서 하려는 것 — 메타인지 구조를 LLM 작동영역으로 해석하고 hallucination을 다루는 것 — 을 **경험적으로 이미 절반 수행**했다. 우리 연구와의 관계:

- **우리(mcbalance)**: 챕터의 심리 이론 → 최소 제어이론 모델(top-down). "hallucination은 왜/언제 생기는가"를 **동역학으로 설명**.
- **NeuroCogMap**: 실제 LLM 내부 특징 → 인지 기능 지도(bottom-up, 데이터 주도). "hallucination이 내부 **어디서** 일어나는가"를 **측정**.

→ 두 접근이 **동일 대상(LLM hallucination)을 위·아래에서** 만난다. NeuroCogMap이 우리 모델의 구성요소에 **측정 가능한 내부 좌표**를 줄 수 있다.

## WHY / HOW / WHAT

- **WHY**: LLM의 광범위한 인지 유사 행동이 내부 표상에서 **재현 가능한 기능 시스템**을 이루는지 불명. 행동 평가는 "무엇을 하는지"만, mechanistic 연구는 국소만 본다 — **시스템 수준** 지도가 부재.
- **HOW**: 인지신경과학의 뇌 지도화 이식. ① SAE(sparse autoencoder)로 내부 특징 추출 → task-evoked 프로파일로 군집 → **functional atlas**(270 parcels). ② parcel에 해석 가능 기능 부여(**cognitive atlas**). ③ perception→representation→abstraction→application의 **cognitive hierarchy**. 모델: Gemma2-2B/9B-IT, Llama-3.1-8B, Pythia(스케일링).
- **WHAT (우리 연구 직결)**:
  - **주요 실패(hallucination, bias, refusal failure, sycophancy)가 서로 구분되는(dissociable) 표상·행동제어 시스템의 교란에 대응** → 기제 유도 검출·개입 가능.
  - **Fig 1e "Pathology Mode"**: hallucination·bias = **representation pathology**; sycophancy·refusal = **behavior-control pathology**. ★두 축 분리는 우리 모델의 **`L`(표상/믿음) 축 vs `alpha`·pivot(제어) 축** 구분과 구조적으로 대응.
  - parcel 활동이 자연어 이해 시 인간 피질 반응 예측 개선(고차 연합피질과 최강 정합).
  - 내부 인지 서명이 고전 의사결정 모델(dual-systems) 정련 — Lieder & Griffiths 계열과 연결.

## 모델 구성요소별 판정 (예비 — Phase 4에서 확정)

| mcbalance 요소 | 판정 | 상세 |
|---|---|---|
| `L` (표상/믿음) 축 | **경험적 정착 후보** | NeuroCogMap의 "representation pathology"(hallucination 소재) = `L` 동역학의 실측 대응. hallucination을 표상 축 사건으로 보는 우리 가정과 합치 |
| `alpha`·pivot (제어) 축 | **경험적 정착 후보** | "behavior-control pathology"(sycophancy=과잉 외부 순응, refusal) = 제어 축 사건. **sycophancy ≈ over-externalization**(맥락/사용자 단서 과의존), **rumination/self-conditioning ≈ over-internalization** 가설의 내부 좌표 제공 가능 |
| 2차 채널 `L_conf` (B-04) | 지지 방향 | 실패의 **검출**이 기제 유도로 가능하다는 결과 = 생성과 분리된 모니터링 신호의 실재 |
| corridor / balance | 확장 후보 | "표상 병리 ↔ 행동제어 병리"의 균형 영역으로 재해석 가능성 |

## ★ residual stream 확인 필요 (사용자 지시 관련)

사용자 지시: "residual stream 키워드가 나오면 LLM_dynamics_analysis 컬렉션을 참고하라." NeuroCogMap은 SAE를 사용하며 통상 **residual stream** 활성에서 특징을 추출한다. **정독 대기 항목**: Methods에서 SAE 부착 지점(residual stream 여부)을 확인하고, 그렇다면 LLM_dynamics_analysis에서 residual stream 관련 문헌을 Phase 4 intake에 편입할 것.

## 정독 대기 (Phase 4)

- Results 전체(pp.5–), 특히 Pathology Attribution/Detection/Mitigation 정량 결과 — 우리 pivot(개입) 설계의 경험적 대응.
- Methods: SAE 부착 지점(residual stream), parcellation·intervention 프로토콜.
- 인간 피질 정합(Fig 1f) — 심리학 앵커 재확인.

## 백로그 / Phase 4 시드

- **[신규 B-13, Phase 4] 매핑 검증축**: mcbalance의 `L`/`alpha` 2축 ↔ NeuroCogMap의 representation/behavior-control 2병리축을 정합 가설로 등록. sycophancy=over-externalization, self-conditioning hallucination=over-internalization 대응을 검증 가능 예측으로 전개.
- llm-bridge.md 초안의 매핑 표에 NeuroCogMap 좌표 열 추가.

## Questions for Han 추가분

9. (Phase 4용) sycophancy(사용자에 과잉 동조)를 over-externalization의 LLM판으로, 자기강화적 confabulation을 over-internalization의 LLM판으로 보는 유비가 임상적으로 자연스러운가요? 두 실패의 심리학적 원형이 실제로 그렇게 나뉘나요?
