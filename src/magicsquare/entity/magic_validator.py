"""Magic square validation for fully filled grids (FR-04)."""

from __future__ import annotations

from magicsquare.entity.constants import (
    GRID_SIZE,
    MAGIC_CONSTANT_N4,
    VALUE_MAX,
    VALUE_MIN,
)

Grid = list[list[int]]


def is_magic_square(matrix: Grid) -> bool:
    """Return True when 1..16 set and all ten lines sum to MAGIC_CONSTANT_N4."""
    values: list[int] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            values.append(matrix[row_index][col_index])

    cell_count = GRID_SIZE * GRID_SIZE
    if len(values) != cell_count:
        return False

    if any(value < VALUE_MIN or value > VALUE_MAX for value in values):
        return False

    if len(set(values)) != cell_count:
        return False

    for row_index in range(GRID_SIZE):
        row_sum = sum(matrix[row_index][col_index] for col_index in range(GRID_SIZE))
        if row_sum != MAGIC_CONSTANT_N4:
            return False

    for col_index in range(GRID_SIZE):
        col_sum = sum(matrix[row_index][col_index] for row_index in range(GRID_SIZE))
        if col_sum != MAGIC_CONSTANT_N4:
            return False

    main_diagonal_sum = sum(
        matrix[line_index][line_index] for line_index in range(GRID_SIZE)
    )
    if main_diagonal_sum != MAGIC_CONSTANT_N4:
        return False

    anti_diagonal_sum = sum(
        matrix[line_index][GRID_SIZE - 1 - line_index]
        for line_index in range(GRID_SIZE)
    )
    if anti_diagonal_sum != MAGIC_CONSTANT_N4:
        return False

    return True
