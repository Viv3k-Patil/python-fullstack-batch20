# 📚 Major Project — CLI-Based Banking System

## 🎯 Learning Objectives

By the end of this project, students will be able to:

* 🎯 Simulate a real-world banking environment using secure, structured Python code
* 🎯 Follow a professional software project lifecycle: requirements → planning → coding → testing → delivery
* 🎯 Design a modular, OOP-based architecture using classes for users, accounts, transactions, authentication, and validation
* 🎯 Apply inheritance, encapsulation, and is-a/has-a relationships in a real, non-toy system
* 🎯 Implement secure authentication, including optional OTP verification
* 🎯 Validate real-world input (names, phone numbers, emails) using regex
* 🎯 Build a clean, color-coded console interface
* 🎯 Persist users, accounts, and transactions to files
* 🎯 Handle errors gracefully using try/except and custom exceptions

---

## 📖 Introduction

This is your **capstone project** 🏆 — everything you've learned across this entire course (OOP, decorators, generators, logging, exceptions, file handling, regex) comes together into ONE real, professional-grade application: a **CLI-Based Banking System**.

Unlike earlier mini-projects, this one is deliberately spread across 10 days, because real software isn't written in one sitting — it's **planned, designed, built in stages, tested, and refined**, exactly like it would be at an actual IT company.

### 🤔 Why does this project exist?

* 🏦 Banking is a domain everyone intuitively understands — accounts, deposits, withdrawals, transfers — making it perfect for practicing serious design without needing new domain knowledge
* 🏗️ It forces you to combine EVERYTHING: OOP, validation, security, persistence, and error handling into one coherent system, not isolated exercises
* 💼 The workflow you'll follow here (requirements → flowcharts → coding → testing) is literally how real IT companies build software

### 🤔 Where is it used?

* 🏦 Real banking software (SBI YONO, HDFC NetBanking, Paytm) — built on these exact same principles, just at a much larger scale
* 💳 Any system involving money, security, and sensitive data — payment gateways, wallets, ATMs
* 🎓 This project format (plan → build → test) mirrors real internship and job tasks almost exactly

> 💡 **Tip**
>
> Don't rush to write code on Day 1. The FIRST thing real developers do is understand requirements and sketch the design — jumping straight to code is one of the most common (and costly) mistakes beginners make.

---

## 🧠 Detailed Notes

### 1️⃣ Project Objective

The goal is to build a **console-based banking system** that behaves like a real (simplified) bank:

* Users can **register** and **log in** securely
* Users can **open accounts**, **deposit**, **withdraw**, and **transfer** money
* Every transaction is **validated**, **logged**, and **saved permanently**
* Sensitive actions (withdrawals, transfers) require **extra security checks**
* The system must **never crash** on bad input — it should fail gracefully with a clear message

```
                    WHAT THE FINISHED SYSTEM SHOULD DO
                    -------------------------------------
   Register/Login  →  Open Account  →  Deposit/Withdraw/Transfer  →  View Statement
        │                                        │
   (validated, secure)                  (validated, logged, persisted)
```

🤔 **Quick thinking question:** Why is "the system must never crash on bad input" listed as a core objective, rather than just a nice-to-have?
✅ **Answer:** A real bank's software crashing mid-transaction could leave money in an inconsistent state (deducted from one account but never credited elsewhere) — reliability isn't optional in financial software, it's a core requirement from day one.

---

### 2️⃣ Real-World Project Lifecycle Training

Before writing a single line of banking logic, real IT teams go through a structured process. You will follow the same stages:

**Step 1 — Requirement Gathering:** List out, in plain English, everything the system must do. For example:

```
- A user can register with name, phone, email, and a password
- A user can log in
- A logged-in user can open a savings account
- An account holder can deposit money
- An account holder can withdraw money (only if sufficient balance)
- An account holder can transfer money to another account
- Every transaction must be recorded with a timestamp
- Withdrawals above ₹10,000 require OTP verification
```

**Step 2 — Flowchart / Logic Planning:** Sketch the FLOW before coding. For example, the withdrawal flow:

```
        WITHDRAWAL FLOW
        -----------------
    Start
      │
      ▼
  Enter amount
      │
      ▼
  Amount > balance? ──Yes──► ❌ Show "Insufficient balance", End
      │No
      ▼
  Amount > ₹10,000? ──Yes──► Send OTP ──► Verify OTP ──Fail──► ❌ End
      │No                                    │Success
      ▼                                       ▼
  Deduct balance ◄──────────────────────────┘
      │
      ▼
  Log transaction, Save to file
      │
      ▼
     End
```

