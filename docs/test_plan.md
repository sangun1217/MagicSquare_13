# 테스트 계획서 — AC-FR01-01 (입력 크기·참조 검증)

| 항목 | 내용 |
|------|------|
| **문서 ID** | TP-MSQ-FR01-01-001 |
| **버전** | 1.0 |
| **작성 역할** | Senior QA Lead |
| **기준 PRD** | [PRD_MagicSquare.md](./PRD_MagicSquare.md) |
| **대상 AC** | **AC-FR01-01** (FR-01 선행 입력 유효성 — 구조·참조) |
| **Track** | Track A — Boundary / UI Contract |
| **기술 스택** | Python 3.11+, pytest, pydantic v2, unittest.mock |
| **상태** | 구현 전 (RED → GREEN 대비) |

---

## 1. 목적 및 범위

### 1.1 목적

`grid = None`을 대표 샘플로, **FR-01 Processing Rule 1**(행·열 4×4) 및 **§12.1 null/empty** 계약을 Boundary에서 먼저 거절하고, **Domain resolver(Solver 및 하위 Entity)가 0회 호출**됨을 pytest로 증명한다.

### 1.2 코드·오류 코드 매핑

| 질의/레거시 표기 | PRD 확정 표기 |
|------------------|---------------|
| `INVALID_SIZE` | **`ERR-VAL-001`** |
| `"Grid must be 4x4."` | **`"Invalid grid dimensions: expected 4x4."`** |
| dict `{ code, message }` | 예외 **`InvalidInputError`** (`.code`, `.message`) |

### 1.3 In-Scope (본 계획서)

| 구분 | 포함 |
|------|------|
| FR | **FR-01** Rule 1, Rule 5 (실패 시 Domain 미호출) |
| AC | **AC-FR01-01** |
| BR | **BR-01** (4×4 입력) |
| RED ID | **RED-BND-001**, **RED-BND-006** |
| 시나리오 | **SC-BND-VAL-001**, **TP-E-01** |
| 컴포넌트 | `BoundaryValidator` (단위), `solve` / Control 진입점 (통합·mock) |
| 계층 | `magicsquare.boundary` |

### 1.4 Out-of-Scope (본 계획서에서 다루지 않음)

| 항목 | 사유 | 별도 계획 |
|------|------|-----------|
| **4×4 정상 입력** (빈칸 2개·값 유효) | AC-FR01-01 범위 **외** — 성공/후속 규칙 | AC-FR01-05, FR-02~05 |
| 빈칸 개수 ≠ 2 | Rule 3 | AC-FR01-02, `ERR-VAL-002` |
| 값 범위 위반 | Rule 2 | AC-FR01-03, `ERR-VAL-003` |
| 중복 값 | Rule 4 | AC-FR01-04, `ERR-VAL-004` |
| Solver 풀이 성공/실패 | Domain 로직 | Track B, `ERR-SOL-001` |

---

## 2. pytest 기반 단위 테스트 범위 및 우선순위

### 2.1 테스트 피라미드 (본 Epic)

```
        [ P2 ] Control.solve + mock (얇은 통합)
       /                              \
 [ P0 ] BoundaryValidator 단위          [ P1 ] pytest.mark.boundary 파라미터
```

### 2.2 우선순위 정의

| 우선순위 | 범위 | 파일(예정) | 목표 |
|----------|------|------------|------|
| **P0** | `BoundaryValidator.validate(grid)` 단위 | `tests/boundary/test_boundary_validator_fr01_01.py` | RED-BND-001: 모든 경계값에서 `ERR-VAL-001` + 메시지 고정 |
| **P1** | 동일 모듈, `@pytest.mark.parametrize` | 위와 동일 | 경계값 표 일괄 회귀 |
| **P2** | Control `solve()` + Domain mock | `tests/boundary/test_solve_domain_isolation_fr01_01.py` | RED-BND-006: 검증 실패 시 Solver/Entity **0 calls** |
| **P3** | pydantic 입력 스키마(어댑터) | `tests/boundary/test_grid_input_schema.py` | raw `None`/`[]` 수신 시 파싱 전 거절 또는 validator 위임 일관성 |

### 2.3 AAA 패턴 및 명명

- **Arrange**: fixture `grid` 주입 (`None`, `[]`, 비정형 행렬)
- **Act**: `validator.validate(grid)` 또는 `solve(grid)`
- **Assert**: `pytest.raises(InvalidInputError)` + `exc_info.value.code == "ERR-VAL-001"`
- 함수명: `test_<RED-ID>_<condition>_<expected_outcome>`

