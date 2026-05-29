"""Track B RED skeleton — D-SOL-01~04 (solution). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.exceptions import UnsolvableDomainError  # noqa: F401
from magicsquare.entity.solver import solution  # noqa: F401

pytestmark = pytest.mark.domain


class TestDSOL01SmallFirst:
    """D-SOL-01: G1 Step A small-first success."""

    def test_d_sol_01_step_a_small_first_g1(self) -> None:
        # Given: G1 — expected [2,2,7,3,3,10]
        # When: solution(matrix)
        pytest.fail("RED: D-SOL-01 — G1 Step A returns [2,2,7,3,3,10]")


class TestDSOL02Reverse:
    """D-SOL-02: G2 Step B reverse success (G2 TBD)."""

    def test_d_sol_02_step_b_reverse_g2(self) -> None:
        # Given: G2 — numeric fixture TBD
        # When: solution(matrix)
        pytest.fail("RED: D-SOL-02 — G2 TBD")


class TestDSOL03Unsolvable:
    """D-SOL-03: G3 both attempts fail."""

    def test_d_sol_03_both_attempts_fail_g3(self) -> None:
        # Given: G3 / TD_UNSOLVABLE
        # When: solution(matrix)
        pytest.fail("RED: D-SOL-03 — G3 raises UnsolvableDomainError")


class TestDSOL04ResultShape:
    """D-SOL-04: result length 6 and 1-index coordinates."""

    def test_d_sol_04_length_six_one_index_coords(self) -> None:
        # Given: G1_SF or successful fixture
        # When: solution(matrix)
        pytest.fail("RED: D-SOL-04 — result length 6 with 1-index coordinates")
