# MagicSquare_xx

4×4 격자에 1~16을 한 번씩 배치했을 때 **행·열·대각선의 합 규칙**을 다루는 학습·연습 프로젝트입니다.

현재 단계는 **구현 이전의 문제 정의**(STEP 1~5)까지 완료된 상태입니다. “마방진을 자동으로 채우는 프로그램”이 아니라, **규칙을 만족하는지 일관되게 판별하고 그 기준을 고정하는 것**을 핵심 문제로 둡니다.

---

## 프로젝트 목적

| 구분 | 내용 |
|------|------|
| **하고 있는 일** | 문제 관찰, Why 분석, Invariant·명세 정리, TDD 관점의 계약 사고 |
| **아직 하지 않는 일** | 구현, UI, 자동 생성, n×n 확장 |

**훈련하려는 사고 능력**

- 규칙 분해·계약 (완성 vs 유효 구분)
- 불변량 인식 (공통 합 34, 10개 줄 검사 등)
- 판정과 생성의 분리
- 검증 우선·완전 검사·회귀 의식

---

## 진짜 문제 정의 (요약)

### 피해야 할 표현 (표면 정의)

> 4×4 마방진을 **완성하는** 프로그램을 만든다.

### 채택한 정의

> 4×4 격자에 1~16을 각각 한 번 배치한 상태가, **행·열·대각선 합 규칙을 모두 만족하는지** 일관되게 **판별**하고, 그 **판별 기준을 반복 가능하게 고정**하는 것이 문제이다.

### 비목표 (1차 범위 밖)

- 특정 구성 방법 강제
- 모든 유효 배치 나열
- 격자 크기 일반화(n×n)를 1차 목표로 둠
- UI·속도 최적화를 1차 목표로 둠

---

## 핵심 Invariant

**도메인**

- 4×4 격자, 각 칸에 하나의 값
- 1~16 정수가 **서로 다르게** 한 번씩 사용
- 검사 대상: **4행 + 4열 + 2대각** (총 10줄)
- 유효 배치: 10줄의 합이 **모두 같음** (1~16 전체 사용 시 **34**)

**판정**

- 같은 배치 → 항상 같은 판정
- 「유효」는 위 규칙을 **전부** 검사한 뒤에만
- 판별 과정이 배치를 바꾸지 않음

---

## 문제 정의 진행 단계

| STEP | 주제 | 핵심 결론 |
|------|------|-----------|
| 1 | Observation | 4×4 제약 격자; 목적(퍼즐/검증/데모)은 관찰 단계에서 정리 |
| 2 | Why #1 | 「완성」 뒤 실제 병목은 **검증·피드백** |
| 3 | Why #2 | 프로그램 = **반복 가능한 자동 검증** + 규칙 명시화 |
| 4 | Why #3 | TDD = **불변·입출력·판정 의미**를 계약으로 통제 |
| 5 | 진짜 문제 | **판별·기준 고정**이 본질; 퍼즐 완성이 아님 |

상세 논의·표·다음 단계 제안은 보고서를 참고하세요.

---

## 저장소 구조

