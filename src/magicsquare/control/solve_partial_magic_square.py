"""Control use case: two-cell magic square completion (FR-05)."""

from __future__ import annotations

from magicsquare.entity.solver import solution

Grid = list[list[int]]
ResultVector = list[int]


class SolvePartialMagicSquare:
    """Orchestrates blank fill attempts after Boundary validation passes."""

    def execute(self, matrix: Grid) -> ResultVector:
        """Run small-first then reverse placement attempts."""
        return solution(matrix)
