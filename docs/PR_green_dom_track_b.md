# PR — Track B GREEN (4 commits): Domain FR-02 ~ FR-05

## PR 메타

| 항목 | 내용 |
|------|------|
| **Base** | `stabilize/green` |
| **Head** | `feat/dom/green-d-loc-01` |
| **TDD 단계** | **GREEN** — Track B Domain 전체 |
| **커밋 수** | 4 (+ 문서·픽스처 보조 커밋) |
| **범위** | Entity: `find_blank_coords` → `find_not_exist_nums` → `is_magic_square` → `solution` |

---

## 배경

Magic Square 4×4 프로젝트는 **Dual-Track TDD**로 진행합니다.

- **Track A (Boundary)**: 입력 검증·출력 계약·Domain 미호출 — **본 PR 범위 외**
- **Track B (Domain)**: 빈칸 탐색 → 누락 숫자 → 마방진 검증 → 풀이 — **본 PR 범위**

RED 단계에서 Track B 테스트(`test_track_b_red.py`, `tests/entity/test_d_*.py`)와 Entity 스텁이 준비되어 있었습니다. 본 PR은 **RED 1묶음씩 최소 구현 → 커밋** 규칙으로 Track B GREEN 4단계를 완료합니다.

### 브랜치·PR 전략

```
feat/dom/green-d-loc-01  ──(단일 PR)──►  stabilize/green  ──►  develop
         │  Commit 1: D-LOC-01
         │  Commit 2: D-MIS-01
         │  Commit 3: D-VAL-01~06
         └  Commit 4: D-SOL-01~04
```

초기에는 커밋별 PR 4개를 계획했으나, **단일 PR + 커밋 4개**로 통합했습니다.

---

## 변경 요약

| 레이어 | 파일 | FR | Test ID |
|--------|------|-----|---------|
| Entity | `blank_locator.py` | FR-02 | D-LOC-01 |
| Entity | `missing_finder.py` | FR-03 | D-MIS-01 |
| Entity | `magic_validator.py` | FR-04 | D-VAL-01~06 |
| Entity | `solver.py` | FR-05 | D-SOL-01~04 |
| Tests | `tests/entity/test_d_*.py` | — | 스켈레톤 → assert |
| Fixtures | `golden_grids.py` | — | G3 unsolvable lock, D-SOL-01 정렬 |
| Infra | `pyproject.toml` | — | `pythonpath`에 `"."` 추가 |
| Docs | `README.md`, Report/12~15 | — | 진행 상태·세션 기록 |

---

## 커밋별 상세

### Commit 1 — D-LOC-01 `find_blank_coords` (`9b77bb1`)

**요구사항 (FR-02):** row-major 스캔, 빈칸(`0`) 2개의 1-index 좌표 `(r1,c1,r2,c2)` 반환.

```python
for row_index in range(GRID_SIZE):
    for col_index in range(GRID_SIZE):
        if matrix[row_index][col_index] == 0:
            blanks.append((row_index + 1, col_index + 1))
```

| 상수 | 용도 |
|------|------|
| `GRID_SIZE` | 격자 크기 |

**통과 테스트:** D-LOC-01 2건 + BR-15 입력 불변 1건

---

### Commit 2 — D-MIS-01 `find_not_exist_nums` (`e321b6b`)

**요구사항 (FR-03):** `{VALUE_MIN..VALUE_MAX} \ S` → `(n1, n2)`, `n1 < n2`.

| 상수 | 용도 |
|------|------|
| `GRID_SIZE`, `VALUE_MIN`, `VALUE_MAX` | 스캔·누락 집합 |

**통과 테스트:** D-MIS-01 2건 (G1 → `(7, 10)`)

---

### Commit 3 — D-VAL-01~06 `is_magic_square` (`cd73f77`)

**요구사항 (FR-04):**

1. 모든 값 ∈ `{1..16}`, 중복 없음, 16셀
2. 4행·4열·주대각·반대각 합 = `MAGIC_CONSTANT_N4`
3. 모두 통과 시 `True`, 하나라도 실패 시 `False`

| 상수 | 용도 |
|------|------|
| `GRID_SIZE`, `VALUE_MIN`, `VALUE_MAX`, `MAGIC_CONSTANT_N4` | 집합·10줄 합 검사 |

**통과 테스트:** D-VAL-01~06 **14건** (Full RED + entity skeleton)

---

### Commit 4 — D-SOL-01~04 `solution`

**요구사항 (FR-05):**

1. `find_blank_coords` + `find_not_exist_nums` 호출
2. **Attempt 1 (small-first):** `n1→blank1`, `n2→blank2` on copy → `is_magic_square`
3. 성공 → `[r1, c1, n1, r2, c2, n2]`
4. **Attempt 2 (reverse):** `n2→blank1`, `n1→blank2` → 검증
5. 성공 → `[r1, c1, n2, r2, c2, n1]`
6. 둘 다 실패 → `UnsolvableDomainError`

입력 행렬은 **절대 수정하지 않음** (`copy.deepcopy` on trial only).

#### Fixture 정합 (GREEN 수치 lock)

