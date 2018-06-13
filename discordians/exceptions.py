__all__ = ["ArgumentError", "DifferentResponseCode"]

class ArgumentError(Exception):
    """Raised when the supplied argument to a method does isn't right."""
    pass


class DifferentResponseCode(Exception):
    """Raised when the API returns a different status code. (non-200)."""
    pass