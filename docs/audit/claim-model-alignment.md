# Phase 1 감사 — 모델·원고 vs 원문 정합성 (Claim–Model Alignment)

- **감사 대상**: `docs/model.md` provenance 표 13행 + `paper/main.tex` (375행) 전체
- **기준 문헌**: Han & Gu (2025), IntechOpen chapter 전체 16면 정독 (2026-07-07)
- **등급**: `FAITHFUL`(원문 직접 지지) / `INTERPRETIVE`(합치하나 수학적 선택 개입, Han 확인 필요) / `EXTRAPOLATED`(원문 범위 밖 확장)

## 1. 총평

원고는 원문을 성실하게 추적하고 있으며, 인용문(fromtext 박스) 10건은 모두 원문과 **문자 그대로 일치**함을 확인했다. 톤은 전반적으로 매우 존중적이다("interpretation, not a competing theory", plain-language 박스, Status 문단). 다만 **구조적 쟁점 2건**(F1, F3)과 **귀속 쟁점 1건**(F2)은 Han과의 디스커션 없이 넘어가면 안 되는 수준이고, 페이지 표기 오류 3건과 톤 개선 포인트 몇 건이 있다.

## 2. 실질 발견 (substantive findings)

### F1 — ★최우선: 1차원 dial `alpha`는 원문 Fig. 2의 기하학과 다르다

- **원문**: Fig. 2 (p.8)의 축은 self-awareness(x)와 context/other-awareness(y), 각각 0–100의 **독립 축**이다. adaptive corridor는 **대각선 y = x 주변의 띠** — 즉 (20,20)도 (80,80)도 corridor 안이다. p.8: "redefines the goal of metacognition from strengthening a single function to **mutual constraint and cooperation between the axes**." 균형 = 어느 수준에서든 두 축의 **동반 성장·상호 견제**이지, 고정 예산의 배분이 아니다.
- **모델**: `alpha ∈ [0,1]`, context 가중치 = `1 − alpha`. 이는 **zero-sum 제약** (simplex) — self가 커지면 context가 반드시 작아진다. 원문 평면의 반(反)대각선 방향 성분(tilt)만 포착하고, 대각선 방향 성분(**전체 관여 수준**, both-high vs both-low)은 소실된다.
- **원고의 처리**: §2.3 "on the simplex these are the two coordinates that you wrote, but **one number suffices**" — 과잉 주장. Exp. 4는 별도의 2차원 벡터장으로 Fig. 2를 렌더링하므로 코드베이스 스스로 이 불일치를 우회하고 있다.
- **판정**: `INTERPRETIVE` (사영으로서는 정당하나, 명시가 필요). **수정 제안**: (a) 원고에서 "alpha는 corridor-횡단 좌표(tilt)만 모델링하며, corridor-종단 좌표(전체 메타인지 관여도)는 본 모델의 범위 밖"임을 명시, 또는 (b) 상태를 (`alpha_self`, `alpha_context`) 2차원으로 확장. → **Questions for Han Q1**

### F2 — JTC의 축 귀속: 원문은 JTC를 over-externalization 쪽에 둔다

- **원문**: "feeling = fact → premature closure (JTC)" 문장(p.5)은 **over-externalization 문단** 안에 있다. p.8도 over-externalization을 "over-interpretation, over-inference, and the 'feeling = fact' shortcut"으로 특징짓고, Table 2(p.11)는 낮은 tolerance of ambiguity를 "external avoidance/**jumping-to-conclusions** tendency"로 해석한다.
- **모델/원고**: Exp. 2는 JTC를 **높은 `alpha0`(자기 기울기) + 작은 `kappa`** 구성 — 즉 over-internalization 형상으로 구현했다. 원고 §2.1은 p.5 인용문을 over-externalization 맥락 표시 없이 사용한다. 한편 Exp. 5는 over-externalizer가 가장 빨리 커밋한다고 보고(p.11–12와 일치) — **원고 내부에서도 Exp. 2와 Exp. 5의 JTC 서사가 어긋난다.**
- **완화 요인**: p.9의 "confidence gain"(증거 대비 확신 상승률)은 축과 독립적인 파라미터로 정의되므로, "JTC = confidence gain 과대"라는 원고의 읽기 자체는 지지 가능하다. 문제는 높은 `alpha0`를 함께 쓴 데서 생기는 채색이다.
- **판정**: `INTERPRETIVE`, 내부 비일관성 있음. **수정 제안**: Exp. 2를 (i) 축 중립적 구성(작은 `kappa`만 조작, `alpha0 = 0.5`)으로 바꾸거나 (ii) 내·외 두 경로의 JTC를 나란히 보이기. → **Q2**

