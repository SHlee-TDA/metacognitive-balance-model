# 연구 파이프라인 — Metacognitive Balance 수리모델 검증 → LLM Hallucination 적용

> 이 문서는 이 연구의 마스터 플랜이자 진행 상태 추적 문서입니다.
> 각 Phase가 끝날 때마다 체크포인트에서 사용자 확인 후 다음 Phase로 진행하며,
> 상태 표시(`[ ]` → `[x]`)와 결정 로그를 이 문서에 직접 갱신합니다.

---

## 1. 연구 개요

| 항목 | 내용 |
|---|---|
| 출발점 | Han & Gu (2025) *Toward Metacognitive Balance* (IntechOpen, doi:10.5772/intechopen.1012821) |
| 현재 자산 | `mcbalance` 제어이론 모델 (문장 단위 provenance 포함), 실험 6종, LaTeX 원고 |
| 최종 목표 | 수리모델을 LLM 작동 방식의 관점에서 재해석하여 hallucination 완화 알고리즘의 이론적 기반 마련 |
| 협업 구조 | 이성헌 (수학·딥러닝) ↔ 한미화 (심리학, 원 논문 저자) — **연구 언어가 다른 두 사람의 소통이 핵심 리스크** |
| 문헌 관리 | Zotero (Han 추천 reference 컬렉션) |

### 산출물 지도

```
Phase 1  →  docs/audit/claim-model-alignment.md   (모델–원문 정합성 감사표)
         →  docs/glossary.md v1                    (수학자용 심리학 용어집)
Phase 2  →  docs/lit/<citekey>.md                  (reference별 비판 메모)
         →  docs/audit/model-revision-backlog.md   (모델 수정 백로그)
         →  docs/briefs/                           (Han 디스커션 브리프, 한국어·비수식)
Phase 3  →  개정된 src/mcbalance + docs/model.md + paper/main.tex
Phase 4  →  docs/llm-bridge.md                     (모델 ↔ LLM 메커니즘 매핑 + 가설)
         →  LLM 프로토타입 실험
Phase 5  →  논문 (모델링 논문 개정판 및/또는 LLM 논문)
```

---

## 2. 협업 커뮤니케이션 프로토콜 (cross-cutting)

두 연구자의 언어 차이를 다루는 규칙. 모든 Phase에 적용.

1. **용어집이 단일 진실 공급원(single source of truth).** 심리학 개념이 모델/코드/논문에
   등장하면 반드시 [glossary.md](glossary.md)에 등재하고, 심리학적 정의 ↔ 수학적 대응물 ↔
   **개념이 어긋나는 지점**(불완전한 번역임을 명시)을 함께 기록한다.
2. **Han에게 보내는 문서는 두 층위로.** `docs/briefs/`의 브리프는 (a) 수식 없는 한국어
   본문 + (b) 부록으로 수식. "이 수식은 선생님 논문의 이 문장을 이렇게 읽은 것입니다"
   형식의 provenance 인용을 유지한다 (기존 원고의 plain-language box 관례 계승).
3. **해석과 주장 구분.** 모델의 각 요소는 세 등급으로 표기:
   - `FAITHFUL` — 원문이 직접 지지
   - `INTERPRETIVE` — 원문과 합치하나 수학적 선택이 개입 (Han 확인 필요)
   - `EXTRAPOLATED` — 원문 범위 밖의 확장 (명시적 디스커션 안건)
4. **디스커션 안건 큐.** Han과 논의할 질문은 발생 즉시 해당 Phase 산출물의
   "Questions for Han" 섹션에 적립하고, Phase 종료 시 브리프로 묶는다.

---

## 3. Phase별 계획

### Phase 0 — 인프라 구축 `[완료 2026-07-07]`

- [x] 프로젝트 자산 파악 (README, docs/, src/, paper/)
- [x] 본 파이프라인 문서 작성
- [x] 용어집 골격 + v0 시드 항목 (docs/glossary.md)
- [x] Zotero 접근 방식 확정 — **Zotero 로컬 API** (Zotero 데스크톱 실행 중
      `localhost:23119`로 조회; Phase 2 시작 시 Zotero 실행 필요)

**체크포인트**: 파이프라인 승인됨 (2026-07-07). 사용자 추가 요청: Phase 1에
main.tex 충실도·톤 검토를 선행 포함.

---

### Phase 1 — 기반 감사: 원문 정독 + 모델 정합성 검증 `[완료 2026-07-07]`