**Step 3 — Identify Modules:** Break the system into logical pieces BEFORE coding: `User`, `Account`, `Transaction`, `AuthService`, `Validators`, `Storage`.

> ⚠️ **Important**
>
> This planning phase might feel slow compared to "just coding," but it saves MUCH more time later — catching a design flaw on paper costs minutes; catching it after writing 500 lines of code costs hours.

🤔 **Quick thinking question:** Why is drawing a flowchart for the withdrawal logic useful, even though you could just "figure it out while coding"?
✅ **Answer:** A flowchart forces you to consider ALL the edge cases (insufficient balance, high-value OTP requirement) BEFORE writing code, rather than discovering them halfway through implementation and having to restructure everything.

---

### 3️⃣ Modular OOP-Based Architecture

Now we design the actual classes — applying the SAME "does this deserve a class?" checklist from earlier OOP topics.

| Concept | Design Choice | Why |
|---|---|---|
| `User` | Class | Has state (name, credentials) and behavior (login) |
| `Account` | Class | Has state (balance) and behavior (deposit, withdraw) — core of the whole system |
| `SavingsAccount`, `CurrentAccount` | Inherit from `Account` | Genuine is-a relationship, with different interest/withdrawal rules |
| `Transaction` | Class (or `dataclass`) | Represents a record — mostly data, but meaningful as its own type |
| `AuthService` | Class | Groups login/registration behavior together (has-a `User` list) |
| `Validators` | Plain functions | Pure logic, no state — a class would add nothing here |

```python
class User:
    def __init__(self, name, phone, email, password_hash):
        self.name = name
        self.phone = phone
        self.email = email
        self._password_hash = password_hash    # encapsulated — never store raw passwords!

    def check_password(self, password_hash):
        return self._password_hash == password_hash


class Account:                          # PARENT class
    def __init__(self, account_number, owner: User, balance=0.0):
        self.account_number = account_number
        self.owner = owner                # Account HAS-A User (composition)
        self._balance = balance
        self.transactions = []             # Account HAS-A list of Transactions

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount


class SavingsAccount(Account):           # SavingsAccount IS-A Account
    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.04):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


class CurrentAccount(Account):            # CurrentAccount IS-A Account
    def __init__(self, account_number, owner, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):            # OVERRIDES parent — different rule!
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit")
        self._balance -= amount
```

**Where inheritance is justified vs. not:**

```
        Account (parent)
           ▲        ▲
           │        │
   SavingsAccount  CurrentAccount
   (interest,      (overdraft,
    no overdraft)   no interest)
```

> 💡 **Tip**
>
> `SavingsAccount` and `CurrentAccount` genuinely override `withdraw()`/add unique behavior — this is a textbook case where inheritance is EARNED, not forced.

🤔 **Quick thinking question:** Why does `Account` store `self.owner` as a `User` OBJECT rather than just storing the owner's name as a string?
✅ **Answer:** Storing the actual `User` object (composition/has-a) means the account always has access to the FULL, up-to-date user data (phone, email, password) — if you only stored a name string, you'd have no way to verify identity or contact the account holder for OTPs.

---

### 4️⃣ Secure Authentication

Every banking system needs to verify: "Are you really who you say you are?" This project covers TWO layers:

**Layer 1 — Password-based login (always required):**

```python
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()     # NEVER store raw passwords!

class AuthService:
    def __init__(self):
        self.users = {}     # phone -> User

    def register(self, name, phone, email, password):
        if phone in self.users:
            raise ValueError("User already registered with this phone number")
        user = User(name, phone, email, hash_password(password))
        self.users[phone] = user
        return user

    def login(self, phone, password):
        user = self.users.get(phone)
        if user is None or not user.check_password(hash_password(password)):
            raise ValueError("Invalid phone number or password")
        return user
```

**Layer 2 — Optional OTP verification for sensitive operations (large withdrawals, transfers):**

```python
import random

class OTPService:
    def __init__(self):
        self._pending_otps = {}     # phone -> otp code

    def generate_otp(self, phone) -> str:
        otp = str(random.randint(100000, 999999))
        self._pending_otps[phone] = otp
        # In a real system: send via Gmail SMTP or Fast2SMS here
        print(f"📩 [SIMULATED SMS] Your OTP is: {otp}")
        return otp

    def verify_otp(self, phone, entered_otp) -> bool:
        actual_otp = self._pending_otps.get(phone)
        if actual_otp == entered_otp:
            del self._pending_otps[phone]      # OTP used only once
            return True
        return False
```

