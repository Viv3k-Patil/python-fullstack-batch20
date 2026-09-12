# CLI Banking System — Student Instructions

## 🔹 How to use this document

You are going to build a banking application **step by step**.

Do not copy the final project from somewhere else.

Do not jump to later phases.

At every phase:

1. Read the objective.
2. Create/change only what the phase asks for.
3. Run the application.
4. Test the behavior.
5. Complete the checkpoint.
6. Only then move to the next phase.

The project is intentionally built in small steps.

The most important rule is:

> **When the current code becomes difficult, do not be afraid of the difficulty. That difficulty is what tells us what concept we need next.**

---

---

## 🔹 Table of Contents & Progress Tracker

Use this as your map. Click a link to jump to a phase (in viewers that support markdown anchors, e.g. VS Code, Obsidian, GitHub). If a link doesn't jump correctly in your viewer, just search the page for the phase title.

Check a box only when you've actually completed that phase's checkpoint below — not before. The checkboxes here are clickable in most markdown editors, so this list doubles as your live progress tracker.

- [ ] [Phase 1 — Create the Project](#phase-1--create-the-project)
- [ ] [Phase 2 — Store the Balance](#phase-2--store-the-balance)
- [ ] [Phase 3 — Get Input from the User](#phase-3--get-input-from-the-user)
- [ ] [Phase 4 — Add Decisions](#phase-4--add-decisions)
- [ ] [Phase 5 — Create a Banking Menu](#phase-5--create-a-banking-menu)
- [ ] [Phase 6 — Connect the Menu to Banking Operations](#phase-6--connect-the-menu-to-banking-operations)
- [ ] [Phase 7 — Refactor into Functions](#phase-7--refactor-into-functions)
- [ ] [Phase 8 — Represent an Account](#phase-8--represent-an-account)
- [ ] [Phase 9 — Support Multiple Accounts](#phase-9--support-multiple-accounts)
- [ ] [Phase 10 — Add Transfer](#phase-10--add-transfer)
- [ ] [Phase 11 — Create the Account Class](#phase-11--create-the-account-class)
- [ ] [Phase 12 — Move Behavior into Account](#phase-12--move-behavior-into-account)
- [ ] [Phase 13 — Create the Bank Class](#phase-13--create-the-bank-class)
- [ ] [Phase 14 — Move Transfer into Bank](#phase-14--move-transfer-into-bank)
- [ ] [Phase 15 — Add Savings and Current Accounts](#phase-15--add-savings-and-current-accounts)
- [ ] [Phase 16 — Add Different Account Behavior](#phase-16--add-different-account-behavior)
- [ ] [Phase 17 — Create the User Model](#phase-17--create-the-user-model)
- [ ] [Phase 18 — Add Transactions](#phase-18--add-transactions)
- [ ] [Phase 19 — Organize the Project into Packages](#phase-19--organize-the-project-into-packages)
- [ ] [Phase 20 — Move Models into Their Own Files](#phase-20--move-models-into-their-own-files)
- [ ] [Phase 21 — Add Custom Exceptions](#phase-21--add-custom-exceptions)
- [ ] [Phase 22 — Create the Validation Service](#phase-22--create-the-validation-service)
- [ ] [Phase 23 — Create a Reusable Input Helper](#phase-23--create-a-reusable-input-helper)
- [ ] [Phase 24 — Create Authentication](#phase-24--create-authentication)
- [ ] [Phase 25 — Create the Transaction Service](#phase-25--create-the-transaction-service)
- [ ] [Phase 26 — Add JSON Persistence](#phase-26--add-json-persistence)
- [ ] [Phase 27 — Add Serialization](#phase-27--add-serialization)
- [ ] [Phase 28 — Save Accounts](#phase-28--save-accounts)
- [ ] [Phase 29 — Load Accounts](#phase-29--load-accounts)
- [ ] [Phase 30 — Rehydrate Account Objects](#phase-30--rehydrate-account-objects)
- [ ] [Phase 31 — Save and Load Users](#phase-31--save-and-load-users)
- [ ] [Phase 32 — Create Application Bootstrap](#phase-32--create-application-bootstrap)
- [ ] [Phase 33 — Persist Before Exit](#phase-33--persist-before-exit)
- [ ] [Phase 34 — Add Transaction Logs](#phase-34--add-transaction-logs)
- [ ] [Phase 35 — Add Account Statements](#phase-35--add-account-statements)
- [ ] [Phase 36 — Generate Account Numbers](#phase-36--generate-account-numbers)
- [ ] [Phase 37 — Create the Registration Flow](#phase-37--create-the-registration-flow)
- [ ] [Phase 38 — Create the Login Flow](#phase-38--create-the-login-flow)
- [ ] [Phase 39 — Restrict Users to Their Own Accounts](#phase-39--restrict-users-to-their-own-accounts)
- [ ] [Phase 40 — Create the Open Account Flow](#phase-40--create-the-open-account-flow)
- [ ] [Phase 41 — Build the Deposit Flow](#phase-41--build-the-deposit-flow)
- [ ] [Phase 42 — Build the Withdrawal Flow](#phase-42--build-the-withdrawal-flow)
- [ ] [Phase 43 — Build the Transfer Flow](#phase-43--build-the-transfer-flow)
- [ ] [Phase 44 — Add OTP Service](#phase-44--add-otp-service)
- [ ] [Phase 45 — Verify OTP](#phase-45--verify-otp)
- [ ] [Phase 46 — Define the OTP Threshold](#phase-46--define-the-otp-threshold)
- [ ] [Phase 47 — Introduce Decorators](#phase-47--introduce-decorators)
- [ ] [Phase 48 — Create Console UI Helpers](#phase-48--create-console-ui-helpers)
- [ ] [Phase 49 — Add `colorama`](#phase-49--add-colorama)
- [ ] [Phase 50 — Create the Logged-In Menu](#phase-50--create-the-logged-in-menu)
- [ ] [Phase 51 — Create the Final Main Menu](#phase-51--create-the-final-main-menu)
- [ ] [Phase 52 — Final Project Structure](#phase-52--final-project-structure)
- [ ] [Phase 53 — End-to-End Testing](#phase-53--end-to-end-testing)
- [ ] [Phase 54 — Error Testing](#phase-54--error-testing)
- [ ] [Phase 55 — Code Quality Check](#phase-55--code-quality-check)
- [ ] [Phase 56 — Final Conceptual Revision](#phase-56--final-conceptual-revision)
- [ ] [Phase 57 — The Story You Should Remember](#phase-57--the-story-you-should-remember)
- [ ] [Final Submission Checklist](#final-submission-checklist)
- [ ] [Final Challenge](#final-challenge)

---

# 🐣 Phase 1 — Create the Project

📄 **File for this phase:** `main.py`

## 🎯 Objective

Create the smallest possible Python application.

## 🔧 Step 1 — Create the project folder

Create a folder named:

```text
banking_app
```

Inside it create:

```text
main.py
```

Your project should look like:

```text
banking_app/
└── main.py
```

## 🔧 Step 2 — Add your first Python code

Open `main.py`.

Write:

```python
print("Welcome to Simple Bank")
```

## 🔧 Step 3 — Run the program

Open a terminal inside the project folder.

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run:

```bash
python main.py
```

Expected output:

```text
Welcome to Simple Bank
```

## 🔹 What did you learn?

You created a Python program and executed it.

Python starts reading the file from the top and executes the instructions.

## 🔹 Your task

Change the message to:

```text
Welcome to My Banking System
```

Run it again.

## ✅ Checkpoint

You should be able to explain:

- What is `main.py`?
- What does `print()` do?
- How do you run a Python file?

### 🚦 Do not move ahead until

- [ ] `main.py` exists.
- [ ] The program runs.
- [ ] You understand that Python executes the file from top to bottom.

---

# 🐣 Phase 2 — Store the Balance

📄 **File for this phase:** `main.py`

## 🎯 Objective

Introduce variables.

A bank needs to remember a balance.

## 🔧 Step 1

Replace your code with:

```python
balance = 1000

print("Welcome to Simple Bank")
print(f"Your balance is: {balance}")
```

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run:

```bash
python main.py
```

Expected:

```text
Welcome to Simple Bank
Your balance is: 1000
```

## 🔧 Step 2 — Deposit money

Add:

```python
balance = balance + 500
```

Then:

```python
print(f"Your balance is: {balance}")
```

Expected:

```text
Your balance is: 1500
```

## 🔧 Step 3 — Withdraw money

Add:

```python
balance = balance - 200
```

Expected final balance:

```text
1300
```

## 🧪 Exercise

Try:

```python
balance += 100
```

Then:

```python
balance -= 50
```

Understand that:

```python
balance += 100
```

means:

```python
balance = balance + 100
```

## ✅ Checkpoint

Answer:

1. What is a variable?
2. What value is stored in `balance`?
3. What is the difference between `=` and `+=`?

### 🚦 Do not move ahead until

- [ ] You can create a variable.
- [ ] You can update a variable.
- [ ] You understand that the balance changes while the program is running.

---

# 🐣 Phase 3 — Get Input from the User

📄 **File for this phase:** `main.py`

## 🎯 Objective

Stop hard-coding everything.

The user should decide how much money to deposit.

## 🔧 Step 1 — Try `input()`

Write:

```python
name = input("What is your name? ")

print(f"Hello {name}")
```

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run it.

Enter your name.

## 🔧 Step 2 — Ask for a deposit

Write:

```python
amount = input("How much do you want to deposit? ")

print(f"You entered {amount}")
```

## ⚠️ Important

`input()` gives you text.

Therefore:

```python
amount = input(...)
```

does not automatically give you a number.

Convert it:

```python
amount = float(input("How much do you want to deposit? "))
```

## 🔧 Step 3 — Update the balance

```python
balance = 1000

amount = float(
    input("How much do you want to deposit? ")
)

balance += amount

print(f"New balance: {balance}")
```

## 🧪 Exercise

Try entering:

```text
500
```

Then:

```text
1250
```

Then:

```text
99.50
```

## ✅ Checkpoint

Understand:

```text
input()
   ↓
text
   ↓
float()
   ↓
number
```

### 🚦 Do not move ahead until

- [ ] You can read input.
- [ ] You understand that `input()` returns text.
- [ ] You know why `float()` is required for monetary input in this simple version.

---

# 🐣 Phase 4 — Add Decisions

📄 **File for this phase:** `main.py`

## 🎯 Objective

The user should choose what the application does.

Introduce `if`.

## 🔧 Step 1

Write:

```python
choice = input(
    "Do you want to deposit? "
)

if choice == "yes":
    print("Deposit selected")
else:
    print("Deposit not selected")
```

## 🔧 Step 2 — Connect it to the balance

```python
balance = 1000

choice = input(
    "Do you want to deposit? "
)

if choice == "yes":

    amount = float(
        input("Amount: ")
    )

    balance += amount

    print(
        f"New balance: {balance}"
    )

else:

    print("No deposit performed.")
```

## 🧪 Exercise

Add another option:

```text
withdraw
```

Use:

```python
elif choice == "withdraw":
```

Then subtract the amount.

## ✅ Checkpoint

You should understand:

```python
if
elif
else
```

### 🚦 Do not move ahead until

- [ ] You can write an `if`.
- [ ] You can write an `elif`.
- [ ] You can write an `else`.
- [ ] Your program behaves differently depending on user input.

---

# 🐣 Phase 5 — Create a Banking Menu

📄 **File for this phase:** `main.py`

## 🎯 Objective

Our application currently performs one operation and ends.

A real banking application should continue running.

## 🔧 Step 1 — Create an infinite loop

Write:

```python
while True:
    print("Banking application is running...")
```

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run it.

The program does not stop.

## 🔧 Step 2 — Add the menu

```python
while True:

    print("\n===== SIMPLE BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input(
        "Choose an option: "
    )
```

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run it.

## 🔧 Step 3 — Add exit

```python
if choice == "4":
    print("Goodbye!")
    break
```

Understand that `break` exits the loop.

## ✅ Checkpoint

Explain:

> Why does `while True` keep the banking application alive?

Explain:

> What does `break` do?

### 🚦 Do not move ahead until

- [ ] The menu repeatedly appears.
- [ ] Option 4 exits.
- [ ] You understand `while True`.
- [ ] You understand `break`.

---

# 🐣 Phase 6 — Connect the Menu to Banking Operations

📄 **File for this phase:** `main.py`

## 🎯 Objective

Make the menu actually perform banking operations.

Start with:

```python
balance = 1000

while True:

    print("\n===== SIMPLE BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input(
        "Choose an option: "
    )
```

## 💰 Deposit

Add:

```python
if choice == "1":

    amount = float(
        input("Amount to deposit: ")
    )

    balance += amount

    print(
        f"New balance: {balance}"
    )
```

## 💸 Withdraw

Add:

```python
elif choice == "2":

    amount = float(
        input("Amount to withdraw: ")
    )

    if amount > balance:

        print(
            "Insufficient funds"
        )

    else:

        balance -= amount

        print(
            f"New balance: {balance}"
        )
```

## 💳 Check balance

```python
elif choice == "3":

    print(
        f"Your balance is: {balance}"
    )
```

## 🔹 Exit

```python
elif choice == "4":

    print("Goodbye!")

    break
```

## 🔹 Invalid choice

```python
else:

    print(
        "Invalid option, try again."
    )
```

## 🔍 Test

Test all four choices.

Also test:

```text
999
```

as a withdrawal when the balance is only `1000`.

Then test:

```text
1001
```

## ✅ Checkpoint

You now have your first working banking application.

### 🚦 Do not move ahead until

- [ ] Deposit works.
- [ ] Withdrawal works.
- [ ] Insufficient balance is detected.
- [ ] Balance can be viewed.
- [ ] Exit works.
- [ ] Invalid choices do not crash the menu.

---

# 🐣 Phase 7 — Refactor into Functions

📄 **File for this phase:** `main.py`

## 🎯 Objective

The menu is becoming large.

Instead of putting everything inside `main`, create reusable functions.

## 💰 Deposit function

Create:

```python
def deposit(balance, amount):

    new_balance = (
        balance + amount
    )

    print(
        f"Deposited {amount}. "
        f"New balance: {new_balance}"
    )

    return new_balance
```

## 💸 Withdraw function

Create:

```python
def withdraw(balance, amount):

    if amount > balance:

        print("Insufficient funds")

        return balance

    new_balance = (
        balance - amount
    )

    print(
        f"Withdrew {amount}. "
        f"New balance: {new_balance}"
    )

    return new_balance
```

## 💳 Balance function

```python
def check_balance(balance):

    print(
        f"Your balance is: {balance}"
    )
```

## 📋 Menu function

```python
def show_menu():

    print("\n===== SIMPLE BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
```

## ⚠️ Important concept

The function:

```python
return new_balance
```

gives a value back to the caller.

Therefore:

```python
balance = deposit(
    balance,
    amount
)
```

updates the balance.

## 🏁 Final structure for this phase

Create:

```python
def deposit(...):
    ...


def withdraw(...):
    ...


def check_balance(...):
    ...


def show_menu():
    ...


def main():
    ...
```

Then:

```python
if __name__ == "__main__":
    main()
```

## ✅ Checkpoint

You should understand:

```text
main()
  ↓
calls function
  ↓
function performs work
  ↓
function returns result
  ↓
main continues
```

### 🚦 Do not move ahead until

- [ ] Deposit is a function.
- [ ] Withdraw is a function.
- [ ] Menu is a function.
- [ ] You understand `return`.
- [ ] `main()` controls the application.

---

# 🐣 Phase 8 — Represent an Account

📄 **File for this phase:** `main.py`

## 🎯 Objective

Our application currently has:

```python
name
balance
account_number
```

These belong together.

Create a dictionary:

```python
account = {
    "name": "Ravi",
    "account_number": "ACC1001",
    "balance": 1000
}
```

Access the values:

```python
print(account["name"])
print(account["account_number"])
print(account["balance"])
```

## 🔧 Update the functions

Instead of:

```python
deposit(balance, amount)
```

use:

```python
deposit(account, amount)
```

Inside:

```python
def deposit(account, amount):

    account["balance"] += amount

    print(
        f"New balance: "
        f"{account['balance']}"
    )
```

Do the same for withdrawal.

## ✅ Checkpoint

Understand why this is better than having many unrelated variables.

### 🚦 Do not move ahead until

- [ ] You can create a dictionary.
- [ ] You can access dictionary values.
- [ ] You can update the account balance through the dictionary.

---

# 🐣 Phase 9 — Support Multiple Accounts

📄 **File for this phase:** `main.py`

## 🎯 Objective

A bank needs more than one account.

Create:

```python
accounts = {
    "ACC1001": {
        "name": "Ravi",
        "balance": 1000
    },

    "ACC1002": {
        "name": "Priya",
        "balance": 2500
    }
}
```

## 🏦 Find an account

```python
account_number = input(
    "Enter account number: "
)

account = accounts.get(
    account_number
)
```

Then:

```python
if account is None:

    print("Account not found")

else:

    print(
        f"Owner: {account['name']}"
    )

    print(
        f"Balance: {account['balance']}"
    )
```

## 🧪 Exercise

Try:

```text
ACC1001
```

and:

```text
ACC9999
```

## ✅ Checkpoint

Explain:

> Why is `accounts` a dictionary whose values are dictionaries?

### 🚦 Do not move ahead until

- [ ] You can store multiple accounts.
- [ ] You can find an account.
- [ ] You can handle an account that doesn't exist.

---

# 🐣 Phase 10 — Add Transfer

📄 **File for this phase:** `main.py`

## 🎯 Objective

A bank account should be able to transfer money to another account.

Create:

```python
def transfer(
    accounts,
    from_acc,
    to_acc,
    amount
):
```

Find both accounts.

Check that both exist.

Check the sender has enough money.

Then:

```python
accounts[from_acc]["balance"] -= amount

accounts[to_acc]["balance"] += amount
```

Print a confirmation.

## 🔍 Test

Create:

```text
ACC1001 → ₹1000
ACC1002 → ₹2500
```

Transfer:

```text
₹300
```

Expected:

```text
ACC1001 → ₹700
ACC1002 → ₹2800
```

## ⚠️ Important

Test failure cases:

1. Sender does not exist.
2. Receiver does not exist.
3. Sender has insufficient funds.
4. Amount is zero.
5. Amount is negative.

At this point some cases may not yet be handled correctly.

That is intentional.

Write down the problems you discover.

They will motivate later phases.

---

# 🧩 Phase 11 — Create the Account Class

📄 **File for this phase:** `main.py`

## 🎯 Objective

Our dictionary-based design is becoming complicated.

We have:

```text
account data
+
functions that operate on account
```

Let's combine them.

Create:

```python
class Account:

    def __init__(
        self,
        account_number,
        name,
        balance=0
    ):
        self.account_number = (
            account_number
        )

        self.name = name

        self.balance = balance
```

Create an object:

```python
account = Account(
    "ACC1001",
    "Ravi",
    1000
)
```

Access:

```python
print(account.name)
print(account.account_number)
print(account.balance)
```

## ⚖️ Compare

Old:

```python
account["balance"]
```

New:

```python
account.balance
```

## ✅ Checkpoint

Explain:

- What is a class?
- What is an object?
- What does `self` represent?
- What does `__init__()` do?

---

# 🧩 Phase 12 — Move Behavior into Account

📄 **File for this phase:** `main.py`

## 🎯 Objective

The account should know how to deposit and withdraw.

Add:

```python
def deposit(self, amount):

    self.balance += amount

    print(
        f"Deposited {amount}. "
        f"New balance: {self.balance}"
    )
```

Add:

```python
def withdraw(self, amount):

    if amount > self.balance:

        print(
            "Insufficient funds"
        )

        return False

    self.balance -= amount

    print(
        f"Withdrew {amount}. "
        f"New balance: {self.balance}"
    )

    return True
```

Add:

```python
def show_balance(self):

    print(
        f"{self.name}'s balance: "
        f"{self.balance}"
    )
```

Now use:

```python
account.deposit(500)
```

and:

```python
account.withdraw(200)
```

## ⚠️ Important mental model

Instead of saying:

> "Run a function on some account data."

we can say:

> "Ask this account to deposit money."

That is:

```python
account.deposit(500)
```

---

# 🧩 Phase 13 — Create the Bank Class

📄 **File for this phase:** `main.py`

## 🎯 Objective

We have `Account`.

Now we need something to manage many accounts.

Create:

```python
class Bank:

    def __init__(self):

        self.accounts = {}
```

Add:

```python
def add_account(self, account):

    self.accounts[
        account.account_number
    ] = account
```

Add:

```python
def get_account(self, account_number):

    return self.accounts.get(
        account_number
    )
```

Use it:

```python
bank = Bank()

bank.add_account(
    Account(
        "ACC1001",
        "Ravi",
        1000
    )
)

bank.add_account(
    Account(
        "ACC1002",
        "Priya",
        2500
    )
)
```

Find:

```python
account = bank.get_account(
    "ACC1001"
)
```

## ✅ Checkpoint

Understand the responsibility:

```text
Account
→ manages one account

Bank
→ manages many accounts
```

---

# 🧩 Phase 14 — Move Transfer into Bank

📄 **File for this phase:** `main.py`

## 🎯 Objective

Transfer involves two accounts, so it makes sense for `Bank` to manage it.

Add:

```python
def transfer(
    self,
    from_acc,
    to_acc,
    amount
):

    sender = self.get_account(
        from_acc
    )

    receiver = self.get_account(
        to_acc
    )

    if sender is None:
        print("Sender not found")
        return

    if receiver is None:
        print("Receiver not found")
        return

    if sender.withdraw(amount):

        receiver.deposit(amount)

        print(
            f"Transferred {amount} "
            f"from {from_acc} "
            f"to {to_acc}"
        )
```

Test it.

## ✅ Checkpoint

You should now understand the first important responsibility split:

```text
Account
    ↓
deposit()
withdraw()

Bank
    ↓
add_account()
get_account()
transfer()
```

---

# 🧩 Phase 15 — Add Savings and Current Accounts

📄 **File for this phase:** `main.py`

## 🎯 Objective

Different account types can have different behavior.

Create:

```python
class SavingsAccount(Account):
    ...
```

and:

```python
class CurrentAccount(Account):
    ...
```

Start with the constructors.

Savings:

```python
class SavingsAccount(Account):

    def __init__(
        self,
        account_number,
        name,
        balance=0,
        interest_rate=0.04
    ):

        super().__init__(
            account_number,
            name,
            balance
        )

        self.interest_rate = (
            interest_rate
        )
```

Current:

```python
class CurrentAccount(Account):

    def __init__(
        self,
        account_number,
        name,
        balance=0,
        overdraft_limit=5000
    ):

        super().__init__(
            account_number,
            name,
            balance
        )

        self.overdraft_limit = (
            overdraft_limit
        )
```

## ✅ Checkpoint

Understand:

```text
Account
  ↑
  ├── SavingsAccount
  └── CurrentAccount
```

This is inheritance.

---

# 🧩 Phase 16 — Add Different Account Behavior

📄 **File for this phase:** `main.py`

## 🔹 Savings interest

Add:

```python
def apply_interest(self):

    interest = (
        self.balance
        * self.interest_rate
    )

    self.balance += interest

    return interest
```

Test:

```python
account = SavingsAccount(
    "ACC1001",
    "Ravi",
    10000
)

account.apply_interest()

print(account.balance)
```

## 🏦 Current account overdraft

Override `withdraw()`:

```python
def withdraw(self, amount):

    if (
        amount
        > self.balance
        + self.overdraft_limit
    ):

        print(
            "Withdrawal exceeds "
            "overdraft limit"
        )

        return False

    self.balance -= amount

    return True
```

## ✅ Checkpoint

Understand:

> Child classes can reuse parent behavior and change behavior when required.

---

# 🧩 Phase 17 — Create the User Model

📄 **File for this phase:** `main.py`

## 🎯 Objective

A bank needs customers/users.

Create:

```python
class User:

    def __init__(
        self,
        name,
        phone,
        email,
        password_hash
    ):

        self.name = name
        self.phone = phone
        self.email = email
        self._password_hash = (
            password_hash
        )
```

The user owns one or more accounts.

When creating an account, associate the owner:

```python
account.owner = user
```

## 🧠 Mental model

```text
User
 └── owns
      ├── Account
      ├── Account
      └── Account
```

---

# 🧩 Phase 18 — Add Transactions

📄 **File for this phase:** `main.py`

## 🎯 Objective

A bank needs transaction history.

Create:

```python
from dataclasses import dataclass
from datetime import datetime
```

Then:

```python
@dataclass
class Transaction:

    account_number: str
    action: str
    amount: float
    timestamp: str = None
```

Add:

```python
def __post_init__(self):

    if self.timestamp is None:

        self.timestamp = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )
```

Create an account transaction list:

```python
self.transactions = []
```

Record a transaction:

```python
account.transactions.append(
    Transaction(
        account.account_number,
        "DEPOSIT",
        amount
    )
)
```

## ✅ Checkpoint

Test that every deposit creates a transaction record.

Then do the same for withdrawals.

---

# 🧩 Phase 19 — Organize the Project into Packages

📄 **This phase creates folders and empty `__init__.py` files** — no business logic yet: `models/`, `services/`, `repositories/`, `ui/` (each with an `__init__.py`), plus the top-level `exceptions.py`.

## 🎯 Objective

The project is becoming too large for one file.

Create:

```text
banking_app/
├── main.py
├── exceptions.py
├── models/
├── services/
├── repositories/
├── ui/
└── data/
```

Inside each Python package directory create:

```text
__init__.py
```

So:

```text
models/
└── __init__.py

services/
└── __init__.py

repositories/
└── __init__.py

ui/
└── __init__.py
```

## 🤔 Why?

We are separating responsibilities.

### 🔹 Models

Things that exist:

```text
User
Account
SavingsAccount
CurrentAccount
Transaction
```

### 🔹 Services

Things the application does:

```text
authentication
transactions
OTP
validation
```

### 🔹 Repositories

Data storage.

### 🔹 UI

Console interaction.

---

# 🧩 Phase 20 — Move Models into Their Own Files

📄 **Files for this phase:** `main.py`, `models/user.py`, `models/account.py`, `models/transaction.py`

Create:

```text
models/
├── __init__.py
├── user.py
├── account.py
└── transaction.py
```

Put `User` in:

```text
models/user.py
```

Put `Account`, `SavingsAccount`, and `CurrentAccount` in:

```text
models/account.py
```

Put `Transaction` in:

```text
models/transaction.py
```

Import them where needed.

Example:

```python
from models.account import Account
```

and:

```python
from models.user import User
```

## 🔍 Test

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run:

```bash
python main.py
```

Make sure imports work before continuing.

🏁 **`models/user.py` and `models/transaction.py` are now FINAL — they will not change again for the rest of this course.**

---

# 🔐 Phase 21 — Add Custom Exceptions

📄 **File for this phase:** `exceptions.py`

## 🎯 Objective

Instead of printing every error or returning `False`, create meaningful exceptions.

Create:

```text
exceptions.py
```

Add:

```python
class BankingError(Exception):
    pass
```

Then:

```python
class InsufficientBalanceError(
    BankingError
):
    pass
```

Add:

```python
class AccountNotFoundError(
    BankingError
):
    pass
```

Add:

```python
class AuthenticationError(
    BankingError
):
    pass
```

Add:

```python
class UserAlreadyExistsError(
    BankingError
):
    pass
```

Add:

```python
class InvalidOTPError(
    BankingError
):
    pass
```

## 🔹 Use one

Instead of:

```python
return False
```

you can eventually do:

```python
raise InsufficientBalanceError(
    "Insufficient funds"
)
```

Then the caller can handle it:

```python
try:

    account.withdraw(amount)

except InsufficientBalanceError as e:

    print(e)
```

## ✅ Checkpoint

Understand the difference between:

```python
print(...)
```

and:

```python
raise ...
```

Printing tells the user something.

Raising an exception tells the application:

> "Something went wrong. Decide how to handle it."

🏁 **`exceptions.py` is now FINAL — it will not change again for the rest of this course.**

---

# 🔐 Phase 22 — Create the Validation Service

📄 **File for this phase:** `services/validators.py`

## 🎯 Objective

Users can enter invalid information.

Create:

```text
services/validators.py
```

Import:

```python
import re
```

## 🧾 Name validation

```python
def is_valid_name(name):

    return bool(
        re.match(
            r"^[A-Za-z\s]{2,50}$",
            name
        )
    )
```

## 🧾 Phone validation

```python
def is_valid_phone(phone):

    return bool(
        re.match(
            r"^[6-9]\d{9}$",
            phone
        )
    )
```

## 🧾 Email validation

```python
def is_valid_email(email):

    return bool(
        re.match(
            r"^[a-zA-Z0-9._%+-]+"
            r"@[a-zA-Z0-9.-]+\."
            r"[a-zA-Z]{2,}$",
            email
        )
    )
```

## 🧾 Amount validation

```python
def is_valid_amount(value):

    try:

        amount = float(value)

        return amount > 0

    except ValueError:

        return False
```

## ✅ Checkpoint

Test each validator independently.

---

# 🔐 Phase 23 — Create a Reusable Input Helper

📄 **File for this phase:** `services/validators.py`

## 🎯 Objective

Do not write the same validation loop repeatedly.

Create:

```python
def get_valid_input(
    prompt,
    validator,
    error_message
):

    while True:

        value = input(prompt)

        if validator(value):

            return value

        print(error_message)
```

Now:

```python
name = get_valid_input(
    "Name: ",
    is_valid_name,
    "Invalid name."
)
```

Phone:

```python
phone = get_valid_input(
    "Phone: ",
    is_valid_phone,
    "Invalid phone."
)
```

## ⚠️ Important concept

You created a reusable function that accepts another function:

```python
validator
```

This is a useful Python concept.

🏁 **`services/validators.py` is now FINAL — it will not change again for the rest of this course.**

---

# 🔐 Phase 24 — Create Authentication

📄 **File for this phase:** `services/auth_service.py`

## 🎯 Objective

Users need registration and login.

Create:

```text
services/auth_service.py
```

Start with password hashing.

For this educational implementation:

```python
import hashlib
```

```python
def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()
```

## 📝 User registration

Create an `AuthService`:

```python
class AuthService:

    def __init__(self):

        self.users = {}
```

Registration should:

1. Check whether the phone already exists.
2. Hash the password.
3. Create a `User`.
4. Store the user.
5. Return the user.

## 🔓 Login

Login should:

1. Find the user.
2. Hash the entered password.
3. Compare it with the stored hash.
4. Raise `AuthenticationError` if invalid.
5. Return the user if successful.

## 🔒 Security note

This SHA-256 example is useful for learning hashing, but it is **not the recommended production design for password storage**. Production applications should use a password-specific hashing algorithm such as Argon2, bcrypt, or scrypt with appropriate parameters.

🏁 **`services/auth_service.py` is now FINAL — it will not change again for the rest of this course.**

---

# 🔐 Phase 25 — Create the Transaction Service

📄 **File for this phase:** `services/transaction_service.py`

## 🎯 Objective

Business workflows are becoming larger.

Create:

```text
services/transaction_service.py
```

The service should coordinate:

```text
Account
+
Transaction
+
Logging
+
Validation
+
Security
```

Create operations such as:

```python
deposit(...)
withdraw(...)
transfer(...)
```

For deposit:

1. Validate amount.
2. Change account balance.
3. Create transaction record.
4. Save/log the transaction.

For withdrawal:

1. Validate amount.
2. Check balance.
3. Change balance.
4. Create transaction record.
5. Save/log the transaction.

## 🧭 Responsibility

The model answers:

> "How does an account deposit?"

The service answers:

> "What complete business process happens when a user deposits?"

---

# 💾 Phase 26 — Add JSON Persistence

📄 **Files for this phase:** `repositories/account_repository.py`, `data/logs/ (folder)`

## 🎯 Objective

Currently all information disappears when the program stops.

We need permanent storage.

Create:

```text
repositories/
├── __init__.py
└── account_repository.py
```

Create:

```text
data/
└── logs/
```

## 🤔 Why JSON?

For this course, JSON is simple and readable.

The flow is:

```text
Python objects
      ↓
dictionary
      ↓
JSON
      ↓
file
```

And when starting:

```text
JSON
 ↓
dictionary
 ↓
Python objects
```

---

# 💾 Phase 27 — Add Serialization

📄 **File for this phase:** `models/account.py`

## 🎯 Objective

Teach objects how to become plain data.

Inside `Account`, create:

```python
def to_dict(self):
```

Return the account information as a dictionary.

For example:

```python
return {
    "account_number":
        self.account_number,

    "balance":
        self.balance,

    "type":
        self.__class__.__name__,

    "owner_phone":
        self.owner.phone
}
```

The exact fields should match the final model you are building.

## 🤔 Why?

JSON understands simple structures such as:

```text
string
number
boolean
list
dictionary
```

It does not automatically understand your custom Python objects.

🏁 **`models/account.py` is now FINAL — it will not change again for the rest of this course.**

---

# 💾 Phase 28 — Save Accounts

📄 **File for this phase:** `repositories/account_repository.py`

Create:

```python
import json
import os
```

Define the data file location.

Then create:

```python
def save_accounts(accounts):
```

Convert each account using:

```python
account.to_dict()
```

Then:

```python
json.dump(
    data,
    file,
    indent=4,
    ensure_ascii=False
)
```

## 🔍 Test

Create an account.

Exit the program.

Open:

```text
data/accounts.json
```

You should see readable JSON.

---

# 💾 Phase 29 — Load Accounts

📄 **File for this phase:** `repositories/account_repository.py`

Create:

```python
def load_accounts_raw():
```

First check:

```python
if not os.path.exists(
    ACCOUNTS_FILE
):
    return {}
```

Then open the file and use:

```python
json.load(file)
```

## ⚠️ Important

At this stage you are loading dictionaries.

You still need to convert them back into:

```text
Account
SavingsAccount
CurrentAccount
```

objects.

That process is called rehydration.

---

# 💾 Phase 30 — Rehydrate Account Objects

📄 **File for this phase:** `main.py`

For each saved account:

1. Read the `type`.
2. Find the owner.
3. Create the correct account class.
4. Restore the balance.
5. Restore transactions if applicable.
6. Put the object back into the bank.

Conceptually:

```text
JSON
 ↓
dict
 ↓
"type"?
 ↓
SavingsAccount / CurrentAccount
 ↓
Python object
```

Test by:

1. Creating an account.
2. Depositing money.
3. Exiting.
4. Restarting.
5. Checking the balance.

The balance should remain.

---

# 💾 Phase 31 — Save and Load Users

📄 **File for this phase:** `repositories/account_repository.py`

Create:

```text
users.json
```

Store user information such as:

```text
name
phone
email
password_hash
```

Do **not** store plain-text passwords.

Create:

```python
save_users(...)
```

and:

```python
load_users(...)
```

At startup, users must be restored before accounts that reference those users.

## ⚠️ Important dependency

The relationship is:

```text
User
 ↑
 │ owner
 │
Account
```

Therefore you need users available when rebuilding accounts.

---

# 💾 Phase 32 — Create Application Bootstrap

📄 **File for this phase:** `main.py`

## 🎯 Objective

Create one place that prepares the application when it starts.

Create:

```python
def bootstrap():
```

It should:

1. Load users.
2. Recreate users.
3. Load accounts.
4. Recreate accounts.
5. Connect accounts to their owners.
6. Prepare services.

The application lifecycle becomes:

```text
START
  ↓
bootstrap()
  ↓
load users
  ↓
load accounts
  ↓
create objects
  ↓
show menu
```

---

# 💾 Phase 33 — Persist Before Exit

📄 **File for this phase:** `main.py`

Create:

```python
def persist_all():
```

It should save:

```text
users
accounts
```

Call it when the user exits.

Also consider calling it after important operations or logout, depending on the design you are implementing.

## 🔍 Test

Perform:

```text
Register
Login
Open account
Deposit
Exit
```

Start again.

Verify:

```text
User exists
Account exists
Balance exists
```

---

# 💾 Phase 34 — Add Transaction Logs

📄 **File for this phase:** `repositories/account_repository.py`

## 🎯 Objective

Current JSON state tells us what the balance is.

Logs tell us what happened.

Create:

```text
data/logs/
```

Create a daily log file such as:

```text
transactions_2026-09-12.log
```

Create:

```python
def log_transaction(
    account_number,
    action,
    amount
):
```

Use append mode:

```python
open(
    log_file,
    "a",
    encoding="utf-8"
)
```

Write:

```text
timestamp | account | action | amount
```

## ⚠️ Important

Use:

```python
"a"
```

because we want to append instead of deleting previous records.

🏁 **`repositories/account_repository.py` is now FINAL — it will not change again for the rest of this course.**

---

# 💾 Phase 35 — Add Account Statements

📄 **File for this phase:** `main.py`

## 🎯 Objective

Users should be able to see their transaction history.

Create a statement flow that:

1. Finds one of the user's accounts.
2. Reads its transactions.
3. Prints each transaction.
4. Prints the current balance.

Example:

```text
===== STATEMENT =====

2026-09-12 10:00:00
DEPOSIT ₹500

2026-09-12 10:05:00
WITHDRAW ₹200

--------------------
Current Balance: ₹1300
```

---

# 💾 Phase 36 — Generate Account Numbers

📄 **File for this phase:** `main.py`

## 🎯 Objective

Users should not manually choose account numbers.

Create a function such as:

```python
def generate_account_number():
```

Generate a candidate such as:

```text
ACC4821
```

Then check whether it already exists.

Use:

```python
while True:
```

to keep generating until you find a unique number.

## ⚠️ Important

This is another practical example of why loops are useful.

---

# 🔁 Phase 37 — Create the Registration Flow

📄 **File for this phase:** `main.py`

Create a UI function:

```python
def register_flow():
```

It should collect:

```text
Name
Phone
Email
Password
```

Use your validators.

Then call the authentication service.

Handle:

```python
UserAlreadyExistsError
```

Display a friendly message.

## ⚠️ Important

The UI should coordinate the process.

It should not contain all the business rules.

---

# 🔁 Phase 38 — Create the Login Flow

📄 **File for this phase:** `main.py`

Create:

```python
def login_flow():
```

Collect:

```text
Phone
Password
```

Call:

```python
auth_service.login(...)
```

On success:

```text
Welcome back!
```

On failure:

```text
Invalid phone number or password
```

Return the logged-in user.

---

# 🔁 Phase 39 — Restrict Users to Their Own Accounts

📄 **File for this phase:** `main.py`

## 🎯 Objective

A user must not be able to type someone else's account number and operate on it.

Create a helper that finds accounts belonging to the current user.

Conceptually:

```python
owned_accounts = [
    account
    for account in bank.accounts.values()
    if account.owner.phone == user.phone
]
```

Display only those accounts.

Before deposit, withdrawal, or statement operations, select from the user's own accounts.

---

# 🔁 Phase 40 — Create the Open Account Flow

📄 **File for this phase:** `main.py`

Create:

```python
def open_account_flow(user):
```

Show:

```text
1. Savings Account
2. Current Account
```

Generate the account number.

Create the correct class.

Attach the owner.

Add it to the bank.

Save the updated data.

Display:

```text
Account ACC1234 opened successfully.
```

---

# 🔁 Phase 41 — Build the Deposit Flow

📄 **File for this phase:** `main.py`

Create:

```python
def deposit_flow(user):
```

Process:

```text
logged-in user
      ↓
select own account
      ↓
enter amount
      ↓
validate amount
      ↓
transaction service
      ↓
update balance
      ↓
record transaction
      ↓
show success
```

Handle banking exceptions.

---

# 🔁 Phase 42 — Build the Withdrawal Flow

📄 **File for this phase:** `main.py`

Create:

```python
def withdraw_flow(user):
```

Process:

```text
logged-in user
      ↓
select own account
      ↓
enter amount
      ↓
validate amount
      ↓
security check
      ↓
withdraw
      ↓
record transaction
      ↓
show result
```

Test:

- valid withdrawal
- zero
- negative amount
- too much money
- invalid input

---

# 🔁 Phase 43 — Build the Transfer Flow

📄 **File for this phase:** `main.py`

Create:

```python
def transfer_flow(user):
```

Process:

```text
choose sender account
       ↓
enter receiver account
       ↓
verify receiver
       ↓
enter amount
       ↓
validate
       ↓
security check
       ↓
withdraw from sender
       ↓
deposit into receiver
       ↓
record transactions
```

Make sure the logged-in user can only use their own account as the sender.

---

# 🔒 Phase 44 — Add OTP Service

📄 **File for this phase:** `services/otp_service.py`

## 🎯 Objective

Large transactions need an additional verification step.

Create:

```text
services/otp_service.py
```

Generate a six-digit OTP.

For this CLI project, simulate SMS by printing it:

```text
[SIMULATED SMS]
Your OTP is: 482913
```

Store pending OTPs temporarily.

Example concept:

```python
self._pending_otps = {}
```

Store:

```text
phone → otp
```

---

# 🔒 Phase 45 — Verify OTP

📄 **File for this phase:** `services/otp_service.py`

Create:

```python
def verify_otp(
    self,
    phone,
    entered_otp
):
```

Check whether the entered OTP matches the stored OTP.

If valid:

```python
del self._pending_otps[phone]
```

Return success.

If invalid:

```python
return False
```

Later the transaction workflow can convert that failure into:

```python
InvalidOTPError
```

## 🤔 Why delete the OTP?

Because an OTP should be one-time use.

---

# 🔒 Phase 46 — Define the OTP Threshold

📄 **File for this phase:** `services/transaction_service.py`

Choose the course requirement, for example:

```python
OTP_THRESHOLD = 10000
```

Then:

```text
Amount <= 10000
        ↓
No OTP

Amount > 10000
        ↓
OTP required
```

Test both cases.

---

# 🔒 Phase 47 — Introduce Decorators

📄 **Files for this phase:** `services/otp_service.py`, `services/transaction_service.py`

## 🎯 Objective

We have a repeated security rule.

Both:

```text
withdraw
transfer
```

may require OTP.

Instead of duplicating security code, create a decorator.

Start with the mental model:

```text
withdraw()
    ↓
OTP wrapper
    ↓
verify OTP
    ↓
withdraw()
```

Import:

```python
from functools import wraps
```

Create:

```python
def requires_otp(
    threshold=10000
):
```

The decorator should:

1. Receive the original function.
2. Create a wrapper.
3. Check the amount.
4. Require OTP above the threshold.
5. Verify OTP.
6. Call the original function.

Then:

```python
@requires_otp(
    threshold=10000
)
def withdraw(...):
    ...
```

## ✅ Checkpoint

You should be able to explain:

> A decorator lets us add reusable behavior around another function.

🏁 **`services/otp_service.py` and `services/transaction_service.py` are now FINAL — they will not change again for the rest of this course.**

---

# 🎨 Phase 48 — Create Console UI Helpers

📄 **File for this phase:** `ui/console.py`

## 🎯 Objective

Don't scatter formatting everywhere.

Create:

```text
ui/
└── console.py
```

Create functions such as:

```python
def print_success(message):
    ...
```

```python
def print_error(message):
    ...
```

```python
def print_info(message):
    ...
```

```python
def print_menu(title, options):
    ...
```

The rest of the application can now call:

```python
print_success(
    "Deposit successful."
)
```

instead of worrying about formatting.

---

# 🎨 Phase 49 — Add `colorama`

📄 **Files for this phase:** `ui/console.py`, `requirements.txt`

If the project uses colored console output, install dependencies from:

```bash
pip install -r requirements.txt
```

or install the required package directly:

```bash
pip install colorama
```

Use:

```python
from colorama import Fore, init

init(autoreset=True)
```

For robustness, you can provide a fallback when `colorama` is unavailable.

## 🔍 Test

Run the application from the terminal.

Make sure:

- success messages are readable
- errors are readable
- menus are readable

🏁 **`ui/console.py` and `requirements.txt` are now FINAL — they will not change again for the rest of this course.**

---

# 🎨 Phase 50 — Create the Logged-In Menu

📄 **File for this phase:** `main.py`

After successful login, show:

```text
===== BANKING MENU =====

1. Open Account
2. Deposit
3. Withdraw
4. Transfer
5. View Statement
6. Logout
```

Create:

```python
def logged_in_menu(user):
```

Use:

```python
while True:
```

Inside the loop, call the appropriate flow function.

Example structure:

```python
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
    break
```

---

# 🎨 Phase 51 — Create the Final Main Menu

📄 **File for this phase:** `main.py`

The top-level menu should be:

```text
===== CLI BANKING SYSTEM =====

1. Register
2. Login
3. Exit
```

`main()` should:

1. Bootstrap the application.
2. Show the main menu.
3. Register users.
4. Login users.
5. Enter the logged-in menu.
6. Persist data before exiting.

The final conceptual structure is:

```text
main()
  ↓
bootstrap()
  ↓
main menu
  ├── register
  ├── login
  │     ↓
  │   banking menu
  │     ├── open account
  │     ├── deposit
  │     ├── withdraw
  │     ├── transfer
  │     ├── statement
  │     └── logout
  │
  └── exit
```

🏁 **`main.py` is now FINAL — it will not change again for the rest of this course.**

---

# 🏁 Phase 52 — Final Project Structure

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

Your project should eventually look similar to:

```text
banking_app/
│
├── main.py
├── exceptions.py
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── account.py
│   ├── transaction.py
│   └── user.py
│
├── services/
│   ├── __init__.py
│   ├── auth_service.py
│   ├── otp_service.py
│   ├── transaction_service.py
│   └── validators.py
│
├── repositories/
│   ├── __init__.py
│   └── account_repository.py
│
├── ui/
│   ├── __init__.py
│   └── console.py
│
└── data/
    ├── accounts.json
    ├── users.json
    └── logs/
        └── transactions_YYYY-MM-DD.log
```

Do not create every file at the beginning.

You should arrive at this structure **because the application became large enough to need it**.

---

# 🏁 Phase 53 — End-to-End Testing

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

**Before you run this: what output do you expect? Say it out loud or jot it down, then run it and check.**

Run:

```bash
python main.py
```

Perform this complete test.

## 🔍 Test 1 — Register

Register a new user.

Verify:

- valid name accepted
- valid phone accepted
- valid email accepted
- password accepted

## 🔍 Test 2 — Duplicate registration

Register using the same phone.

Expected:

```text
User already exists
```

## 🔍 Test 3 — Login

Use the correct password.

Expected:

```text
Welcome back!
```

## 🔍 Test 4 — Wrong password

Use the wrong password.

Expected:

```text
Authentication failed
```

## 🔍 Test 5 — Open Savings Account

Expected:

```text
ACCxxxx
```

## 🔍 Test 6 — Open Current Account

Verify the user can have multiple accounts.

## 🔍 Test 7 — Deposit

Deposit:

```text
₹500
```

Verify balance increases.

## 🔍 Test 8 — Withdrawal

Withdraw:

```text
₹200
```

Verify balance decreases.

## 🔍 Test 9 — Insufficient funds

Attempt to withdraw more than the balance.

Expected:

```text
Insufficient funds
```

## 🔍 Test 10 — Transfer

Transfer between two accounts.

Verify both balances.

## 🔍 Test 11 — Statement

Verify transaction history contains the operations performed.

## 🔍 Test 12 — OTP

Perform a transaction below the threshold.

Verify no OTP is required.

Perform a transaction above the threshold.

Verify OTP is required.

Enter the correct OTP.

Verify success.

Enter an incorrect OTP.

Verify failure.

## 🔍 Test 13 — Persistence

Exit the application.

Start it again.

Verify:

- users remain
- accounts remain
- balances remain
- account types remain
- relevant transaction history remains

---

# 🏁 Phase 54 — Error Testing

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

Do not only test the happy path.

Try to break your application.

## 📝 Registration

Try:

```text
A
```

as a name.

Try:

```text
123
```

as a phone.

Try:

```text
hello
```

as an email.

## 🔹 Amounts

Try:

```text
abc
```

Try:

```text
-100
```

Try:

```text
0
```

## 🏦 Account numbers

Try:

```text
ACC9999
```

when it does not exist.

## 🔐 Authentication

Try:

```text
wrong password
```

## 🔑 OTP

Try:

```text
wrong OTP
```

## 🔁 Transfer

Try:

```text
transfer to yourself
```

if your requirements prohibit it.

Try transferring more money than the sender has.

---

# 🏁 Phase 55 — Code Quality Check

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

Before considering the project complete, check the following.

## 🔹 `main.py`

It should mainly coordinate the application.

It should not contain every business rule.

## 🔹 Models

Models should represent:

```text
User
Account
SavingsAccount
CurrentAccount
Transaction
```

## 🔹 Services

Services should contain application/business workflows.

## 🔹 Repository

Repository code should handle persistence.

## 🔹 UI

UI code should handle console interaction and presentation.

## 💥 Exceptions

Application-specific failures should use meaningful exception classes.

---

# 🏁 Phase 56 — Final Conceptual Revision

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

Without looking at your code, explain each of these.

## 🔹 Python basics

- What is a variable?
- What does `input()` return?
- What does `float()` do?
- What does `if` do?
- What does `while True` mean?
- What does `break` do?

## 🔧 Functions

- Why do we create functions?
- What is a parameter?
- What does `return` do?

## 🔹 Data structures

- Why did we first use a dictionary?
- Why do we have a dictionary of accounts?

## 🔹 OOP

- What is a class?
- What is an object?
- What is `self`?
- What is `__init__()`?
- What is inheritance?
- What does `super()` do?
- What is method overriding?

## 🔹 Architecture

- What belongs in `models`?
- What belongs in `services`?
- What belongs in `repositories`?
- What belongs in `ui`?
- Why should `main.py` not contain everything?

## 💾 Persistence

- Why can't we simply keep everything in variables?
- Why do we serialize objects?
- What is JSON?
- What is rehydration?

## 🔒 Security

- Why should we not store plain passwords?
- What is password hashing?
- Why do we use OTP?
- Why should an OTP be deleted after successful use?

## 🎁 Decorators

- What problem does the OTP decorator solve?
- What does `@requires_otp` mean conceptually?

---

# 🏁 Phase 57 — The Story You Should Remember

📄 **This phase has no new code file** — it's a review / testing / reflection phase.

Do not memorize 50 files.

Remember the story.

We started with:

```python
print()
```

because we needed a program.

Then:

```python
balance = 1000
```

because we needed data.

Then:

```python
input()
```

because the user needed control.

Then:

```python
if
```

because the user needed choices.

Then:

```python
while True
```

because the application needed to stay alive.

Then functions because the code became repetitive.

Then dictionaries because an account had multiple pieces of information.

Then multiple accounts because a bank has many accounts.

Then classes because dictionaries plus functions became difficult to manage.

Then inheritance because different account types behave differently.

Then users because accounts need owners.

Then transactions because banks need history.

Then services because business workflows became larger.

Then validators because users enter bad data.

Then exceptions because failures need clean handling.

Then JSON because data must survive application restarts.

Then logs because we need an audit trail.

Then OTP because important transactions need additional verification.

Then decorators because the OTP rule is reusable.

Then UI modules because presentation should be separated from business logic.

That is the architecture story.

> **Every new concept exists because the previous version had a problem.**

If you understand that story, you understand the project.

---

# 📦 Final Submission Checklist

## 🔹 Project

- [ ] Project runs with `python main.py`.
- [ ] No unnecessary files are present.
- [ ] Folder structure is understandable.

## 🔐 Authentication

- [ ] Registration works.
- [ ] Duplicate users are rejected.
- [ ] Login works.
- [ ] Wrong passwords are rejected.
- [ ] Passwords are not stored as plain text.

## 🏦 Accounts

- [ ] Savings account works.
- [ ] Current account works.
- [ ] Account numbers are unique.
- [ ] Users can own multiple accounts.

## 🔹 Transactions

- [ ] Deposit works.
- [ ] Withdrawal works.
- [ ] Transfer works.
- [ ] Insufficient balance is handled.
- [ ] Transaction records are created.
- [ ] Statements can be viewed.

## 🔒 Security

- [ ] Large transactions require OTP.
- [ ] Correct OTP succeeds.
- [ ] Incorrect OTP fails.
- [ ] OTP cannot be reused.

## 💾 Persistence

- [ ] Users are saved.
- [ ] Accounts are saved.
- [ ] Balances survive restart.
- [ ] Account types survive restart.
- [ ] Transaction history survives restart where required.
- [ ] Logs are written.

## 🧾 Validation

- [ ] Invalid names are rejected.
- [ ] Invalid phones are rejected.
- [ ] Invalid emails are rejected.
- [ ] Invalid amounts are rejected.
- [ ] Invalid menu options are handled.

## 🔹 Architecture

- [ ] Models are separated.
- [ ] Services are separated.
- [ ] Repository is separated.
- [ ] UI helpers are separated.
- [ ] Exceptions are centralized.
- [ ] `main.py` remains understandable.

---

# 🏆 Final Challenge

After completing the project, add one feature **without following a tutorial**.

Choose one:

1. Change password.
2. Close an account.
3. Show all accounts owned by the user.
4. Add a minimum balance rule.
5. Add a transaction limit.
6. Add interest calculation for savings accounts.
7. Add a mini statement showing the last five transactions.
8. Add an account search.
9. Add a daily withdrawal limit.
10. Add a "forgot password" simulation.

Before coding, answer:

```text
What problem am I solving?

Which class owns this behavior?

Is this model logic, service logic, repository logic, or UI logic?

Do I need a new function?

Do I need a new class?

Do I need a new exception?

Do I need to change persistence?
```

Then implement it.

The objective is no longer to copy code.

The objective is to **make an architectural decision yourself**.


---

# 📚 Complete Final Source Code — Copy Every File

The following files are the **complete final source files** from the supplied `phase7_full_project.zip`. Do not replace these with shortened snippets or `...`. Create the folders and files exactly as shown, then copy the complete code into each file.

This section is intentionally complete so that a student can rebuild the final project from this Markdown alone.

## 📄 `main.py`

```python
"""
Main CLI entry point. This file is deliberately "dumb" - it only shows menus
and calls into services/. No banking business logic should live here.
"""

import random

from models.account import SavingsAccount, CurrentAccount
from services.auth_service import AuthService
from services.otp_service import OTPService
from services import transaction_service as txn
from services.validators import (
    is_valid_name,
    is_valid_phone,
    is_valid_email,
    get_valid_input,
)
from repositories.account_repository import (
    save_accounts,
    load_accounts_raw,
    save_users,
    load_users_raw,
)
from exceptions import (
    BankingError,
    AccountNotFoundError,
    UserAlreadyExistsError,
    AuthenticationError,
)
from ui.console import print_success, print_error, print_info, print_menu

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
```

## 📄 `exceptions.py`

```python
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
```

## 📄 `requirements.txt`

```text
colorama
```

## 📄 `models/__init__.py`

```python

```

## 📄 `models/account.py`

```python
from exceptions import InsufficientBalanceError


class Account:
    """Parent class for all account types."""

    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner  # Account HAS-A User (composition)
        self._balance = balance
        self.transactions = []  # Account HAS-A list of Transactions

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient balance")
        self._balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "owner_phone": self.owner.phone,
            "balance": self._balance,
            "type": type(self).__name__,
        }


class SavingsAccount(Account):
    """SavingsAccount IS-A Account, earns interest, no overdraft."""

    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.04):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


class CurrentAccount(Account):
    """CurrentAccount IS-A Account, allows overdraft, no interest."""

    def __init__(self, account_number, owner, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # overrides parent - different rule!
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientBalanceError("Exceeds overdraft limit")
        self._balance -= amount
```

## 📄 `models/transaction.py`

```python
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    account_number: str
    action: str          # "DEPOSIT", "WITHDRAW", "TRANSFER_OUT", "TRANSFER_IN"
    amount: float
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} | Account: {self.account_number} | {self.action}: ₹{self.amount}"
```

## 📄 `models/user.py`

```python
class User:
    """Represents a registered bank customer."""

    def __init__(self, name, phone, email, password_hash):
        self.name = name
        self.phone = phone
        self.email = email
        self._password_hash = password_hash  # encapsulated - never store raw passwords!

    def check_password(self, password_hash):
        return self._password_hash == password_hash

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "password_hash": self._password_hash,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["email"], data["password_hash"])
```

## 📄 `services/__init__.py`

```python

```

## 📄 `services/auth_service.py`

```python
import hashlib

from models.user import User
from exceptions import UserAlreadyExistsError, AuthenticationError


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()  # never store raw passwords!


class AuthService:
    def __init__(self):
        self.users = {}  # phone -> User

    def register(self, name, phone, email, password):
        if phone in self.users:
            raise UserAlreadyExistsError("User already registered with this phone number")
        user = User(name, phone, email, hash_password(password))
        self.users[phone] = user
        return user

    def login(self, phone, password):
        user = self.users.get(phone)
        if user is None or not user.check_password(hash_password(password)):
            raise AuthenticationError("Invalid phone number or password")
        return user

    def load_users(self, users_dict):
        """Rehydrate users from persisted data on startup."""
        self.users = {phone: User.from_dict(data) for phone, data in users_dict.items()}

    def dump_users(self):
        """Serialize users for persistence."""
        return {phone: user.to_dict() for phone, user in self.users.items()}
```

## 📄 `services/otp_service.py`

```python
import random
from functools import wraps

from exceptions import InvalidOTPError


class OTPService:
    def __init__(self):
        self._pending_otps = {}  # phone -> otp code

    def generate_otp(self, phone) -> str:
        otp = str(random.randint(100000, 999999))
        self._pending_otps[phone] = otp
        # In a real system: send via Gmail SMTP or an SMS gateway here
        print(f"📩 [SIMULATED SMS to {phone}] Your OTP is: {otp}")
        return otp

    def verify_otp(self, phone, entered_otp) -> bool:
        actual_otp = self._pending_otps.get(phone)
        if actual_otp is not None and actual_otp == entered_otp:
            del self._pending_otps[phone]  # OTP used only once
            return True
        return False


def requires_otp(threshold=10000):
    """
    Decorator factory implementing 'step-up authentication':
    functions wrapped with this require OTP verification if amount > threshold.

    Wrapped function signature must be: func(account, amount, *args, **kwargs)
    Caller must supply otp_service, phone, and entered_otp as keyword args.
    """

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
```

## 📄 `services/transaction_service.py`

```python
from models.transaction import Transaction
from services.otp_service import requires_otp
from repositories.account_repository import log_transaction
from exceptions import InsufficientBalanceError, InvalidOTPError
from ui.console import print_success, print_error, print_info

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
```

## 📄 `services/validators.py`

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


def get_valid_input(prompt, validator, error_message):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        print(f"❌ {error_message}")
```

## 📄 `repositories/__init__.py`

```python

```

## 📄 `repositories/account_repository.py`

```python
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
```

## 📄 `ui/__init__.py`

```python

```

## 📄 `ui/console.py`

```python
try:
    from colorama import Fore, init
    init(autoreset=True)
    _HAS_COLOR = True
except ImportError:
    # Falls back to plain text if colorama isn't installed
    _HAS_COLOR = False

    class _NoColor:
        def __getattr__(self, name):
            return ""

    Fore = _NoColor()


def print_success(message):
    print(Fore.GREEN + "✅ " + message)


def print_error(message):
    print(Fore.RED + "❌ " + message)


def print_info(message):
    print(Fore.CYAN + "ℹ️  " + message)


def print_menu(title, options):
    print(Fore.YELLOW + f"\n===== {title} =====")
    for key, label in options.items():
        print(f"{key}. {label}")
    print(Fore.YELLOW + "=" * (len(title) + 12))
```

## 📁 Final Runtime Folders

Create these folders as part of the final project structure. The application creates `data/logs/` automatically, but creating the folders up front is also fine.

```text
data/
└── logs/
```

The ZIP also contains generated runtime files such as `data/accounts.json`, `data/users.json`, and a dated transaction log. These are runtime data, not Python source code, so they are not required to build the application from scratch.

## ▶️ Final Run

From the `banking_app` project root, run:

```bash
python main.py
```
