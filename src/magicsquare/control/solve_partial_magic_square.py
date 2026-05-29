"""Control use case: two-cell magic square completion (FR-05)."""

from __future__ import annotations

from magicsquare.boundary.failure import ValidationFailure

Grid = list[list[int]]
ResultVector = list[int]
SolveResult = ResultVector | ValidationFailure


class SolvePartialMagicSquare:
    """Orchestrates blank fill attempts after Boundary validation passes."""

    def execute(self, matrix: Grid) -> SolveResult:
        """Run small-first then reverse placement attempts.

        Args:
            matrix: Boundary-validated 4x4 grid with exactly two zeros.

        Returns:
            Six-element 1-index result vector on success.

        Raises:
            NotImplementedError: RED phase placeholder.
            UnsolvableDomainError: When both attempts fail (GREEN).
        """
        raise NotImplementedError("RED: SolvePartialMagicSquare.execute not implemented")