**Sending a REAL OTP via Gmail SMTP (optional, for a real deployment):**

```python
import smtplib
from email.mime.text import MIMEText

def send_otp_email(receiver_email, otp, sender_email, sender_app_password):
    message = MIMEText(f"Your banking OTP is: {otp}")
    message["Subject"] = "Your OTP Code"
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_app_password)     # use an App Password, not your real password!
        server.sendmail(sender_email, receiver_email, message.as_string())
```

> ⚠️ **Important**
>
> NEVER store plain-text passwords — always hash them. And NEVER hardcode your real Gmail password in code — Gmail requires a separate **App Password** for SMTP access, which should be kept in an environment variable, not committed to your code.

🤔 **Quick thinking question:** Why does `verify_otp()` delete the OTP from `_pending_otps` immediately after a successful match?
✅ **Answer:** To ensure each OTP can only be used ONCE — if it stayed stored, someone who intercepted an old OTP could potentially reuse it later for an unauthorized transaction.

**Is a decorator appropriate here? — Yes, and this is a genuine real-world pattern.**

This is called **"step-up authentication"** in the industry: a user is already logged in, but a SPECIFIC sensitive action requires ONE MORE verification step before it's allowed to run. Real systems implement this as middleware/decorators — e.g., Stripe's "3D Secure" step-up flow, or Django views wrapped in a custom `@requires_step_up_auth`. It's structurally the SAME pattern as the `@requires_permission` decorator from the earlier RBAC mini-project — just checking "was OTP verified?" instead of "does this role have permission?"

```python
from functools import wraps

def requires_otp(threshold=10000):
    """Decorator FACTORY (accepts its own argument, like @requires_permission did)."""
    def decorator(func):
        @wraps(func)
        def wrapper(account, amount, otp_service, phone, entered_otp=None, *args, **kwargs):
            if amount > threshold:
                if entered_otp is None:
                    raise InvalidOTPError("OTP required for this amount, but none was provided")
                if not otp_service.verify_otp(phone, entered_otp):
                    raise InvalidOTPError("OTP verification failed")
            return func(account, amount, *args, **kwargs)
        return wrapper
    return decorator


@requires_otp(threshold=10000)
def withdraw(account, amount):
    account.withdraw(amount)


# Usage — the OTP check happens BEFORE withdraw() ever runs:
withdraw(my_account, 15000, otp_service=otp_service, phone="9876543210", entered_otp="482913")
```

Notice `withdraw()` itself contains ZERO security-checking code — exactly the "separation of concerns" benefit from the RBAC project. The core banking logic (`account.withdraw(amount)`) stays completely clean; the decorator handles the security layer separately, and can be reused on `transfer()` too without duplicating the OTP logic.

| Without decorator | With `@requires_otp` decorator |
|---|---|
| OTP check written manually inside every sensitive function | OTP check written ONCE, applied to any function with one line |
| Easy to forget the check on a new function | New sensitive functions are automatically protected just by adding `@requires_otp` |
| Business logic and security logic mixed together | Business logic and security logic cleanly separated |

> ⚠️ **Important**
>
> Don't reach for a decorator just because it's possible — the earlier `try/except` version of `withdraw_with_otp()` works fine too, and is arguably easier to read for a smaller project. Use the decorator once you have MULTIPLE functions (withdraw, transfer, close_account) that all need the SAME OTP rule — that's when the reuse actually pays off.

🤔 **Quick thinking question:** Why does `@requires_otp(threshold=10000)` need to be a "decorator factory" (three nested function layers) instead of a plain two-layer decorator?
✅ **Answer:** Because it needs to accept its OWN configuration argument (`threshold`) before it can wrap a function — the outer layer captures `threshold` via closure, exactly like `@repeat(times=3)` needed an extra layer in the earlier decorators topic.

---

### 5️⃣ Robust Input Validation (Regex)

Just like the earlier regex topic, every piece of user input needs validation BEFORE it's trusted.

```python
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
```

**Using these during registration, with clear feedback:**

```python
def get_valid_input(prompt, validator, error_message):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(f"❌ {error_message}")

name = get_valid_input("Enter name: ", is_valid_name, "Name must contain only letters and spaces.")
phone = get_valid_input("Enter phone: ", is_valid_phone, "Phone must be a valid 10-digit Indian number.")
```