### F3 — over-externalization = "양성 노이즈 추적"은 원문 병리의 절반만 포착

- **원문**: p.5 over-externalization은 "hyper-suspiciousness, and **threat interpretations (externalizing/personalizing attributions) are reinforced**", p.7 "hyper-mentalizing others' intentions, over-inference" — 외부 단서(소문 포함)에 의해 **위협 해석이 강화**될 수 있다.
- **모델**: `lambda_C = aC + xi(t)`에서 `aC ≤ 0`(단서는 위협을 반증하는 경향) — 외부 채널이 본질적으로 교정적이다. 따라서 낮은 `alpha`에서는 erratic한 저신념만 나오고, **편집증적 과잉추론(외부 기원 위협 신념)은 구조적으로 생성 불가능**하다.
- **판정**: `INTERPRETIVE` (단일 시나리오의 선택으로는 정당하나, over-externalization 병리의 서술 범위보다 좁음). **수정 제안**: 외부 채널에 위협 부합 성분(예: `aC`의 부호/시변, 또는 적대적 단서 사건)을 허용하는 변형 실험. → **Q3**

### F4 — 시간 다층성(temporal multilayering): 세션 간 `alpha0`, `gamma` 재보정 미구현

- **원문**: p.8, p.10 §4.2 — 세 시간 척도(세션 내 교정 / **세션 간 set-point·gain 재보정** / 일상 일반화). p.10은 문자 그대로 "between-session recalibration of the **control-theoretic set point and gain**"이라 쓴다(모델의 `alpha0`, `gamma` 명명에 대한 강한 FAITHFUL 앵커이자, 미구현 slow dynamics의 명시적 초대장).
- **원고의 처리**: Discussion limitation 문단이 fast/slow 구분을 이미 인정 — 양호. 다만 `d(alpha0)/dt` 느린 방정식은 자연스러운 다음 구조 확장. **판정**: 현 상태 `FAITHFUL`(범위 명시됨), 확장 후보. → **Q4**

### F5 — 연속 제어 `u(t)` vs 원문의 이산 5-step micro-cycle

- **원문**: Fig. 1(p.5) + fn.2(p.6) — micro-cycle은 ①confidence 평가 ②대안 2–3개 생성 ③핵심 증거 대조 ④맥락 단서 재가중 ⑤confidence 재보정의 **이산 절차**이며, pivot은 어느 단계에서든 ⑤로 라우팅한다.
- **모델**: 연속시간 피드백 항 `u(t)`로 근사. ②③(대안 생성, 증거 대조)의 내용적 단계는 대응물이 없다.
- **판정**: `INTERPRETIVE` (합리적 추상화; 원고 §2.7이 "repeated application of this loop"로 연결하고 있으나, 이산 구조의 소실은 명시할 가치).

### F6 — 히스테리시스(PivotLatch)는 원문에 없는 추가

- 원고 §2.7과 Discussion이 이미 명시적으로 밝히고 동기(chattering 방지)를 설명 — **모범적 처리**. **판정**: `EXTRAPOLATED`(선언됨). 임상 실무와의 부합 여부는 Han 확인. → **Q5**

## 3. Provenance 표 13행 등급

