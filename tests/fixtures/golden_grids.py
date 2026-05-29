"""Golden grid fixtures from Report/02 Appendix B and PRD §16.4.

Grid type: ``list[list[int]]`` with ``0`` marking blank cells.
Coordinates in expected outputs use 1-index (BR-10).
"""

from typing import Final

Grid = list[list[int]]
ResultVector = list[int]

# --- Report/02 Appendix B ---

G_VALID_A: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

G_VALID_B: Final[Grid] = [
    [1, 15, 14, 4],
    [12, 6, 7, 9],
    [8, 10, 11, 5],
    [13, 3, 2, 16],
]

G_INVALID_DUP: Final[Grid] = [
    [1, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

G_INVALID_ROW: Final[Grid] = [
    [16, 3, 2, 20],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# --- PRD §16.4 solve fixtures ---

# TD-SUCCESS-SF-001: Attempt 1 only succeeds (DN-04 companion).
# G_VALID_A blanks at (0,1) and (3,2) 0-index → (1,2) and (4,3) 1-index.
# Missing {3, 14}; Attempt 1 (3→blank1, 14→blank2) restores G_VALID_A.
# Note: PRD §16.4 example [1,1,1,4,4,16] uses (0,0)/(3,3) which yields REV semantics.
TD_SUCCESS_SF_001: Final[Grid] = [
    [16, 0, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 0, 1],
]
TD_SUCCESS_SF_001_EXPECTED: Final[ResultVector] = [1, 2, 3, 4, 3, 14]
TD_SUCCESS_SF_001_MISSING: Final[tuple[int, int]] = (3, 14)

# DN-04 resolved: G_VALID_A blanks at (1,1) and (2,2) 0-index → (2,2),(3,3) 1-index.
# Attempt 1 (n1=7→blank1, n2=10→blank2) invalid; Attempt 2 (n2→blank1, n1→blank2) valid.
TD_SUCCESS_REV_001: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]
TD_SUCCESS_REV_001_EXPECTED: Final[ResultVector] = [2, 2, 10, 3, 3, 7]
TD_SUCCESS_REV_001_MISSING: Final[tuple[int, int]] = (7, 10)

# --- PRD §16.4 invalid input fixtures ---

TD_INVALID_SIZE: Final[Grid] = [
    [16, 3, 2],
    [5, 10, 11],
    [9, 6, 7],
    [4, 15, 14],
]

TD_INVALID_BLANK_ONE: Final[Grid] = [
    [0, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

TD_INVALID_BLANK_THREE: Final[Grid] = [
    [0, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 0, 7, 12],
    [4, 15, 14, 1],
]

TD_INVALID_RANGE: Final[Grid] = [
    [17, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]

TD_DUPLICATE: Final[Grid] = [
    [1, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 0],
]

# TD-UNSOLVABLE: numeric values to be confirmed at RED-DOM-SOL-003.
