"""Track A RED skeleton — U-FLOW-02 (invalid input → Domain execute 0 calls)."""

from __future__ import annotations

import pytest

from magicsquare.boundary.input_validator import InputValidator  # noqa: F401
from magicsquare.boundary.ui_boundary import UIBoundary  # noqa: F401
from magicsquare.control.solve_partial_magic_square import (  # noqa: F401
    SolvePartialMagicSquare,
)

pytestmark = pytest.mark.boundary


class TestUFLOW02DomainExecuteIsolation:
    """U-FLOW-02: Boundary reject → SolvePartialMagicSquare.execute not called."""

    def test_u_flow_02_null_matrix_execute_zero_calls(self) -> None:
        # Given: matrix = None
        # When: UIBoundary(solver=mock).solve(matrix)
        # Spy: SolvePartialMagicSquare.execute — assert call_count == 0
        pytest.fail("RED: U-FLOW-02 — null input leaves execute uncalled")

    def test_u_flow_02_invalid_size_execute_zero_calls(self) -> None:
        # Given: TD_INVALID_SIZE_3X4
        # When: UIBoundary(solver=mock).solve(matrix)
        # Spy: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E001 size failure leaves execute uncalled")

    def test_u_flow_02_invalid_blank_count_execute_zero_calls(self) -> None:
        # Given: TD_INVALID_BLANK_THREE
        # When: UIBoundary(solver=mock).solve(matrix)
        # Spy: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E002 blank failure leaves execute uncalled")

    def test_u_flow_02_out_of_range_execute_zero_calls(self) -> None:
        # Given: TD_INVALID_RANGE
        # When: UIBoundary(solver=mock).solve(matrix)
        # Spy: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E004 range failure leaves execute uncalled")

    def test_u_flow_02_duplicate_execute_zero_calls(self) -> None:
        # Given: TD_DUPLICATE
        # When: UIBoundary(solver=mock).solve(matrix)
        # Spy: execute.call_count == 0
        pytest.fail("RED: U-FLOW-02 — E005 duplicate failure leaves execute uncalled")