**목적**: Han 논문(16면) 전체와 기존 모델링을 대조하여, reference 검토 전에
"현재 모델이 원문을 얼마나 충실히 읽었는가"의 기준선을 세운다.

| 작업 | 산출물 | 상태 |
|---|---|---|
| Han & Gu (2025) 16면 전체 정독 | 독서 노트 | ✅ 2026-07-07 |
| (사용자 요청) `paper/main.tex` 충실도 + 톤(Han 존중) 검토 | 감사 문서 §5 톤 검토 | ✅ 2026-07-07 |
| `docs/model.md` provenance 13개 매핑 재검증, FAITHFUL/INTERPRETIVE/EXTRAPOLATED 등급 | [`docs/audit/claim-model-alignment.md`](audit/claim-model-alignment.md) | ✅ 2026-07-07 |
| 원문에 있으나 모델에 **없는** 개념 목록화 (누락 감사) | 위 문서 §6 | ✅ |
| 용어집 v1: 전 항목 원문 검증 | `docs/glossary.md` | ✅ |
| Han 확인 필요 항목 → 질문 큐 (6건: F1 기하학, F2 JTC 귀속 등) | 감사 문서 §7 | ✅ |
| 감사 결과 사용자 리뷰 + 정오표(P0) 반영 여부 결정 | 반영 완료 (컴파일 확인) | ✅ 2026-07-07 |

**Phase 1 완료 (2026-07-07).** 잔여: F1–F3 구조 쟁점은 Han 답변 대기 (브리프 1호 발송 대기: `briefs/2026-07-07-questions-for-han.md`).

**품질 게이트**: 모든 provenance 행에 등급이 부여되고, 등급 근거가 원문 인용으로
뒷받침될 것. (ARS integrity 검증 원칙 준용 — 인용 없는 주장 금지)

**체크포인트 (FULL)**: 감사표 리뷰 후 Phase 2 진입 확인.

---

### Phase 2 — Reference 기반 비판적 재검토 `[진행 중 2026-07-07]`

> Intake 완료: [`docs/lit/00-intake.md`](lit/00-intake.md) — Zotero "Metacognition" 컬렉션
> 11편(+원문), 4축 분류(형식 이론 / 임상 근거 / LLM 교량 / **감각 박탈→환각**),
> 우선순위 P0×3 → P1×3 → P2×3 → Phase 4 예습×2.
> **P0+P1 완료 (2026-07-07, 7편)**: fleming2017, nelson1990, wells2019 (P0);
> daniel2014, merabet2004, lieder2017 (P1); sun2026-neurocogmap (사용자 추가).
> 백로그 B-04~B-13 적립. 종합 관찰: 세 문헌이 독립적으로 **2차 메타인지 채널**
> 확장(B-04)으로 수렴 — insight 결핍 + hallucination 검출을 동시에 여는 핵심.
> 잔여: P2 3편(wiesepape/leucht/lutgens), 사용자 추가 proust2012/hanlee2022,
> Phase 4 예습 2편(deboer/farquhar).

**목적**: Han 추천 reference들(Zotero)로 모델의 각 구성요소를 삼각검증한다.
"이 모델링 선택이 심리학 문헌 전반과 부합하는가, Han 논문에만 과적합되었는가?"

**절차** (reference 1편당):

1. WHY/HOW/WHAT 구조 독해 (ARS `3W` 스캔 방식) → `docs/lit/<citekey>.md`
2. 모델 구성요소별 판정: 각 문헌이 어떤 요소를 **지지/반박/정교화**하는지 매핑
   - 대상 요소: `L` 동역학, `alpha` dial, rumination 항 `r·sigmoid(L)`, OU 노이즈 `xi`,
     leak `kappa`, pivot hysteresis, corridor attractor, 두 minimal indices
3. 판정 결과를 수정 백로그에 적립 → `docs/audit/model-revision-backlog.md`
   (항목 형식: 근거 문헌 / 영향받는 수식·코드 / 수정 제안 / 우선순위)
4. 용어집에 신규 용어 추가

**예상 핵심 문헌 축** (Zotero 컬렉션 확인 후 확정):
- Proust — procedural vs explicit metacognition (모델의 이중 채널 구조 직접 검증)
- MCI-S 원 논문 — 순차 모델의 실증 결과 (Exp. 6의 비교 대상 타당성)
- JTC / beads task 문헌 — Exp. 2의 실증적 anchor (기존 계산 모델과 비교 가능)
- Bayesian brain / predictive processing 계열 — `dL/dt` 형식의 대안 정식화 존재 여부

