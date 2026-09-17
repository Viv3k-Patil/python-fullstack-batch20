from class_activity.vivek.projects.phase7_full_project.models.transaction import Transaction
from class_activity.vivek.projects.phase7_full_project.services.otp_service import requires_otp
from class_activity.vivek.projects.phase7_full_project.repositories.account_repository import log_transaction
from class_activity.vivek.projects.phase7_full_project.exceptions import InsufficientBalanceError, InvalidOTPError
from class_activity.vivek.projects.phase7_full_project.ui.console import print_success, print_error, print_info

OTP_THRESHOLD = 10000


@requires_otp(threshold=OTP_THRESHOLD)
def withdraw(account, amount):
    """Business logic stays clean - the decorator handles the OTP check."""
    account.withdraw(amount)
    account.transactions.append(Transaction(account.account_number, "WITHDRAW", amount))
    log_transaction(account.account_number, "WITHDRAW", amount)


def deposit(account, amount):
    account.deposit(amount)
    account.transactions.append(Transaction(account.account_number, "DEPOSIT", amount))
    log_transaction(account.account_number, "DEPOSIT", amount)


@requires_otp(threshold=OTP_THRESHOLD)
def transfer(from_account, amount, *, to_account):
    """
    Transfer money between two accounts.
    Note: @requires_otp expects (account, amount, ...) - to_account is passed
    as a keyword-only extra arg so the decorator's signature still matches.
    """
    from_account.withdraw(amount)
    try:
        to_account.deposit(amount)
    except Exception:
        # roll back the withdrawal if the deposit side fails for any reason
        from_account.deposit(amount)
        raise

    from_account.transactions.append(Transaction(from_account.account_number, "TRANSFER_OUT", amount))
    to_account.transactions.append(Transaction(to_account.account_number, "TRANSFER_IN", amount))
    log_transaction(from_account.account_number, "TRANSFER_OUT", amount)
    log_transaction(to_account.account_number, "TRANSFER_IN", amount)


def withdraw_with_otp(account, amount, otp_service, phone, entered_otp=None):
    """
    Non-decorator version, kept for teaching contrast: this is the same
    OTP rule written by hand with try/except instead of @requires_otp.
    """
    try:
        if amount > OTP_THRESHOLD:
            if entered_otp is None or not otp_service.verify_otp(phone, entered_otp):
                raise InvalidOTPError("OTP verification failed for high-value withdrawal")
        account.withdraw(amount)
    except InsufficientBalanceError as e:
        print_error(f"Withdrawal failed: {e}")
    except InvalidOTPError as e:
        print_error(f"Security check failed: {e}")
    else:
        print_success(f"₹{amount} withdrawn successfully!")
        account.transactions.append(Transaction(account.account_number, "WITHDRAW", amount))
        log_transaction(account.account_number, "WITHDRAW", amount)
    finally:
        print_info("Withdrawal attempt finished.")
