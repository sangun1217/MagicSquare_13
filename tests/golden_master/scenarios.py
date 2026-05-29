"""Golden Master scenario definitions for solver regression (GM-TC-01~05)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Literal

from tests.fixtures.golden_grids import (
    G1,
    G1_SF,
    TD_INVALID_BLANK_THREE,
)

Grid = list[list[int]]
ScenarioKind = Literal["success", "error"]
AttemptKind = Literal["small_first", "reverse"]


@dataclass(frozen=True, slots=True)
class GoldenMasterScenario:
    """Single Golden Master input scenario."""

    tc_id: str
    section_id: str
    grid: Grid
    kind: ScenarioKind
    expected_error: str | None = None
    expected_attempt: AttemptKind | None = None


GM_TC_01_NORMAL_SUCCESS: Final[GoldenMasterScenario] = GoldenMasterScenario(
    tc_id="GM-TC-01",
    section_id="normal_success",
    grid=G1_SF,
    kind="success",
    expected_attempt="small_first",
)

GM_TC_02_REVERSE_SUCCESS: Final[GoldenMasterScenario] = GoldenMasterScenario(
    tc_id="GM-TC-02",
    section_id="reverse_success",
    grid=G1,
    kind="success",
    expected_attempt="reverse",
)

GM_TC_03_INVALID_BLANK_COUNT: Final[GoldenMasterScenario] = GoldenMasterScenario(
    tc_id="GM-TC-03",
    section_id="invalid_blank_count",
    grid=TD_INVALID_BLANK_THREE,
    kind="error",
    expected_error="INVALID_BLANK_COUNT",
)

GM_TC_04_DUPLICATE_NUMBER: Final[GoldenMasterScenario] = GoldenMasterScenario(
    tc_id="GM-TC-04",
    section_id="duplicate_number",
    grid=[
        [1, 3, 2, 13],
        [5, 1, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 0],
    ],
    kind="error",
    expected_error="DUPLICATE_NUMBER",
)

GM_TC_05_NO_VALID_MAGIC_SQUARE: Final[GoldenMasterScenario] = GoldenMasterScenario(
    tc_id="GM-TC-05",
    section_id="no_valid_magic_square",
    grid=[
        [16, 5, 2, 13],
        [3, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ],
    kind="error",
    expected_error="NO_VALID_MAGIC_SQUARE",
)

GOLDEN_MASTER_SCENARIOS: Final[tuple[GoldenMasterScenario, ...]] = (
    GM_TC_01_NORMAL_SUCCESS,
    GM_TC_02_REVERSE_SUCCESS,
    GM_TC_03_INVALID_BLANK_COUNT,
    GM_TC_04_DUPLICATE_NUMBER,
    GM_TC_05_NO_VALID_MAGIC_SQUARE,
)

GOLDEN_MASTER_SCENARIO_BY_TC: Final[dict[str, GoldenMasterScenario]] = {
    scenario.tc_id: scenario for scenario in GOLDEN_MASTER_SCENARIOS
}
