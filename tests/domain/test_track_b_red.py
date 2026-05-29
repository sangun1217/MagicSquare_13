"""Track B RED — D-LOC / D-MIS / D-VAL / D-SOL (Domain Mock 금지)."""

from __future__ import annotations

import copy

import pytest

from magicsquare.entity.blank_locator import find_blank_coords
from magicsquare.entity.exceptions import UnsolvableDomainError
from magicsquare.entity.magic_validator import is_magic_square
from magicsquare.entity.missing_finder import find_not_exist_nums
from magicsquare.entity.solver import solution
from tests.fixtures.golden_grids import (
    D_SOL_01_EXPECTED,
    G0,
    G1,
    G2,
    G3,
    G_INVALID_COL,
    G_INVALID_DIAG,
    G_INVALID_DUP,
    G_INVALID_RANGE_FULL,
    G_INVALID_ROW,
    G_INVALID_ZERO_IN_FULL,
    G1_SF,
    G1_SF_EXPECTED,
    TD_SUCCESS_REV_001_EXPECTED,
)

pytestmark = pytest.mark.domain


class TestDLOC01FindBlankCoords:
    """D-LOC-01: G1 row-major blanks (2,2), (3,3) 1-index."""

    def test_find_blank_coords_row_major_g1(self) -> None:
        assert find_blank_coords(G1) == (2, 2, 3, 3)


class TestDMIS01FindMissingNumbers:
    """D-MIS-01: G1 → (7, 10) ascending."""

    def test_find_missing_numbers_sorted_g1(self) -> None:
        assert find_not_exist_nums(G1) == (7, 10)


class TestDVAL01MagicSquareTrue:
    """D-VAL-01: G0 complete grid → True."""

    def test_is_magic_square_true_on_complete_g0(self) -> None:
        assert is_magic_square(G0) is True


class TestDVAL02MagicSquareFalseRow:
    """D-VAL-02: row sum violation → False."""

    def test_is_magic_square_false_when_row_sum_wrong(self) -> None:
        assert is_magic_square(G_INVALID_ROW) is False


class TestDVAL03MagicSquareFalseColumn:
    """D-VAL-03: column sum violation → False."""

    def test_is_magic_square_false_when_column_sum_wrong(self) -> None:
        assert is_magic_square(G_INVALID_COL) is False


class TestDVAL04MagicSquareFalseDiagonal:
    """D-VAL-04: diagonal sum violation → False."""

    def test_is_magic_square_false_when_diagonal_sum_wrong(self) -> None:
        assert is_magic_square(G_INVALID_DIAG) is False


class TestDVAL05MagicSquareFalseSet:
    """D-VAL-05: 1~16 set / duplicate violation → False."""

    @pytest.mark.parametrize(
        "matrix",
        [G_INVALID_RANGE_FULL, G_INVALID_DUP],
        ids=["out_of_range", "duplicate"],
    )
    def test_is_magic_square_false_when_set_or_duplicate_violated(
        self,
        matrix: list[list[int]],
    ) -> None:
        assert is_magic_square(matrix) is False


class TestDVAL06MagicSquareFalseZero:
    """D-VAL-06: zero in full grid → False."""

    def test_is_magic_square_false_when_zero_in_full_grid(self) -> None:
        assert is_magic_square(G_INVALID_ZERO_IN_FULL) is False


class TestDSOL01SmallFirstSuccess:
    """D-SOL-01: G1 Step A small-first → [2,2,7,3,3,10]."""

    def test_solution_step_a_small_first_success_g1(self) -> None:
        assert solution(G1) == D_SOL_01_EXPECTED


class TestDSOL02ReverseSuccess:
    """D-SOL-02: G2 Step B reverse → [2,2,10,3,3,7]."""

    def test_solution_step_b_reverse_success_g2(self) -> None:
        assert solution(G2) == TD_SUCCESS_REV_001_EXPECTED


class TestDSOL03Unsolvable:
    """D-SOL-03: G3 both attempts fail → UnsolvableDomainError."""

    def test_solution_raises_when_both_attempts_fail_g3(self) -> None:
        with pytest.raises(UnsolvableDomainError):
            solution(G3)


class TestDSOL04ResultShape:
    """D-SOL-04: length 6 and 1-index coordinates."""

    def test_solution_result_length_six_and_one_index_coords(self) -> None:
        result = solution(G1_SF)
        assert len(result) == 6
        r1, c1, _n1, r2, c2, _n2 = result
        assert result == G1_SF_EXPECTED
        for coord in (r1, c1, r2, c2):
            assert 1 <= coord <= 4


class TestDomainInputImmutability:
    """BR-15: domain calls must not mutate input (RED guard for GREEN)."""

    def test_find_blank_coords_does_not_mutate_g1(self) -> None:
        original = copy.deepcopy(G1)
        try:
            find_blank_coords(G1)
        except NotImplementedError:
            pass
        assert G1 == original