> 💡 **Tip**
>
> Centralizing validation into small, reusable functions (like in the `Validators` module) means you write each rule ONCE and reuse it everywhere — registration, profile updates, transfers all use the SAME phone/email validators.

🤔 **Quick thinking question:** Why is `get_valid_input()` written as a reusable helper function instead of repeating the same `while True` loop for every field?
✅ **Answer:** It avoids duplicating the same "keep asking until valid" logic for name, phone, and email separately — any improvement to how validation errors are shown only needs to be made in ONE place.

---

### 6️⃣ Console UI Enhancements (Color-Coded Feedback)

A plain black-and-white console is hard to read quickly. Using ANSI color codes (or the `colorama` library for cross-platform support) makes success/failure instantly recognizable.

```python
from colorama import Fore, Style, init
init(autoreset=True)      # ensures colors reset after each print automatically

def print_success(message):
    print(Fore.GREEN + "✅ " + message)

def print_error(message):
    print(Fore.RED + "❌ " + message)

def print_info(message):
    print(Fore.CYAN + "ℹ️  " + message)

print_success("Deposit successful!")
print_error("Insufficient balance!")
print_info("Please enter your OTP.")
```

**A reusable menu formatter for clean navigation:**

```python
def print_menu(title, options):
    print(Fore.YELLOW + f"\n===== {title} =====")
    for key, label in options.items():
        print(f"{key}. {label}")
    print(Fore.YELLOW + "=" * (len(title) + 12))

print_menu("BANKING MENU", {
    "1": "Deposit",
    "2": "Withdraw",
    "3": "Transfer",
    "4": "View Statement",
    "0": "Logout"
})
```

| Color | Typically Used For |
|---|---|
| 🟢 Green | Success messages (deposit successful, login successful) |
| 🔴 Red | Errors (insufficient balance, invalid OTP) |
| 🟡 Yellow | Menu headers, warnings |
| 🔵 Cyan | Informational prompts |

> ⚠️ **Important**
>
> Install `colorama` with `pip install colorama` before using it — and always call `init(autoreset=True)` once at the start of your program, or colors may "bleed" into later text on some terminals.

🤔 **Quick thinking question:** Why is `autoreset=True` important when using `colorama`?
✅ **Answer:** Without it, once you print colored text, the color would continue applying to ALL subsequent output until manually reset — `autoreset=True` automatically resets the color after each `print()` statement, preventing this bleed-over effect.

---

### 7️⃣ Persistent Storage

Without saving data to files, all users/accounts/transactions vanish the moment the program closes. This project uses **JSON files** for structured, human-readable persistence.

```python
import json
import os

DATA_FILE = "accounts.json"

def save_accounts(accounts: dict):
    data = {
        acc_no: {
            "owner_name": acc.owner.name,
            "balance": acc.balance,
            "type": type(acc).__name__
        }
        for acc_no, acc in accounts.items()
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_accounts() -> dict:
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)
```

**Appending each transaction to a daily log file (never overwritten — always appended):**

```python
from datetime import datetime

def log_transaction(account_number, action, amount):
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"transactions_{today}.log"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:                 # "a" = append, never erase history!
        file.write(f"{timestamp} | Account: {account_number} | {action}: ₹{amount}\n")

log_transaction("ACC1001", "DEPOSIT", 5000)
log_transaction("ACC1001", "WITHDRAW", 2000)
```

This creates a new log file EACH DAY (`transactions_2026-08-16.log`), keeping a clean, organized, permanent history.

> 💡 **Tip**
>
> Using `"a"` (append) mode for logs and `"w"` (write) mode for the "current state" snapshot (`accounts.json`) is a deliberate choice — you want FULL transaction HISTORY preserved, but only the LATEST account balances saved.

🤔 **Quick thinking question:** Why does the transaction log use a NEW file for each day (`transactions_2026-08-16.log`), rather than one single giant log file forever?
✅ **Answer:** Daily log files keep each file a manageable size and make it much easier to find/review transactions from a SPECIFIC day, rather than searching through one massive, ever-growing file — this is standard practice in real production logging.

---

### 8️⃣ Exception & Error Handling

Every risky operation — deposits, withdrawals, file access, OTP verification — must be wrapped safely.

**Custom exceptions for banking-specific errors:**