### 2.4 pydantic 역할 (Boundary 어댑터)

| 모델(예정) | 역할 |
|------------|------|
| `GridInput` | 외부 raw 입력(`list \| None`) 수신; `model_validate` 전 `None` 거절 정책 명시 |
| `Grid4x4` | 4×4 통과 후 normalized `list[list[int]]` (본 AC 범위 외 — GREEN 후속) |

**원칙:** AC-FR01-01 실패 경로는 **Domain 진입 전**에 종료. pydantic ValidationError를 그대로 노출하지 않고 **`InvalidInputError(ERR-VAL-001)`** 로 매핑할지 여부는 구현 시 Control/Boundary 정책으로 고정하고, 테스트는 **관찰 가능한 최종 예외**만 검증한다.

### 2.5 실행 명령 (로컬)

```bash
pip install -e ".[dev]"
pytest tests/boundary/test_boundary_validator_fr01_01.py -v
pytest tests/boundary/ -m boundary -v
```

---

## 3. 경계값 케이스 목록

모든 케이스는 **동일 기대 결과**: `InvalidInputError`, `code == "ERR-VAL-001"`, `message == "Invalid grid dimensions: expected 4x4."`, Domain resolver **0회**.

| TC ID | 입력 `grid` | 설명 | PRD 근거 |
|-------|-------------|------|----------|
| **TC-BND-01-01** | `None` | 명시적 None | §12.1 null, §13, DN-06 |
| **TC-BND-01-02** | `[]` | 빈 리스트 (행 0) | §12.1 empty |
| **TC-BND-01-03** | `[[]] * 4` | 행 4개·열 0 (`len(row)==0`) | Rule 1 — 열 길이 ≠ 4 |
| **TC-BND-01-04** | `3×4` 행렬 (3행×4열) | `TD-INVALID-SIZE` 유형 | AC-FR01-01, TP-E-01 |
| **TC-BND-01-05** | `4×3` 행렬 | 열 부족 | §12.1 `[4][3]` |
| **TC-BND-01-06** | `5×5` 행렬 | 행·열 초과 | §16.4 TD-INVALID-SIZE |
| ~~TC-BND-01-07~~ | ~~4×4 정상 격자~~ | **포함 금지** | AC-FR01-05 / FR-02+ 영역 |

### 3.1 구체 입력 스펙 (Arrange 데이터)

#### TC-BND-01-01 — `grid = None`

```text
grid = None
```

#### TC-BND-01-02 — `grid = []`

```text
grid = []
```

#### TC-BND-01-03 — `grid = [[]] * 4`

```text
grid = [[], [], [], []]   # 동치: [[]] * 4
```

> **주의:** `[[]] * 4`는 4개 행이 **동일 빈 리스트 객체를 참조**할 수 있음. 불변성 테스트와 무관하나, Rule 1(열 개수) 검증 목적에는 유효.

#### TC-BND-01-04 — 3×4

```text
grid = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
]
```

(프로젝트 fixture: `tests/fixtures/golden_grids.TD_INVALID_SIZE`)

#### TC-BND-01-05 — 4×3

```text
grid = [
    [16, 3, 2],
    [5, 10, 11],
    [9, 6, 7],
    [4, 15, 14],
]
```

#### TC-BND-01-06 — 5×5

```text
grid = [[1,2,3,4,5] for _ in range(5)]
```

### 3.2 기대 출력 (공통)

| 필드 | 값 |
|------|-----|
| 예외 타입 | `InvalidInputError` |
| `code` | `ERR-VAL-001` |
| `message` | `Invalid grid dimensions: expected 4x4.` |
| 반환값 | 없음 (예외 전파) |
| Domain 호출 | **0** |

### 3.3 포함 금지 케이스 (명시적 제외)

| 입력 | 제외 사유 |
|------|-----------|
| `TD_SUCCESS_SF_001` 등 4×4·빈칸 2개·값 유효 | Rule 1 통과 → AC-FR01-01 **비해당**; AC-FR01-05·Track B로 분리 |
| `G_VALID_A` 완전 마방진 | 동일 |
| 빈칸 1개/3개, 값 17, 중복 | 각각 `ERR-VAL-002`~`004` 전용 계획서 |

---

## 4. 예외·특이 케이스 목록

