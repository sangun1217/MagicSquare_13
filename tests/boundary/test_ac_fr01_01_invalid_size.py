"""AC-FR-01-01 invalid grid size / reference — RED tests (Track A).

AC-FR-01-01, PRD §8.1 INVALID_SIZE (charter); PRD §13 ERR-VAL-001 (canonical).
"""

from __future__ import annotations

from typing import Any
from unittest.mock import patch

import pytest

from magicsquare.boundary.boundary_validator import BoundaryValidator
from magicsquare.boundary.exceptions import InvalidInputError
from magicsquare.control.solve_entry import solve
from tests.boundary.ac_fr01_01_constants import (
    AC_DOCSTRING_LINE,
    AC_ID,
    CHARTER_CODE_INVALID_SIZE,
    CHARTER_MESSAGE,
    EXCLUDED_AC_IDS,
    PRD_ERR_VAL_001_MESSAGE,
)
from tests.fixtures.golden_grids import (
    G_VALID_A,
    TD_INVALID_BLANK_ONE,
    TD_INVALID_RANGE,
    TD_SUCCESS_SF_001,
)

pytestmark = pytest.mark.boundary

# --- Arrange fixtures (AC-FR-01-01 scope only) ---

GRID_NONE: None = None
GRID_EMPTY: list[list[int]] = []
GRID_FOUR_EMPTY_ROWS: list[list[int]] = [[]] * 4
GRID_3X4: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
]
GRID_4X3: list[list[int]] = [
    [16, 3, 2],
    [5, 10, 11],
    [9, 6, 7],
    [4, 15, 14],
]
GRID_5X5: list[list[int]] = [[1, 2, 3, 4, 5] for _ in range(5)]


def _assert_charter_invalid_size_error(exc: InvalidInputError) -> None:
    """Assert charter code and message for INVALID_SIZE failures."""
    assert exc.code == CHARTER_CODE_INVALID_SIZE
    assert exc.message == CHARTER_MESSAGE


def _assert_prd_message_char_by_char(message: str) -> None:
    """Assert message matches PRD §13 ERR-VAL-001 fixed string exactly."""
    assert len(message) == len(PRD_ERR_VAL_001_MESSAGE)
    assert message == PRD_ERR_VAL_001_MESSAGE
    assert list(message) == list(PRD_ERR_VAL_001_MESSAGE)


