# PR #1 — `green(dom): D-LOC-01 find_blank_coords`

## PR 메타

| 항목 | 내용 |
|------|------|
| **Base** | `stabilize/green` |
| **Head** | `feat/dom/green-d-loc-01` |
| **커밋** | `9b77bb1` — `green(dom): implement find_blank_coords for D-LOC-01` |
| **TDD 단계** | **GREEN** (Commit 1 / 4) |
| **요구사항** | FR-02 Blank Coordinate Discovery |
| **Test ID** | D-LOC-01 |

---

## 배경

Magic Square 프로젝트는 **Dual-Track TDD**로 진행 중입니다.

- **Track A (Boundary)**: 입력 검증·출력 계약·Domain 미호출
- **Track B (Domain)**: 빈칸 탐색 → 누락 숫자 → 마방진 검증 → 풀이

RED 단계에서 Track B 테스트(`test_track_b_red.py`, `tests/entity/test_d_*.py`)는 이미 작성되어 있었고, `find_blank_coords`는 `NotImplementedError` 스텁 상태였습니다.

이 PR은 **Track B GREEN 4커밋 계획의 1번째 커밋**으로, **D-LOC-01 묶음만** 최소 구현해 통과시키는 것이 목표입니다.

```
feat/dom/green-d-loc-01  →  PR #1  →  stabilize/green
feat/dom/green-d-mis-01  →  PR #2  →  stabilize/green  (후속)
feat/dom/green-d-val-01  →  PR #3  →  stabilize/green  (후속)
feat/dom/green-d-sol-01  →  PR #4  →  stabilize/green  (후속)
                              ↓
                          develop  (4 PR 완료 후)
```

---

## 변경 요약

| 파일 | 변경 내용 |
|------|-----------|
| `src/magicsquare/entity/blank_locator.py` | `find_blank_coords` 최소 구현 (RED 스텁 제거) |
| `tests/entity/test_d_loc.py` | D-LOC-01 스켈레톤 `pytest.fail` → assert 전환 |
| `pyproject.toml` | `pythonpath`에 `"."` 추가 (테스트 수집 오류 해소) |
| `README.md` | Track B GREEN 4-commit 계획·진행 상태 반영 |

**변경 파일 수:** 4개  
**추가/삭제:** +41 / −29 lines

---

## 구현 상세 — `find_blank_coords`

### 요구사항 (PRD FR-02)

- 4×4 격자를 **row-major**(행 우선) 순서로 스캔
- 값이 `0`인 셀을 빈칸으로 간주
- 첫 번째·두 번째 빈칸의 **1-index** 좌표 `(r, c)` 반환
- 반환 형식: `(r1, c1, r2, c2)`

### 구현 방식

```python
for row_index in range(GRID_SIZE):
    for col_index in range(GRID_SIZE):
        if matrix[row_index][col_index] == 0:
            blanks.append((row_index + 1, col_index + 1))
return (blanks[0][0], blanks[0][1], blanks[1][0], blanks[1][1])
```

- 격자 크기는 named constant **`GRID_SIZE`** (`entity/constants.py`) 사용 — 매직 넘버 `4` 하드코딩 없음
- 입력 행렬 **비변경** (in-place 수정 없음) → BR-15 입력 불변 가드 충족
- FR-01(입력 검증)은 Boundary 책임 — Domain은 FR-01 통과 입력만 받는다고 가정 (빈칸 ≠ 2 예외 처리 없음, GREEN 범위 밖)

### G1 픽스처 기대값

```
G1 = [
    [16,  3,  2, 13],
    [ 5,  0, 11,  8],   ← (2,2) 1-index
    [ 9,  6,  0, 12],   ← (3,3) 1-index
    [ 4, 15, 14,  1],
]
→ find_blank_coords(G1) == (2, 2, 3, 3)
```

---

## 테스트 변경 — D-LOC-01

### Before (RED Skeleton)

```python
pytest.fail("RED: D-LOC-01 — G1 row-major blanks (2,2) and (3,3) 1-index")
```

### After (Full RED → GREEN 통과)

```python
assert find_blank_coords(G1) == (2, 2, 3, 3)
```

스켈레톤에서 assert로 전환한 것이지, **기대값 약화·테스트 삭제는 없음**.

### 이 PR에서 통과하는 테스트 (3건)

| # | 파일 | 테스트 | 검증 내용 |
|---|------|--------|-----------|
| 1 | `tests/domain/test_track_b_red.py` | `TestDLOC01FindBlankCoords::test_find_blank_coords_row_major_g1` | Full RED — G1 → `(2,2,3,3)` |
| 2 | `tests/entity/test_d_loc.py` | `TestDLOC01BlankCoordinates::test_d_loc_01_row_major_blanks_g1` | Skeleton → Full RED 전환 |
| 3 | `tests/domain/test_track_b_red.py` | `TestDomainInputImmutability::test_find_blank_coords_does_not_mutate_g1` | BR-15 입력 불변 |

### 검증 명령

