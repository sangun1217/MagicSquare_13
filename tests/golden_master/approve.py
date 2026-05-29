"""Approve-pattern utilities for Golden Master regression tests."""

from __future__ import annotations

import difflib
import os
import re
from pathlib import Path

SECTION_HEADER_PATTERN = re.compile(r"^\[(?P<section_id>[^\]]+)\]\s*$", re.MULTILINE)
SECTION_SEPARATOR = "________________________________________"


def parse_golden_master_document(content: str) -> dict[str, str]:
    """Parse a Golden Master document into section_id → body mappings."""
    sections: dict[str, str] = {}
    chunks = re.split(rf"\n{re.escape(SECTION_SEPARATOR)}\n", content.strip())
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        lines = chunk.splitlines()
        header = lines[0].strip()
        match = SECTION_HEADER_PATTERN.match(header)
        if not match:
            msg = f"invalid Golden Master section header: {header!r}"
            raise ValueError(msg)
        section_id = match.group("section_id")
        body = "\n".join(lines[1:]).strip()
        sections[section_id] = body
    return sections


def format_failure_diff(expected: str, actual: str, *, label: str) -> str:
    """Format expected vs actual diff for Golden Master test failures."""
    diff_lines = list(
        difflib.unified_diff(
            expected.splitlines(),
            actual.splitlines(),
            fromfile="expected",
            tofile="actual",
            lineterm="",
        ),
    )
    if not diff_lines:
        return ""
    return "\n".join([*diff_lines, SECTION_SEPARATOR])


def unified_diff(expected: str, actual: str, *, label: str) -> str:
    """Return unified diff text for expected vs actual Golden Master content."""
    expected_lines = expected.splitlines(keepends=True)
    actual_lines = actual.splitlines(keepends=True)
    diff = difflib.unified_diff(
        expected_lines,
        actual_lines,
        fromfile=f"{label} (expected)",
        tofile=f"{label} (actual)",
        lineterm="",
    )
    return "".join(f"{line}\n" for line in diff)


def approve_or_assert(
    actual_document: str,
    expected_path: Path,
    *,
    approve: bool | None = None,
) -> None:
    """Write baseline when missing/approve; otherwise compare and fail on mismatch."""
    should_approve = (
        approve
        if approve is not None
        else os.environ.get("PYTEST_APPROVE", "").lower() in {"1", "true", "yes"}
    )

    expected_path.parent.mkdir(parents=True, exist_ok=True)

    if should_approve or not expected_path.is_file():
        expected_path.write_text(actual_document, encoding="utf-8")
        return

    expected_document = expected_path.read_text(encoding="utf-8")
    if expected_document == actual_document:
        return

    expected_sections = parse_golden_master_document(expected_document)
    actual_sections = parse_golden_master_document(actual_document)
    all_section_ids = sorted(set(expected_sections) | set(actual_sections))

    diff_parts: list[str] = []
    for section_id in all_section_ids:
        expected_body = expected_sections.get(section_id, "")
        actual_body = actual_sections.get(section_id, "")
        if expected_body != actual_body:
            diff_parts.append(
                unified_diff(expected_body, actual_body, label=section_id),
            )

    full_diff = unified_diff(expected_document, actual_document, label="golden_master")
    diff_message = "\n".join(
        [
            "Golden Master mismatch.",
            "Re-run with PYTEST_APPROVE=1 to update the baseline.",
            "",
            full_diff,
            *diff_parts,
        ],
    )
    raise AssertionError(diff_message)


def read_expected_sections(expected_path: Path) -> dict[str, str]:
    """Load section bodies from the Golden Master baseline file."""
    if not expected_path.is_file():
        return {}
    return parse_golden_master_document(expected_path.read_text(encoding="utf-8"))


def assert_golden_master_section(
    section_id: str,
    actual_body: str,
    expected_path: Path,
    *,
    approve: bool | None = None,
) -> None:
    """Compare one section body against the baseline using the approve pattern."""
    from tests.golden_master.capture import render_golden_master_document

    should_approve = (
        approve
        if approve is not None
        else os.environ.get("PYTEST_APPROVE", "").lower() in {"1", "true", "yes"}
    )

    expected_path.parent.mkdir(parents=True, exist_ok=True)

    if should_approve or not expected_path.is_file():
        document = render_golden_master_document()
        expected_path.write_text(document, encoding="utf-8")
        return

    expected_sections = read_expected_sections(expected_path)
    expected_body = expected_sections.get(section_id, "")

    if expected_body == actual_body.strip():
        return

    diff = format_failure_diff(expected_body, actual_body.strip(), label=section_id)
    raise AssertionError(
        "\n".join(
            [
                f"Golden Master mismatch in [{section_id}].",
                "Re-run with PYTEST_APPROVE=1 to update the baseline.",
                "",
                diff,
            ],
        ),
    )