class TestNormalFailureReturn:
    """정상 실패 반환: InvalidInputError with INVALID_SIZE charter fields."""

    __doc__ = AC_DOCSTRING_LINE

    def test_grid_none_raises_invalid_input_error(self) -> None:
        """# AC-FR-01-01"""
        # Given: explicit None grid
        grid = GRID_NONE
        validator = BoundaryValidator()
        # When: boundary validation runs
        with pytest.raises(InvalidInputError) as exc_info:
            validator.validate(grid)  # type: ignore[arg-type]
        # Then: charter failure contract
        _assert_charter_invalid_size_error(exc_info.value)

    def test_grid_none_error_code_is_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)  # type: ignore[arg-type]
        # Then
        assert exc_info.value.code == CHARTER_CODE_INVALID_SIZE

    def test_grid_none_error_message_is_grid_must_be_4x4(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)  # type: ignore[arg-type]
        # Then
        assert exc_info.value.message == CHARTER_MESSAGE

    def test_grid_none_exception_str_contains_code_and_message(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)  # type: ignore[arg-type]
        # Then
        assert str(exc_info.value) == f"{CHARTER_CODE_INVALID_SIZE}: {CHARTER_MESSAGE}"

    def test_grid_none_does_not_return_normalized_grid(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        validator = BoundaryValidator()
        # When / Then: no successful return
        with pytest.raises(InvalidInputError):
            validator.validate(grid)  # type: ignore[arg-type]


class TestBoundaryValues:
    """경계값: null/empty/ragged/non-4x4 shapes → INVALID_SIZE."""

    __doc__ = AC_DOCSTRING_LINE

    def test_grid_empty_list_raises_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_EMPTY
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_charter_invalid_size_error(exc_info.value)

    def test_grid_four_empty_rows_raises_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given: four rows, zero columns each
        grid = GRID_FOUR_EMPTY_ROWS
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_charter_invalid_size_error(exc_info.value)

    def test_grid_3x4_raises_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_3X4
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_charter_invalid_size_error(exc_info.value)

    def test_grid_4x3_raises_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_4X3
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_charter_invalid_size_error(exc_info.value)

    def test_grid_5x5_raises_invalid_size(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_5X5
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_charter_invalid_size_error(exc_info.value)


class TestDomainIsolation:
    """격리 검증: FR-01 failure must not call resolve()."""

    __doc__ = AC_DOCSTRING_LINE

    @patch("magicsquare.control.solve_entry.resolve")
    def test_grid_none_resolve_zero_calls(self, mock_resolve: Any) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        # When
        with pytest.raises(InvalidInputError):
            solve(grid)
        # Then
        mock_resolve.assert_not_called()

    @patch("magicsquare.control.solve_entry.resolve")
    def test_grid_empty_resolve_zero_calls(self, mock_resolve: Any) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_EMPTY
        # When
        with pytest.raises(InvalidInputError):
            solve(grid)
        # Then
        mock_resolve.assert_not_called()

    @patch("magicsquare.control.solve_entry.resolve")
    def test_grid_four_empty_rows_resolve_zero_calls(
        self, mock_resolve: Any
    ) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_FOUR_EMPTY_ROWS
        # When
        with pytest.raises(InvalidInputError):
            solve(grid)
        # Then
        mock_resolve.assert_not_called()

    @patch("magicsquare.control.solve_entry.resolve")
    def test_grid_3x4_resolve_zero_calls(self, mock_resolve: Any) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_3X4
        # When
        with pytest.raises(InvalidInputError):
            solve(grid)
        # Then
        mock_resolve.assert_not_called()

    @patch("magicsquare.control.solve_entry.resolve")
    def test_grid_4x3_resolve_zero_calls(self, mock_resolve: Any) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_4X3
        # When
        with pytest.raises(InvalidInputError):
            solve(grid)
        # Then
        mock_resolve.assert_not_called()


class TestMessageIdentity:
    """메시지 동일성: PRD §13 ERR-VAL-001 문자열과 문자 단위 일치."""

    __doc__ = AC_DOCSTRING_LINE

    def test_grid_none_message_char_by_char_prd_section(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_NONE
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)  # type: ignore[arg-type]
        # Then: PRD §13 fixed message (§12.1 / §8 Stage 2 contract)
        _assert_prd_message_char_by_char(exc_info.value.message)

    def test_grid_empty_message_char_by_char_prd_section(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_EMPTY
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_prd_message_char_by_char(exc_info.value.message)

    def test_grid_four_empty_rows_message_char_by_char_prd_section(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_FOUR_EMPTY_ROWS
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_prd_message_char_by_char(exc_info.value.message)

    def test_grid_3x4_message_char_by_char_prd_section(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_3X4
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_prd_message_char_by_char(exc_info.value.message)

    def test_grid_4x3_message_char_by_char_prd_section(self) -> None:
        """# AC-FR-01-01"""
        # Given
        grid = GRID_4X3
        # When
        with pytest.raises(InvalidInputError) as exc_info:
            BoundaryValidator().validate(grid)
        # Then
        _assert_prd_message_char_by_char(exc_info.value.message)


class TestScopeRestriction:
    """범위 제한: AC-FR-01-02~05 및 FR-02~05 케이스는 본 모듈에서 실행 금지."""

    __doc__ = AC_DOCSTRING_LINE

    def test_module_excludes_ac_fr01_02_blank_count_fixture(self) -> None:
        """# AC-FR-01-01 — scope guard (AC-FR-01-02 excluded)."""
        # Given: TD_INVALID_BLANK_ONE belongs to AC-FR-01-02 / ERR-VAL-002
        assert AC_ID not in EXCLUDED_AC_IDS
        assert "AC-FR-01-02" in EXCLUDED_AC_IDS
        # When / Then: this module must not parametrize blank-count cases
        assert TD_INVALID_BLANK_ONE not in (
            GRID_NONE,
            GRID_EMPTY,
            GRID_FOUR_EMPTY_ROWS,
            GRID_3X4,
            GRID_4X3,
            GRID_5X5,
        )

    def test_module_excludes_ac_fr01_03_invalid_range_fixture(self) -> None:
        """# AC-FR-01-01 — scope guard (AC-FR-01-03 excluded)."""
        # Given
        assert "AC-FR-01-03" in EXCLUDED_AC_IDS
        # Then
        assert TD_INVALID_RANGE not in (
            GRID_NONE,
            GRID_EMPTY,
            GRID_FOUR_EMPTY_ROWS,
            GRID_3X4,
            GRID_4X3,
            GRID_5X5,
        )

    def test_module_excludes_ac_fr01_05_valid_4x4_success_fixture(self) -> None:
        """# AC-FR-01-01 — scope guard (AC-FR-01-05 / FR-02+ excluded)."""
        # Given: complete valid magic square — out of FR-01-01 failure scope
        assert "AC-FR-01-05" in EXCLUDED_AC_IDS
        # Then: G_VALID_A must not be used as failure-case input in this file
        assert G_VALID_A not in (
            GRID_NONE,
            GRID_EMPTY,
            GRID_FOUR_EMPTY_ROWS,
            GRID_3X4,
            GRID_4X3,
            GRID_5X5,
        )

    def test_module_excludes_fr02_solver_success_partial_grid(self) -> None:
        """# AC-FR-01-01 — scope guard (FR-02 / FR-05 excluded)."""
        # Given: partial solve fixture for Track B
        assert "AC-FR-05" in EXCLUDED_AC_IDS
        # Then
        assert TD_SUCCESS_SF_001 not in (
            GRID_NONE,
            GRID_EMPTY,
            GRID_FOUR_EMPTY_ROWS,
            GRID_3X4,
            GRID_4X3,
            GRID_5X5,
        )

    @pytest.mark.parametrize(
        "excluded_ac",
        sorted(EXCLUDED_AC_IDS),
    )
    def test_excluded_ac_ids_documented_out_of_scope(self, excluded_ac: str) -> None:
        """# AC-FR-01-01 — scope guard."""
        # Given / Then: sibling AC/FR items are explicitly out of scope
        assert excluded_ac != AC_ID
        assert excluded_ac.startswith("AC-FR-")
