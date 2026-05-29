"""Sprint 0 smoke tests — validate fixture catalog and project skeleton."""

from magicsquare.entity.constants import (
    BLANK_COUNT,
    GRID_SIZE,
    MAGIC_CONSTANT_N4,
    VALUE_MAX,
    VALUE_MIN,
)
from tests.fixtures.golden_grids import (
    G_VALID_A,
    G_VALID_B,
    TD_SUCCESS_REV_001,
    TD_SUCCESS_REV_001_EXPECTED,
    TD_SUCCESS_REV_001_MISSING,
    TD_SUCCESS_SF_001,
    TD_SUCCESS_SF_001_EXPECTED,
    TD_SUCCESS_SF_001_MISSING,
)


def _row_sums(grid: list[list[int]]) -> list[int]:
    return [sum(row) for row in grid]


def _col_sums(grid: list[list[int]]) -> list[int]:
    size = len(grid)
    return [sum(grid[r][c] for r in range(size)) for c in range(size)]


def _main_diagonal_sum(grid: list[list[int]]) -> int:
    return sum(grid[i][i] for i in range(len(grid)))


def _anti_diagonal_sum(grid: list[list[int]]) -> int:
    size = len(grid)
    return sum(grid[i][size - 1 - i] for i in range(size))


def _is_complete_magic_square(grid: list[list[int]]) -> bool:
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return False
    if any(cell < 1 or cell > VALUE_MAX for row in grid for cell in row):
        return False
    values = sorted(cell for row in grid for cell in row)
    if values != list(range(VALUE_MIN, VALUE_MAX + 1)):
        return False
    line_sums = (
        _row_sums(grid)
        + _col_sums(grid)
        + [_main_diagonal_sum(grid), _anti_diagonal_sum(grid)]
    )
    return all(total == MAGIC_CONSTANT_N4 for total in line_sums)


def _blank_count(grid: list[list[int]]) -> int:
    return sum(row.count(0) for row in grid)


def test_g_valid_a_is_4x4() -> None:
    assert len(G_VALID_A) == GRID_SIZE
    assert all(len(row) == GRID_SIZE for row in G_VALID_A)


def test_g_valid_a_is_complete_magic_square() -> None:
    assert _is_complete_magic_square(G_VALID_A)


def test_g_valid_b_is_complete_magic_square() -> None:
    assert _is_complete_magic_square(G_VALID_B)


def test_td_success_sf_001_has_two_blanks() -> None:
    assert _blank_count(TD_SUCCESS_SF_001) == BLANK_COUNT


def test_td_success_sf_001_expected_output_length() -> None:
    assert len(TD_SUCCESS_SF_001_EXPECTED) == 6


def test_td_success_sf_001_attempt1_restores_valid_square() -> None:
    n1, n2 = TD_SUCCESS_SF_001_MISSING
    grid = [row[:] for row in TD_SUCCESS_SF_001]
    grid[0][1] = n1
    grid[3][2] = n2
    assert _is_complete_magic_square(grid)


def test_td_success_sf_001_attempt2_is_invalid() -> None:
    n1, n2 = TD_SUCCESS_SF_001_MISSING
    grid = [row[:] for row in TD_SUCCESS_SF_001]
    grid[0][1] = n2
    grid[3][2] = n1
    assert not _is_complete_magic_square(grid)


def test_td_success_rev_001_attempt1_is_invalid() -> None:
    n1, n2 = TD_SUCCESS_REV_001_MISSING
    grid = [row[:] for row in TD_SUCCESS_REV_001]
    grid[1][1] = n1
    grid[2][2] = n2
    assert not _is_complete_magic_square(grid)


def test_td_success_rev_001_attempt2_is_valid() -> None:
    n1, n2 = TD_SUCCESS_REV_001_MISSING
    grid = [row[:] for row in TD_SUCCESS_REV_001]
    grid[1][1] = n2
    grid[2][2] = n1
    assert _is_complete_magic_square(grid)


def test_td_success_rev_001_expected_output_matches_ac_fr05_02() -> None:
    n1, n2 = TD_SUCCESS_REV_001_MISSING
    assert TD_SUCCESS_REV_001_EXPECTED == [2, 2, n2, 3, 3, n1]


def test_td_success_sf_001_expected_output_matches_fixture() -> None:
    n1, n2 = TD_SUCCESS_SF_001_MISSING
    assert TD_SUCCESS_SF_001_EXPECTED == [1, 2, n1, 4, 3, n2]
