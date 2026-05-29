"""Domain-layer exceptions for solve failures."""


class UnsolvableDomainError(Exception):
    """Raised when both placement attempts fail (FR-05 / I10)."""

    def __init__(self, message: str = "No valid completion: both placement attempts failed.") -> None:
        """Initialize with a stable domain message."""
        self.message = message
        super().__init__(message)
