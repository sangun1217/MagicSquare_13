# 11-dual-track-red-skeleton-tests Report

## 작업 배경/목표

- Magic Square 4×4 **Dual-Track TDD**에서 **RED (Skeleton)** 단계만 수행한다.
- SSOT: `Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md`(참조 요청; 저장소 미존재 → PRD·이전 RED 설계표·`golden_grids`로 매핑), `docs/PRD_MagicSquare.md`, Report/08 Full RED(`test_ac_fr01_01_invalid_size.py`).
- **목표:** Report/09 설계표 중 **아직 pytest가 없던** Test ID에 대해 `pytest.fail()` 스켈레톤만 추가; `src/`·Report/08 기존 13건 Full RED **불변**.

## 수행 내용

### RED Skeleton 규칙 적용

- 테스트 파일·클래스·함수·import 구조만 작성; 본문은 `pytest.fail("RED: <Test ID> — …")` 한 줄.
- Given/When/Then은 **주석만**; Then assert **금지**.
- Track A: `tests/boundary/test_u_*.py` (U-OUT/U-FLOW에 mock/spy **주석**).
- Track B: `tests/entity/test_d_*.py` (**Domain Mock 금지**).
- `tests/entity/conftest.py`: G0~G3 **주석·placeholder**; D-SOL-02는 `G2 TBD` 명시.

### 범위 (중복 제외)

| 포함 | 제외 |
|------|------|
| U-IN-04~08, U-OUT-01~03, U-FLOW-02(5건 확장) | U-IN-01~03 (Report/08) |
| D-LOC-01, D-MIS-01, D-VAL-01~06, D-SOL-01~04 | `test_ac_fr01_01` 수정·삭제 |
| | `src/` 구현·stub |

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 생성 | `tests/boundary/test_u_in.py` (6 tests) |
| 생성 | `tests/boundary/test_u_out.py` (3 tests) |
| 생성 | `tests/boundary/test_u_flow.py` (5 tests) |
| 생성 | `tests/entity/__init__.py` |
| 생성 | `tests/entity/conftest.py` |
| 생성 | `tests/entity/test_d_loc.py` (1 test) |
| 생성 | `tests/entity/test_d_mis.py` (1 test) |
| 생성 | `tests/entity/test_d_val.py` (7 tests) |
| 생성 | `tests/entity/test_d_sol.py` (4 tests) |
| **미수정** | `tests/boundary/test_ac_fr01_01_invalid_size.py` |
| **미수정** | `src/**` (본 작업 세션) |

**스켈레톤 합계:** 27 test functions.

## 검증 결과

| 명령 | 결과 | 비고 |
|------|------|------|
| `pytest tests/boundary/test_u_in.py tests/boundary/test_u_out.py tests/boundary/test_u_flow.py tests/entity/` | **27 failed, 0 passed** | 전부 `pytest.fail` — Skeleton RED 충족 |
| `pytest tests/boundary/ tests/entity/` | **60 failed, 13 passed** | 13 passed = Report/08 `TestScopeRestriction` 가드 |

## Test ID 매핑 요약

| Track | ID | 파일 |
|-------|-----|------|
| A | U-IN-04 ~ U-IN-08 | `test_u_in.py` |
| A | U-OUT-01 ~ U-OUT-03 | `test_u_out.py` |
| A | U-FLOW-02 (×5 시나리오) | `test_u_flow.py` |
| B | D-LOC-01 | `test_d_loc.py` |
| B | D-MIS-01 | `test_d_mis.py` |
| B | D-VAL-01 ~ D-VAL-06 | `test_d_val.py` |
| B | D-SOL-01 ~ D-SOL-04 | `test_d_sol.py` (D-SOL-02: G2 TBD) |

## 남은 이슈 및 다음 액션

1. **Report/09** 문서를 저장소에 추가해 Test ID·메시지 SSOT 고정.
2. **Full RED 전환** — 스켈레톤 `pytest.fail` → Then assert 교체 (Track A `InputValidator` Failure envelope 등).
3. **Track A GREEN** — `InputValidator.validate` short-circuit 구현.
4. **D-SOL-02** — G2 격자·기대 `[2,2,10,3,3,7]` fixture lock.
5. **계약 정리** — E00x envelope vs Report/08 `InvalidInputError` / `ERR-VAL-*`.
6. 기존 `tests/boundary/test_track_a_red.py`, `tests/domain/test_track_b_red.py`와 신규 `test_u_*`/`test_d_*` 중복 ID 정리(선택).

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | Dual-Track RED Skeleton 27건 추가 세션 |