**도구**: ARS `deep-research` (3W 스캔, fact-check 모드), `/ars-lit-review`.
사용자가 실제로 읽은 문헌은 `/ars-mark-read <citekey>`로 기록 (읽음 신호 관리).

**체크포인트 (MANDATORY)**: 백로그 우선순위를 사용자와 합의. Han 브리프 1호 발송 여부 결정.

---

**Phase 2 완료 (2026-07-07): 12편 검토.** 종합: [`docs/lit/synthesis.md`](lit/synthesis.md).
두 수렴(2차 채널 B-04, 외부 채널 위협 확증 B-05)이 Phase 3 최우선. note 작성 방향은
**제안 1**(기존 노트 유지 + 문장별 reference 근거 추가) 채택 — 근거는 아래 결정 로그.

---

### Phase 3 — 모델 개정 `[진행 중 2026-07-08]`

> **Han 회신 도착 (연구노트 2건, 2026-07-07/08)** — Q1·Q2 답변 + 신규 개념 체계
> (관점 P, 관점 성찰, Δ의 하위요소, reflective interval, 읽기 4분해).
> 정리: [`briefs/2026-07-08-han-feedback-intake.md`](briefs/2026-07-08-han-feedback-intake.md).
> 사용자 제안(α의 벡터화: 방향 = 배분, 크기 = Δ를 인식·견딤·조절하는 힘)을 골격으로
> v2 설계 초안 작성: [`model-v2-design.md`](../docs/model-v2-design.md).
> 미결 결정: m의 작용 수준(A/B/C안), fusion 조작화, λ_C 수정 형태, 영문 명명.

**목적**: 백로그를 코드·문서·원고에 반영한다.

- [ ] `src/mcbalance` 수정 + `tests/test_model.py` 갱신, 실험 6종 재실행
- [ ] `docs/model.md` provenance 표를 **다중 문헌 provenance**로 확장
      (Han & Gu 단일 앵커 → 문헌 삼각 앵커)
- [ ] `paper/main.tex` + `paper/references.bib` 갱신
- [ ] 무결성 게이트: 모든 인용·수치·주장 재검증 (ARS Stage 2.5 방식, 7-mode
      AI research failure checklist 포함 — 특히 "hallucinated results", "bug-as-insight" 점검)

**체크포인트 (MANDATORY, 무결성 게이트)**: PASS 후 Phase 4.

---

### Phase 4 — LLM Bridge: 작동영역 해석 + hallucination 가설 `[대기]`

**목적**: 검증된 모델을 LLM 메커니즘의 언어로 번역하고, 검증 가능한 가설과
프로토타입 실험을 설계한다.

**작업 4.1 — 매핑 문서** (`docs/llm-bridge.md`). 초기 후보 매핑 (Phase 1–3 결과로 수정 전제):

| 모델 요소 | LLM 대응 후보 | 비고 |
|---|---|---|
| `alpha` (self ↔ context dial) | parametric knowledge ↔ in-context evidence(RAG/프롬프트) 가중 | over-internalization ≈ 내부 지식 과신으로 인한 hallucination |
| rumination `r·sigmoid(L)` | self-conditioning: 자기 생성 토큰이 후속 생성을 강화 (error snowballing) | 양성 피드백 구조 동형성 |
| leak `kappa` | calibration / entropy 정규화 | Exp. 5의 ECE는 이미 LLM 문헌과 공용 언어 |
| JTC (premature closure) | 저증거 고확신 조기 커밋 (greedy decoding 과신) | Exp. 2와 직접 대응 |
| Pivot A/B (hysteresis) | abstention·retrieval trigger·self-check 발동 정책 | "언제 외부 근거로 전환하는가" |
| adaptive corridor | hallucination 억제 동작 영역 (dwell-fraction을 평가 지표화) | Exp. 6의 policy 비교 재현 |

**작업 4.2 — 가설 목록 + 실험 설계**: 각 매핑을 "측정 가능한 예측"으로 변환
(예: self-conditioning 강도 `r`의 대리 지표가 큰 조건에서 hallucination율 증가).
소규모 프로토타입 (logit 기반 confidence 추출, RAG 가중 개입 등) 설계.

**작업 4.3 — 개념 검증 실험 실행** 및 결과 정리.

