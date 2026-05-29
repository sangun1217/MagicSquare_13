# 15-green-dom-d-sol-01 Report

## 작업 배경/목표

- Track B GREEN **Commit 4 / 4** — D-SOL-01~04 묶음 최소 구현.
- 단일 PR(`feat/dom/green-d-loc-01` → `stabilize/green`) 마지막 커밋.
- **목표:** `solution` (FR-05) — small-first → reverse, `int[6]` 반환, `UnsolvableDomainError`.
- 4커밋 완료 후 **통합 PR Description** 작성 (`docs/PR_green_dom_track_b.md`).

## 수행 내용

### `solution` 구현

| 단계 | 내용 |
|------|------|
| 1 | `find_blank_coords` → 1-index `(r1,c1,r2,c2)` |
| 2 | `find_not_exist_nums` → `(n1,n2)` 오름차순 |
| 3 | Attempt 1 (small-first): 복사본에 `n1→blank1`, `n2→blank2` → `is_magic_square` |
| 4 | 성공 시 `[r1,c1,n1,r2,c2,n2]` 반환 |
| 5 | Attempt 2 (reverse): `n2→blank1`, `n1→blank2` → 검증 |
| 6 | 성공 시 `[r1,c1,n2,r2,c2,n1]` 반환 |
| 7 | 둘 다 실패 → `UnsolvableDomainError` |

- 입력 행렬 **비변경** (`copy.deepcopy` on trial grid only).

### Fixture 정합 (GREEN 수치 lock)

| Fixture | 변경 | 사유 |
|---------|------|------|
| **G3** | unsolvable 격자로 교체 | 기존 G3는 small-first 성공 → D-SOL-03 모순 (Report/10 TBD) |
| **D-SOL-01** | `G1` → `G1_SF` | G1은 reverse만 성공; small-first 성공은 `G1_SF` (Report/10 분리 권고) |

### 테스트 전환

- `tests/entity/test_d_sol.py`: 4개 스켈레톤 → assert.
- `tests/domain/test_track_b_red.py`: D-SOL-01 `G1_SF`/`G1_SF_EXPECTED` 정렬.

### README

- Commit 4 `[x]`, Track B RED 전부 통과 `[x]`.

### 통합 PR Description

- `docs/PR_green_dom_track_b.md` — 4커밋 총체 Description.

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 수정 | `src/magicsquare/entity/solver.py` |
| 수정 | `tests/entity/test_d_sol.py` |
| 수정 | `tests/domain/test_track_b_red.py` |
| 수정 | `tests/fixtures/golden_grids.py` (G3) |
| 수정 | `README.md` |
| 생성 | `docs/PR_green_dom_track_b.md` |
| 생성 | `Report/15-green-dom-d-sol-01_Report.md` |
| 생성 | `Prompting/15-green-dom-d-sol-01_Prompt.md` |

## 검증 결과

| 명령 | 결과 |
|------|------|
| `pytest tests/domain/test_track_b_red.py tests/entity/ -v` | **27 passed** |
| Track B 전체 | D-LOC ~ D-SOL + entity skeleton 전환 완료 |

## 남은 이슈 및 다음 액션

1. 단일 PR 리뷰·머지 (`feat/dom/green-d-loc-01` → `stabilize/green`).
2. `stabilize/green` → `develop` 통합 PR.
3. Track A GREEN (InputValidator 등) — 별도 진행.
4. REFACTOR — `LineSumChecker`, `BLANK_COUNT` 검증 등.

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | Track B GREEN Commit 4 (D-SOL-01~04) + 통합 PR Description |
