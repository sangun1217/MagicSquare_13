"""Entity layer: domain rules and invariants."""

from magicsquare.entity.blank_locator import find_blank_coords
from magicsquare.entity.exceptions import UnsolvableDomainError
from magicsquare.entity.magic_validator import is_magic_square
from magicsquare.entity.missing_finder import find_not_exist_nums
from magicsquare.entity.solver import solution

__all__ = [
    "UnsolvableDomainError",
    "find_blank_coords",
    "find_not_exist_nums",
    "is_magic_square",
    "solution",
]
