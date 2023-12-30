from typing import Optional


class SquadError(Exception):
    """
    Base exception for Squad errors.
    """


class InvalidSecretKey(SquadError):
    """Raised when the secret key is invalid."""

    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__("Invalid secret key" if message is None else message)