| TC ID | 카테고리 | 입력/조건 | 기대 | 비고 |
|-------|----------|-----------|------|------|
| **TC-EX-01** | 타입 이상 | `grid = ""` (빈 문자열) | `ERR-VAL-001` | Rule 1 실패로 통합 처리 권장 |
| **TC-EX-02** | 타입 이상 | `grid = 123` (스칼라) | `ERR-VAL-001` | iterable 아님 |
| **TC-EX-03** | 혼합 행 길이 | `[[1,2,3,4], [1,2,3], [1,2,3,4], [1,2,3,4]]` | `ERR-VAL-001` | 열 길이 불일치 |
| **TC-EX-04** | `None` 행 | `[[1,2,3,4], None, [1,2,3,4], [1,2,3,4]]` | `ERR-VAL-001` | 행이 list 아님 |
| **TC-EX-05** | 빈 행 1개 | `[[1,2,3,4], [], [1,2,3,4], [1,2,3,4]]` | `ERR-VAL-001` | TC-BND-01-03 변형 |
| **TC-EX-06** | 이중 실패 | `None` + Solver mock | `ERR-VAL-001`, mock **0** | P2 격리 시나리오 |
| **TC-EX-07** | 메시지 회귀 | 임의 3×4 | `message` 문자열 **완전 일치** | §13 고정 문자열 |
| **TC-EX-08** | 코드 회귀 | `[]` | `.code` only `ERR-VAL-001` (not 002~004) | 오분류 방지 |
| **TC-EX-09** | 예외 체인 | `raise ... from e` 사용 시 | `InvalidInputError` 최외곽 유지 | 구현 선택; 관찰 가능 예외만 assert |
| **TC-EX-10** | pydantic 경로 | `GridInput.model_validate(None)` | Boundary 정책과 동일 최종 예외 | P3; 매핑 정책 테스트 |

---

## 5. Domain 계층 진입점 호출 횟수 검증 전략 (mock / spy)

### 5.1 Domain 진입점 정의 (PRD §17~18)

| 진입점 | Layer | FR-01 실패 시 기대 호출 |
|--------|-------|-------------------------|
| `Solver.solve` (또는 resolver facade) | Entity/Control | **0** |
| `BlankFinder.find` | Entity | **0** |
| `MissingNumberFinder.find` | Entity | **0** |
| `MagicSquareValidator.validate` | Entity | **0** |

**FR-01 Rule 5:** 검증 실패 시 Domain resolver 미호출 (§13, AC-FR01-01).

### 5.2 Mock 대상 및 주입 위치

| 레벨 | Mock 대상 | 패치 경로(예시) | 용도 |
|------|-----------|-----------------|------|
| **L1 — 단위** | Domain 미사용 | mock 없음 | `BoundaryValidator`만 테스트 (P0) |
| **L2 — Control** | `Solver` | `magicsquare.control.<module>.Solver` | `solve(None)` 시 Solver **0 calls** |
| **L2 — Control** | resolver facade | `DomainResolver.resolve` (도입 시) | 단일 스파이 지점 |
| **L3 — Entity** | `BlankFinder`, `MissingNumberFinder`, `MagicSquareValidator` | 각 entity 모듈 | 세부 누수 탐지 (선택) |

**권장:** RED-BND-006은 **L2 Control `solve()`** 에서 **Solver(또는 facade) 1곳**만 mock/spy하고, P0 단위 테스트와 분리한다.

### 5.3 unittest.mock 패턴 (설계 수준)

```text
# 의사코드 — 구현 시 tests/boundary/test_solve_domain_isolation_fr01_01.py

with patch("magicsquare.control.<solve_module>.Solver") as solver_cls:
    solver_cls.return_value.solve = MagicMock()
    with pytest.raises(InvalidInputError) as exc:
        solve(grid=None)
    assert exc.value.code == "ERR-VAL-001"
    solver_cls.return_value.solve.assert_not_called()
    # 또는 solver_cls.assert_not_called()
```

| 기법 | 사용 시점 |
|------|-----------|
| `@patch` / `patch.object` | Control 통합, 클래스 메서드 |
| `MagicMock` + `assert_not_called()` | 호출 0회 단언 |
| `wraps=` (spy) | GREEN 후 리팩터 회귀 — 실제 함수 감싸 호출 카운트 |
| `autospec=True` | 시그니처 드리프트 방지 |

### 5.4 검증 매트릭스 (격리)

| TC ID | `BoundaryValidator` | `Solver` | `BlankFinder` | 비고 |
|-------|---------------------|----------|---------------|------|
| TC-BND-01-01 ~ 06 | 호출 1, 실패 | 0 | 0 | P0 + P2 |
| TC-EX-06 | 호출 1, 실패 | 0 | 0 | `None` 대표 |

### 5.5 실패 시 진단

