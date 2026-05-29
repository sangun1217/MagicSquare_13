"""Sprint 0 smoke tests for Boundary layer skeleton."""

from magicsquare.boundary.result_formatter import format_result


def test_format_result_assembles_int6_vector() -> None:
    result = format_result(1, 1, 1, 4, 4, 16)
    assert result == [1, 1, 1, 4, 4, 16]
    assert len(result) == 6
