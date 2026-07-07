# Phase 2 종합 — 12편 문헌이 mcbalance 모델에 대해 말하는 것

*2026-07-07. 개별 메모(docs/lit/*.md)의 상위 종합. Phase 3 개정과 note 작성(제안 1)의 근거표.*

## 1. 한 문장 결론

문헌 검토는 **모델의 제어이론적 골격이 심리학 내부 전통과 연속적임을 확인**하는 한편,
서로 독립적인 여러 문헌이 **동일한 두 확장** — (A) 2차 메타인지 채널, (B) 외부 채널의
위협 확증 모드 — 으로 수렴한다. 어느 것도 모델을 뒤집지 않으며, 둘 다 원문(Han)이
미포착했다고 감사에서 표시한 변수(insight, 편집적 외재화)를 정확히 겨눈다.

## 2. 모델 구성요소 × 문헌 근거 매트릭스

기호: ✔ 지지 / ✎ 정교화·확장 / ✘ 반박·한계. (제안 1의 문장별 인용에 그대로 사용)

| 모델 구성요소 | 지지 문헌 | 방향 |
|---|---|---|
| 믿음 = 확률 `L` (log-odds) | Fleming & Daw 2017 ✔; Proust 2012 (AAM=accumulator) ✔ | 신호검출·누적기 전통과 동일 계열 |
| 메타인지 = 제어, `dL/dt` rate law | Nelson & Narens 1990 ✔; Wells 2019 ✔; Proust 2012 ✔ | meta/object 2수준·comparator·AAM이 모두 제어 형식 |
| confidence `c = \|2b−1\|` | Fleming & Daw 2017 ✘; Nelson & Narens 1990 ✎; Merabet 2004 ✘; Han & Lee 2022 ✘ | **현 정의는 "1차 모델"** — 2차 채널 필요 (핵심 발견) |
| self–context 배분 `alpha` (simplex) | Wiesepape 2026 ✎ (Lysaker 4영역) | 4영역 중 self-reflectivity/decentration 축과 대응; F1(전체 수준) 미해결 |
| rumination `r·sigmoid(L)` | Wells 2019 ✎; Nelson & Narens 1990 ✔; Daniel 2014 ✔ | 자기 감시 출력의 재입력; belief 의존 파라미터로 재해석 |
| 외부 채널 `aC ≤ 0` | Wells 2019 (threat monitoring) ✘; Daniel 2014 ✘ | 위협 **확증** 모드 부재 — F3, B-05 |
| pivot `u(t)` / 히스테리시스 | Lieder & Griffiths 2017 ✎; Nelson & Narens 1990 ✔; Proust 2012 (Hampton 4조건) ✔ | rational metareasoning으로 유도 가능; 히스테리시스 정리화 경로 |
| corridor / balance 목표 | Wiesepape 2026 ✔; Leucht 2025 (E/I 균형 은유, 과잉해석 주의) ✎ | 기능 결과의 매개 경로로서 정당 |
| minimal indices (Exp. 5) | Fleming & Daw (ECE 분해) ✎; Proust 2012 (opt-out) ✎; Wiesepape 2026 ✔ | 측정 타당성 + LLM abstention 교량 |
| Exp. 6 sequential vs balance | Han & Lee 2022 ✎; Lutgens 2017 ✎ | 캐리커처임을 명시(T1); 효과 크기 과대해석 방지 |

## 3. 두 개의 수렴 (Phase 3 최우선)

### 수렴 A — 2차 메타인지 채널 `L_conf` (백로그 B-04)
네 문헌이 **독립 경로로 같은 결론**:
- **Fleming & Daw**: 현 `c`는 1차 모델 → error detection·수행–자기평가 해리 표현 불가.
- **Nelson & Narens**: monitoring은 다차원(EOL/JOL/FOK 비상관).
- **Merabet 2004**: 건강인 박탈 환각에서 **환각 내용 ↔ insight 해리** (환각하되 가짜임을 앎).
- **Han & Lee 2022**: MCI-S가 delusion·social cognition은 개선했으나 **insight·환각은 미개선** — 1차 개입이 못 건드리는 변수.

→ `L`과 상관 ρ의 별도 confidence 변수 도입 시 **ρ = insight 파라미터**. 이 하나가
조현병 insight 결핍(원문 미포착) + Phase 4 hallucination-검출 채널을 **동시에** 연다.
측정 앵커: Beck Cognitive Insight Scale(= self-reflection − self-certainty, Han & Lee).

### 수렴 B — 외부 채널 위협 확증 모드 (백로그 B-05, 감사 F3)
- **Wells 2019**: CAS의 threat monitoring = 환경 위험 능동 스캔.
- **Daniel 2014**: 환각 성향 = 내부 생성 자극의 외부 오귀속.
→ `aC`가 주의 전략/상태에 따라 부호를 바꿀 수 있어야. (Han Q3 답변과 연동)

## 4. 규범적 격상 기회

- **pivot/히스테리시스 → 정리**: Lieder & Griffiths의 rational metareasoning(VOC − 전환비용)으로
  pivot을 유도하면, 히스테리시스(engage/release 분리)가 **자원 합리적 최적 정책으로 창발**할
  가능성 (B-12). 성립 시 EXTRAPOLATED → 정리. Han Q5의 수학 측 답.
- **good regulator 정리** (Nelson & Narens, Conant & Ashby): "제어기는 피제어계의 모델을
  내장" → Phase 4에서 "hallucination 제어기 = 생성기 모델 내장"의 이론 축 (B-10).
  ※ Proust 2012 각주 2가 이 정리를 재해석(메타표상 불필요)하므로 인용 전 결론부 확인.

## 5. Phase 4(LLM) 예비 교량 — 이미 드러난 것

| 심리학(모델) | LLM | 근거 문헌 |
|---|---|---|
| 외부 채널 소거(감각 박탈) → 내부 생성 폭주 | closed-book/무접지 생성 → confabulation | Daniel 2014, Merabet 2004 |
| over-externalization(단서 과의존) | **sycophancy** (사용자/맥락 과동조) | Sun 2026 (behavior-control pathology) |
| over-internalization(자기강화 반추) | self-conditioning / error snowballing | Sun 2026 (representation pathology) |
| tolerance of ambiguity / opt-out | **abstention** | Proust 2012, Farquhar 2024(예정) |
| 2차 confidence 채널 (insight) | hallucination 검출 신호 (semantic entropy) | Fleming & Daw, Merabet, Farquhar(예정) |
| pivot 발동 정책 | retrieval/self-check trigger (VOC) | Lieder & Griffiths |
| `L`/`alpha` 2축 | representation / behavior-control 2병리축 | Sun 2026 (검증축 B-13) |

`residual stream` 확인 대기: NeuroCogMap의 SAE 부착 지점 확인 후, 해당 시에만
LLM_dynamics_analysis 컬렉션 편입 (사용자 지시).

## 6. Han 디스커션 큐 누적 (브리프용)

1호 발송 대기분 Q1–Q6 (briefs/2026-07-07) + Phase 2 추가:
- Q7 (Fleming & Daw): 수행–자기평가 해리(insight)와 증거 처리 기울기는 별개 현상인가?
- Q8 (Wells): balance 관점과 MCS의 역할 분담(제어기 해부학 vs 제어 목표 기하학)?
- Q9 (Sun): sycophancy=over-ext, self-conditioning=over-int 유비가 임상적으로 자연스러운가?
- Q10 (Han & Lee): MCI-S에서 insight 미변화 = 기간 부족인가, 다른 표적(2차 채널)이 필요한 신호인가?
