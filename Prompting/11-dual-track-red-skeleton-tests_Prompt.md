# 11-dual-track-red-skeleton-tests — Session Transcript

## 세션 개요

| 항목 | 내용 |
|------|------|
| **주제** | Dual-Track TDD — RED (Skeleton) 테스트만 작성 |
| **에이전트** | Dual-Track UI + Logic TDD 전문가 / report-backup-agent |
| **SSOT** | Report/09(요청), PRD, Report/02, Report/08 `test_ac_fr01_01` |

---

## Turn 1 — User

**TDD phase: RED (Skeleton)** — 테스트 스켈레톤만.

**금지:** src 구현·stub, GREEN/REFACTOR, skip/xfail, assert 기대값, Report/08 `test_ac_fr_01_01` 수정·삭제.

**범위:** U-IN-04~08, U-OUT-01~03, U-FLOW-02(확장), D-LOC-01, D-MIS-01, D-VAL-01~06, D-SOL-01~04. U-IN-01~03 중복 금지.

**규칙:** `pytest.fail("RED: …")` 한 줄; Given/When 주석; `tests/boundary/test_u_*.py`, `tests/entity/test_d_*.py`; G2 TBD.

**완료 조건:** `pytest tests/boundary/ tests/entity/` 전부 RED; src 변경 없음.

---

## Turn 1 — Assistant (실행)

1. `tests/boundary/test_u_in.py` — U-IN-04~08 (6 functions)
2. `tests/boundary/test_u_out.py` — U-OUT-01~03
3. `tests/boundary/test_u_flow.py` — U-FLOW-02 ×5
4. `tests/entity/test_d_loc.py`, `test_d_mis.py`, `test_d_val.py`, `test_d_sol.py`
5. `tests/entity/conftest.py` — G0~G3 placeholder

**pytest (스켈레톤만):** 27 failed, 0 passed.  
**pytest (boundary+entity):** 60 failed, 13 passed (Report/08 scope 가드).

---

## Turn 2 — User

`@.cursor/agents/report-backup-agent.md 리포트/백업`

---

## Turn 2 — Assistant

`Report/11-dual-track-red-skeleton-tests_Report.md`, `Prompting/11-dual-track-red-skeleton-tests_Prompt.md` 생성.

---

## 최종 결과 요약

| 항목 | 상태 |
|------|------|
| Skeleton 27건 | 완료 (`pytest.fail`) |
| src/ 변경 | 없음 (본 세션) |
| Report/08 Full RED | 불변 |
| 다음 | Full RED assert → Track A GREEN |
