"""Track B RED skeleton — D-VAL-01~06 (is_magic_square). Domain Mock 금지."""

from __future__ import annotations

import pytest

from magicsquare.entity.magic_validator import is_magic_square  # noqa: F401

pytestmark = pytest.mark.domain


class TestDVAL01ValidComplete:
    """D-VAL-01: G0 complete → True."""

    def test_d_val_01_complete_g0_true(self) -> None:
        # Given: G0 / G_VALID_A
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-01 — G0 complete grid returns True")


class TestDVAL02RowSum:
    """D-VAL-02: one row sum ≠ 34 → False."""

    def test_d_val_02_wrong_row_sum_false(self) -> None:
        # Given: G_INVALID_ROW
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-02 — row sum mismatch returns False")


class TestDVAL03ColumnSum:
    """D-VAL-03: one column sum ≠ 34 → False."""

    def test_d_val_03_wrong_column_sum_false(self) -> None:
        # Given: G_INVALID_COL
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-03 — column sum mismatch returns False")


class TestDVAL04DiagonalSum:
    """D-VAL-04: diagonal sum ≠ 34 → False."""

    def test_d_val_04_wrong_diagonal_sum_false(self) -> None:
        # Given: G_INVALID_DIAG
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-04 — diagonal sum mismatch returns False")


class TestDVAL05SetAndDuplicate:
    """D-VAL-05: 1~16 set violation → False."""

    def test_d_val_05_out_of_range_full_grid_false(self) -> None:
        # Given: G_INVALID_RANGE_FULL
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-05 — out-of-range full grid returns False")

    def test_d_val_05_duplicate_values_false(self) -> None:
        # Given: G_INVALID_DUP
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-05 — duplicate values returns False")


class TestDVAL06ZeroInFullGrid:
    """D-VAL-06: zero in otherwise complete grid → False."""

    def test_d_val_06_zero_cell_false(self) -> None:
        # Given: G_INVALID_ZERO_IN_FULL
        # When: is_magic_square(matrix)
        pytest.fail("RED: D-VAL-06 — zero in full grid returns False")
