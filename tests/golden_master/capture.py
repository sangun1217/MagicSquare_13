"""Serialize solver results for Golden Master baseline files."""

from __future__ import annotations

from magicsquare.boundary.failure import (
    E002,
    E005,
    ValidationFailure,
)
from magicsquare.boundary.ui_boundary import UIBoundary
from magicsquare.entity.exceptions import UnsolvableDomainError
from tests.golden_master.scenarios import GOLDEN_MASTER_SCENARIOS, GoldenMasterScenario

Grid = list[list[int]]

GM_ERROR_LABELS: dict[str, str] = {
    E002: "INVALID_BLANK_COUNT",
    E005: "DUPLICATE_NUMBER",
}
GM_NO_VALID_MAGIC_SQUARE: str = "NO_VALID_MAGIC_SQUARE"


def format_grid_input(grid: Grid) -> str:
    """Render a 4x4 grid as space-separated rows."""
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def format_success_output(result: list[int]) -> str:
    """Render a six-element success vector."""
    return f"[{','.join(str(value) for value in result)}]"


def format_error_output(label: str) -> str:
    """Render a Golden Master error section body."""
    return f"Error:\n{label}"


def capture_scenario(boundary: UIBoundary, scenario: GoldenMasterScenario) -> str:
    """Capture serialized output for one Golden Master scenario."""
    input_block = format_grid_input(scenario.grid)
    try:
        result = boundary.solve(scenario.grid)
    except UnsolvableDomainError:
        body = format_error_output(GM_NO_VALID_MAGIC_SQUARE)
        return f"Input:\n{input_block}\n{body}"

    if isinstance(result, ValidationFailure):
        label = GM_ERROR_LABELS.get(result.error.code, result.error.code)
        body = format_error_output(label)
        return f"Input:\n{input_block}\n{body}"

    body = f"Output:\n{format_success_output(result)}"
    return f"Input:\n{input_block}\n{body}"


def render_golden_master_document(boundary: UIBoundary | None = None) -> str:
    """Render the full Golden Master expected document from live solver output."""
    solver_boundary = boundary or UIBoundary()
    sections: list[str] = []
    for scenario in GOLDEN_MASTER_SCENARIOS:
        section_body = capture_scenario(solver_boundary, scenario)
        sections.append(f"[{scenario.section_id}]\n{section_body}")
    return "\n________________________________________\n\n".join(sections) + "\n"
