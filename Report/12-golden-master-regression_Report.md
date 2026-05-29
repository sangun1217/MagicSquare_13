# 12-golden-master-regression Report

## 작업 배경/목표

- Magic Square Solver의 **관찰 가능한 출력**을 Golden Master baseline으로 고정하고, Refactoring·GREEN 이후 **회귀를 자동 검출**하는 안전장치를 구축한다.
- 작업은 GM-1(기준 파일·approve 패턴) → GM-2(테스트 코드·계약 검증) → GM-3(README 문서화) 순으로 진행되었다.
- **목표:** `tests/golden_master_expected.txt` 생성·버전 관리, `pytest -m golden_master` 회귀 suite, GM-TC-01~05 시나리오 및 Error Contract 보호.

## 수행 내용

### GM-1 — 기준 파일 및 approve 패턴 (Golden Master baseline)

1. **캡처 전략:** `UIBoundary.solve()` 결과를 Result DTO serialize (`tests/golden_master/capture.py`).
2. **시나리오 5건:** 정상(small-first), reverse, `INVALID_BLANK_COUNT`, `DUPLICATE_NUMBER`, `NO_VALID_MAGIC_SQUARE`.
3. **approve 패턴:** baseline 없으면 자동 생성; 있으면 `open(expected).read()` vs actual 비교; 불일치 시 unified diff 후 FAIL (`tests/golden_master/approve.py`).
4. **생성 스크립트:** `scripts/generate_golden_master.py` (`--approve` 지원).
5. **설계 문서:** `docs/golden_master_approve_pattern.md`.
6. **실제 출력 캡처**를 위해 Entity/Boundary/Control 최소 구현 추가 (blank_locator, missing_finder, magic_validator, solver, input_validator, SolvePartialMagicSquare).
7. `pyproject.toml`: `pythonpath = ["src", "."]`, `@pytest.mark.golden_master` 마커 등록.

### GM-2 — Golden Master 테스트 코드

1. **`tests/integration/test_golden_master_magic_square.py`**
   - GM-TC-01~05 개별 테스트 + 전체 문서 회귀 (`test_golden_master_document_matches_baseline`).
   - `@pytest.mark.golden_master` + `@pytest.mark.integration`.
2. **`tests/golden_master/contracts.py`**
   - int[6], 1-index, row-major 좌표, small-first / reverse fallback, Error label 계약 검증.
3. **`tests/golden_master/scenarios.py`**
   - GM-TC-01~05 SSOT (`tc_id`, `section_id`, `kind`, `expected_attempt` / `expected_error`).
4. **section 단위 approve:** `assert_golden_master_section()` 추가.
5. `tests/integration/test_golden_master.py` → `test_golden_master_magic_square.py`로 대체.

### GM-3 — README 업데이트

- **`docs/README.md`** 신규 생성: 문서 인덱스, `## RED 단계 To-Do 리스트`, **Golden Master 회귀 안전장치** (GM-01~10 체크리스트).

### 시나리오·baseline 확정 사항

| Section | TC | 내용 | 비고 |
|---------|-----|------|------|
| `normal_success` | GM-TC-01 | `G1_SF` small-first | `[1,2,3,4,3,14]` |
| `reverse_success` | GM-TC-02 | `G1` reverse fallback | `[2,2,10,3,3,7]` |
| `invalid_blank_count` | GM-TC-03 | `TD_INVALID_BLANK_THREE` | `INVALID_BLANK_COUNT` |
| `duplicate_number` | GM-TC-04 | 2 blanks + duplicate `1` | `DUPLICATE_NUMBER` |
| `no_valid_magic_square` | GM-TC-05 | unsolvable 전용 격자 | `NO_VALID_MAGIC_SQUARE` |

- `TD_DUPLICATE`(빈칸 1개), `G3`(실제 solvable)는 Golden Master baseline에 부적합 → 전용 격자 사용.

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 생성 | `tests/golden_master_expected.txt` (baseline, `git add` staged) |
| 생성 | `scripts/generate_golden_master.py` |
| 생성 | `tests/golden_master/__init__.py` |
| 생성 | `tests/golden_master/scenarios.py` |
| 생성 | `tests/golden_master/capture.py` |
| 생성 | `tests/golden_master/approve.py` |
| 생성 | `tests/golden_master/contracts.py` |
| 생성 | `tests/integration/test_golden_master_magic_square.py` |
| 생성 | `tests/integration/conftest.py` |
| 생성 | `docs/golden_master_approve_pattern.md` |
| 생성 | `docs/README.md` |
| 수정 | `pyproject.toml` |
| 수정 | `src/magicsquare/entity/blank_locator.py` |
| 수정 | `src/magicsquare/entity/missing_finder.py` |
| 수정 | `src/magicsquare/entity/magic_validator.py` |
| 수정 | `src/magicsquare/entity/solver.py` |
| 수정 | `src/magicsquare/boundary/input_validator.py` |
| 수정 | `src/magicsquare/control/solve_partial_magic_square.py` |
| 삭제 | `tests/integration/test_golden_master.py` (GM-2에서 대체) |

## 검증 결과

| 명령 | 결과 |
|------|------|
| `pytest -m golden_master -v` | **6 passed**, 91 deselected |
| `python scripts/generate_golden_master.py --approve` | baseline 갱신 성공 |
| `git add tests/golden_master_expected.txt` | staged (GM-03 GM-03 항목) |

**Golden Master 테스트 6건**

- `test_gm_tc_01_normal_success_small_first`
- `test_gm_tc_02_reverse_success_fallback`
- `test_gm_tc_03_invalid_blank_count_error_contract`
- `test_gm_tc_04_duplicate_number_error_contract`
- `test_gm_tc_05_no_valid_magic_square_error_contract`
- `test_golden_master_document_matches_baseline`

## 남은 이슈 및 다음 액션

1. **커밋** — Golden Master 인프라·baseline·docs 일괄 커밋 (사용자 지시 시).
2. **Track B RED/GREEN 정합** — `test_track_b_red.py`의 D-SOL-01(G1 small-first 기대) vs 실제 reverse-only 성공 불일치 해소.
3. **Track A fixture** — `TD_DUPLICATE`, `TD_INVALID_RANGE` 등 빈칸 1개 fixture → E004/E005 테스트와 검증 순서 정렬.
4. **CI gate** — PR CI에 `pytest -m golden_master -v` 추가 (approve 금지).
5. **Refactoring Phase** — Golden Master PASS 유지하며 ECB·named constants 리팩터.

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | GM-1~3 Golden Master 회귀 안전장치 구축 세션 |
