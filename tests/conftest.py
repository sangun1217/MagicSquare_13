"""Shared pytest fixtures."""

from tests.fixtures.golden_grids import G_VALID_A, G_VALID_B

import pytest

Grid = list[list[int]]


@pytest.fixture
def g_valid_a() -> Grid:
    """Return a deep copy of golden grid G_VALID_A."""
    return [row[:] for row in G_VALID_A]


@pytest.fixture
def g_valid_b() -> Grid:
    """Return a deep copy of golden grid G_VALID_B."""
    return [row[:] for row in G_VALID_B]
