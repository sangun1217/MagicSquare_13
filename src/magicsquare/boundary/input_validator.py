"""Boundary input validation with Failure envelope (FR-01)."""

from __future__ import annotations

from magicsquare.boundary.failure import (
    E001,
    E002,
    E003,
    E004,
    E005,
    MSG_E001,
    MSG_E002,
    MSG_E003,
    MSG_E004,
    MSG_E005,
    ErrorDetail,
    ValidationFailure,
)
from magicsquare.entity.constants import BLANK_COUNT, GRID_SIZE, VALUE_MAX, VALUE_MIN

Grid = list[list[int]]
ValidateResult = Grid | ValidationFailure


class InputValidator:
    """Validates raw matrix before Domain access; returns Failure envelope on reject."""

    def validate(self, matrix: Grid | None) -> ValidateResult:
        """Validate structure, blanks, range, and duplicates."""
        if matrix is None:
            return ValidationFailure(error=ErrorDetail(code=E003, message=MSG_E003))

        if not matrix:
            return ValidationFailure(error=ErrorDetail(code=E001, message=MSG_E001))

        if len(matrix) != GRID_SIZE:
            return ValidationFailure(error=ErrorDetail(code=E001, message=MSG_E001))

        for row in matrix:
            if not isinstance(row, list) or len(row) != GRID_SIZE:
                return ValidationFailure(error=ErrorDetail(code=E001, message=MSG_E001))

        blank_count = sum(cell == 0 for row in matrix for cell in row)
        if blank_count != BLANK_COUNT:
            return ValidationFailure(error=ErrorDetail(code=E002, message=MSG_E002))

        non_zero_values: list[int] = []
        for row in matrix:
            for cell in row:
                if cell == 0:
                    continue
                if cell < VALUE_MIN or cell > VALUE_MAX:
                    return ValidationFailure(error=ErrorDetail(code=E004, message=MSG_E004))
                non_zero_values.append(cell)

        if len(non_zero_values) != len(set(non_zero_values)):
            return ValidationFailure(error=ErrorDetail(code=E005, message=MSG_E005))

        return matrix
