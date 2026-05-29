"""Two-cell solver: small-first then reverse (FR-05)."""

from __future__ import annotations

import copy

from magicsquare.entity.blank_locator import find_blank_coords
from magicsquare.entity.exceptions import UnsolvableDomainError
from magicsquare.entity.magic_validator import is_magic_square
from magicsquare.entity.missing_finder import find_not_exist_nums

Grid = list[list[int]]
ResultVector = list[int]


def _is_valid_completion(
    matrix: Grid,
    row1: int,
    col1: int,
    row2: int,
    col2: int,
    first_value: int,
    second_value: int,
) -> bool:
    """Return True when placing two values on a copy yields a magic square."""
    trial = copy.deepcopy(matrix)
    trial[row1 - 1][col1 - 1] = first_value
    trial[row2 - 1][col2 - 1] = second_value
    return is_magic_square(trial)


def solution(matrix: Grid) -> ResultVector:
    """Complete partial grid and return [r1, c1, n1, r2, c2, n2].

    Raises:
        UnsolvableDomainError: When both placement attempts fail.
    """
    row1, col1, row2, col2 = find_blank_coords(matrix)
    smaller_missing, larger_missing = find_not_exist_nums(matrix)

    if _is_valid_completion(
        matrix, row1, col1, row2, col2, smaller_missing, larger_missing
    ):
        return [row1, col1, smaller_missing, row2, col2, larger_missing]

    if _is_valid_completion(
        matrix, row1, col1, row2, col2, larger_missing, smaller_missing
    ):
        return [row1, col1, larger_missing, row2, col2, smaller_missing]

    raise UnsolvableDomainError()