```bash
pip install -e ".[dev]"

# D-LOC-01 관련만
pytest tests/domain/test_track_b_red.py::TestDLOC01FindBlankCoords \
       tests/entity/test_d_loc.py \
       tests/domain/test_track_b_red.py::TestDomainInputImmutability::test_find_blank_coords_does_not_mutate_g1 -v
# Expected: 3 passed
```

---

## 인프라 수정 — `pyproject.toml`

**문제:** `tests/boundary/test_track_a_red.py` 등에서 `from tests.conftest import ...` 시 `ModuleNotFoundError: No module named 'tests.conftest'` 발생.

**원인:** `pythonpath = ["src"]`만 설정되어 프로젝트 루트가 PYTHONPATH에 없음.

**수정:** `pythonpath = ["src", "."]`

이 변경으로 `PYTHONPATH=.` 없이도 전체 suite 수집이 가능해집니다. Track B GREEN 작업 전반에 필요한 설정이므로 Commit 1에 포함했습니다.

---

## GREEN 제약 준수 체크리스트

| 제약 | 준수 여부 | 비고 |
|------|-----------|------|
| RED 1묶음(D-LOC-01)만 통과 | ✅ | D-MIS/D-VAL/D-SOL 미구현 |
| 테스트 약화·삭제 금지 | ✅ | 스켈레톤 → 동일 기대값 assert |
| 하드코딩·매직 넘버 금지 | ✅ | `GRID_SIZE` 사용 |
| REFACTOR 금지 | ✅ | 구조 추출·리네이밍 없음 |
| 한 커밋에 모든 RED 해결 금지 | ✅ | `blank_locator.py`만 구현 |
| Domain Mock 금지 | ✅ | 실제 구현 호출 |
| PyQt / Screen only | ✅ | UI 코드 없음 |

---

## 의도적으로 포함하지 않은 것

리뷰 시 **이 PR 범위 밖**임을 확인해 주세요.

- `find_not_exist_nums` (D-MIS-01) — PR #2
- `is_magic_square` (D-VAL-01~06) — PR #3
- `solution` (D-SOL-01~04) — PR #4
- Track A `InputValidator` / `BoundaryValidator` GREEN
- 빈칸 개수 ≠ 2에 대한 Domain 예외 처리 (Boundary FR-01 책임)
- REFACTOR (`LineEnumerator` 추출, `BLANK_COUNT` 검증 추가 등)
- `RED-DOM-DET-001` 결정론 테스트

**전체 suite 기준:** D-LOC-01 외 Track B·Track A 테스트는 여전히 RED(실패) 상태가 정상입니다.

---

## README 변경

Track B GREEN 4-commit 로드맵을 README에 문서화했습니다.

- Phase 1 Track B RED 항목 → `[x]` (테스트 작성 완료 표시)
- Phase 2 Track B GREEN → 4-commit × 4-PR 표 추가
- Commit 1 → `[x]`, Commit 2~4 → `[ ]`
- Git 브랜치 규칙에 `feat/dom/green-*` → `stabilize/green` 추가

---

## 리뷰 포인트 (동료 리뷰용)

1. **row-major 순서** — `range(GRID_SIZE)` 이중 루프가 PRD FR-02 §196~199와 일치하는지
2. **1-index 변환** — `row_index + 1`, `col_index + 1`이 BR-10 계약과 맞는지
3. **입력 불변** — `matrix`를 수정하지 않는지 (BR-15)
4. **최소 구현 범위** — D-LOC-01 외 기능이 섞이지 않았는지
5. **상수 사용** — `4` 리터럴 없이 `GRID_SIZE`만 사용하는지
6. **테스트 전환** — `test_d_loc.py`의 assert가 `test_track_b_red.py`와 동일 계약인지
7. **pythonpath 변경** — 부작용 없이 전체 suite 수집이 되는지

### 선택적 후속 (이 PR에서 하지 않음)

- `BLANK_COUNT`로 빈칸 개수 검증 추가 → REFACTOR 또는 Boundary 연동 시
- `find_blank_coords`에 대한 빈칸 0개/3개 방어 코드 → FR-01 이후 논의

---

## 머지 후 다음 단계

PR #1 머지 → `stabilize/green` 업데이트 후:

- **PR #2:** `feat/dom/green-d-mis-01` — `find_not_exist_nums` (D-MIS-01)
- 기대: G1 → `(7, 10)` 오름차순 튜플

---

## Test Plan (체크리스트)

- [x] `pytest` D-LOC-01 관련 3건 통과
- [x] `find_blank_coords(G1) == (2, 2, 3, 3)` 수동 확인
- [x] G1 deepcopy 후 호출해도 원본 불변
- [ ] 전체 suite GREEN — **의도적으로 미달** (Track B 2~4, Track A RED 잔존)
- [ ] Coverage gate 80% — GREEN 4-commit 완료 후 확인 예정

---

## 관련 문서

- [Report/12-green-dom-d-loc-01_Report.md](../Report/12-green-dom-d-loc-01_Report.md)
- [Prompting/12-green-dom-d-loc-01_Prompt.md](../Prompting/12-green-dom-d-loc-01_Prompt.md)
