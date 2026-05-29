"""Row-major blank coordinate discovery (FR-02)."""

from __future__ import annotations

from magicsquare.entity.constants import GRID_SIZE

Grid = list[list[int]]


def find_blank_coords(matrix: Grid) -> tuple[int, int, int, int]:
    """Return 1-index (r1, c1, r2, c2) for the two zeros in row-major order."""
    blanks: list[tuple[int, int]] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            if matrix[row_index][col_index] == 0:
                blanks.append((row_index + 1, col_index + 1))
    return (blanks[0][0], blanks[0][1], blanks[1][0], blanks[1][1])