```python
class BankingError(Exception):          # base exception for the whole app
    pass

class InsufficientBalanceError(BankingError):
    pass

class InvalidOTPError(BankingError):
    pass

class AccountNotFoundError(BankingError):
    pass
```

**Using them throughout the system:**

```python
def withdraw_with_otp(account, amount, otp_service, phone, entered_otp=None):
    try:
        if amount > 10000:
            if entered_otp is None or not otp_service.verify_otp(phone, entered_otp):
                raise InvalidOTPError("OTP verification failed for high-value withdrawal")
        account.withdraw(amount)
    except InsufficientBalanceError as e:
        print_error(f"Withdrawal failed: {e}")
    except InvalidOTPError as e:
        print_error(f"Security check failed: {e}")
    else:
        print_success(f"₹{amount} withdrawn successfully!")
        log_transaction(account.account_number, "WITHDRAW", amount)
    finally:
        print_info("Withdrawal attempt finished.")
```

> ⚠️ **Important**
>
> Custom exceptions like `InsufficientBalanceError` make the CODE and LOGS far more readable than generic `ValueError`s — anyone reviewing a log file instantly understands what went wrong.

🤔 **Quick thinking question:** Why does this project define a `BankingError` base exception, with `InsufficientBalanceError` and `InvalidOTPError` inheriting from it?
✅ **Answer:** This lets code catch EITHER a specific error type (e.g., just `InsufficientBalanceError`) OR any banking-related error generically (using `except BankingError`), giving flexibility depending on how precisely the calling code needs to react.

---

### 9️⃣ Outcomes

By the end of this 10-day project, you will have personally taken a system from a blank page through the FULL real-world lifecycle:

```
   Requirements  →  Flowcharts  →  Class Design  →  Coding  →  Testing  →  Delivery
        │                │              │              │           │            │
   "what should      "how should    "which classes  "actual    "does it     "final,
   it do?"           it flow?"       do we need?"    code"      work?"       working app"
```

You'll walk away with a genuinely **portfolio-worthy project** demonstrating: OOP design, security awareness, input validation, clean UX, persistence, and professional error handling — all in pure Python, no external frameworks required.

🤔 **Quick thinking question:** Why is "testing" listed as its own distinct stage, separate from "coding"?
✅ **Answer:** Writing code that COMPILES/RUNS is not the same as writing code that WORKS CORRECTLY for all realistic scenarios — dedicated testing (trying edge cases, invalid inputs, boundary values) is what actually verifies the system behaves correctly, and skipping it is how bugs reach real users.

---

### 🔟 Suggested Project Structure

Following the SAME `models / services / repositories` split used in the earlier Society Management project — this is a real, reusable pattern, not something specific to one project.

```
banking_system/
│
├── main.py                      # CLI entry point — menu loop only, no business logic
│
├── models/
│   ├── __init__.py
│   ├── user.py                  # User class
│   ├── account.py                # Account, SavingsAccount, CurrentAccount
│   └── transaction.py             # Transaction dataclass
│
├── services/
│   ├── auth_service.py            # register(), login(), password hashing
│   ├── otp_service.py              # generate_otp(), verify_otp(), @requires_otp decorator
│   ├── transaction_service.py       # deposit(), withdraw(), transfer()
│   └── validators.py                  # is_valid_name, is_valid_phone, is_valid_email, is_valid_amount
│
├── repositories/
│   └── account_repository.py       # save_accounts(), load_accounts() — the ONE place that touches accounts.json
│
├── ui/
│   └── console.py                  # print_success/print_error/print_info, print_menu, colorama setup
│
├── exceptions.py                    # BankingError, InsufficientBalanceError, InvalidOTPError, AccountNotFoundError
│
├── data/
│   ├── accounts.json                # current snapshot of all accounts (overwritten each save)
│   └── logs/
│       ├── transactions_2026-08-16.log
│       └── transactions_2026-08-17.log
│
└── requirements.txt                  # colorama, etc.
```

| Folder | Responsibility | Matches earlier topic |
|---|---|---|
| `models/` | Pure state — `User`, `Account` hierarchy, `Transaction` | Society project's `models/` |
| `services/` | All behavior — auth, OTP, deposit/withdraw/transfer logic, validators | Society project's `services/` |
| `repositories/` | The ONLY code that reads/writes `accounts.json` | Society project's `repositories/` |
| `ui/` | Console-only concerns — colors, menu formatting, input prompts | New here — banking project has more UI than the society one did |
| `exceptions.py` | Custom exception hierarchy, used across services | From the Logging & Exceptions topic |
| `data/logs/` | Daily append-only transaction logs | From the File Handling topic |

