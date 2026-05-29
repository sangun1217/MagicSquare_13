# 12-golden-master-regression — Session Transcript

## 세션 개요

| 항목 | 내용 |
|------|------|
| **주제** | Magic Square Solver Golden Master 회귀 안전장치 (GM-1 ~ GM-3) |
| **에이전트** | 회귀 테스트(Approval/Golden Master) 설계 / report-backup-agent |
| **SSOT** | GM-TC-01~05, `tests/golden_master_expected.txt`, PRD FR-05 출력 계약 |

---

## Turn 1 — User (GM-1)

**요청:** Magic Square Solver 실제 출력 기반 Golden Master 기준 파일 생성 및 버전 관리.

**구현 요구사항:**

1. 기준 출력 파일 생성 — 정상/reverse/invalid blank/duplicate/no valid solution 시나리오; stdout 또는 Result DTO serialize.
2. approve 패턴 — 파일 없으면 생성, 있으면 actual vs expected 비교, 불일치 시 unified diff + FAIL.
3. 기준 파일 구조 — `[section_id]`, `Input:`, `Output:` / `Error:` 블록.

**산출물:** `tests/golden_master_expected.txt`, 생성 스크립트, approve 패턴 설계 문서.

---

## Turn 1 — Assistant (GM-1 실행)

1. `tests/golden_master/` 모듈 — `scenarios.py`, `capture.py`, `approve.py`.
2. `scripts/generate_golden_master.py` — baseline 생성 CLI.
3. `docs/golden_master_approve_pattern.md` — 설계 문서.
4. Entity/Boundary/Control 최소 구현 — 실제 Solver 출력 캡처 가능하도록 GREEN 최소 코드.
5. `pyproject.toml` — `pythonpath = ["src", "."]`, `golden_master` 마커.
6. `tests/golden_master_expected.txt` 생성 및 `git add` staged.

---

## Turn 2 — User (GM-2)

**요청:** Golden Master 테스트 코드 작성.

**요구사항:**

- API result serialization 또는 stdout capture.
- `open(expected).read()` vs actual, approve 패턴.
- `@pytest.mark.golden_master`, `pytest -m golden_master -v`.
- 실패 시 `--- expected` / `+++ actual` unified diff.
- GM-TC-01~05: 정상/reverse/INVALID_BLANK_COUNT/DUPLICATE_NUMBER/NO_VALID_MAGIC_SQUARE.
- 검증: int[6], row-major, 1-index, small-first, reverse fallback, Error Contract.

**산출물:** `test_golden_master_magic_square.*`, baseline, 실행 결과.

---

## Turn 2 — Assistant (GM-2 실행)

1. `tests/integration/test_golden_master_magic_square.py` — GM-TC-01~05 + 전체 문서 테스트 (6건).
2. `tests/golden_master/contracts.py` — 출력·attempt·Error 계약 검증.
3. `assert_golden_master_section()` — section 단위 approve/compare.
4. 시나리오 정리 — GM-TC-01 `G1_SF` (small-first), GM-TC-02 `G1` (reverse); `NO_VALID_MAGIC_SQUARE` 라벨 통일.
5. `tests/integration/test_golden_master.py` 삭제·대체.
6. **`pytest -m golden_master -v` → 6 passed.**

---

## Turn 3 — User (GM-3)

**요청:** `@docs/README.md`에 `## RED 단계 To-Do 리스트` 아래 Golden Master 회귀 안전장치 섹션 추가.

**항목:** GM-01~10 (기준 파일, 테스트 코드, 회귀 보호) 체크리스트.

---

## Turn 3 — Assistant (GM-3 실행)

1. `docs/README.md` 신규 생성 (기존 파일 없음).
2. 문서 인덱스 + RED To-Do + Golden Master GM-01~10 체크리스트 (완료 `[x]`) + 실행 명령·관련 파일 링크.

---

## Turn 4 — User

`@.cursor/agents/report-backup-agent.md 리포트/백업`

---

## Turn 4 — Assistant

`Report/12-golden-master-regression_Report.md`, `Prompting/12-golden-master-regression_Prompt.md` 생성.

---

## 최종 결과 요약

| 항목 | 상태 |
|------|------|
| GM-1 baseline + approve | 완료 |
| GM-2 테스트 6건 | PASS |
| GM-3 docs/README.md | 완료 |
| baseline staged | `tests/golden_master_expected.txt` |
| 다음 | 커밋, CI `-m golden_master`, Track B RED fixture 정합 |

**실행 예**

```bash
pytest -m golden_master -v
PYTEST_APPROVE=1 pytest -m golden_master -v
python scripts/generate_golden_master.py --approve
```
