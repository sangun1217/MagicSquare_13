"""Track B RED skeleton — D-SOL-01~04 (solution). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.exceptions import UnsolvableDomainError
from magicsquare.entity.solver import solution
from tests.fixtures.golden_grids import (
    G1,
    G1_SF,
    G1_SF_EXPECTED,
    G2,
    G3,
    TD_SUCCESS_REV_001_EXPECTED,
)

pytestmark = pytest.mark.domain


class TestDSOL01SmallFirst:
    """D-SOL-01: G1_SF Step A small-first success."""

    def test_d_sol_01_step_a_small_first_g1(self) -> None:
        assert solution(G1_SF) == G1_SF_EXPECTED


class TestDSOL02Reverse:
    """D-SOL-02: G2 Step B reverse success."""

    def test_d_sol_02_step_b_reverse_g2(self) -> None:
        assert solution(G2) == TD_SUCCESS_REV_001_EXPECTED


class TestDSOL03Unsolvable:
    """D-SOL-03: G3 both attempts fail."""

    def test_d_sol_03_both_attempts_fail_g3(self) -> None:
        with pytest.raises(UnsolvableDomainError):
            solution(G3)


class TestDSOL04ResultShape:
    """D-SOL-04: result length 6 and 1-index coordinates."""

    def test_d_sol_04_length_six_one_index_coords(self) -> None:
        result = solution(G1_SF)
        assert len(result) == 6
        r1, c1, _n1, r2, c2, _n2 = result
        assert result == G1_SF_EXPECTED
        for coord in (r1, c1, r2, c2):
            assert 1 <= coord <= 4