> 💡 **Tip**
>
> `main.py` should be as "dumb" as possible — just showing menus and calling `services/` functions, exactly like `cli.py` was in the Society Management project. If you find yourself writing `if balance < amount` directly inside `main.py`, that logic has leaked out of `services/` and should be moved back.

🤔 **Quick thinking question:** Why does `otp_service.py` live in `services/` rather than `models/`, even though `OTPService` is a class with its own state (`_pending_otps`)?
✅ **Answer:** Because `OTPService` represents an OPERATION/PROCESS (generating and checking time-limited codes), not a persistent domain entity like `User` or `Account` — the `models/` vs `services/` split is about "state that represents the business domain" vs. "logic that acts on that state," and OTP generation is squarely the latter.

---

## 💡 Real-Life Analogy

* 🏦 **The Whole Project → Building an Actual Bank Branch** — You wouldn't start construction (coding) without architectural blueprints (flowcharts) and a clear list of what the branch needs to do (requirements) first.
* 🔐 **Password + OTP → A Bank Locker with Two Keys** — Your password is YOUR key, always required. The OTP is like a SECOND key held by the bank, only needed for high-value/sensitive actions — both keys must turn together.
* 📝 **File-Based Logging → A Bank's Physical Transaction Ledger** — Every action is written down permanently in daily pages (log files), never erased, so there's always a complete, honest paper trail to look back on.
* 🚦 **Color-Coded CLI → Traffic Lights at a Bank Kiosk** — Green means "proceed, all good," red means "stop, something's wrong" — instantly understandable without reading every word.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| OOP account hierarchy | Core banking systems (Finacle, used by many Indian banks) model Savings/Current/Loan accounts similarly |
| OTP-based security | Every UPI app (PhonePe, Google Pay), net banking portal |
| Regex validation | Every bank's signup/KYC form |
| JSON/file persistence | Smaller fintech tools, internal admin dashboards, config-driven systems |
| Custom exceptions | Payment gateway SDKs (Razorpay, Stripe) use domain-specific exceptions extensively |
| Color-coded CLI | DevOps and admin tools (like AWS CLI, git) use colored output for the same clarity reasons |

---

## 🔍 Industry Example

**Scenario:** A **graduate trainee developer** joins a fintech company and is assigned to build an internal **"mini-ledger" tool** for the operations team to manually adjust customer balances during support escalations.

1. Before writing code, they sit with the operations team to **gather requirements**: what actions are needed, what security is required, what should be logged.
2. They sketch a **flowchart** for the "manual balance adjustment" flow, including a mandatory OTP step for any adjustment above a threshold — exactly like the withdrawal flow in this project.
3. They design classes mirroring `User`, `Account`, `Transaction` — using **inheritance** only where account types genuinely behave differently, and composition everywhere else.
4. All operator inputs (customer ID, amount, reason) are validated with **regex** before processing.
5. Every adjustment is both **saved to a JSON snapshot** (current state) and **appended to a daily audit log** — because financial tools require a permanent, unmodifiable history for compliance.
6. **Custom exceptions** (`InsufficientBalanceError`, `InvalidOTPError`) ensure operators get clear, specific error messages instead of confusing generic Python tracebacks.
7. The finished tool goes through **dedicated testing** (trying invalid inputs, boundary amounts, wrong OTPs) before being handed over to the operations team — mirroring the "testing → delivery" stages of this very project.

This exact workflow — from requirements to a tested, delivered tool — is standard practice in real fintech engineering teams, even for "small" internal tools.

---

## 📊 Diagram

