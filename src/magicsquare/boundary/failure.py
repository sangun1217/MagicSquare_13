"""Failure envelope for Boundary validation (not raised as generic Exception)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

# Stable E00x codes (Dual-Track RED design SSOT).
E001: Final[str] = "E001"
E002: Final[str] = "E002"
E003: Final[str] = "E003"
E004: Final[str] = "E004"
E005: Final[str] = "E005"

MSG_E001: Final[str] = "Invalid grid dimensions: expected 4x4."
MSG_E002: Final[str] = "Invalid blank count: expected exactly 2 zeros."
MSG_E003: Final[str] = "Grid reference is null."
MSG_E004: Final[str] = "Invalid cell value: must be 0 or 1..16."
MSG_E005: Final[str] = "Duplicate non-zero value detected."


@dataclass(frozen=True, slots=True)
class ErrorDetail:
    """Structured error payload inside a Failure envelope."""

    code: str
    message: str


@dataclass(frozen=True, slots=True)
class ValidationFailure:
    """Boundary validation failure returned to callers (FR-01)."""

    error: ErrorDetail
