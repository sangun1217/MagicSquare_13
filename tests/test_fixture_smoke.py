"""Smoke tests for golden fixture constants."""

from __future__ import annotations

from tests.fixtures.golden_grids import G0, G1, G1_SF, TD_SUCCESS_REV_001_EXPECTED


def test_g0_is_4x4() -> None:
    assert len(G0) == 4
    assert all(len(row) == 4 for row in G0)


def test_g1_has_two_zeros() -> None:
    assert sum(cell == 0 for row in G1 for cell in row) == 2


def test_rev_expected_length_six() -> None:
    assert len(TD_SUCCESS_REV_001_EXPECTED) == 6


def test_g1_sf_small_first_vector_length() -> None:
    from tests.fixtures.golden_grids import G1_SF_EXPECTED

    assert len(G1_SF_EXPECTED) == 6
