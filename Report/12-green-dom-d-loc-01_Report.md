# 12-green-dom-d-loc-01 Report

## 작업 배경/목표

- Magic Square 4×4 **Dual-Track TDD**에서 **GREEN 단계**를 Track B 우선·4커밋 단위로 진행한다.
- 브랜치: `stabilize/green` (통합) ← `feat/dom/green-*` (커밋별 PR).
- **목표 (Commit 1):** D-LOC-01 묶음만 최소 구현 — `find_blank_coords` (FR-02) 통과.
- **제약:** 테스트 약화·삭제 금지, 매직 넘버 금지(`GRID_SIZE` 사용), REFACTOR 금지, RED 1묶음만 GREEN.

## 수행 내용

### GREEN 준비 (이전 세션)

1. `develop`에서 `stabilize/green` 브랜치 생성·원격 푸시.
2. RED 베이스라인 확인: 73 failed, 18 passed (`PYTHONPATH=.` 또는 `pyproject.toml` 수정 후).
3. Track B 4-commit 순서 확정: D-LOC-01 → D-MIS-01 → D-VAL-01~06 → D-SOL-01~04.

### Track B GREEN 계획 문서화

- `README.md` Phase 2 Track B GREEN 섹션을 4-commit × 4-PR 표로 갱신.
- Phase 1 Track B RED 항목 `[x]` 처리 (테스트 작성 완료).
- Git 브랜치 규칙에 `feat/dom/green-*` → `stabilize/green` 추가.

### Commit 1 — D-LOC-01 구현

| 항목 | 내용 |
|------|------|
| 함수 | `find_blank_coords(matrix) -> (r1, c1, r2, c2)` |
| 알고리즘 | `GRID_SIZE` 이중 루프, row-major, `0` 셀 탐색, 1-index 반환 |
| 상수 | `magicsquare.entity.constants.GRID_SIZE` |
| 입력 불변 | matrix in-place 수정 없음 (BR-15) |

### 테스트 전환

- `tests/entity/test_d_loc.py`: 스켈레톤 `pytest.fail` → `assert find_blank_coords(G1) == (2, 2, 3, 3)`.
- `tests/domain/test_track_b_red.py::TestDLOC01FindBlankCoords`: Full RED — 구현으로 통과.
- `TestDomainInputImmutability::test_find_blank_coords_does_not_mutate_g1`: 부수 통과.

### 인프라

- `pyproject.toml`: `pythonpath = ["src", "."]` — `tests.conftest` import 수집 오류 해소.

### PR #1

- 브랜치: `feat/dom/green-d-loc-01` → base `stabilize/green`.
- 커밋: `9b77bb1` — `green(dom): implement find_blank_coords for D-LOC-01`.
- 원격 푸시 완료; `gh pr create`는 collaborator 권한 오류로 수동 PR 생성 필요.
- PR 본문: `docs/PR_green_dom_d_loc_01.md` (리뷰 첨부용).

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 수정 | `src/magicsquare/entity/blank_locator.py` |
| 수정 | `tests/entity/test_d_loc.py` |
| 수정 | `pyproject.toml` |
| 수정 | `README.md` |
| 생성 | `docs/PR_green_dom_d_loc_01.md` |
| 생성 | `Report/12-green-dom-d-loc-01_Report.md` |
| 생성 | `Prompting/12-green-dom-d-loc-01_Prompt.md` |

## 검증 결과

| 명령 | 결과 |
|------|------|
| `pytest tests/domain/test_track_b_red.py::TestDLOC01FindBlankCoords tests/entity/test_d_loc.py tests/domain/test_track_b_red.py::TestDomainInputImmutability::test_find_blank_coords_does_not_mutate_g1 -v` | **3 passed** |
| 전체 suite | D-LOC-01 외 **의도적 RED** (Track B 2~4, Track A 미구현) |

## 남은 이슈 및 다음 액션

1. **PR #1** — 동료 리뷰 후 `stabilize/green`에 머지 (사용자 수동).
2. **PR #2** — `feat/dom/green-d-mis-01`: `find_not_exist_nums` (D-MIS-01), G1 → `(7, 10)`.
3. **PR #3** — `feat/dom/green-d-val-01`: `is_magic_square` (D-VAL-01~06).
4. **PR #4** — `feat/dom/green-d-sol-01`: `solution` (D-SOL-01~04).
5. 4 PR 완료 후 `stabilize/green` → `develop` 통합 PR.
6. `RED-DOM-DET-001` 결정론 — GREEN 4-commit 후속.

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | Track B GREEN Commit 1 (D-LOC-01) 세션 |
