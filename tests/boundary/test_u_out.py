"""Track A RED skeleton — U-OUT-01~03 (output contract on valid input)."""

from __future__ import annotations

import pytest

from magicsquare.boundary.ui_boundary import UIBoundary  # noqa: F401
from magicsquare.control.solve_partial_magic_square import (  # noqa: F401
    SolvePartialMagicSquare,
)

pytestmark = pytest.mark.boundary


class TestUOUT01ResultLength:
    """U-OUT-01: success vector length = 6."""

    def test_u_out_01_success_result_length_six(self) -> None:
        # Given: G1 valid partial grid (Boundary-valid)
        # When: UIBoundary().solve(matrix)
        pytest.fail("RED: U-OUT-01 — success result has length 6")


class TestUOUT02OneIndexCoordinates:
    """U-OUT-02: r1,c1,r2,c2 ∈ [1,4] 1-index."""

    def test_u_out_02_coordinates_one_index_in_range(self) -> None:
        # Given: G1
        # When: UIBoundary().solve(matrix)
        pytest.fail("RED: U-OUT-02 — coordinates are 1-index in [1,4]")


class TestUOUT03MissingValuesInResult:
    """U-OUT-03: n1,n2 are the two missing numbers from {1..16}."""

    def test_u_out_03_placed_values_match_missing_set(self) -> None:
        # Given: G1 — missing {7,10}
        # When: UIBoundary().solve(matrix)
        pytest.fail("RED: U-OUT-03 — n1,n2 match missing numbers on success")
