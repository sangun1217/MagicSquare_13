"""Track A RED — U-IN / U-OUT / U-FLOW (Dual-Track design SSOT)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from magicsquare.boundary.failure import (
    E001,
    E002,
    E003,
    E004,
    E005,
    MSG_E001,
    MSG_E002,
    MSG_E003,
    MSG_E004,
    MSG_E005,
    ValidationFailure,
)
from magicsquare.boundary.input_validator import InputValidator
from magicsquare.boundary.ui_boundary import UIBoundary
from magicsquare.control.solve_partial_magic_square import SolvePartialMagicSquare
from tests.conftest import assert_validation_failure
from tests.fixtures.golden_grids import (
    D_SOL_01_EXPECTED,
    G1,
    TD_DUPLICATE,
    TD_INVALID_BLANK_THREE,
    TD_INVALID_BLANK_ZERO,
    TD_INVALID_RANGE,
    TD_INVALID_RANGE_NEG,
    TD_INVALID_SIZE_3X4,
    TD_INVALID_SIZE_4X3,
    TD_INVALID_SIZE_5X5,
)

pytestmark = pytest.mark.boundary


class TestUIN01RejectNull:
    """U-IN-01: matrix=null → E003."""

    def test_reject_null_grid_returns_e003(self, input_validator: InputValidator) -> None:
        result = input_validator.validate(None)
        assert_validation_failure(result, code=E003, message=MSG_E003)


class TestUIN02RejectNon4x4:
    """U-IN-02: size ≠ 4×4 → E001."""

    @pytest.mark.parametrize(
        "matrix",
        [
            TD_INVALID_SIZE_3X4,
            TD_INVALID_SIZE_4X3,
            TD_INVALID_SIZE_5X5,
            [],
        ],
        ids=["3x4", "4x3", "5x5", "empty"],
    )
    def test_reject_non_4x4_dimensions_returns_e001(
        self,
        input_validator: InputValidator,
        matrix: list[list[int]],
    ) -> None:
        result = input_validator.validate(matrix)
        assert_validation_failure(result, code=E001, message=MSG_E001)


class TestUIN03RejectZeroBlanks:
    """U-IN-03: blank count 0 → E002."""

    def test_reject_zero_blanks_returns_e002(
        self,
        input_validator: InputValidator,
    ) -> None:
        result = input_validator.validate(TD_INVALID_BLANK_ZERO)
        assert_validation_failure(result, code=E002, message=MSG_E002)


class TestUIN04RejectThreeBlanks:
    """U-IN-04: blank count 3 → E002."""

    def test_reject_three_blanks_returns_e002(
        self,
        input_validator: InputValidator,
    ) -> None:
        result = input_validator.validate(TD_INVALID_BLANK_THREE)
        assert_validation_failure(result, code=E002, message=MSG_E002)


class TestUIN05RejectOutOfRange:
    """U-IN-05: value ∉ {0}∪{1..16} → E004."""

    @pytest.mark.parametrize(
        "matrix",
        [TD_INVALID_RANGE_NEG, TD_INVALID_RANGE],
        ids=["negative", "seventeen"],
    )
    def test_reject_out_of_range_cell_returns_e004(
        self,
        input_validator: InputValidator,
        matrix: list[list[int]],
    ) -> None:
        result = input_validator.validate(matrix)
        assert_validation_failure(result, code=E004, message=MSG_E004)


class TestUIN06RejectDuplicate:
    """U-IN-06: non-zero duplicate → E005."""

    def test_reject_duplicate_nonzero_returns_e005(
        self,
        input_validator: InputValidator,
    ) -> None:
        result = input_validator.validate(TD_DUPLICATE)
        assert_validation_failure(result, code=E005, message=MSG_E005)


class TestUOUT01SuccessLengthSix:
    """U-OUT-01: success vector length 6."""

    def test_success_result_has_length_six(self, ui_boundary: UIBoundary) -> None:
        result = ui_boundary.solve(G1)
        assert isinstance(result, list)
        assert len(result) == 6


class TestUOUT02SuccessOneIndexCoords:
    """U-OUT-02: r,c ∈ [1,4] 1-index."""

    def test_success_coordinates_are_one_indexed_in_range(
        self,
        ui_boundary: UIBoundary,
    ) -> None:
        result = ui_boundary.solve(G1)
        assert isinstance(result, list)
        r1, c1, _n1, r2, c2, _n2 = result
        for coord in (r1, c1, r2, c2):
            assert 1 <= coord <= 4


class TestUFLOW02InvalidSkipsExecute:
    """U-FLOW-02: invalid input → execute call_count == 0."""

    def test_invalid_input_never_calls_domain_execute(self) -> None:
        solver = SolvePartialMagicSquare()
        solver.execute = MagicMock()  # type: ignore[method-assign]
        boundary = UIBoundary(validator=InputValidator(), solver=solver)

        result = boundary.solve(None)

        assert_validation_failure(result, code=E003, message=MSG_E003)
        solver.execute.assert_not_called()
