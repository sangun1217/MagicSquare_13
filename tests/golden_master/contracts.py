"""Golden Master contract validators for solver output semantics."""

from __future__ import annotations

import copy
import re

from magicsquare.entity.blank_locator import find_blank_coords
from magicsquare.entity.magic_validator import is_magic_square
from magicsquare.entity.missing_finder import find_not_exist_nums

Grid = list[list[int]]
ResultVector = list[int]

OUTPUT_PATTERN = re.compile(r"^Output:\n\[(?P<values>[\d,]+)\]$", re.MULTILINE)
ERROR_PATTERN = re.compile(r"^Error:\n(?P<label>.+)$", re.MULTILINE)


def _place_values(
    matrix: Grid,
    r1: int,
    c1: int,
    n_at_first: int,
    r2: int,
    c2: int,
    n_at_second: int,
) -> Grid:
    """Return a copy of matrix with values placed at 1-index blank coordinates."""
    completed = copy.deepcopy(matrix)
    completed[r1 - 1][c1 - 1] = n_at_first
    completed[r2 - 1][c2 - 1] = n_at_second
    return completed


def parse_success_vector(body: str) -> ResultVector:
    """Extract the six-element vector from a serialized success body."""
    match = OUTPUT_PATTERN.search(body.strip())
    if not match:
        msg = f"expected Output block in Golden Master body: {body!r}"
        raise AssertionError(msg)
    values = [int(part) for part in match.group("values").split(",")]
    if len(values) != 6:
        msg = f"expected int[6], got length {len(values)}: {values}"
        raise AssertionError(msg)
    return values


def parse_error_label(body: str) -> str:
    """Extract the Golden Master error label from a serialized error body."""
    match = ERROR_PATTERN.search(body.strip())
    if not match:
        msg = f"expected Error block in Golden Master body: {body!r}"
        raise AssertionError(msg)
    return match.group("label").strip()


def assert_int_six_format(result: ResultVector) -> None:
    """Assert result is a six-element integer vector."""
    assert len(result) == 6, f"expected int[6], got {result!r}"
    assert all(isinstance(value, int) for value in result), (
        f"all elements must be int: {result!r}"
    )


def assert_one_index_coords(result: ResultVector) -> None:
    """Assert blank coordinates are 1-index and within the 4x4 grid."""
    r1, c1, _n1, r2, c2, _n2 = result
    for name, coord in (("r1", r1), ("c1", c1), ("r2", r2), ("c2", c2)):
        assert isinstance(coord, int), f"{name} must be int"
        assert 1 <= coord <= 4, f"{name} must be 1-index in [1,4], got {coord}"


def assert_row_major_coords(grid: Grid, result: ResultVector) -> None:
    """Assert result coordinates match row-major blank discovery."""
    expected = find_blank_coords(grid)
    r1, c1, _n1, r2, c2, _n2 = result
    assert (r1, c1, r2, c2) == expected, (
        f"row-major coords expected {expected}, got {(r1, c1, r2, c2)}"
    )


def assert_small_first_or_reverse(grid: Grid, result: ResultVector) -> str:
    """Assert placement follows small-first then reverse fallback; return attempt used."""
    r1, c1, n_at_first, r2, c2, n_at_second = result
    n1, n2 = find_not_exist_nums(grid)
    assert n1 < n2, f"missing numbers must be sorted: ({n1}, {n2})"

    small_first = _place_values(grid, r1, c1, n1, r2, c2, n2)
    if is_magic_square(small_first):
        assert result == [r1, c1, n1, r2, c2, n2], (
            "small-first success must return [r1,c1,n1,r2,c2,n2]"
        )
        return "small_first"

    reverse = _place_values(grid, r1, c1, n2, r2, c2, n1)
    assert is_magic_square(reverse), "result must come from a valid completion"
    assert result == [r1, c1, n2, r2, c2, n1], (
        "reverse fallback must return [r1,c1,n2,r2,c2,n1]"
    )
    return "reverse"


def assert_success_contract(
    grid: Grid,
    body: str,
    *,
    expected_attempt: str | None = None,
) -> ResultVector:
    """Validate success Golden Master body against solver output contracts."""
    result = parse_success_vector(body)
    assert_int_six_format(result)
    assert_one_index_coords(result)
    assert_row_major_coords(grid, result)
    attempt = assert_small_first_or_reverse(grid, result)
    if expected_attempt is not None:
        assert attempt == expected_attempt, (
            f"expected attempt {expected_attempt!r}, got {attempt!r}"
        )
    return result


def assert_error_contract(body: str, expected_label: str) -> None:
    """Validate error Golden Master body against the error contract."""
    label = parse_error_label(body)
    assert label == expected_label, (
        f"expected error label {expected_label!r}, got {label!r}"
    )
