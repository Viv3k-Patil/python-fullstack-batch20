import re


def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z\s]{2,50}$", name))


def is_valid_phone(phone):
    return bool(re.match(r"^[6-9]\d{9}$", phone))


def is_valid_email(email):
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))


def is_valid_amount(amount_str):
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False


def get_valid_input(prompt, validator, error_message):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(f"❌ {error_message}")
