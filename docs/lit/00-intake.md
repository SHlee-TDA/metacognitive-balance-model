# Phase 2 Intake — Zotero "Metacognition" 컬렉션 (Han 추천 reference)

- 반출: 2026-07-07, Zotero DB 읽기 전용 사본 (로컬 API 미활성 → 대체 경로; 원본 무변경)
- 컬렉션: `Metacognition` (12편, 원 논문 Han & Gu 2025 포함 → 검토 대상 11편)
- PDF: 모두 `내 드라이브/papers/`에 링크됨
- 인접 컬렉션: `LLM_dynamics_analysis` (15편) — Phase 4에서 별도 intake 예정

## 컬렉션의 구조 (읽기 전 관찰)

Han의 추천 목록은 세 축으로 나뉜다. 특기할 점: **감각 박탈 → 환각** 계열(D축)이
포함되어 있다는 것 — 이는 모델 언어로 "외부 채널 차단(`alpha → 1` 강제) 시 내부
양성 피드백이 환각적 신념을 생성한다"는 예측과 정확히 맞물리고, "훈련된 내부
지식에만 의존하는 LLM의 hallucination"이라는 Phase 4 교량의 심리학 측 앵커가 된다.
Han이 이미 그 방향을 가리키고 있다고 읽힌다 (디스커션에서 확인 가치).

| 축 | 문헌 | 모델 관련성 |
|---|---|---|
| A. 형식적 메타인지 이론 | Fleming & Daw 2017; Nelson & Narens 1990; Lieder & Griffiths 2017; Wells 2019 | `L`·confidence 정식화, monitoring–control 구조, pivot의 규범적 근거 |
| B. 조현병 임상 근거 | Wiesepape 2026 (scoping review); Lutgens 2017 (메타분석); Leucht 2025 (질환 리뷰) | 파라미터의 임상 타당성, minimal indices |
| C. LLM 교량 | De Boer 2026 (LLM 오류 ↔ 정신병리); Farquhar 2024 (semantic entropy) | Phase 4 직접 입력 |
| D. 외부 채널 박탈 → 환각 | Daniel 2014 (단기 감각 박탈); Merabet 2004 (장기 안대) | F3, `alpha` 극단 영역의 실증; hallucination 확장의 관문 |

## 검토 우선순위 (모델 영향 기준)

