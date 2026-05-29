# 17-ecb-refactor-plan-analysis Report

## 작업 배경/목표

- 프롬프트 ECB 매핑(`domain.py` → Control, `boundary.py` → Boundary, `gui/main_window` → Screen)에 대응하는 실제 파일을 점검하고, REFACTOR phase 전 **구조 개선 계획**을 수립한다.
- 대상: `solve_partial_magic_square.py`, `ui_boundary.py`, `main_window.py`(미존재), 연관 `input_validator.py`, `entity/solver.py`.
- 코드 변경 없이 분석·계획만 수행 (Ask mode 세션).

## 수행 내용

### 1. 코드 스멜 점검 (1차)

| 우선순위 | 주요 이슈 |
|----------|-----------|
| High | `UnsolvableDomainError` Boundary 누출; `main_window.py` 미존재 |
| Medium | Control pass-through; `Grid`/`ResultVector` alias 15+ 중복; stale docstring; `ResultFormatter` 미연동 |
| Low | `BoundarySolveResult` 타입 불완전; Entity 함수명 `solution` |

### 2. ECB 역할·의존 분석 (2차)

- **Control** (`solve_partial_magic_square.py`): 명목 Control, 실질 Entity 1줄 위임 → **부분 적합**.
- **Boundary** (`ui_boundary.py`): E001~E005는 적합; E006/E007·int[6] schema·도메인 실패 envelope 미완 → **부분 적합**.
- **Screen** (`boundary/screen/main_window.py`): **미존재** → GM 직렬화가 `tests/golden_master/capture.py`에 혼재.
- **Entity** (`entity/solver.py`): locate→find→Step A/B + int[6] 조립이 Entity에 몰림 (PRD상 Control·Boundary 책임).

**P0/P1 분리 순서**

| 우선 | 항목 |
|------|------|
| P0 | Control 오케스트레이션 Entity→Control 이동 |
| P0 | Boundary E006/E007(≈ERR-SOL-001) envelope 매핑 |
| P0 | U-FLOW-02·U-OUT-01~03 RED 스켈레톤 테스트 선행 |
| P1 | int[6] → `result_formatter`; `two_cell_solver` 분리; `solve_entry` ECB 위반 제거; Screen 신규 |

### 3. SRP 점검 (3차)

| 항목 | 결과 |
|------|------|
| ① 함수 다중 역할 | `ui_boundary.py:26-41` — FR-01 검증 게이트 + FR-05 Control 위임 |
| ② 클래스 데이터+검증 혼재 | 해당 없음; `UIBoundary` 클래스 복수 책임(wiring + solve 진입) |
| ③ UI 비즈니스 판단 | 해당 없음 (main_window 미존재) |

### 4. REFACTOR 계획서 (4차)

- 우선순위 10건 대상 목록 (P0~P3), 테스트 선행 항목, 회귀 검증 명령(`pytest -ra`, `-m golden_master`, `--cov-fail-under=80`) 정리.

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 생성 | `Report/17-ecb-refactor-plan-analysis_Report.md` (본 문서) |
| 생성 | `Prompting/17-ecb-refactor-plan-analysis_Prompt.md` |

**프로덕션 코드 변경:** 없음 (분석·문서만).

## 검증 결과

| 항목 | 결과 |
|------|------|
| 코드 수정 | 없음 |
| 기존 테스트 | 세션 중 미실행 (Ask mode) |
| Git 상태 (세션 종료 시) | `develop` = `origin/develop`; untracked Report/16·Prompting/16 + 본 세션 17번 문서 |

## 남은 이슈 및 다음 액션

1. **P0** — Characterization 테스트 추가 후 `entity/solver.py` 오케스트레이션을 Control로 이동.
2. **P0** — `UIBoundary.solve` 도메인 실패 envelope(E006/E007) 및 Golden Master baseline 고정.
3. **P0** — `test_u_flow.py`·`test_u_out.py` RED 스켈레톤 → GREEN 전환.
4. **P1** — `entity/services/two_cell_solver.py` 분리, `ResultFormatter` Boundary 연동.
5. **P2** — `boundary/screen/main_window.py` Screen 계층 신규; `capture.py` 직렬화 역할 Boundary로 이전.
6. **P1** — `control/solve_entry.py` 제거(control→boundary 금지 의존).

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | ECB·SRP·REFACTOR 계획 분석 세션 기록 |
