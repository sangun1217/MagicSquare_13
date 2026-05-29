"""Two-cell solver: small-first then reverse (FR-05)."""

from __future__ import annotations

from magicsquare.entity.exceptions import UnsolvableDomainError

Grid = list[list[int]]
ResultVector = list[int]


def solution(matrix: Grid) -> ResultVector:
    """Complete partial grid and return [r1, c1, n1, r2, c2, n2].

    Raises:
        NotImplementedError: RED phase placeholder.
        UnsolvableDomainError: When both attempts fail.
    """
    raise NotImplementedError("RED: solution not implemented")
