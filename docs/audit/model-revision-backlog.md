# 모델 수정 백로그 (Phase 2 적립 → Phase 3 실행)

상태: `제안` → `Han 확인 대기` → `승인` → `구현` → `기각(사유)`

> **2026-07-08 Han 회신 반영** ([intake](../briefs/2026-07-08-han-feedback-intake.md)):
> B-02 **승인**(2층 구조 확정 — 사용자의 α 벡터화 제안으로 설계, [v2 설계](../model-v2-design.md)),
> B-03 **승인**(JTC 두 경로 분리 확정), B-04 **승인·확장**(insight = "해석을 관점으로
> 볼 수 있는가"로 조작적 정의 확보), B-05 **승인**(context-dominant JTC가 해당 기제).
> 신규: **B-16** Δ의 조작화(모델은 "Δ의 한 조작화"로 자칭; Δ = λ_S − λ_C, 부호 = 방향),
> **B-17** pivot 의미론 전환(교정 → reflective interval: 융합 정지 + 대안 개방),
> **B-18** social-other vs situational-context 채널 분리(장기),
> **B-19** 관점 구성 P — ~~창발적 readout~~ → **2026-07-15 사용자 지시로 세 번째 상태변수로 승격** (3-결합계; Han 메일이 독자 발전 허용. Δ 정의 불변 원칙은 유지),
> **B-20** action tendency / behavioral safety distance 행동 게이트(확신 ≠ 행동).

| ID | 우선 | 항목 | 근거 | 영향 범위 | 상태 |
|---|---|---|---|---|---|
| B-01 | P0 | 정오표 4건 + 톤 수정 (E1–E5, T1–T5, T8) | 감사 §4–5 | main.tex, model.md, README | **구현 완료** 2026-07-07 |
| B-02 | P1 | `alpha` zero-sum 사영 해소: 원고 한계 명시(완료) → 필요시 2D 상태 (tilt + 총 관여) | 감사 F1 | model.py, main.tex | Han 확인 대기 (Q1) |
| B-03 | P1 | Exp. 2 JTC 축 중립화 또는 내·외 이중 경로 | 감사 F2 | experiments.py | Han 확인 대기 (Q2) |
| B-04 | P1 | 2차 메타인지 구조: `L`과 상관 ρ의 별도 confidence 변수 `L_conf` — **ρ = insight 파라미터**. 현 `c = \|2b−1\|`은 Fleming & Daw의 "1차 모델"로, error detection과 수행–자기평가 해리(insight 결핍)를 구조적으로 표현 불가 | lit/fleming2017.md | model.py, metrics.py, main.tex | Han 확인 대기 (Q7) |
| B-05 | P2 | 외부 채널 위협 부합 성분 (`aC` 부호 변형 / 적대적 단서 사건) | 감사 F3 | model.py, experiments.py | Han 확인 대기 (Q3) |
| B-06 | P2 | 세션 간 slow dynamics: `alpha0`, `gamma`의 느린 시간 척도 방정식 | 감사 F4 | model.py | Han 확인 대기 (Q4) |
| B-07 | P2 | Exp. 5 미보정 원천 분리 실험 (기울기 vs 메타인지 잡음) | lit/fleming2017.md | experiments.py | 제안 |
| B-08 | P3 | 이산 5-step micro-cycle의 구조 반영 여부 검토 | 감사 F5 | model.py | 제안 |
| B-09 | P3 | `r`을 metacognitive belief 의존 파라미터로 해석하는 주석 (치료=파라미터 변경) | lit/wells2019.md | main.tex | 제안 |
| B-10 | Phase4 | good regulator 정리를 LLM bridge 이론 축으로: "hallucination 제어기 = 생성기 모델 내장" | lit/nelson1990.md | docs/llm-bridge.md | 제안 |
| B-11 | P1 | **Exp. 7 — 감각 박탈 시뮬레이션**: `aC=0, sigC→0`에서 `alpha0 × r` 격자 스윕, state×trait 패턴 재현 (Daniel 2014 / Merabet 2004 실증 대응) | lit/daniel2014.md, merabet2004.md | model.py, experiments.py | 제안 (강력) |
| B-12 | P2 | pivot의 메타추론적 유도: 전환 비용 하 VOC 최적 정책 vs PivotLatch — 히스테리시스 창발 검증 | lit/lieder2017.md | model.py | 제안 |
| B-13 | Phase4 | mcbalance `L`/`alpha` 2축 ↔ NeuroCogMap representation/behavior-control 2병리축 정합; sycophancy=over-ext, self-conditioning=over-int 검증 | lit/sun2026-neurocogmap.md | docs/llm-bridge.md | 제안 |
| **B-14** | **P0(문서)** | **★Exp. 5 tolerance 서술이 코드/그림과 정반대**. 코드 재실행값(exp5_indices.png): over-int **1.7**(가장 빨리 커밋) / balanced **8.8**(중간) / over-ext **17.4**(가장 오래 버팀). 본문은 "balanced가 가장 tolerant, over-ext가 가장 빨리 커밋"이라 서술 — 둘 다 틀림. 그림 suptitle "balanced가 두 지표 모두 최고"도 절반만 참(calibration만). **기존 버그**(이번 교정 무관), double-check로 발견. F2/Q2(JTC 축 귀속)와 직접 연결 | 코드 재실행 2026-07-07 | main.tex Exp.5, experiments.py suptitle | **완료** (2026-07-07, 본문·그림·suptitle 정정) |
| **B-15** | **P0(문서), 완료** | **★Exp. 4의 벡터장은 모델(L,α)에서 유도된 것이 아니라 손으로 만든 삽화**. `experiments.py`의 `field(x,y)`는 `(x,y)`=(self,context) 0–100 평면에서 대각선·중심(50,50)으로 당기는 힘을 계수(0.15, 0.05)로 직접 설계한 것 — `dL/dt`, `dα/dt`(식 6–7)와 무관. 원인은 F1과 동일: 실제 α는 simplex 위 1차원이라 챕터 Fig.2의 2차원 평면 자체를 표현할 자유도가 없음. 사용자가 재검토 중 질문해 발견 | 사용자 질문 2026-07-07 | main.tex §3.4 본문·캡션 | **완료** (2026-07-07, 본문·캡션에 "모델 유도 아님, 챕터 Fig.2의 삽화" 명시) |

## ★ B-14 상세 (commit 전 결정 필요)

**사실관계** (kappa 포함 정확한 exp5 regime 파라미터로 재실행):
| regime | ECE | tolerance (커밋까지 시간) |
|---|---|---|
| over-internalizing (α₀=0.85, κ=0.20) | 0.46 (높음, 확신 오류) ✓본문일치 | **1.7 (가장 빨리 커밋)** |
| balanced (α₀=0.50, κ=0.30) | 0.17 (최저, 최선 보정) ✓본문일치 | 8.8 (중간) |
| over-externalizing (α₀=0.15, κ=0.30) | 0.42 (높음) | **17.4 (가장 오래 버팀)** |

- **ECE(그림 a) 서술은 정확** — balanced 최선 보정, over-int 확신 오류. 이 부분 문제 없음.
- **tolerance(그림 b) 서술만 틀림.** 본문: "balanced가 가장 ambiguity-tolerant … over-externalizer가 가장 빨리 커밋(JTC)". 코드: 정반대(over-int이 가장 빨리 커밋, over-ext가 가장 오래 버팀).
- **모델은 내부적으로 일관**: over-int이 빠르게 커밋하는 것은 Exp. 2(JTC를 고 α₀로 구현)와 정합. 즉 **코드는 감사 F2가 지적한 "JTC=over-internalization" 구현을 따르고, 본문 서술만 챕터(JTC=over-externalization)에 맞추려다 그림과 어긋남.**
- 개념적으로 "모호(무정보) 자극에서 오래 안 버티는 것"이 반드시 병리도 아님 — "balanced가 tolerance 1등"이라는 전제 자체가 모델에서 성립 안 함.

**해소 옵션**:
- (A) 본문을 **그림에 맞게** 정정: over-int이 가장 빨리 커밋(=JTC), over-ext가 가장 오래 버팀, balanced 중간. "두 지표 모두 최고" 서사 폐기, "두 지표가 regime을 **분리**한다"로 약화. 그림 suptitle도 수정. → Han 불필요, 정직. 단 논문의 "balance가 최선" 중심 서사 약화.
- (B) **모델을 챕터에 맞게** 수정(JTC를 over-ext로): F2/Q2의 Han 답변 필요. Phase 3 사안.
- (C) 지금은 (A)로 정직하게 서술 정정 + F2/Q2 열린 질문임을 명시, 모델 수정은 Han 답변 후. **권장** — commit 전에 최소한 그림과 모순되는 서술은 고쳐야 함.

## Phase 2 종합 관찰

문헌 검토가 **모델의 큰 방향을 지지**하되 두 개의 구조적 확장을 반복적으로 가리킨다:

1. **2차 메타인지 채널 (`L_conf`, B-04)** — Fleming & Daw(1차/2차 구분), Nelson & Narens(monitoring 다차원), Merabet(환각↔insight 해리)가 **독립적으로 같은 결론**으로 수렴. 이 확장이 조현병 insight 결핍(원문 미포착 변수)과 Phase 4의 hallucination-검출 채널을 **동시에** 연다. → Phase 3 최우선 후보.
2. **외부 채널의 threat 확증 모드 (B-05, F3)** — Wells(threat monitoring), Daniel(외부 오귀속)이 `aC ≤ 0` 가정의 한계를 지지.

또한 pivot·히스테리시스가 임의 장치가 아니라 rational metareasoning의 정리로 **격상 가능**(B-12)하다는 경로가 열렸다. 모든 확장은 Han 답변 대기 항목과 얽혀 있으므로 브리프 회신 후 Phase 3 착수 권장.
