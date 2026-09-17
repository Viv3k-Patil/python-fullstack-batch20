"""
Main CLI entry point. This file is deliberately "dumb" - it only shows menus
and calls into services/. No banking business logic should live here.
"""

import random

from class_activity.vivek.projects.phase7_full_project.models.account import SavingsAccount, CurrentAccount
from class_activity.vivek.projects.phase7_full_project.services.auth_service import AuthService
from class_activity.vivek.projects.phase7_full_project.services.otp_service import OTPService
from class_activity.vivek.projects.phase7_full_project.services import transaction_service as txn
from class_activity.vivek.projects.phase7_full_project.services.validators import (
    is_valid_name,
    is_valid_phone,
    is_valid_email,
    get_valid_input,
)
from class_activity.vivek.projects.phase7_full_project.repositories.account_repository import (
    save_accounts,
    load_accounts_raw,
    save_users,
    load_users_raw,
)
from class_activity.vivek.projects.phase7_full_project.exceptions import (
    BankingError,
    AccountNotFoundError,
    UserAlreadyExistsError,
    AuthenticationError,
)
from class_activity.vivek.projects.phase7_full_project.ui.console import print_success, print_error, print_info, print_menu

auth_service = AuthService()
otp_service = OTPService()
accounts = {}  # account_number -> Account object


def bootstrap():
    """Load persisted users/accounts on startup."""
    users_raw = load_users_raw()
    auth_service.load_users(users_raw)

    accounts_raw = load_accounts_raw()
    for acc_no, data in accounts_raw.items():
        owner = auth_service.users.get(data["owner_phone"])
        if owner is None:
            continue  # orphaned account data, skip
        if data["type"] == "SavingsAccount":
            accounts[acc_no] = SavingsAccount(acc_no, owner, data["balance"])
        else:
            accounts[acc_no] = CurrentAccount(acc_no, owner, data["balance"])


def persist_all():
    save_users(auth_service.dump_users())
    save_accounts(accounts)


def generate_account_number():
    while True:
        acc_no = f"ACC{random.randint(1000, 9999)}"
        if acc_no not in accounts:
            return acc_no


def register_flow():
    print_info("=== Register ===")
    name = get_valid_input("Enter name: ", is_valid_name, "Name must contain only letters and spaces.")
    phone = get_valid_input("Enter phone: ", is_valid_phone, "Phone must be a valid 10-digit Indian number.")
    email = get_valid_input("Enter email: ", is_valid_email, "Enter a valid email address.")
    password = input("Enter password: ")

    try:
        user = auth_service.register(name, phone, email, password)
        print_success(f"Registered successfully! Welcome, {user.name}.")
        return user
    except UserAlreadyExistsError as e:
        print_error(str(e))
        return None


def login_flow():
    print_info("=== Login ===")
    phone = input("Phone: ")
    password = input("Password: ")
    try:
        user = auth_service.login(phone, password)
        print_success(f"Welcome back, {user.name}!")
        return user
    except AuthenticationError as e:
        print_error(str(e))
        return None


def open_account_flow(user):
    print_menu("OPEN ACCOUNT", {"1": "Savings Account", "2": "Current Account"})
    choice = input("Choose type: ")
    acc_no = generate_account_number()

    if choice == "1":
        account = SavingsAccount(acc_no, user)
    elif choice == "2":
        account = CurrentAccount(acc_no, user)
    else:
        print_error("Invalid choice.")
        return

    accounts[acc_no] = account
    print_success(f"Account {acc_no} opened for {user.name}.")


def get_own_account(user):
    """Simple helper: pick from accounts owned by the logged-in user."""
    owned = {acc_no: acc for acc_no, acc in accounts.items() if acc.owner.phone == user.phone}
    if not owned:
        print_error("You have no accounts yet. Open one first.")
        return None

    print_info("Your accounts:")
    for acc_no, acc in owned.items():
        print(f"  {acc_no} - Balance: {acc.balance}")

    acc_no = input("Enter account number: ")
    account = owned.get(acc_no)
    if account is None:
        print_error("That account is not yours or doesn't exist.")
        return None
    return account


def deposit_flow(user):
    account = get_own_account(user)
    if account is None:
        return
    amount = float(input("Amount to deposit: "))
    try:
        txn.deposit(account, amount)
        print_success(f"₹{amount} deposited into {account.account_number}.")
    except BankingError as e:
        print_error(str(e))


def withdraw_flow(user):
    account = get_own_account(user)
    if account is None:
        return
    amount = float(input("Amount to withdraw: "))

    entered_otp = None
    if amount > txn.OTP_THRESHOLD:
        otp_service.generate_otp(user.phone)
        entered_otp = input("Enter the OTP you received: ")

    try:
        txn.withdraw(account, amount, otp_service=otp_service, phone=user.phone, entered_otp=entered_otp)
        print_success(f"₹{amount} withdrawn from {account.account_number}.")
    except BankingError as e:
        print_error(str(e))


def transfer_flow(user):
    account = get_own_account(user)
    if account is None:
        return
    to_acc_no = input("Transfer to account number: ")
    to_account = accounts.get(to_acc_no)
    if to_account is None:
        print_error("Destination account not found.")
        return

    amount = float(input("Amount to transfer: "))

    entered_otp = None
    if amount > txn.OTP_THRESHOLD:
        otp_service.generate_otp(user.phone)
        entered_otp = input("Enter the OTP you received: ")

    try:
        txn.transfer(
            account, amount,
            otp_service=otp_service, phone=user.phone, entered_otp=entered_otp,
            to_account=to_account,
        )
        print_success(f"₹{amount} transferred from {account.account_number} to {to_acc_no}.")
    except BankingError as e:
        print_error(str(e))


def statement_flow(user):
    account = get_own_account(user)
    if account is None:
        return
    print_info(f"Statement for {account.account_number}:")
    if not account.transactions:
        print("  No transactions yet.")
    for t in account.transactions:
        print(f"  {t}")
    print(f"  Current balance: {account.balance}")


def logged_in_menu(user):
    while True:
        print_menu("BANKING MENU", {
            "1": "Open Account",
            "2": "Deposit",
            "3": "Withdraw",
            "4": "Transfer",
            "5": "View Statement",
            "6": "Logout",
        })
        choice = input("Choose an option: ")

        if choice == "1":
            open_account_flow(user)
        elif choice == "2":
            deposit_flow(user)
        elif choice == "3":
            withdraw_flow(user)
        elif choice == "4":
            transfer_flow(user)
        elif choice == "5":
            statement_flow(user)
        elif choice == "6":
            persist_all()
            print_info("Logged out. Data saved.")
            break
        else:
            print_error("Invalid option.")


def main():
    bootstrap()

    while True:
        print_menu("CLI BANKING SYSTEM", {
            "1": "Register",
            "2": "Login",
            "3": "Exit",
        })
        choice = input("Choose an option: ")

        if choice == "1":
            register_flow()
        elif choice == "2":
            user = login_flow()
            if user:
                logged_in_menu(user)
        elif choice == "3":
            persist_all()
            print_info("Goodbye! All data saved.")
            break
        else:
            print_error("Invalid option.")


if __name__ == "__main__":
    main()
