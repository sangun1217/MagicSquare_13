"""Track B RED skeleton — D-LOC-01 (row-major blank coordinates). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.blank_locator import find_blank_coords
from tests.fixtures.golden_grids import G1

pytestmark = pytest.mark.domain


class TestDLOC01BlankCoordinates:
    """D-LOC-01: G1 → (2,2), (3,3) 1-index row-major."""

    def test_d_loc_01_row_major_blanks_g1(self) -> None:
        assert find_blank_coords(G1) == (2, 2, 3, 3)
