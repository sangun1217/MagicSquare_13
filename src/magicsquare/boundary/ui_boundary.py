"""UI/BCLI boundary adapter: validate then solve (FR-01 + FR-05)."""

from __future__ import annotations

from magicsquare.boundary.failure import ValidationFailure
from magicsquare.boundary.input_validator import InputValidator
from magicsquare.control.solve_partial_magic_square import SolvePartialMagicSquare

Grid = list[list[int]]
ResultVector = list[int]
BoundarySolveResult = ResultVector | ValidationFailure


class UIBoundary:
    """External entry: input validation then domain solve orchestration."""

    def __init__(
        self,
        validator: InputValidator | None = None,
        solver: SolvePartialMagicSquare | None = None,
    ) -> None:
        """Wire validator and solver collaborators."""
        self._validator = validator or InputValidator()
        self._solver = solver or SolvePartialMagicSquare()

    def solve(self, matrix: Grid | None) -> BoundarySolveResult:
        """Validate input; on success delegate to Control execute.

        Args:
            matrix: Raw grid from external caller.

        Returns:
            ValidationFailure envelope or six-element success vector.

        Raises:
            NotImplementedError: RED phase when validate/execute not implemented.
        """
        validation = self._validator.validate(matrix)
        if isinstance(validation, ValidationFailure):
            return validation
        return self._solver.execute(validation)
