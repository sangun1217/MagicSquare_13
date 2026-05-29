"""Boundary input validation for raw grids (FR-01)."""

from __future__ import annotations

Grid = list[list[int]]


class BoundaryValidator:
    """Validates raw matrix shape and reference before Domain access (FR-01)."""

    def validate(self, grid: Grid | None) -> Grid:
        """Validate grid dimensions and structure.

        Args:
            grid: Raw input matrix; may be None.

        Returns:
            Normalized 4x4 grid when validation passes.

        Raises:
            InvalidInputError: When validation fails (not yet implemented — RED).
            NotImplementedError: RED phase placeholder.
        """
        raise NotImplementedError("RED: BoundaryValidator.validate not implemented")
