"""Track B RED skeleton — D-MIS-01 (missing numbers sorted). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.missing_finder import find_not_exist_nums
from tests.fixtures.golden_grids import G1

pytestmark = pytest.mark.domain


class TestDMIS01MissingNumbers:
    """D-MIS-01: G1 → missing {7,10} ascending."""

    def test_d_mis_01_missing_pair_sorted_g1(self) -> None:
        assert find_not_exist_nums(G1) == (7, 10)