| 순위 | citekey | 문헌 | 검토 질문 (모델 구성요소) | 상태 |
|---|---|---|---|---|
| P0-1 | fleming2017 | Fleming & Daw, *Psych Review* | `L` log-odds + `c = \|2b−1\|` 정식화가 기존 Bayesian confidence 모델과 정합/경합하는가? 2차(second-order) 구조 필요성? | ✅ [메모](fleming2017.md) — 현 confidence는 "1차 모델"; 2차 구조 ρ=insight 파라미터 제안 (B-04) |
| P0-2 | nelson1990 | Nelson & Narens, metamemory | monitoring–control 2수준 구조: `dL/dt` 제어 법칙의 고전적 선례와의 대응 | ✅ [메모](nelson1990.md) — 2수준 구조 강한 지지; good regulator 정리 (Phase 4 앵커 B-10); meta/object(수직) ≠ self/context(수평) 주의 |
| P0-3 | wells2019 | Wells, cybernetic code (원문 ref [12]) | 메타인지 **제어 시스템** 관점의 선행 — 모델의 제어이론 선택이 심리학 내부 전통과 연속적인가? | ✅ [메모](wells2019.md) — 제어이론적 선택이 챕터 계보와 연속; threat monitoring이 F3(외부 채널 위협 확증)의 기제 제공 |
| P1-1 | daniel2014 | Daniel et al., 감각 박탈 | 외부 채널 차단 → 정신병 유사 경험: `alpha → 1` 극단의 실증; F3 | ✅ [메모](daniel2014.md) — state×trait 패턴 = 모델 예측과 동형; Exp. 7 후보 (B-11); closed-book LLM 유비 |
| P1-2 | merabet2004 | Merabet et al., 안대 환각 | 동일 주제 장기 버전; 환각 내용·시간 경과 | ✅ [메모](merabet2004.md) — 환각↔insight 해리가 B-04(2차 구조) 핵심 증거 |
| P1-3 | lieder2017 | Lieder & Griffiths, metareasoning | pivot을 "합리적 전략 선택"으로 규범화 가능한가? `u(t)`의 원리적 유도 | ✅ [메모](lieder2017.md) — pivot을 rational metareasoning으로 유도 가능; 히스테리시스 정리화 경로 (B-12) |
| **신규** | **sun2026** | **Sun et al., NeuroCogMap (arXiv 2607.00397, 사용자 추가)** | **LLM 내부 인지 지도 — Phase 4 직접 교량** | ✅ [메모](sun2026-neurocogmap.md) — hallucination=representation pathology, sycophancy=behavior-control pathology; mcbalance `L`/`alpha` 2축과 대응 (B-13). **residual stream 확인 대기** |
| P2 | wiesepape2026 / leucht2025 / lutgens2017 | 임상 근거 축 (scoping review / 질환 리뷰 / 음성증상 메타분석) | 배경 정확성; minimal indices 타당성; Exp. 6 효과 크기 현실화 | ✅ [통합 메모](P2-clinical-context.md) — 구조 변경 없음; Exp. 6 과대해석 방지(Lutgens SMD~0.3–0.5), Lysaker 4영역 매핑 |
| P0추가 | proust2012 | Proust, "Metacognition and mindreading" (사용자 추가) | 원문 §2.2 procedural/explicit 이중 구조 1차 출처 | ✅ [메모](proust2012.md) — AAM=accumulator가 `dL/dt` 계열 지지; opt-out=abstention 교량; 2013 book은 access 없음 |
| P0추가 | hanlee2022 | Han & Lee, MCI-S 원 논문 (사용자 추가) | Exp. 6 sequential policy 캐리커처의 타당성 검증 | ✅ [메모](hanlee2022.md) — T1 조치 타당성 확정; insight·환각 미개선이 B-04(2차 채널)의 임상 증거 |
| P4예습-1 | deboer2026 | De Boer et al., ChatGPT psychiatrist | LLM 오류 ↔ 정신병리 유비 지도 | ⬜ (Phase 4) |
| P4예습-2 | farquhar2024 | Farquhar et al., semantic entropy | hallucination 검출 = 불확실성 신호 | ⬜ (Phase 4) |

**Phase 2 문헌 검토 완료 (2026-07-07): 12편** (P0 3 + P1 3 + NeuroCogMap + Proust 2012 + Han & Lee 2022 + P2 3). 잔여는 Phase 4 예습 2편(deboer/farquhar)뿐 — Phase 4에서 수행.

## 메모 형식 (docs/lit/<citekey>.md)

WHY(문제의식)/HOW(방법)/WHAT(발견) 요약 → 모델 구성요소별 판정
(지지/반박/정교화, 대상: `L` 동역학 · `alpha` dial · rumination 항 · OU 노이즈 ·
leak · pivot · corridor · minimal indices) → 백로그 항목 → 용어집 신규 용어 →
Questions for Han 추가분.

## 원문 참고문헌과의 관계 (2026-07-07 갱신)

Han & Gu (2025)의 참고문헌 23편 중 원래 컬렉션과 겹치는 것은 Wells 2019 ([12])뿐 —
즉 Han이 협업(수리화+LLM)을 위해 **별도로 고른 목록**. 이후 보강됨:
- **사용자 추가**: Proust 2012 ([17]), Han & Lee 2022 MCI-S 원 논문 ([16]),
  NeuroCogMap (arXiv, 사용자 선택 — Han 추천 아님).
- **접근 불가**: Proust 2013 book ([18]) — 대형 서적, access 없음 → 2012 챕터로 대체.
- JTC 메타분석 ([3][4], Dudley/Ross)은 여전히 미보유 — Phase 2 후반 보강 여부 결정.

## 컬렉션 스코프 규칙 (사용자 지시, 2026-07-07)

- `LLM_dynamics_analysis` 컬렉션(15편)은 **다른 연구용** — 원칙적으로 미참고.
  **예외**: 이 연구에서 `residual stream` 키워드가 나올 경우에만 참고.
  → NeuroCogMap이 SAE(residual stream 가능성)를 쓰므로, Phase 4 정독 시 확인 후
  해당 시 편입 (sun2026 메모 "residual stream 확인 필요" 참조).
