## Summary

This PR merges `feature/dual-track-tdd` into `develop` with the full Dual-Track TDD implementation kickoff for Magic Square 4x4 Practice.

- Adds a **Dual-Track TDD task board** to `README.md` (Sprint 0–3, quality gates, branch naming).
- Completes **Sprint 0**: `pyproject.toml`, ECB package layout (`boundary` / `control` / `entity`), golden fixtures, smoke tests (12 passing).
- Adds **QA artifacts**: `docs/test_plan.md` (AC-FR01-01), `docs/defect_list.md` (DEF-001–006).
- Adds **Track A RED tests** for AC-FR-01-01 (`tests/boundary/test_ac_fr01_01_invalid_size.py`) — 20 intentional failures until `BoundaryValidator` GREEN.
- Adds session backup **Report/Prompting 09**.

## Commits (4)

| Commit | Description |
|--------|-------------|
| `f73f833` | README Dual-Track checklist |
| `ca1dd92` | Sprint 0 project skeleton |
| `330d0ce` | AC-FR-01-01 RED tests, test plan, defect list, session report |
| `3f6d758` | PR description draft file |

**Diff:** 27 files, +1692 / −9 lines vs `develop`

## Test plan

```bash
pip install -e ".[dev]"
pytest -q
```

| Result | Meaning |
|--------|---------|
| **24 passed** | Sprint 0 smoke + AC-FR-01-01 scope guards |
| **20 failed** | **Expected RED** — `BoundaryValidator.validate()` not implemented (DEF-001) |

- [x] RED evidence captured in `docs/defect_list.md`
- [ ] GREEN (`BoundaryValidator` FR-01 Rule 1) — follow-up PR

## Key files

| Area | Path |
|------|------|
| PRD alignment | `docs/test_plan.md`, `docs/defect_list.md` |
| Boundary (RED stub) | `src/magicsquare/boundary/boundary_validator.py` |
| Control entry | `src/magicsquare/control/solve_entry.py` |
| RED tests | `tests/boundary/test_ac_fr01_01_invalid_size.py` |
| Fixtures | `tests/fixtures/golden_grids.py` (DN-04/05 resolved) |

## Known issues (pre-GREEN)

| ID | Summary |
|----|---------|
| DEF-001 | `BoundaryValidator` raises `NotImplementedError` instead of `InvalidInputError` |
| DEF-003 | Charter (`INVALID_SIZE`) vs PRD (`ERR-VAL-001`) — unify before GREEN |
| DEF-005 | `TD_INVALID_SIZE` fixture is 4×3; rename/clarify |

## Out of scope for this PR

- GREEN implementation of FR-01~05
- Track B Domain RED tests
- Coverage CI gates (85%/95%) — enable after GREEN

## Checklist

- [x] Dual-Track tests separated under `tests/boundary/`
- [x] No weakening of assertions for forced GREEN
- [x] Domain not invoked on invalid input (test design + mock; verified after GREEN)
- [x] ECB skeleton respects `boundary → control → entity` direction