```
                CLI BANKING SYSTEM — ARCHITECTURE OVERVIEW
                ---------------------------------------------

    AuthService  ──has-a──►  User (many)
         │
         ▼
    login/register (password hashing)


    User  ──has-a (via Account.owner)──►  Account (parent class)
                                              ▲        ▲
                                     is-a │            │ is-a
                                   SavingsAccount   CurrentAccount

    Account  ──has-a──►  Transaction (many)


    Sensitive operation (withdraw > ₹10,000)
              │
              ▼
       OTPService.generate_otp()  ──►  (SMS/Email sent)
              │
              ▼
       OTPService.verify_otp()  ──Fail──► ❌ InvalidOTPError
              │Success
              ▼
       Account.withdraw()  ──►  log_transaction()  ──►  save_accounts()


         PROJECT LIFECYCLE (applied across 10 days)
         ----------------------------------------------
    Requirements → Flowcharts → Class Design → Build → Test → Deliver


         @requires_otp DECORATOR — WHERE IT SITS
         -------------------------------------------
    withdraw(amount=15000)
           │
           ▼
    @requires_otp(threshold=10000)   ← intercepts the call FIRST
           │
      amount > threshold?
           │
        ┌──┴──┐
        ▼       ▼
      Yes       No
        │        └──────────────► run withdraw() directly
        ▼
   verify_otp()
        │
    ┌───┴───┐
    ▼         ▼
  Valid     Invalid
    │         └──► ❌ InvalidOTPError, withdraw() NEVER runs
    ▼
  run withdraw()
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "I can start coding immediately and figure out the design as I go."
  ✅ **Correct:** Planning requirements and flowcharts FIRST prevents costly restructuring later — this is standard professional practice, not extra busywork.

* ❌ **Wrong belief:** "It's fine to store passwords as plain text since this is just a practice project."
  ✅ **Correct:** ALWAYS hash passwords, even in practice projects — building the habit now prevents serious security mistakes later in real jobs.

* ❌ **Wrong belief:** "`SavingsAccount` and `CurrentAccount` should just be flags/fields on one `Account` class instead of separate classes."
  ✅ **Correct:** Since they genuinely have DIFFERENT behavior (interest vs. overdraft, different withdrawal rules), separate classes via inheritance is the more appropriate, and more extensible, design.

* ❌ **Wrong belief:** "Using `\"w\"` mode for the transaction log file is fine, since it's simpler."
  ✅ **Correct:** `\"w\"` mode would ERASE the entire transaction history every time the program restarts — always use `\"a\"` (append) mode for logs.

* ❌ **Wrong belief:** "Generic Python exceptions like `ValueError` are good enough for a banking system."
  ✅ **Correct:** Custom exceptions like `InsufficientBalanceError` make both the CODE and any LOGS/audit trails far clearer about exactly what went wrong.

* ❌ **Wrong belief:** "Since decorators are powerful, I should wrap EVERY function in this project with one, including simple things like `view_statement()`."
  ✅ **Correct:** Reach for a decorator only when the SAME cross-cutting rule (like OTP checking) needs to apply to MULTIPLE functions — wrapping something with no real security/logging need adds indirection without any benefit.

---

## 💬 Interview Corner

**Q1: Why is requirement gathering and flowchart planning done BEFORE writing any code in a real software project?**
✅ It surfaces edge cases, missing requirements, and design flaws EARLY — when they're cheap to fix — instead of discovering them after significant code has already been written, which is far more expensive to restructure.

**Q2: In this banking project, where is inheritance genuinely justified, and where would it be overkill?**
✅ Justified: `SavingsAccount`/`CurrentAccount` inheriting from `Account`, since they have real, divergent behavior. Overkill: creating separate classes for things like "phone validator" or "email validator" — those are simple, stateless functions, not classes needing inheritance.

**Q3: Why should sensitive operations like large withdrawals require OTP verification IN ADDITION TO the initial login?**
✅ Login proves identity ONCE at the start of a session; OTP verification adds a SECOND, time-limited check specifically for high-risk actions, protecting against situations where a session might be compromised or misused after login.

**Q4: Why use JSON for storing account data instead of a plain text file with comma-separated values?**
✅ JSON preserves STRUCTURE (nested data, clear key-value labeling) in a way that's both human-readable and easy to reliably parse back into Python objects using the built-in `json` module — plain CSV-style text would require writing fragile custom parsing logic.

**Q5: Is using a decorator for OTP verification a "real" pattern, or just a classroom exercise?**
✅ It's real — it's an example of "step-up authentication," where an already-logged-in user must pass ONE MORE check before a specific sensitive action is allowed. Production systems (payment gateways, banking backends) implement this exact idea as middleware or decorators wrapping only the endpoints/functions that need it, keeping the core business logic free of security-checking code.

---

## 📝 Quick Summary

