# 결함 목록 (Defect List)

| 항목 | 내용 |
|------|------|
| **문서 ID** | DEF-MSQ-RED-001 |
| **버전** | 1.0 |
| **기준 일자** | 2026-05-29 |
| **브랜치** | `feature/dual-track-tdd` |
| **pytest 스냅샷** | 20 failed, 24 passed (`pytest -q`, 전체 suite) |
| **관련 테스트** | `tests/boundary/test_ac_fr01_01_invalid_size.py` |
| **관련 계획** | [test_plan.md](./test_plan.md), [PRD_MagicSquare.md](./PRD_MagicSquare.md) |

---

## 요약

| Severity | 건수 | 상태 |
|----------|------|------|
| Critical | 1 | Open |
| High | 2 | Open |
| Medium | 2 | Open |
| Low | 1 | Open |

**RED 단계 의도:** DEF-001은 TDD RED로 **의도된 실패**이나, GREEN 착수 전 결함 추적·수정 범위 정의를 위해 등록한다. DEF-002~006은 구현 전에 해소할 **설계·문서·테스트 정합** 이슈다.

---

## 결함 상세

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|-------|-----------|--------|--------|-----------|-----------|
| DEF-001 | Critical | AC-FR-01-01 | 1. `pip install -e ".[dev]"` 2. `pytest tests/boundary/test_ac_fr01_01_invalid_size.py -v` 3. `TestNormalFailureReturn::test_grid_none_raises_invalid_input_error` 실행 4. `BoundaryValidator().validate(None)` | `InvalidInputError` 발생, `code="INVALID_SIZE"`, `message="Grid must be 4x4."` | `NotImplementedError: RED: BoundaryValidator.validate not implemented` (`boundary_validator.py:24`) | FR-01 Rule 1 미구현; `validate()`가 RED 스텁으로만 존재 | `grid is None` / `[]` / 비 4×4 분기 구현 후 `InvalidInputError` raise; Rule 5(실패 시 조기 반환) 적용 |
| DEF-002 | Critical | AC-FR-01-01, RED-BND-006 | 1. 동일 테스트 모듈에서 `TestDomainIsolation::test_grid_none_resolve_zero_calls` 실행 2. `@patch resolve` 후 `solve(None)` 호출 | `pytest.raises(InvalidInputError)` 통과, `resolve.assert_not_called()` | `NotImplementedError` (validate 스텁에서 동일, `solve`가 validate까지 도달 못 함) | DEF-001과 동일 — Boundary 검증 미구현으로 Control 격리 시나리오 전단 실패 | DEF-001 해결 후 재실행; `solve()`는 validate 실패 시 `resolve()` 호출 금지 유지 |
| DEF-003 | High | AC-FR-01-01 | 1. GREEN 가정으로 `validate(None)`이 charter 계약으로 구현됨 2. `TestNormalFailureReturn` 통과 3. `TestMessageIdentity::test_grid_none_message_char_by_char_prd_section` 실행 | `exc.message == "Invalid grid dimensions: expected 4x4."` (PRD §13) | (DEF-001 해소 후 예상) charter 메시지 `"Grid must be 4x4."`와 불일치로 assert 실패 | 동일 AC에 **charter**(`INVALID_SIZE`, `Grid must be 4x4.`)와 **PRD**(`ERR-VAL-001`, §13 고정 문자열) 이중 기대가 테스트 클래스에 공존 | GREEN 전 단일 계약 확정: (A) PRD §13 채택 시 charter 테스트·상수 정렬, 또는 (B) charter 채택 시 PRD MessageIdentity 테스트·README 정렬 |
| DEF-004 | Medium | AC-FR-01-01, RED-BND-001 | 1. [README.md](../README.md) Phase 1 `RED-BND-001` 항목 확인 2. `tests/boundary/ac_fr01_01_constants.py` 확인 | README·PRD·테스트가 동일 error `code` 사용 | README/PRD: `ERR-VAL-001`; 테스트 charter: `INVALID_SIZE` | 추적성 문서와 RED 테스트 charter 간 명명 불일치 | README `RED-BND-001`과 `CHARTER_CODE`를 `ERR-VAL-001`로 통일하거나, PRD 부록에 `INVALID_SIZE` alias 명시 |
| DEF-005 | Medium | AC-FR-01-01 | 1. `tests/fixtures/golden_grids.py`의 `TD_INVALID_SIZE` 확인 (4행×3열) 2. [test_plan.md](./test_plan.md) TC-BND-01-04(3×4)와 비교 | fixture 이름이 3×4 또는 4×3 중 하나로 명확 | 4×3 행렬이 `TD_INVALID_SIZE`로 명명됨; AC 테스트는 `GRID_3X4` 인라인 사용 | fixture 명명·차원 혼동 | `TD_INVALID_SIZE_4X3` / `TD_INVALID_SIZE_3X4` 분리 또는 주석·리네이밍; test_plan·golden 정합 |
| DEF-006 | Low | — | 1. `pytest --cov=magicsquare.boundary --cov-fail-under=85` 실행 (BoundaryValidator 미구현) | Boundary layer coverage ≥ 85% (NFR-02) | `boundary_validator.py` 미실행 분기·미커버 | GREEN 전 RED 단계라 coverage gate 미달은 예상 | GREEN 후 `BoundaryValidator` 분기 커버; CI gate는 FR-01 GREEN PR 이후 활성화 |

---

## 실패 테스트 매핑 (DEF-001 / DEF-002)

| 테스트 클래스 | 실패 건수 | 대표 결함 ID |
|---------------|-----------|--------------|
| `TestNormalFailureReturn` | 5 | DEF-001, DEF-003(잠재) |
| `TestBoundaryValues` | 5 | DEF-001 |
| `TestDomainIsolation` | 5 | DEF-001, DEF-002 |
| `TestMessageIdentity` | 5 | DEF-001, DEF-003(잠재) |
| `TestScopeRestriction` | 0 (12 passed) | — |

---

## 재현 명령 (공통)

```bash
pip install -e ".[dev]"
pytest tests/boundary/test_ac_fr01_01_invalid_size.py -v --tb=short
pytest -q
```

**대표 실패 스택 (DEF-001):**

```text
src/magicsquare/boundary/boundary_validator.py:24: NotImplementedError:
  RED: BoundaryValidator.validate not implemented
```

---

## 수정 우선순위 (QA 권고)

1. **DEF-003 / DEF-004** — error `code`·`message` 단일 기준 확정 (PRD §13 vs charter).
2. **DEF-001** — `BoundaryValidator.validate()` FR-01 Rule 1 최소 구현 (`None`, `[]`, ragged row, 3×4/4×3/5×5).
3. **DEF-002** — DEF-001 통과 후 `solve()` + `resolve` mock 격리 5건 재검증.
4. **DEF-005** — fixture 정리(회귀 데이터 혼동 방지).
5. **DEF-006** — GREEN PR에서 coverage gate 확인.

---

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR-01-01 RED 실행 결과 기반 초기 결함 6건 등록 |
