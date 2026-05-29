# 10-dual-track-red-full-design-and-tests Report

## 작업 배경/목표

- Magic Square 4×4 프로젝트에서 **Dual-Track UI + Logic TDD**의 **RED 단계**를 진행한다.
- 1차: SSOT(PRD, Report/02, 프로젝트 계약) 기준 **RED 설계표만** 작성(구현·테스트·파일 저장 금지).
- 2차: 사용자 「진행」 지시에 따라 설계표를 **실패하는 pytest**와 **최소 ECB 스텁**으로 착수한다.

## 수행 내용

### Turn 1 — RED 설계표 (문서만)

- **TDD phase: RED** — Track A(U-IN/U-OUT/U-FLOW) + Track B(D-LOC~D-SOL) 설계표 출력.
- SSOT: `docs/PRD_MagicSquare.md`, `Report/02-tdd-design-report.md`(부록 B), 사용자 계약(E001~E005 Failure envelope, `int[6]` 1-index).
- `Report/02.MagicSquare_DualTrack_TDD_Design_Report.md`는 저장소에 없음 → `golden_grids`·README DN-04로 G0~G3 매핑.
- 자체 검수 체크리스트 6항 모두 충족 확인.

### Turn 2 — RED 테스트·스텁 구현

- `tests/fixtures/golden_grids.py` 복구·확장(G0/G1/G2/G3, invalid/solve 픽스처).
- Boundary: `failure.py`(E001~E005 envelope), `input_validator.py`, `ui_boundary.py`.
- Control: `solve_partial_magic_square.py`.
- Entity: `blank_locator`, `missing_finder`, `magic_validator`, `solver`, `constants`, `exceptions`.
- Track A: `tests/boundary/test_track_a_red.py` (U-IN-01~06, U-OUT-01~02, U-FLOW-02).
- Track B: `tests/domain/test_track_b_red.py` (D-LOC-01 ~ D-SOL-04, 입력 불변 1건).
- `tests/conftest.py`, `tests/test_fixture_smoke.py` 추가.
- 레거시 `test_ac_fr01_01_invalid_size.py` 수집 오류 해소: `TD_INVALID_BLANK_ONE` 픽스처 alias 추가.

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 생성 | `src/magicsquare/boundary/failure.py` |
| 생성 | `src/magicsquare/boundary/input_validator.py` |
| 생성 | `src/magicsquare/boundary/ui_boundary.py` |
| 생성 | `src/magicsquare/control/__init__.py` |
| 생성 | `src/magicsquare/control/solve_partial_magic_square.py` |
| 생성 | `src/magicsquare/entity/__init__.py` |
| 생성 | `src/magicsquare/entity/constants.py` |
| 생성 | `src/magicsquare/entity/exceptions.py` |
| 생성 | `src/magicsquare/entity/blank_locator.py` |
| 생성 | `src/magicsquare/entity/missing_finder.py` |
| 생성 | `src/magicsquare/entity/magic_validator.py` |
| 생성 | `src/magicsquare/entity/solver.py` |
| 생성 | `tests/fixtures/__init__.py` |
| 생성 | `tests/fixtures/golden_grids.py` |
| 생성 | `tests/conftest.py` |
| 생성 | `tests/boundary/__init__.py` |
| 생성 | `tests/boundary/test_track_a_red.py` |
| 생성 | `tests/domain/test_track_b_red.py` |
| 생성 | `tests/test_fixture_smoke.py` |
| 수정 | `tests/fixtures/golden_grids.py` (`TD_INVALID_BLANK_ONE` — 레거시 호환) |
| 기존 | `src/magicsquare/boundary/boundary_validator.py` (RED 스텁 유지) |
| 기존 | `tests/boundary/test_ac_fr01_01_invalid_size.py` (미수정, 병행 실패) |

## 검증 결과

| 항목 | 결과 |
|------|------|
| 명령 | `pytest tests/` |
| 스냅샷 | **46 failed, 18 passed** |
| Track A 신규 (`test_track_a_red.py`) | 13 failed — `InputValidator.validate` → `NotImplementedError` |
| Track B 신규 (`test_track_b_red.py`) | 13 failed, 1 passed — Entity 스텁 `NotImplementedError`; 불변성 가드 1 passed |
| 레거시 AC-FR-01-01 | 20 failed, 12 passed — `BoundaryValidator` 스텁 |
| 스모크 | 4 passed (`test_fixture_smoke.py` 등) |
| RED 적합성 | 의도된 실패 유형: **미구현** (`NotImplementedError`). GREEN 전 정상. |

## 남은 이슈 및 다음 액션

1. **Track A GREEN** — `InputValidator.validate` short-circuit (null → size → blank → range → duplicate) + Failure envelope 반환.
2. **U-FLOW-02** — validate Failure 시 `SolvePartialMagicSquare.execute` 0회 (배선은 `UIBoundary.solve`에 존재).
3. **계약 이원화** — 신규 E00x envelope vs 레거시 `InvalidInputError` / `ERR-VAL-*` (`BoundaryValidator`) 통합 정책 확정.
4. **D-SOL-01 vs D-SOL-02** — 동일 `G1`에 Step A `[2,2,7,3,3,10]` vs Step B `[2,2,10,3,3,7]`; GREEN 시 `G1_SF`(`TD_SUCCESS_SF_001`) 분리.
5. **G3 / TD_UNSOLVABLE** — 수치 확정 후 `UnsolvableDomainError` (현재 D-SOL-03은 `NotImplementedError`로 실패).
6. **Track B GREEN** — `find_blank_coords` → `find_not_exist_nums` → `is_magic_square` → `solution` 순 최소 구현.
7. **REFACTOR** — GREEN 통과 후; 테스트 약화 금지.

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | Dual-Track RED 설계표 + RED 테스트·스텁 착수 세션 |
