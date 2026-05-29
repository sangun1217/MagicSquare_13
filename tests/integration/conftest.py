"""Shared fixtures for Golden Master integration tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from magicsquare.boundary.ui_boundary import UIBoundary

GOLDEN_MASTER_PATH = Path(__file__).resolve().parents[1] / "golden_master_expected.txt"


@pytest.fixture
def golden_master_path() -> Path:
    """Path to the approved Golden Master baseline file."""
    return GOLDEN_MASTER_PATH


@pytest.fixture
def ui_boundary() -> UIBoundary:
    """Fresh UIBoundary for end-to-end Golden Master capture."""
    return UIBoundary()
