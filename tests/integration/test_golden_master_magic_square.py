"""Golden Master regression tests — Magic Square Solver (GM-TC-01~05).

[TAG][GoldenMaster]
Run: ``pytest -m golden_master -v``
Approve: ``PYTEST_APPROVE=1 pytest -m golden_master -v``
"""

from __future__ import annotations

from pathlib import Path

import pytest

from magicsquare.boundary.ui_boundary import UIBoundary
from tests.golden_master.approve import approve_or_assert, assert_golden_master_section
from tests.golden_master.capture import capture_scenario, render_golden_master_document
from tests.golden_master.contracts import assert_error_contract, assert_success_contract
from tests.golden_master.scenarios import (
    GM_TC_01_NORMAL_SUCCESS,
    GM_TC_02_REVERSE_SUCCESS,
    GM_TC_03_INVALID_BLANK_COUNT,
    GM_TC_04_DUPLICATE_NUMBER,
    GM_TC_05_NO_VALID_MAGIC_SQUARE,
    GoldenMasterScenario,
)

pytestmark = [pytest.mark.integration, pytest.mark.golden_master]


def _run_golden_master_case(
    scenario: GoldenMasterScenario,
    boundary: UIBoundary,
    golden_master_path: Path,
) -> None:
    """Capture, validate contracts, and compare one Golden Master scenario."""
    actual_body = capture_scenario(boundary, scenario)

    if scenario.kind == "success":
        assert_success_contract(
            scenario.grid,
            actual_body,
            expected_attempt=scenario.expected_attempt,
        )
    else:
        assert scenario.expected_error is not None
        assert_error_contract(actual_body, scenario.expected_error)

    assert_golden_master_section(
        scenario.section_id,
        actual_body,
        golden_master_path,
    )


class TestGoldenMasterMagicSquare:
    """[TAG][GoldenMaster] API serialization vs golden_master_expected.txt."""

    def test_gm_tc_01_normal_success_small_first(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """GM-TC-01: small-first combination succeeds with int[6] output."""
        _run_golden_master_case(GM_TC_01_NORMAL_SUCCESS, ui_boundary, golden_master_path)

    def test_gm_tc_02_reverse_success_fallback(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """GM-TC-02: reverse fallback succeeds when small-first fails."""
        _run_golden_master_case(GM_TC_02_REVERSE_SUCCESS, ui_boundary, golden_master_path)

    def test_gm_tc_03_invalid_blank_count_error_contract(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """GM-TC-03: blank count violation returns INVALID_BLANK_COUNT."""
        _run_golden_master_case(
            GM_TC_03_INVALID_BLANK_COUNT,
            ui_boundary,
            golden_master_path,
        )

    def test_gm_tc_04_duplicate_number_error_contract(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """GM-TC-04: duplicate non-zero returns DUPLICATE_NUMBER."""
        _run_golden_master_case(GM_TC_04_DUPLICATE_NUMBER, ui_boundary, golden_master_path)

    def test_gm_tc_05_no_valid_magic_square_error_contract(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """GM-TC-05: both attempts fail returns NO_VALID_MAGIC_SQUARE."""
        _run_golden_master_case(
            GM_TC_05_NO_VALID_MAGIC_SQUARE,
            ui_boundary,
            golden_master_path,
        )

    def test_golden_master_document_matches_baseline(
        self,
        ui_boundary: UIBoundary,
        golden_master_path: Path,
    ) -> None:
        """Full-document approve: open(expected).read() vs rendered actual."""
        actual_document = render_golden_master_document(ui_boundary)
        approve_or_assert(actual_document, golden_master_path)
