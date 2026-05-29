"""Track A RED skeleton — U-IN-04~08 (input validation, Failure envelope).

U-IN-01~03: Report/08 Full RED — tests/boundary/test_ac_fr01_01_invalid_size.py (do not duplicate).
"""

from __future__ import annotations

import pytest

from magicsquare.boundary.input_validator import InputValidator  # noqa: F401

pytestmark = pytest.mark.boundary


class TestUIN04ZeroBlanks:
    """U-IN-04: blank count 0 → E002."""

    def test_u_in_04_zero_empty_cells_returns_e002(self) -> None:
        # Given: G0 / TD_INVALID_BLANK_ZERO — complete 16 cells, zero blanks
        # When: InputValidator().validate(matrix)
        pytest.fail("RED: U-IN-04 — zero blanks returns E002 Failure envelope")


class TestUIN05ThreeBlanks:
    """U-IN-05: blank count 3 → E002."""

    def test_u_in_05_three_zeros_returns_e002(self) -> None:
        # Given: TD_INVALID_BLANK_THREE — exactly three 0 cells
        # When: InputValidator().validate(matrix)
        pytest.fail("RED: U-IN-05 — three blanks returns E002 Failure envelope")


class TestUIN06OutOfRange:
    """U-IN-06: cell value ∉ {0}∪{1..16} → E004."""

    def test_u_in_06_negative_cell_returns_e004(self) -> None:
        # Given: TD_INVALID_RANGE_NEG
        # When: InputValidator().validate(matrix)
        pytest.fail("RED: U-IN-06 — negative value returns E004 Failure envelope")

    def test_u_in_06_seventeen_cell_returns_e004(self) -> None:
        # Given: TD_INVALID_RANGE
        # When: InputValidator().validate(matrix)
        pytest.fail("RED: U-IN-06 — value 17 returns E004 Failure envelope")


class TestUIN07Duplicate:
    """U-IN-07: non-zero duplicate → E005."""

    def test_u_in_07_duplicate_nonzero_returns_e005(self) -> None:
        # Given: TD_DUPLICATE
        # When: InputValidator().validate(matrix)
        pytest.fail("RED: U-IN-07 — duplicate non-zero returns E005 Failure envelope")


class TestUIN08ShortCircuitOrder:
    """U-IN-08: size failure before blank/range/duplicate checks (short-circuit)."""

    def test_u_in_08_non_4x4_skips_blank_and_range_rules(self) -> None:
        # Given: TD_INVALID_SIZE_3X4 (size fail + would also fail blank count if checked)
        # When: InputValidator().validate(matrix)
        # Then: E001 only, not E002/E004
        pytest.fail("RED: U-IN-08 — short-circuit returns E001 before later rules")
