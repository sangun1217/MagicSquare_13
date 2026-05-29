"""Track B RED skeleton — D-LOC-01 (row-major blank coordinates). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.blank_locator import find_blank_coords  # noqa: F401

pytestmark = pytest.mark.domain


class TestDLOC01BlankCoordinates:
    """D-LOC-01: G1 → (2,2), (3,3) 1-index row-major."""

    def test_d_loc_01_row_major_blanks_g1(self) -> None:
        # Given: G1 partial grid (tests/fixtures/golden_grids.G1)
        # When: find_blank_coords(matrix)
        pytest.fail("RED: D-LOC-01 — G1 row-major blanks (2,2) and (3,3) 1-index")
