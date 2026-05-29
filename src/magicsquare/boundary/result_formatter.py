"""Output contract adapter for int[6] solve results.

Decision DN-05: ResultFormatter lives in Boundary because it performs
format-only assembly of ``[r1, c1, n1, r2, c2, n2]`` without domain rules.
Attempt orchestration remains in Control; Solver remains in Entity.
"""

from typing import Sequence

GridRow = list[int]
ResultVector = list[int]


def format_result(
    r1: int,
    c1: int,
    n1: int,
    r2: int,
    c2: int,
    n2: int,
) -> ResultVector:
    """Assemble a six-element 1-index coordinate result vector.

    Args:
        r1: First blank row (1-index).
        c1: First blank column (1-index).
        n1: Value placed at first blank.
        r2: Second blank row (1-index).
        c2: Second blank column (1-index).
        n2: Value placed at second blank.

    Returns:
        Result vector ``[r1, c1, n1, r2, c2, n2]``.
    """
    return [r1, c1, n1, r2, c2, n2]
