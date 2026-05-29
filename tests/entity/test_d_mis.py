"""Track B RED skeleton — D-MIS-01 (missing numbers sorted). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.missing_finder import find_not_exist_nums  # noqa: F401

pytestmark = pytest.mark.domain


class TestDMIS01MissingNumbers:
    """D-MIS-01: G1 → missing {7,10} ascending."""

    def test_d_mis_01_missing_pair_sorted_g1(self) -> None:
        # Given: G1
        # When: find_not_exist_nums(matrix)
        pytest.fail("RED: D-MIS-01 — G1 missing numbers (7, 10) ascending")
