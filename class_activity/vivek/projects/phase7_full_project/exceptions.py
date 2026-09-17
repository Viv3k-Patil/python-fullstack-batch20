class BankingError(Exception):
    """Base exception for the whole app."""
    pass


class InsufficientBalanceError(BankingError):
    pass


class InvalidOTPError(BankingError):
    pass


class AccountNotFoundError(BankingError):
    pass


class UserAlreadyExistsError(BankingError):
    pass


class AuthenticationError(BankingError):
    pass