* 🏦 This capstone project combines OOP, security, validation, persistence, and error handling into one complete banking system
* 🪜 Real software follows a lifecycle: requirements → flowcharts → class design → coding → testing → delivery — plan BEFORE coding
* 🧩 `Account` is the core class; `SavingsAccount`/`CurrentAccount` inherit from it ONLY because they have genuinely different behavior
* 🔐 Passwords are always hashed; sensitive actions (large withdrawals/transfers) get an additional OTP layer
* ✅ Regex validates names, phone numbers, and emails consistently across the whole app using shared, reusable functions
* 🎨 Color-coded CLI output (green=success, red=error, yellow=menu) makes the interface far easier to use
* 💾 Account snapshots use `"w"` mode (latest state); transaction logs use `"a"` mode (full history, never erased)
* 🚨 Custom exceptions (`InsufficientBalanceError`, `InvalidOTPError`) built on a shared `BankingError` base keep error handling clear and specific
* 🎭 `@requires_otp(threshold=...)` is a real "step-up authentication" pattern — reach for it once MULTIPLE functions need the same OTP rule, not before
* 🗂️ A `models / services / repositories / ui` project structure keeps state, behavior, storage, and console concerns cleanly separated
* 🎯 The final outcome is a genuinely professional, portfolio-ready project demonstrating the full real-world software development process

---

## 🎯 Class Activity

**"Plan Before You Build" 🏗️**

Since this project spans multiple days, today's activity is entirely about STAGE 1-2 of the lifecycle:

1. Write out a full requirements list (in plain English) for the banking system, covering at minimum: registration, login, deposit, withdrawal, transfer, and viewing a statement.
2. Draw a flowchart (on paper or using any diagramming tool) for the "money transfer between two accounts" flow, including what happens if the sender has insufficient balance.
3. List out every class you believe the system needs, and for each one, write one sentence justifying WHY it deserves to be a class (using the checklist from earlier OOP topics).
4. Identify which of your planned classes should use inheritance, and explain the genuine "is-a" relationship that justifies it.
5. Bonus: Sketch the exact folder/file structure you'll use to organize this project (similar to the `models/`, `services/`, `repositories/` structure from earlier projects).


---

# 📋 Assignments — Major Project — CLI-Based Banking System

| Assignment |
|---|
| Write the complete requirements list AND a flowchart for the full banking system (registration, login, deposit, withdrawal, transfer, statement view) before writing any code. |
| Implement the `User`, `Account`, `SavingsAccount`, and `CurrentAccount` classes exactly as outlined, and test creating both account types with different behaviors. |
| Build the `AuthService` class with `register()` and `login()` methods, including password hashing, and test both successful and failed login attempts. |
| Implement the `OTPService` class with `generate_otp()` and `verify_otp()`, and simulate a full high-value withdrawal flow requiring OTP confirmation. |
| Write all four validator functions (`is_valid_name`, `is_valid_phone`, `is_valid_email`, `is_valid_amount`) and test each with at least 3 valid and 3 invalid examples. |
| Install `colorama` and build the `print_success`, `print_error`, and `print_info` helper functions, using them throughout a simple test menu. |
| Implement `save_accounts()` and `load_accounts()` using JSON, and confirm that account data survives a program restart. |
| Implement `log_transaction()` using daily-dated append-mode log files, and generate at least 5 log entries across "different days" (you can fake the date for testing). |
| Create the custom exception hierarchy (`BankingError`, `InsufficientBalanceError`, `InvalidOTPError`, `AccountNotFoundError`) and use each one in an appropriate place in your code. |
| Build a complete `withdraw_with_otp()` function (as shown in this topic) and test it with: a normal small withdrawal, a large withdrawal with correct OTP, and a large withdrawal with incorrect OTP. |
| Rewrite `withdraw_with_otp()` as a `@requires_otp(threshold=10000)` decorator instead, and apply it to BOTH `withdraw()` and `transfer()` — confirm the OTP rule now protects both without duplicating any code. |
| Set up the full `models/ services/ repositories/ ui/` folder structure shown in this topic, and move your existing code into the correct files — confirm the project still runs after the reorganization. |
| Design and implement a full menu-driven `main()` loop that ties together registration, login, deposit, withdrawal, transfer, and viewing a statement. |
| Add a `transfer_money(from_account, to_account, amount)` function that safely moves money between two accounts, using proper exception handling if the transfer fails partway through. |
| Test your entire system end-to-end: register 2 users, open accounts for both, transfer money between them, and confirm both the JSON snapshot and the daily log file reflect the correct final state. |
| Write a one-page "Test Report" (as a markdown or text file) listing at least 10 test cases you ran (valid and invalid), and whether each passed or failed. |
| Write a short reflection (5–8 sentences) on how this project's lifecycle (planning → coding → testing) differed from how you approached earlier, smaller projects in this course. |