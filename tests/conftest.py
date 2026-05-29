"""Shared pytest fixtures."""

from __future__ import annotations

import pytest

from magicsquare.boundary.failure import ValidationFailure
from magicsquare.boundary.input_validator import InputValidator
from magicsquare.boundary.ui_boundary import UIBoundary
from magicsquare.control.solve_partial_magic_square import SolvePartialMagicSquare


@pytest.fixture
def input_validator() -> InputValidator:
    """Fresh InputValidator for Boundary RED tests."""
    return InputValidator()


@pytest.fixture
def ui_boundary() -> UIBoundary:
    """UIBoundary with default validator and solver collaborators."""
    return UIBoundary()


def assert_validation_failure(
    result: object,
    *,
    code: str,
    message: str,
) -> ValidationFailure:
    """Assert result is a Failure envelope with exact code and message."""
    assert isinstance(result, ValidationFailure), (
        f"expected ValidationFailure, got {type(result)!r}"
    )
    assert result.error.code == code
    assert result.error.message == message
    return result