| 항목 | RED 상태 | GREEN 조치 |
|------|----------|------------|
| **G3 / TD_UNSOLVABLE** | TBD placeholder — small-first 실제 성공 | unsolvable 격자로 수치 확정 |
| **D-SOL-01** | G1 + `[2,2,7,3,3,10]` — G1에서 small-first 수학적 불가 | `G1_SF` + `[1,2,3,4,3,14]` (Report/10 분리 권고 반영) |

**G3 (unsolvable, 확정):**

```
[[ 2,  3,  0, 13],
 [ 5, 10, 11,  8],
 [ 9,  6,  0, 12],
 [ 4, 15, 14,  1]]
```

**D-SOL 시나리오 매핑:**

| Test ID | Fixture | 기대 결과 | 경로 |
|---------|---------|-----------|------|
| D-SOL-01 | `G1_SF` | `[1,2,3,4,3,14]` | small-first 성공 |
| D-SOL-02 | `G2` (= `G1`) | `[2,2,10,3,3,7]` | reverse 성공 |
| D-SOL-03 | `G3` | `UnsolvableDomainError` | both fail |
| D-SOL-04 | `G1_SF` | 길이 6, 1-index 좌표 | 결과 형태 |

**통과 테스트:** D-SOL 8건 (track_b + entity)

---

## 검증 결과

```bash
pip install -e ".[dev]"

# Track B 전체
pytest tests/domain/test_track_b_red.py tests/entity/ -v
# Expected: 27 passed
```

| 구분 | passed |
|------|--------|
| `test_track_b_red.py` | 14 |
| `tests/entity/test_d_*.py` | 13 |
| **합계** | **27** |

Track A·레거시 AC-FR-01-01 테스트는 **의도적 RED** (본 PR 범위 외).

---

## GREEN 제약 준수 체크리스트

| 제약 | 준수 |
|------|------|
| RED 1묶음씩 최소 구현 | ✅ 4커밋 분리 |
| 테스트 약화·삭제 금지 | ✅ 스켈레톤 → 동일/정합 assert |
| 매직 넘버 금지 | ✅ `GRID_SIZE`, `VALUE_*`, `MAGIC_CONSTANT_N4` |
| REFACTOR 금지 | ✅ `LineSumChecker` 등 미추출 |
| Domain Mock 금지 | ✅ 실제 구현·협력 호출 |
| 입력 불변 (BR-15) | ✅ deep copy on trial |
| PyQt / Screen only | ✅ UI 코드 없음 |

---

## 의도적으로 포함하지 않은 것

- Track A `InputValidator` / `BoundaryValidator` GREEN
- Control layer 오케스트레이션 (Integration GREEN)
- REFACTOR (`LineEnumerator`, `BLANK_COUNT` Domain 검증 등)
- `RED-DOM-DET-001` 결정론 테스트
- Coverage gate 80% (Track B GREEN 완료 후 별도 확인)

---

## 리뷰 포인트

1. **ECB 의존 방향** — `solver` → `blank_locator`, `missing_finder`, `magic_validator` (entity 내부만)
2. **1-index 계약** — `find_blank_coords` 출력 ↔ `solution` 반환 좌표
3. **small-first / reverse 순서** — FR-05 Attempt 1→2 순서 준수
4. **G3 / D-SOL-01 fixture 변경** — 수학적 정합·Report/10 TBD 해소
5. **입력 불변** — `solution`, `find_blank_coords` 호출 후 원본 동일
6. **상수 사용** — `4`, `16`, `34` 리터럴 없음

---

## 관련 문서

| 문서 | 내용 |
|------|------|
| [Report/12-green-dom-d-loc-01_Report.md](../Report/12-green-dom-d-loc-01_Report.md) | Commit 1 세션 |
| [Report/13-green-dom-d-mis-01_Report.md](../Report/13-green-dom-d-mis-01_Report.md) | Commit 2 세션 |
| [Report/14-green-dom-d-val-01_Report.md](../Report/14-green-dom-d-val-01_Report.md) | Commit 3 세션 |
| [Report/15-green-dom-d-sol-01_Report.md](../Report/15-green-dom-d-sol-01_Report.md) | Commit 4 세션 |
| [docs/PR_green_dom_d_loc_01.md](./PR_green_dom_d_loc_01.md) | Commit 1 단독 Description (참고용, 본 문서가 SSOT) |

---

## Test Plan

- [x] `pytest tests/domain/test_track_b_red.py tests/entity/` — 27 passed
- [x] D-LOC-01 ~ D-SOL-04 개별 묶음 회귀
- [x] G3 both-fail 수동 검증
- [x] G1_SF small-first / G1 reverse 수동 검증
- [ ] 전체 suite GREEN — Track A RED 잔존 (정상)
- [ ] Coverage ≥ 80% — follow-up

---

## 머지 후 다음 단계

1. `feat/dom/green-d-loc-01` → `stabilize/green` 머지
2. `stabilize/green` → `develop` 통합 PR
3. Track A GREEN (`InputValidator` E00x envelope)
4. Phase 3 REFACTOR (Track B `LineSumChecker` 등)
