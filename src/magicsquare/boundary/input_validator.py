"""Boundary input validation with Failure envelope (FR-01)."""

from __future__ import annotations

from magicsquare.boundary.failure import ValidationFailure

Grid = list[list[int]]
ValidateResult = Grid | ValidationFailure


class InputValidator:
    """Validates raw matrix before Domain access; returns Failure envelope on reject."""

    def validate(self, matrix: Grid | None) -> ValidateResult:
        """Validate structure, blanks, range, and duplicates.

        Args:
            matrix: Raw 4x4 integer grid or None.

        Returns:
            Normalized grid on success, or ValidationFailure on reject.

        Raises:
            NotImplementedError: RED phase — no production validation yet.
        """
        raise NotImplementedError("RED: InputValidator.validate not implemented")
