"""Shared constants for AC-FR-01-01 (FR-01 Rule 1) RED tests."""

AC_ID: str = "AC-FR-01-01"

# Test charter (QA brief) — expected at GREEN for code/message assertions.
CHARTER_CODE_INVALID_SIZE: str = "INVALID_SIZE"
CHARTER_MESSAGE: str = "Grid must be 4x4."

# PRD §13 canonical ERR-VAL-001 (Input Contract §12.1; User Journey §8 Stage 2).
PRD_ERR_VAL_001_CODE: str = "ERR-VAL-001"
PRD_ERR_VAL_001_MESSAGE: str = "Invalid grid dimensions: expected 4x4."

AC_DOCSTRING_LINE: str = (
    "AC-FR-01-01, PRD §8.1 INVALID_SIZE (charter); PRD §13 ERR-VAL-001 (canonical)."
)

# AC-FR-01-02~05 / FR-02~05 — must not appear in this module's active cases.
EXCLUDED_AC_IDS: frozenset[str] = frozenset(
    {
        "AC-FR-01-02",
        "AC-FR-01-03",
        "AC-FR-01-04",
        "AC-FR-01-05",
        "AC-FR-02",
        "AC-FR-03",
        "AC-FR-04",
        "AC-FR-05",
    }
)
