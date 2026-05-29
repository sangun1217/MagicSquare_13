"""Boundary-layer exception types for input validation failures."""


class InvalidInputError(Exception):
    """Raised when raw input fails Boundary validation (FR-01)."""

    def __init__(self, code: str, message: str) -> None:
        """Initialize with a stable error code and human-readable message."""
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")
