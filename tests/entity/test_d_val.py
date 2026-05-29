"""Track B RED skeleton — D-VAL-01~06 (is_magic_square). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.magic_validator import is_magic_square
from tests.fixtures.golden_grids import (
    G0,
    G_INVALID_COL,
    G_INVALID_DIAG,
    G_INVALID_DUP,
    G_INVALID_RANGE_FULL,
    G_INVALID_ROW,
    G_INVALID_ZERO_IN_FULL,
)

pytestmark = pytest.mark.domain


class TestDVAL01ValidComplete:
    """D-VAL-01: G0 complete → True."""

    def test_d_val_01_complete_g0_true(self) -> None:
        assert is_magic_square(G0) is True


class TestDVAL02RowSum:
    """D-VAL-02: one row sum ≠ 34 → False."""

    def test_d_val_02_wrong_row_sum_false(self) -> None:
        assert is_magic_square(G_INVALID_ROW) is False


class TestDVAL03ColumnSum:
    """D-VAL-03: one column sum ≠ 34 → False."""

    def test_d_val_03_wrong_column_sum_false(self) -> None:
        assert is_magic_square(G_INVALID_COL) is False


class TestDVAL04DiagonalSum:
    """D-VAL-04: diagonal sum ≠ 34 → False."""

    def test_d_val_04_wrong_diagonal_sum_false(self) -> None:
        assert is_magic_square(G_INVALID_DIAG) is False


class TestDVAL05SetAndDuplicate:
    """D-VAL-05: 1~16 set violation → False."""

    def test_d_val_05_out_of_range_full_grid_false(self) -> None:
        assert is_magic_square(G_INVALID_RANGE_FULL) is False

    def test_d_val_05_duplicate_values_false(self) -> None:
        assert is_magic_square(G_INVALID_DUP) is False


class TestDVAL06ZeroInFullGrid:
    """D-VAL-06: zero in otherwise complete grid → False."""

    def test_d_val_06_zero_cell_false(self) -> None:
        assert is_magic_square(G_INVALID_ZERO_IN_FULL) is False
