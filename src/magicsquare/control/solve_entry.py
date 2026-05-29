"""Control-layer solve entry: Boundary validation then domain resolution."""

from __future__ import annotations

from magicsquare.boundary.boundary_validator import BoundaryValidator

Grid = list[list[int]]


def resolve(grid: Grid) -> list[int]:
    """Domain resolver entry point (Entity/Control orchestration stub).

    Args:
        grid: Boundary-validated 4x4 grid.

    Returns:
        Six-element result vector.

    Raises:
        NotImplementedError: RED phase — domain not implemented.
    """
    raise NotImplementedError("RED: resolve() not implemented")


def solve(grid: Grid | None) -> list[int]:
    """Run FR-01 validation then domain resolve.

    Args:
        grid: Raw input matrix or None.

    Returns:
        Solve result when validation and domain succeed.

    Raises:
        InvalidInputError: When Boundary validation fails (FR-01).
        NotImplementedError: When domain path is not yet implemented.
    """
    BoundaryValidator().validate(grid)
    return resolve(grid)
