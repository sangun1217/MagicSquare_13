# MagicSquare — 문서 인덱스

구현·TDD 진행 시 참고하는 문서 모음입니다.

| 문서 | 설명 |
|------|------|
| [PRD_MagicSquare.md](./PRD_MagicSquare.md) | FR/BR, Dual-Track TDD, Traceability |
| [defect_list.md](./defect_list.md) | RED 단계 결함 추적 |
| [test_plan.md](./test_plan.md) | AC-FR01-01 테스트 계획 |
| [golden_master_approve_pattern.md](./golden_master_approve_pattern.md) | Golden Master approve 패턴 설계 |

루트 [README.md](../README.md)의 「Dual-Track TDD — 해야 할 목록」과 함께 보면 Sprint·Phase 진행 상황을 추적할 수 있습니다.

---

## RED 단계 To-Do 리스트

Dual-Track RED(테스트만, 의도한 실패 확인) 착수 전·중에 확인할 항목입니다. 상세 Task ID는 [PRD §15](./PRD_MagicSquare.md) 및 루트 README Phase 1을 따릅니다.

- [ ] Track A RED — `RED-BND-001`~`007` (입력 검증·출력 계약·Domain 미호출)
- [ ] Track B RED — `RED-DOM-BLK/MIS/VAL/SOL-*` (빈칸·누락·검증·Solver)
- [ ] Integration RED — `SC-DOM-SOL-001` (Control end-to-end)
- [x] `pytest` 실행 → 의도한 실패 로그 확보 — [defect_list.md](./defect_list.md)

### Golden Master 회귀 안전장치

Refactoring 시작 전 구축.  
GREEN 완료 후 즉시 적용.

#### 기준 파일 생성

- [x] **GM-01:** `tests/golden_master_expected.txt` 생성
- [x] **GM-02:** 정상/역순/오류 시나리오 추가 (GM-TC-01~05)
- [x] **GM-03:** `git add tests/golden_master_expected.txt` (버전 관리 포함)

#### 테스트 코드

- [x] **GM-04:** `tests/integration/test_golden_master_magic_square.py` 작성
- [x] **GM-05:** approve 패턴 적용 (`tests/golden_master/approve.py`, `PYTEST_APPROVE=1`)
- [x] **GM-06:** Golden Master 테스트 PASS 확인 (`pytest -m golden_master -v`)

#### 회귀 보호

- [x] **GM-07:** row-major 규칙 보호 (`tests/golden_master/contracts.py`)
- [x] **GM-08:** 1-index 출력 보호
- [x] **GM-09:** reverse 조합 fallback 보호
- [x] **GM-10:** Error Contract 보호 (`INVALID_BLANK_COUNT`, `DUPLICATE_NUMBER`, `NO_VALID_MAGIC_SQUARE`)

**실행**

```bash
pip install -e ".[dev]"
pytest -m golden_master -v
python scripts/generate_golden_master.py --approve   # baseline 갱신
```

**관련 파일**

- Baseline: `tests/golden_master_expected.txt`
- 시나리오 SSOT: `tests/golden_master/scenarios.py`
- 설계: [golden_master_approve_pattern.md](./golden_master_approve_pattern.md)