| 관찰 | 결함 추정 |
|------|-----------|
| Solver 1 call | Boundary 우회 또는 Control에서 검증 누락 |
| BlankFinder 1 call | Rule 1 통과 후 조기 Domain 호출 |
| `ERR-VAL-002` on `None` | null 분기 오분류 |

---

## 6. 커버리지 목표

| NFR | Layer 경로 | 목표 | 본 계획서 기여 |
|-----|------------|------|----------------|
| **NFR-02** | `src/magicsquare/boundary/` | **≥ 85%** | `BoundaryValidator` Rule 1 분기 전면 커버 |
| **NFR-01** | `src/magicsquare/entity/`, `control/` | **≥ 95%** | 본 AC는 Domain **미호출** — 직접 기여 낮음; mock 테스트로 Control 분기 커버 |
| **NFR-11** | `src/magicsquare/` 전체 | **≥ 80%** floor | CI gate |

**본 Epic 완료 시 최소 기대**

- `boundary/boundary_validator.py` (구현 예정): Line/Branch **100%** (Rule 1 + null/empty/크기 분기)
- `boundary/exceptions.py`: `InvalidInputError` 생성 경로 **100%**

---

## 7. pytest-cov 측정 전략

### 7.1 설치

```bash
pip install pytest-cov
# 또는
pip install -e ".[dev]"
```

### 7.2 로컬 측정 (전체)

```bash
pytest --cov=src --cov-report=term-missing
```

### 7.3 Layer별 측정 (NFR-01 / NFR-02 정합)

```bash
# Boundary ≥ 85%
pytest tests/boundary/ \
  --cov=magicsquare.boundary \
  --cov-report=term-missing \
  --cov-fail-under=85

# Domain ≥ 95% (Track B Epic; 본 FR-01 Epic과 병행)
pytest tests/domain/ \
  --cov=magicsquare.entity \
  --cov=magicsquare.control \
  --cov-report=term-missing \
  --cov-fail-under=95
```

### 7.4 본 AC 전용 (좁은 범위)

```bash
pytest tests/boundary/test_boundary_validator_fr01_01.py \
  tests/boundary/test_solve_domain_isolation_fr01_01.py \
  --cov=magicsquare.boundary \
  --cov-report=term-missing \
  -v
```

### 7.5 CI 권장 게이트

| Gate | 명령 | 실패 조건 |
|------|------|-----------|
| Global | `pytest --cov=magicsquare --cov-fail-under=80` | 전체 < 80% |
| Boundary | `--cov=magicsquare.boundary --cov-fail-under=85` | Boundary < 85% |
| Domain | `--cov=magicsquare.entity --cov=magicsquare.control --cov-fail-under=95` | Domain < 95% |

### 7.6 커버리지 해석 주의

| 항목 | 설명 |
|------|------|
| Mock 사용 구간 | Control 테스트는 mock된 Solver로 **실제 Entity 코드 미실행** — Domain 95%는 Track B 테스트로 충족 |
| 미구현 모듈 | `BoundaryValidator` RED 단계에서는 0%; GREEN 후 본 계획 TC로 급상승 예상 |
| `term-missing` | Rule 1의 `None` / `[]` / ragged row 분기 누락 라인 즉시 확인 |

---

## 8. 추적성 매트릭스

| Concept | BR | FR | AC | Error | TP | RED | TC (본 문서) |
|---------|-----|-----|-----|-------|-----|-----|----------------|
| 4×4 / null·empty | BR-01 | FR-01 | AC-FR01-01 | ERR-VAL-001 | TP-E-01 | RED-BND-001 | TC-BND-01-01~06 |
| Domain 미호출 | — | FR-01 R5 | AC-FR01-01 | — | TP-E-01 | RED-BND-006 | TC-EX-06 |

---

## 9. TDD 게이트 및 산출물

| Phase | 산출물 | 완료 기준 |
|-------|--------|-----------|
| **RED** | `tests/boundary/test_*_fr01_01.py` | TC-BND-01-01~06 **실패**(구현 없음), 실패 로그 보관 |
| **GREEN** | `boundary_validator.py` 최소 구현 | 전 TC 통과, mock 0 calls |
| **REFACTOR** | Rule 1 추출, 상수 `GRID_SIZE` | suite GREEN, coverage 유지 |

**금지:** assert 약화, 4×4 정상 케이스를 본 파일에 넣어 GREEN 우회, Domain 선구현 후 Boundary 추가.

---

## 10. 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR01-01 샘플 기반 테스트 계획서 초안 |

---

*본 문서는 테스트 코드를 포함하지 않는다. 구현 시 [PRD_MagicSquare.md](./PRD_MagicSquare.md) §13 오류 표를 단일 진실 공급원으로 따른다.*