**주의**: 이 Phase의 모든 매핑은 기본적으로 `EXTRAPOLATED` 등급 — 심리학→LLM 유추가
은유에 그치는지, 구조적 동형성인지 명시적으로 논증할 것. Han 브리프 2호의 핵심 안건.

**체크포인트 (FULL)**: 가설 우선순위와 실험 범위 합의.

---

### Phase 5 — 논문화 + 리뷰 `[대기]`

산출 논문 후보 (범위는 Phase 4 결과로 결정):
- (a) 모델링 논문 개정판 (다중 문헌 provenance 반영)
- (b) LLM bridge 논문 (position paper 또는 알고리즘 논문)

ARS 표준 파이프라인 적용: 무결성 검증(Stage 2.5) → 5인 모의 리뷰 패널(Stage 3,
`/ars-reviewer`) → 개정(Stage 4) → 재리뷰(Stage 3') → 최종 무결성(Stage 4.5) → 포맷 변환(Stage 5).

---

## 4. 운영 규칙

- **체크포인트**: 각 Phase 종료 시 사용자 확인 필수. 무결성 게이트(Phase 3, 5)는 생략 불가.
- **수정 루프 상한**: 리뷰-개정 2회 (수렴 시 조기 종료 제안).
- **비용 감각**: ARS full 파이프라인 1회 ≈ $4–6 수준(참고치). Phase 1–4는 대화형 세션
  위주라 그보다 낮음. 대규모 dispatch 전에 예상 규모를 먼저 보고.
- **재현성**: 모든 실험은 `scripts/run_all.py` 경유, 시드 고정. 모델 수정은 git 이력으로 추적.
- **상태 갱신**: Phase 완료 시 이 문서의 상태 마커와 아래 결정 로그를 갱신.

## 5. 결정 로그

| 날짜 | 결정 | 근거 |
|---|---|---|
| 2026-07-07 | 파이프라인 5-Phase 구조 확정, 사용자 승인 | 세션 킥오프 |
| 2026-07-07 | Zotero 접근 = 로컬 API (localhost:23119) | 사용자 선택 |
| 2026-07-07 | Phase 1에 main.tex 충실도·톤 검토 선행 포함 | 사용자 요청 |
| 2026-07-07 | 감사 완료: FAITHFUL 7 / INTERPRETIVE 5 / EXTRAPOLATED 1(선언됨), 실질 발견 F1–F6, 정오표 4건, 톤 권고 8건 | claim-model-alignment.md |
| 2026-07-07 | 정오표·톤 수정(E1–E5, T1–T5, T8) main.tex/model.md/README 반영, pdflatex 컴파일 확인 | 사용자 승인 |
| 2026-07-07 | Han 브리프 1호 작성 (질문 6건, 비수식 한국어) | briefs/2026-07-07-questions-for-han.md |
| 2026-07-07 | Zotero 로컬 API 미활성 → DB 읽기 전용 사본으로 대체 (원본 무변경). 향후 설정 → 고급 → local API 활성화 권장 | Phase 2 intake |
| 2026-07-07 | Phase 2 진입. Fleming & Daw 2017 검토 — 현 confidence 정의가 "1차 모델"임을 확인, 2차 구조(insight 파라미터 ρ) 도입 제안 (B-04) | lit/fleming2017.md |
| 2026-07-07 | 원고 오귀속 수정: α_self/α_context는 챕터가 아니라 사용자 초안의 정의(convex hull/simplex 배분). 관련 서술을 "convex allocation, 배분 비율 vs 전체 수준"으로 정정, 브리프 Q1도 "기울기"→"배분"으로 재작성 | 사용자 지적 |
| 2026-07-07 | 브리프 용어를 원문 그대로 유지(번역 제거) | 사용자 지시 |
| 2026-07-07 | Zotero 컬렉션 스코프 확정: Metacognition만 참고; LLM_dynamics_analysis는 residual stream 키워드 시에만 | 사용자 지시 |
| 2026-07-07 | 사용자 추가 문헌 반영: Proust 2012, Han & Lee 2022(MCI-S), NeuroCogMap(arXiv). Proust 2013 book은 access 불가 | 사용자 |
| 2026-07-07 | P0(3)+P1(3)+NeuroCogMap 검토 완료. 핵심 수렴: 2차 메타인지 채널 확장(B-04) | lit/*.md |
| 2026-07-07 | Phase 2 완료: 총 12편(+Han&Lee 2022, Proust 2012, P2 임상 3편). 종합 메모 작성 | lit/synthesis.md |
| 2026-07-07 | **note 작성 = 제안 1 채택** (기존 노트 유지 + 문장별 reference 근거 추가). 제안 2(독립 수리논문)는 Phase 5로 연기 — Han 답변 전 원문 앵커 제거는 시기상조 | 사용자 요청 평가 |
| 2026-07-07 | 사용자 주석 C1–C6 반영: §2.1 probability 동기를 연구노트 의도(가설 생성→argmax)로 재작성 + 인용 box를 p.6 fn.2로 교체(F2 부수 해소); 직관 그림 placeholder+생성 프롬프트; confidence 정의를 §3으로 이동; 채널 파라미터의 원문 근거·S(t) 분해 서술; 연구노트의 추상 시스템 (M,G) 제시 + α–L 결합(u 경유) 명시; κ 원문 근거 설명; TikZ 메커니즘 도식 추가 | main.tex |
| 2026-07-07 | 제안 1 실행: Phase 2 문헌 11건 인용 부착 + references.bib 11편 추가. Discussion에 "What the wider literature adds" 문단 (제어 계보 / 박탈 예측 / 1차 구조 한계 / pivot 유도 전망) | main.tex, references.bib |
| 2026-07-08 | Han 회신 intake: Q1(2층 구조), Q2(JTC 두 경로), 관점 P·관점 성찰·Δ 하위요소·reflective interval·읽기 4분해. 백로그 B-02/03/04/05 승인, B-16~20 신규 | briefs/2026-07-08-han-feedback-intake.md |
| 2026-07-08 | 사용자 제안 채택: α의 벡터화 **a** = m·(α̂, 1−α̂) — 방향 = 배분(v1의 α), 크기 m = 전체 관여(Δ 인식·견딤·조절력). v1은 m=1 특수 경우로 보존. "관점 = α" 등식은 Han의 대응표에 맞춰 정정(관점의 내용 방향은 L·b, 형성 가중은 α, P는 창발적 readout) | model-v2-design.md |
| 2026-07-15 | **v2 구조 확정 방향: 3-결합계** (L, **a**, P) — 사용자 지시로 P를 상태변수로 승격 (Han 메일이 독자 발전 허용). Δ = f(S, a) → 관점 성찰 → dP/dt; dα/dt = G(L, L̇, P; u). 기존 실험 개폐 허용 | model-v2-design.md (2차 초안) |
| 2026-07-15 | 용어 정돈: b를 belief → **credence(주관적 확률)** 로 개명 제안 (심리학의 belief 함의 충돌·통계 confidence 충돌 회피; Han의 "belief content" = ĥ와 정렬). 사용자 확정 대기 (D5) | model-v2-design.md §0 |
| 2026-07-15 | Δ 조작화 모서리 사례 발견: 사용자 공식(가중 밀기 차)은 융합 상태에서 Δ가 최대가 됨 — 임상적으로는 융합 = Δ를 못 느낌. δ(구동 불균형, pivot 트리거) + Δ̂ = a_self·a_context·\|s_self−s_outer\|(지각된 관점 간 차이, 성찰 구동) 이원 신호 제안 (D1) | model-v2-design.md §2 |
| 2026-07-15 | **모서리 사례 판정 정정 (사용자)**: 극단은 '융합'이 아니라 '**편향**' — 편향자의 Δ(성찰 **수요**)가 최대인 것은 옳음; 다만 편향 때문에 **수용성**은 최저. 수요/수용성을 서로 다른 슬롯으로 분리 (편향 = p의 극단성[상태 성질], 융합 = 주체↔관점 관계의 소실) | mbt-ontology.md §4 |
| 2026-07-15 | **재단계화 (사용자 지시)**: 구체 수식 보류, 추상화 우선 — Han 노트의 개념/작용 분리가 선행 과제. MBT 온톨로지 작성: 용어 전수 분류(상태·작용·신호·관계·능력·영역·실패양상), 흐림 지점 7건, 추상 타입 골격, Han 질문 7건 | mbt-ontology.md |
| 2026-07-15 | 표기 변경 (사용자): 구 α → **p**(관점 위치, simplex 상태) + **R**(CRS 조절기, 작용)로 분리. C는 confidence 충돌로 기각. 충돌 경보: 구 pivot gain p 개명 필요(η), R vs r 주의 | mbt-ontology.md §1 |
| 2026-07-15 | D5(credence)는 확정하지 않고 **다음 보고서의 제안 TODO**로 이관 | mbt-ontology.md §6 |
