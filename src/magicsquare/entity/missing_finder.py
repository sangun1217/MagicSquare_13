"""Missing number discovery from partial grid (FR-03)."""

from __future__ import annotations

from magicsquare.entity.constants import GRID_SIZE, VALUE_MAX, VALUE_MIN

Grid = list[list[int]]


def find_not_exist_nums(matrix: Grid) -> tuple[int, int]:
    """Return missing values (n1, n2) with n1 < n2."""
    present: set[int] = set()
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            value = matrix[row_index][col_index]
            if value != 0:
                present.add(value)
    missing = [
        number
        for number in range(VALUE_MIN, VALUE_MAX + 1)
        if number not in present
    ]
    return (missing[0], missing[1])