| # | model.md 행 | 등급 | 비고 |
|---|---|---|---|
| 1 | 통합+조절 (p.1) | FAITHFUL | 인용 일치 |
| 2 | 믿음=확률, JTC=조기 종결 (p.5) | FAITHFUL / **주의** | 확률 표현은 지지; JTC 맥락은 F2 |
| 3 | 메타인지=제어 → rate law (p.3) | FAITHFUL | p.10 "control-theoretic set point and gain"이 추가 지지 |
| 4 | confidence 절차 신호 | FAITHFUL + errata | 인용 위치 **p.2 → p.3** 정정; fluency·effort 1차원 축약은 INTERPRETIVE |
| 5 | self–context dial `alpha` (p.7) | **INTERPRETIVE** | F1 — zero-sum 사영 |
| 6 | 동시 결합 시스템 (abstract/p.2) | FAITHFUL | |
| 7 | rumination 항 `r·sigmoid(L)` (p.4–5) | INTERPRETIVE | "finding the cause within"의 양성 피드백 독해는 그럴듯한 도약 — Han 확인 가치 |
| 8 | over-externalization = 단서 추적 (p.5) | **INTERPRETIVE** | F3 — 적대적 과잉추론 미포착 |
| 9 | pivot `u(t)` 피드백 제어 (p.6 fn.3) | FAITHFUL | 히스테리시스는 F6 (EXTRAPOLATED, 선언됨) |
| 10 | 4대 제어 파라미터 (p.9) | FAITHFUL | 가장 강한 앵커 |
| 11 | set-point·gain·성격 (p.8) | FAITHFUL | F4 — 세션 간 재보정은 미래 확장 |
| 12 | adaptive corridor attractor (p.7–8) | INTERPRETIVE | attractor 독해 자체 + F1 기하학 |
| 13 | minimal indices (p.**7**) | FAITHFUL + errata | 페이지 **p.6 → p.7** 정정; ECE 조작화는 INTERPRETIVE(합리적) |

## 4. 인용·페이지 정오표 (errata)

| 위치 | 현재 | 정정 |
|---|---|---|
| main.tex §2.2 fromtext, model.md 행4 | Proust "monitors and corrects…" **p.2** | **p.3** (§2.2) |
| main.tex Exp. 5 헤더, model.md 행13 | minimal indices **p.6** | **p.7** ("Minimal evaluation suffices…") |
| main.tex Exp. 5 본문 | Table 2 해석 힌트 **p.12** | **p.11** (Table 2 소재 면) |
| main.tex Exp. 3 | "loop must be brief and iterated (p.5)" | **p.6** ("stop-check-shift routines should be iterated multiple times within sessions") |
| main.tex 내부 참조 | §2.4 "the leak of §1" — κ는 §1 표기표에만 등장, 도입 서술 없음 | 내부 참조 정리 |

## 5. 톤 검토 (Han의 주장에 대한 존중)

**긍정**: provenance 인용 박스 + plain-language 박스의 이중 구조, "not a competing theory", "The tune should be recognizably yours", Status 문단("a candidate formal specification of the kind the authors reserved for future work… a shared, runnable object we can now poke at together")은 원문 p.7("details of the formal specification … are reserved for a separate peer-reviewed article")과 p.14("offered as a conceptual direction rather than a formal model")를 정확히 존중한다. §4.1 scope note의 fast/slow 경고를 limitation에 반영한 것도 좋다.

**개선 권고** (우선순위순):

| # | 위치 | 문제 | 권고 |
|---|---|---|---|
| T1 | Exp. 6 / Discussion | "sequential policy"가 MCI-S의 캐리커처임을 원고가 명시하지 않음 — MCI-S는 Han의 실증 프로그램(망상 감소·사회기능 개선, p.2)이며 원문도 "preserves the core strengths of MCI-S"(p.4, 7)를 강조. 현재로선 "Han의 기존 프로그램이 0.84 대 0.12로 패배"로 읽힐 위험 | Exp. 6에 한 문장: 비교 대상은 피드백 없는 게이트라는 **의도적 극단화**이지 실제 임상의 MCI-S가 아니며, 결과는 원문 자신의 서열→균형 논증(§2.4)의 정량화임을 명시 |
| T2 | §2.3 (line ~169) | "…that you wrote, but **one number suffices**" — Han의 표현을 교정하는 뉘앙스 + F1상 기술적으로도 과잉 주장 | "충분하다" 대신 tilt 성분만의 사영임을 인정하는 서술로 교체 |
| T3 | §2.5 | "the mathematical signature of **a delusion becoming fixed**" — 원문은 "potentially intensifying … delusional interpretations"로 신중함 | "delusion-like fixity"(Exp. 1의 표현) 수준으로 헤지 |
| T4 | line ~194 | "(Note: in your draft both lines … were typeset as dX/dt)" — 챕터에는 수식이 없으므로 지시 대상 불명; Han의 미공개 초안 지적이라면 원고가 아닌 사적 브리프로 전달할 사안 | 원고에서 제거, 브리프로 이동 |
| T5 | abstract | "takes their **verbal** framework at face value" — 미묘하게 격하 뉘앙스 | 원문 자신의 용어 "conceptual"로 교체 |
| T6 | 전반 | 2인칭("your Figure 2", "your abstract") — 협업 노트로는 적절하나 투고본에서는 전환 필요 | 노트/논문 이원 트랙 결정 |
| T7 | 제목/본문 | Han이 p.7에서 부여한 작업명 "**Metacognitive Balance Theory** (working name)"를 원고가 사용하지 않음 | 명명을 채택·인용하면 우선권 존중이 명확해짐 |
| T8 | 저자란 | "[Your name]" 플레이스홀더 | 실명 기입 |

