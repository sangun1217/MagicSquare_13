"""Golden grid fixtures from Report/02 Appendix B and PRD §16.4.

Grid type: ``list[list[int]]`` with ``0`` marking blank cells.
Coordinates in expected outputs use 1-index (BR-10).
"""

from typing import Final

Grid = list[list[int]]
ResultVector = list[int]

# --- Report/02 Appendix B (G0 = complete valid magic square) ---

G0: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

G_VALID_A: Final[Grid] = G0

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

# Column 0 sum broken (G0 variant for D-VAL-03).
G_INVALID_COL: Final[Grid] = [
    [20, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Main diagonal sum broken (G0 variant for D-VAL-04).
G_INVALID_DIAG: Final[Grid] = [
    [20, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Complete grid with one zero (D-VAL-06).
G_INVALID_ZERO_IN_FULL: Final[Grid] = [
    [0, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# Out-of-range value in otherwise complete grid (D-VAL-05).
G_INVALID_RANGE_FULL: Final[Grid] = [
    [17, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# --- G1 / G2 partial solve fixtures (DN-04) ---

G1: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

G2: Final[Grid] = G1

TD_SUCCESS_REV_001: Final[Grid] = G1
TD_SUCCESS_REV_001_EXPECTED: Final[ResultVector] = [2, 2, 10, 3, 3, 7]
TD_SUCCESS_REV_001_MISSING: Final[tuple[int, int]] = (7, 10)

# Small-first success: blanks (1,2) and (4,3) 1-index; missing {3, 14}.
G1_SF: Final[Grid] = [
    [16, 0, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 0, 1],
]
G1_SF_EXPECTED: Final[ResultVector] = [1, 2, 3, 4, 3, 14]

TD_SUCCESS_SF_001: Final[Grid] = G1_SF
TD_SUCCESS_SF_001_EXPECTED: Final[ResultVector] = G1_SF_EXPECTED

# Design-doc alias: Step-A intent on G1 blanks (2,2)/(3,3) — numeric lock at GREEN.
D_SOL_01_EXPECTED: Final[ResultVector] = [2, 2, 7, 3, 3, 10]

# --- PRD §16.4 invalid input fixtures ---

TD_INVALID_SIZE_3X4: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
]

TD_INVALID_SIZE_4X3: Final[Grid] = [
    [16, 3, 2],
    [5, 10, 11],
    [9, 6, 7],
    [4, 15, 14],
]

TD_INVALID_SIZE_5X5: Final[Grid] = [[1, 2, 3, 4, 5] for _ in range(5)]

TD_INVALID_BLANK_ZERO: Final[Grid] = G0

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

TD_INVALID_RANGE_NEG: Final[Grid] = [
    [-1, 3, 2, 13],
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

# G3: FR-01 valid; both placement attempts fail (numeric lock at GREEN Commit 4).
G3: Final[Grid] = [
    [2, 3, 0, 13],
    [5, 10, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

TD_UNSOLVABLE: Final[Grid] = G3
