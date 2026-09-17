import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(DATA_DIR, "logs")
ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

os.makedirs(LOG_DIR, exist_ok=True)


def save_accounts(accounts: dict):
    """accounts: dict of account_number -> Account object"""
    data = {acc_no: acc.to_dict() for acc_no, acc in accounts.items()}
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_accounts_raw() -> dict:
    """Returns raw dicts - main.py rehydrates these into real Account objects,
    since Account needs a live User object as its owner."""
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users_dict: dict):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users_dict, file, indent=4, ensure_ascii=False)


def load_users_raw() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def log_transaction(account_number, action, amount):
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"transactions_{today}.log")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # encoding="utf-8" is required here: Windows defaults to cp1252, which
    # cannot encode the ₹ symbol and would raise UnicodeEncodeError otherwise.
    with open(log_file, "a", encoding="utf-8") as file:  # append - never erase history!
        file.write(f"{timestamp} | Account: {account_number} | {action}: ₹{amount}\n")