```
MagicSquare_xx/
├── README.md                 ← 이 파일 (프로젝트 개요)
├── docs/
│   └── PRD_MagicSquare.md    ← 구현 전 PRD (Dual-Track TDD 기준)
├── Report/                   ← 문제 정의·TDD 설계·세션 보고서
├── Prompting/                ← 프롬프트·대화 기록
├── .cursor/rules/            ← TDD·ECB·코드 스타일 규칙
└── src/, tests/              ← (예정) ECB 구현·테스트
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [docs/PRD_MagicSquare.md](docs/PRD_MagicSquare.md) | 구현 전 PRD — FR/BR, Dual-Track TDD, Traceability |
| [Report/01-problem-definition-report.md](Report/01-problem-definition-report.md) | STEP 1~5 통합 보고서 (관찰, Why, Invariant, 사고 능력) |
| [Report/02-tdd-design-report.md](Report/02-tdd-design-report.md) | TDD 설계 — 계약, TC 카탈로그, R-G-R 순서 |
| [Report/08-magicsquare-tdd-readme-todo-draft_Report.md](Report/08-magicsquare-tdd-readme-todo-draft_Report.md) | TDD 추적 보드 (23 Task, 15 Scenario) |

**읽는 순서:** `01` → `02` → `PRD` → 본 README 「해야 할 목록」

---

## 다음에 결정할 것

구현에 들어가기 전에 아래를 문서로 좁히는 것이 권장됩니다.

1. **미완성 격자** — 무효와 별도 상태로 둘지, 단일 「비유효」로 둘지
2. **출력 수준** — 유효/무효만 vs 위반 설명(어느 줄, 중복 값)
3. **1차 범위** — 판정기만 vs 생성·UI 포함
4. **이해관계자·시나리오** — 학습자 직접 입력 vs 데모용 고정 격자

---

## 상태

| 항목 | 상태 |
|------|------|
| 문제 정의 (STEP 1~5) | 완료 |
| PRD·TDD 설계·Cursor Rules | 완료 |
| Dual-Track TDD 구현 | **GREEN 진행 중** (`stabilize/green`) — Track B 4-commit |
| 실행 방법 | `pip install -e ".[dev]"` 후 `pytest` |

---

## Dual-Track TDD — 해야 할 목록

개발 방법론: **Dual-Track UI + Logic TDD → GREEN → Dual-Track Refactoring**

- **Track A (Boundary / UI Contract)**: 입력 검증, 출력 계약, Domain 미호출
- **Track B (Domain / Logic)**: BlankFinder, MissingNumberFinder, Validator, Solver

참고: [docs/PRD_MagicSquare.md](docs/PRD_MagicSquare.md) §15, [Report/08-magicsquare-tdd-readme-todo-draft_Report.md](Report/08-magicsquare-tdd-readme-todo-draft_Report.md)

### Sprint 0 — 프로젝트 골격

- [x] `pyproject.toml` 생성 (pytest, pytest-cov, ruff/black)
- [x] ECB 디렉터리 스켈레톤 (`src/boundary/`, `src/control/`, `src/entity/`)
- [x] 테스트 디렉터리 분리 (`tests/boundary/`, `tests/domain/`, `tests/integration/`)
- [x] Golden fixture 상수 정의 (PRD §16.4, Report/02 부록 B)
- [x] `TD-SUCCESS-REV-001` 수치 확정 (PRD DN-04) — blanks `(2,2)/(3,3)` 1-index, expected `[2,2,10,3,3,7]`
- [x] `ResultFormatter` Layer 결론 (PRD DN-05) — **Boundary** (format-only assembly)

### Phase 1 — Dual-Track RED (테스트만, 실패 확인)

- [x] **결함 목록 연결** — [docs/defect_list.md](docs/defect_list.md) (AC-FR-01-01 RED: 20 failed / 24 passed, 2026-05-29)

#### Track A — Boundary

- [ ] `RED-BND-001` — 비 4×4 입력 → `ERR-VAL-001`, Domain 미호출
- [ ] `RED-BND-002` — 빈칸 개수 ≠ 2 → `ERR-VAL-002`, Domain 미호출
- [ ] `RED-BND-003` — 값 범위 위반 → `ERR-VAL-003`, Domain 미호출
- [ ] `RED-BND-004` — 중복 값 → `ERR-VAL-004`, Domain 미호출
- [ ] `RED-BND-005` — 출력 좌표 1-index
- [ ] `RED-BND-006` — 검증 실패 시 Domain 0회 호출 (mock/spy)
- [ ] `RED-BND-007` — 반환 배열 길이 6 (`int[6]`)

#### Track B — Domain

- [x] `RED-DOM-BLK-001` — row-major 빈칸 2개 1-index 좌표 (FR-02) — `test_track_b_red` + `test_d_loc`
- [x] `RED-DOM-MIS-001` — 누락 숫자 2개 탐색 (FR-03) — `test_track_b_red` + `test_d_mis`
- [x] `RED-DOM-MIS-002` — 누락 숫자 오름차순 `(n1 < n2)` — D-MIS-01에 포함
- [x] `RED-DOM-VAL-001` — 유효 격자 `True` (FR-04) — `test_track_b_red` + `test_d_val`
- [x] `RED-DOM-VAL-002` — 행/열/대각선 합 34 검사 — D-VAL-02~06
- [x] `RED-DOM-SOL-001` — small-first 성공 (FR-05) — D-SOL-01
- [x] `RED-DOM-SOL-002` — reverse 성공 — D-SOL-02
- [x] `RED-DOM-SOL-003` — 두 조합 실패 → `ERR-SOL-001` — D-SOL-03
- [x] `RED-DOM-MUT-001` — 입력 행렬 불변 (BR-15) — `test_track_b_red::TestDomainInputImmutability`
- [ ] `RED-DOM-DET-001` — 결정론 (NFR-03) — GREEN 후속

#### Integration RED

- [ ] `SC-DOM-SOL-001` — Control 오케스트레이션 end-to-end
- [x] `pytest` 실행 → **의도한 실패** 로그 확보 (RED 증거) — [defect_list.md](docs/defect_list.md) DEF-001~002

### Phase 2 — GREEN (최소 구현, Track별 PR merge)

#### Track A GREEN

- [ ] `BoundaryValidator` — FR-01 입력 검증 최소 구현
- [ ] `ResultFormatter` — `int[6]` 출력 조립 (FR-05)
- [ ] Track A RED 테스트 전부 통과

#### Track B GREEN (`stabilize/green` — 커밋 4개 · PR 1개)

브랜치 전략: `feat/dom/green-d-loc-01` (단일 PR) → `stabilize/green` → (완료 후) `develop`  
커밋을 4개로 나누고, PR Description은 4커밋 완료 후 일괄 작성.

| # | 커밋 | Test ID | 구현 대상 | 상태 |
|---|------|---------|-----------|------|
| 1 | `green(dom): D-LOC-01 find_blank_coords` | D-LOC-01 | `find_blank_coords` (FR-02) | [x] |
| 2 | `green(dom): D-MIS-01 find_not_exist_nums` | D-MIS-01 | `find_not_exist_nums` (FR-03) | [x] |
| 3 | `green(dom): D-VAL-01~06 is_magic_square` | D-VAL-01~06 | `is_magic_square` (FR-04) | [x] |
| 4 | `green(dom): D-SOL-01~04 solution` | D-SOL-01~04 | `solution` (FR-05) | [x] |

- [x] Commit 1 — `find_blank_coords` — D-LOC-01 통과
- [x] Commit 2 — `find_not_exist_nums` — D-MIS-01 통과
- [x] Commit 3 — `is_magic_square` — D-VAL-01~06 통과
- [x] Commit 4 — `solution` — D-SOL-01~04 통과
- [x] Track B RED 테스트 전부 통과 (`test_track_b_red` + `tests/entity/test_d_*`)

#### Integration GREEN

- [ ] Control layer — Attempt 순서 오케스트레이션
- [ ] 전체 Scenario 15건 Tracking Board 통과

### Phase 3 — Dual-Track Refactoring

#### Track A Refactor

- [ ] `refactor/bnd/fr-01` — BoundaryValidator 책임 분리
- [ ] named constants 추출 (`GRID_SIZE`, `BLANK_COUNT`, `VALUE_MIN`, `VALUE_MAX`)

#### Track B Refactor

- [ ] `refactor/dom/fr-04` — `LineSumChecker`, `LineEnumerator` 추출
- [ ] `MAGIC_CONSTANT_N4 = 34` 중앙화 (NFR-07)

#### Integration Refactor

- [ ] ECB import 방향 정리 (NFR-06)
- [ ] Golden fixture 파일 분리 (TC-G-01 ~ TC-G-04)
- [ ] 전체 suite GREEN + coverage ≥ 80% (layer별 95/85 — PRD NFR-01/02)

### Quality Gates (모든 PR)

- [ ] RED: production 코드 없이 테스트 실패 확인
- [ ] GREEN: assert 약화·테스트 삭제 없음
- [ ] REFACTOR: 동작 변경 없이 구조 개선
- [ ] Track A/B 테스트 파일 분리 유지
- [ ] Domain 전부 구현 후 Boundary 붙이기 **금지**

### Git 브랜치 규칙 (요약)

| 단계 | 브랜치 패턴 | 병합 대상 |
|------|-------------|-----------|
| Track A RED/GREEN | `feat/bnd/red-bnd-*` | `develop` |
| Track B RED | `feat/dom/red-dom-*` | `develop` |
| Track B GREEN (4-commit, 1 PR) | `feat/dom/green-d-loc-01` → `stabilize/green` | `develop` |
| Integration | `feat/int/sc-*` | `develop` |
| Refactoring | `refactor/bnd/*`, `refactor/dom/*`, `refactor/int/*` | `develop` |
| Release | `develop` → `main` | Epic-001 완료 후 |

---

## 라이선스

미정 (필요 시 추가)