## 6. 원문에 있으나 모델에 없는 것 (uncovered claims)

- fluency·effort (confidence 외 절차 신호, p.3, p.9) — 1차원 축약 선언됨
- 상태 요인: 수면·스트레스·투약이 tilt·역치를 변화 (p.9) — `alpha0(t)` 시변으로 부분 수용 가능
- 보조 지표: cue-utilization ratio, JTC tendency (p.9)
- 급성기 인지부하 관리: 대안 1–2개 제한, self-work 시간 제한 (p.13 §5.4) — 제어 제약으로 번역 가능
- insight(병식)·환각: 원문 p.2가 MCI-S에서 제한적 변화를 보고한 바로 그 변수들 — 모델 밖 (원고 limitation이 hallucination 부재는 명시)
- 교육 장면 적용 (p.12 §5.2) — LLM bridge에서 오히려 유관해질 수 있음

## 7. Questions for Han (디스커션 안건 큐)

1. **[F1]** Fig. 2에서 self·context awareness가 **동시에 높은** 상태(예: 80, 80)는 임상적으로 어떤 상태인가요? 균형은 "수준 불문 등가(parity)"인가요, 총 관여량이 고정된 배분인가요? — 모델의 1차원 dial 유지 vs 2차원 확장을 가르는 질문
2. **[F2]** JTC는 선생님 관점에서 주로 over-externalization의 현상인가요(p.5, p.8, Table 2), 축과 무관한 confidence gain의 문제인가요, 아니면 양쪽 경로가 모두 있나요?
3. **[F3]** over-externalization에서 외부 단서가 위협 해석을 **강화**하는 경우(소문, hyper-mentalizing)와 단순히 이리저리 끌려다니는 경우 — 어느 쪽이 일차적인가요?
4. **[F4]** 세션 간 set-point/gain 재보정(p.10)을 느린 시간 척도 방정식으로 넣는 것이 다음 단계로 적절할까요?
5. **[F6]** pivot에 engage/release 임계를 분리한 것(한번 개입하면 불균형이 확실히 해소될 때까지 유지)이 실제 임상 감각과 맞나요?
6. **[T7]** "Metacognitive Balance Theory"라는 작업명을 이 formalization에도 사용해도 될까요?

## 8. Phase 3 백로그 시드 (우선순위 초안)

| 우선순위 | 항목 | 근거 | 영향 범위 |
|---|---|---|---|
| P0 | 정오표 4건 반영 | §4 | main.tex, docs/model.md |
| P0 | T1 (MCI-S 캐리커처 명시), T3, T4, T5 톤 수정 | §5 | main.tex |
| P1 | F1: alpha 사영 명시 또는 2D 확장 | Han Q1 답변 후 | model.py, main.tex |
| P1 | F2: Exp. 2 축 중립화 또는 이중 경로 | Han Q2 답변 후 | experiments.py |
| P2 | F3: 외부 채널 위협 부합 변형 실험 | Han Q3 답변 후 | model.py, experiments.py |
| P2 | F4: 세션 간 slow dynamics | Han Q4 답변 후 | model.py |
