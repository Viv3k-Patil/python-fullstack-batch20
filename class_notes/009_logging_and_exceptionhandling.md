# 📚 Logging & Exception Handling

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand why logging is essential in real-world applications
* 🎯 Use Python's built-in `logging` module effectively
* 🎯 Create and configure loggers, including file logging and log levels
* 🎯 Understand what exceptions are and why programs raise them
* 🎯 Use `try`, `except`, `else`, and `finally` blocks to handle errors gracefully
* 🎯 Create and use custom exceptions for domain-specific error handling

---

## 📖 Introduction

Have you ever used an app that suddenly crashed with no explanation? 😩 Frustrating, right? Real software doesn't just need to **work** — it needs to **fail gracefully**, tell developers exactly what went wrong, and keep a record of what happened for later investigation.

This topic covers two closely related survival skills for any developer:

* 📝 **Logging** — recording what your program is doing, so you (or your team) can understand its behavior later, especially when something goes wrong
* 🚨 **Exception Handling** — anticipating and gracefully managing errors, instead of letting your program crash unexpectedly

### 🤔 Why does this topic exist?

* 🕵️ When something breaks in a live application used by thousands of people, you can't just "watch it happen" — you need **logs** to investigate after the fact
* 💥 Programs will inevitably encounter unexpected situations (bad user input, network failures, missing files) — exception handling lets you respond to these safely instead of crashing
* 🏢 Every professional codebase you'll ever work on uses both of these techniques extensively

### 🤔 Where is it used?

* 🏦 Banking apps — every transaction is logged for auditing and fraud detection
* 🌐 Websites — server errors are logged so developers can fix bugs without needing the user to describe what happened
* 📱 Mobile apps — crash reports rely on logs to show developers exactly what led to a crash
* 🛒 E-commerce — try/except blocks prevent a single failed operation (like a broken payment gateway) from crashing the entire checkout process

> 💡 **Tip**
>
> Think of logging as your program's "flight recorder" (black box) ✈️ — quietly recording everything, so that if something goes wrong, you can rewind and see exactly what happened.

---

## 🧠 Detailed Notes

### 1️⃣ Importance of Logging in Real-World Apps

Many beginners rely on `print()` statements to debug their code. That works fine for small practice scripts, but it falls apart in real applications:

| `print()` Statements | Proper Logging |
|---|---|
| Always shows on screen, can't be turned off easily | Can be turned on/off, or filtered by severity level |
| No timestamp, no context, no severity level | Includes timestamp, severity level, and source info automatically |
| Disappears once the terminal closes | Can be saved permanently to a file for later review |
| Must be manually removed before final code | Can stay in the code permanently — it's meant to be there |
| Not organized — everything looks the same | Organized into levels: DEBUG, INFO, WARNING, ERROR, CRITICAL |

```python
# The "beginner way" — using print() for debugging
print("User logged in")
print("ERROR: Payment failed")     # looks exactly the same as any other print, easy to miss!

# The "professional way" — using logging
import logging
logging.info("User logged in")
logging.error("Payment failed")     # clearly marked as an ERROR, can be filtered/searched later
```

> ⚠️ **Important**
>
> `print()` statements are meant for showing information TO the user. Logging is meant for recording information FOR developers/administrators — they solve different problems, even though they might look similar at first glance.

🤔 **Quick thinking question:** Why is logging considered more "production-ready" than sprinkling `print()` statements throughout your code?
✅ **Answer:** Logging provides structured, filterable, permanently-stored records with severity levels and timestamps — while `print()` output disappears once the terminal closes and provides no way to control what's shown or search through it later.

---

### 2️⃣ Python's Logging Module

Python comes with a built-in `logging` module — no installation required. It provides **5 standard severity levels**, from least to most serious:

| Level | Numeric Value | When to Use | Example |
|---|---|---|---|
| `DEBUG` | 10 | Detailed info, useful only while developing/debugging | "Variable x = 42" |
| `INFO` | 20 | General confirmation that things are working as expected | "User logged in successfully" |
| `WARNING` | 30 | Something unexpected happened, but the program still works | "Disk space running low" |
| `ERROR` | 40 | A serious problem — some functionality failed | "Failed to save file" |
| `CRITICAL` | 50 | A very serious error — the program itself may be unable to continue | "Database connection lost" |

**Basic usage:**

```python
import logging

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
```

Output (by default, only WARNING and above are shown!):
```
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

Notice that `debug` and `info` messages didn't print — Python's default logging level is `WARNING`, meaning anything less severe is silently ignored unless you configure it otherwise.

```python
import logging

logging.basicConfig(level=logging.DEBUG)     # now show EVERYTHING, from DEBUG upward

logging.debug("This will now show!")
logging.info("This will now show too!")
```

> 💡 **Tip**
>
> Think of log levels like a **volume filter** — setting the level to `WARNING` means "only show me warnings and anything more serious"; setting it to `DEBUG` means "show me absolutely everything."

🤔 **Quick thinking question:** If you call `logging.info("Server started")` without any configuration, why might it NOT appear in your output?
✅ **Answer:** Because Python's default logging level is `WARNING` — `INFO` messages are considered less severe and are silently ignored unless you explicitly configure the logging level to `INFO` or lower (like `DEBUG`).

---

### 3️⃣ Creating and Configuring Loggers (File Logging, Log Levels)

**Configuring logging to write to a FILE instead of (or in addition to) the console:**

```python
import logging

logging.basicConfig(
    filename="app.log",                                   # log messages saved to this file
    level=logging.DEBUG,                                    # show all levels, DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s"      # customize how each log line looks
)

logging.debug("Application starting up...")
logging.info("User 'priya' logged in")
logging.warning("API response took longer than expected")
logging.error("Failed to connect to payment gateway")
logging.critical("Database is completely unreachable!")
```

This creates a file `app.log` containing:
```
2026-08-16 10:15:23,102 - DEBUG - Application starting up...
2026-08-16 10:15:23,105 - INFO - User 'priya' logged in
2026-08-16 10:15:24,210 - WARNING - API response took longer than expected
2026-08-16 10:15:25,330 - ERROR - Failed to connect to payment gateway
2026-08-16 10:15:26,001 - CRITICAL - Database is completely unreachable!
```

**Creating a custom, named logger** (the recommended, more professional approach in real projects):

```python
import logging

# Create a custom logger
logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)

# Create a handler that writes to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Create a formatter and attach it to the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Attach the handler to the logger
logger.addHandler(file_handler)

logger.info("This log goes through our custom logger!")
logger.error("Something went wrong in the payment module")
```

**Logging to BOTH the console AND a file at the same time (very common in real apps):**

```python
import logging

logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)

# Handler 1: writes to a file
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

# Handler 2: shows in the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)     # console only shows WARNING and above

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("Detailed debug info")           # only goes to the FILE
logger.warning("Something looks off")          # goes to BOTH the file AND the console
```

| Component | Purpose |
|---|---|
| `Logger` | The main object your code calls (`logger.info(...)`, etc.) |
| `Handler` | Decides WHERE the log goes — file, console, email, etc. |
| `Formatter` | Decides HOW each log message is structured/displayed |
| `Level` | Decides WHICH messages get through (filters by severity) |

> ⚠️ **Important**
>
> You can set DIFFERENT levels for the logger itself, and for each individual handler — this lets you, for example, save EVERYTHING to a file, while only showing WARNING and above in the console.

🤔 **Quick thinking question:** In the "console AND file" example, why does `logger.debug(...)` only appear in the file, but `logger.warning(...)` appears in both places?
✅ **Answer:** Because the `console_handler` is set to `WARNING` level, meaning it filters out anything less severe (like DEBUG) — while the `file_handler` is set to `DEBUG`, allowing everything through to the file.

---

### 4️⃣ Understanding Exceptions

An **exception** is an error that occurs DURING program execution, disrupting the normal flow. If not handled, it crashes the program and shows a "traceback" (error report).

```python
print("Before the error")
result = 10 / 0                # ZeroDivisionError — this crashes the program!
print("After the error")        # this line never runs
```

Output:
```
Before the error
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

**Common built-in exception types:**

| Exception | When It Happens | Example |
|---|---|---|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Wrong VALUE for the correct type | `int("abc")` |
| `TypeError` | Operation on an incompatible TYPE | `"5" + 5` |
| `IndexError` | Accessing a list index that doesn't exist | `[1,2,3][10]` |
| `KeyError` | Accessing a dictionary key that doesn't exist | `{"a":1}["b"]` |
| `FileNotFoundError` | Trying to open a file that doesn't exist | `open("missing.txt")` |
| `AttributeError` | Calling a method/attribute that doesn't exist on an object | `"hello".push()` |

> 💡 **Tip**
>
> Exceptions aren't necessarily "bad" — they're Python's way of telling you clearly and specifically WHAT went wrong, instead of silently producing incorrect results.

🤔 **Quick thinking question:** What is the key difference between a `SyntaxError` and a runtime exception like `ZeroDivisionError`?
✅ **Answer:** A `SyntaxError` means Python couldn't even understand/parse your code (the program never starts running), while a runtime exception like `ZeroDivisionError` occurs DURING execution — the code was valid, but something went wrong while it was actually running.

---

### 5️⃣ Try, Except, Else, Finally Blocks

Python provides a structured way to **catch** exceptions and respond to them gracefully, instead of crashing.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ You can't divide by zero!")

print("Program continues running normally 🎉")
```

Output:
```
❌ You can't divide by zero!
Program continues running normally 🎉
```

**Catching multiple, specific exception types:**

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError:
    print("❌ You can't divide by zero!")
```

**Catching multiple exceptions with ONE handler:**

```python
try:
    risky_operation()
except (ValueError, TypeError) as e:
    print(f"❌ Something went wrong: {e}")
```

**The full structure — `try`, `except`, `else`, `finally`:**

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError:
    print("❌ You can't divide by zero!")
else:
    print(f"✅ Success! Result: {result}")      # runs ONLY if NO exception occurred
finally:
    print("🔚 This always runs, no matter what.")  # runs REGARDLESS of success or failure
```

```
             try/except/else/finally FLOW
             --------------------------------
     try:  ──► code that might raise an exception
       │
       ├── ❌ Exception occurs ──► matching except block runs
       │
       └── ✅ No exception ──► else block runs

     finally:  ──► ALWAYS runs, no matter what happened above
```

| Block | When It Runs |
|---|---|
| `try` | Always attempted first — contains the "risky" code |
| `except` | Runs ONLY if a matching exception occurs inside `try` |
| `else` | Runs ONLY if NO exception occurred in `try` |
| `finally` | ALWAYS runs — whether an exception occurred or not (great for cleanup like closing files) |

**A realistic file-handling example, showing `finally` used for cleanup:**

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("❌ File not found!")
else:
    print("✅ File read successfully!")
    print(content)
finally:
    print("🔒 Closing resources (if file was opened)...")
```

> ⚠️ **Important**
>
> `finally` is commonly used to **release resources** — closing files, database connections, or network sockets — because it guarantees that cleanup code runs, even if an error occurred.

🤔 **Quick thinking question:** Why would a developer put `file.close()` inside a `finally` block instead of just at the end of the `try` block?
✅ **Answer:** If an exception occurs partway through the `try` block, any code AFTER that point (including a `file.close()` at the end of `try`) would be skipped entirely — but code inside `finally` is GUARANTEED to run regardless, ensuring the file always gets properly closed.

---

### 6️⃣ Creating and Using Custom Exceptions

Sometimes Python's built-in exceptions (`ValueError`, `TypeError`, etc.) aren't specific enough for YOUR application's needs. You can create your OWN exception types by creating a class that inherits from `Exception`.

```python
class InsufficientBalanceError(Exception):        # custom exception — inherits from Exception
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Cannot withdraw ₹{amount}, balance is only ₹{self.balance}")
        self.balance -= amount
        print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}")

account = BankAccount(1000)

try:
    account.withdraw(5000)
except InsufficientBalanceError as e:
    print(f"❌ Transaction failed: {e}")
```

Output:
```
❌ Transaction failed: Cannot withdraw ₹5000, balance is only ₹1000
```

**Adding extra data/context to a custom exception using `__init__`:**

```python
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)         # pass the message up to the base Exception class

def register_user(name, age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    print(f"✅ Registered {name}, age {age}")

try:
    register_user("Rahul", 200)
except InvalidAgeError as e:
    print(f"❌ Registration failed: {e.message} (you entered: {e.age})")
```

**Building a small hierarchy of custom exceptions (common in larger real projects):**

```python
class ApplicationError(Exception):                  # base custom exception for the whole app
    pass

class InsufficientBalanceError(ApplicationError):     # specific error types inherit from it
    pass

class InvalidAccountError(ApplicationError):
    pass

try:
    raise InsufficientBalanceError("Not enough funds")
except ApplicationError as e:                              # catches ANY error in the hierarchy
    print(f"❌ App error occurred: {e}")
```

| Concept | Purpose |
|---|---|
| `class MyError(Exception):` | Creates a new, custom exception type |
| `raise MyError("message")` | Triggers the custom exception, with an optional message |
| Custom exception hierarchies | Let you catch either a SPECIFIC error, or ANY error from a related family, using the shared parent class |

> 💡 **Tip**
>
> Custom exceptions make your error messages far more meaningful. `InsufficientBalanceError` immediately tells another developer exactly what went wrong — much clearer than a generic `ValueError`.

🤔 **Quick thinking question:** Why might a real banking application define its own `InsufficientBalanceError` instead of just using Python's built-in `ValueError` for the same situation?
✅ **Answer:** A custom exception name like `InsufficientBalanceError` immediately communicates the EXACT business problem to anyone reading the code or logs, making debugging much faster — a generic `ValueError` could mean almost anything and requires reading the message to understand the actual issue.

---

## 💡 Real-Life Analogy

* ✈️ **Logging → An Airplane's Black Box Flight Recorder** — It quietly records everything happening throughout the flight (INFO), notes unusual turbulence (WARNING), and captures critical system failures (CRITICAL) — all so investigators can later understand exactly what happened, even without watching the flight live.
* 🚦 **Exceptions → A Car's Warning Lights Dashboard** — When something goes wrong (low fuel, engine issue), the car doesn't just silently break down — it raises a clear signal (an exception) telling the driver exactly what's wrong, so they can respond appropriately.
* 🛡️ **try/except → A Safety Net Under a Tightrope Walker** — The tightrope walker (your risky code) attempts something that could fail; if they DO fall (an exception occurs), the safety net (`except`) catches them gracefully instead of letting them crash to the ground.
* 🧹 **finally → Cleaning Up After a Cooking Class, No Matter What Happened** — Whether the dish turned out perfectly (`else`) or was a total disaster (`except`), you ALWAYS clean the kitchen (`finally`) before leaving.
* 🏷️ **Custom Exceptions → Specific, Labeled Warning Signs Instead of a Generic "Caution" Sign** — A generic "Caution" sign (built-in `ValueError`) tells you something's wrong, but a specific sign like "Wet Floor" (`InsufficientBalanceError`) tells you EXACTLY what to watch out for.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Logging | Every major tech company (Google, Amazon, Netflix) uses extensive logging to monitor and debug live production systems |
| File/rotating logs | Server applications (like Django/Flask apps) commonly log to files, often rotated daily to avoid huge log files |
| Exception handling | Payment gateways (Razorpay, Stripe) wrap risky operations in try/except to prevent one failed transaction from crashing the whole checkout flow |
| Custom exceptions | Django's ORM has custom exceptions like `ObjectDoesNotExist`; many APIs define custom exceptions like `InvalidTokenError` |
| Log levels | DevOps monitoring tools (like Datadog, Splunk) filter and alert based on log severity levels (e.g., alert only on ERROR/CRITICAL) |

---

## 🔍 Industry Example

**Scenario:** A **Backend Developer at an e-commerce company** (similar to Flipkart) is handling the "Place Order" feature, which involves checking stock, charging payment, and updating the database.

1. They wrap the ENTIRE order-placement logic in a `try/except` block, since many things could go wrong: insufficient stock, payment gateway failure, database connection issues.
2. For each specific failure type, they define a **custom exception**: `OutOfStockError`, `PaymentFailedError`, `DatabaseConnectionError` — each inheriting from a shared `OrderProcessingError` base exception.
3. When an error occurs, instead of crashing the whole server, the `except` block gracefully returns a clear error message to the user (e.g., "This item is out of stock") while the FULL technical details are recorded using the `logging` module.
4. They configure their logger to write `DEBUG` and `INFO` level messages only to a file (for detailed internal review), while `ERROR` and `CRITICAL` messages are ALSO sent to their team's monitoring dashboard in real-time, so engineers get alerted immediately if something serious breaks.
5. The `finally` block ensures that database connections are always properly closed and any temporary "processing" locks on the order are released — regardless of whether the order succeeded or failed.

This combination of structured logging and custom exception handling is exactly what keeps real, high-traffic e-commerce platforms stable and debuggable.

---

## 📊 Diagram

```
              TRY / EXCEPT / ELSE / FINALLY FLOW
              -------------------------------------

     try:
         risky_code()
              │
       ┌──────┴──────┐
       ▼               ▼
   ❌ Exception      ✅ No Exception
       │               │
       ▼               ▼
   except:          else:
   handle error     success code runs
       │               │
       └───────┬───────┘
               ▼
          finally:
          ALWAYS runs (cleanup, closing files, etc.)


          LOG LEVEL SEVERITY SCALE
          ----------------------------
     DEBUG  <  INFO  <  WARNING  <  ERROR  <  CRITICAL
      🔍         ℹ️         ⚠️          ❌          🔥
    (least severe) ───────────────────► (most severe)


          CUSTOM EXCEPTION HIERARCHY
          ------------------------------
                Exception (built-in)
                     ▲
                     │
              ApplicationError (custom base)
                 ▲            ▲
                 │            │
     InsufficientBalanceError  InvalidAccountError
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Using `print()` statements everywhere is just as good as proper logging."
  ✅ **Correct:** Logging provides severity levels, timestamps, permanent file storage, and the ability to filter — none of which `print()` offers.

* ❌ **Wrong belief:** "`logging.info(...)` will always show up when you run your program."
  ✅ **Correct:** Python's default logging level is `WARNING` — `INFO` and `DEBUG` messages are hidden unless you explicitly configure a lower level using `logging.basicConfig(level=...)`.

* ❌ **Wrong belief:** "Wrapping your entire program in one giant `try/except` block is good practice."
  ✅ **Correct:** It's better to wrap only the SPECIFIC risky code in `try/except`, and catch SPECIFIC exception types — catching everything broadly can hide real bugs and make debugging much harder.

* ❌ **Wrong belief:** "The `finally` block only runs if an exception occurred."
  ✅ **Correct:** `finally` ALWAYS runs — whether the `try` block succeeded, failed, or even if a `return` statement was hit inside the `try` block.

* ❌ **Wrong belief:** "Custom exceptions need lots of special code to work properly."
  ✅ **Correct:** A custom exception can be as simple as `class MyError(Exception): pass` — inheriting from `Exception` is often all that's needed to create a perfectly usable custom exception type.

---

## 💬 Interview Corner

**Q1: What is the difference between using `print()` statements and using the `logging` module for debugging?**
✅ Logging provides structured severity levels, timestamps, the ability to write to files, and fine-grained control over what gets shown/recorded — `print()` offers none of this and is meant for simple, temporary output.

**Q2: What is the difference between the `except` and `finally` blocks?**
✅ `except` runs ONLY if a matching exception occurs in the `try` block. `finally` ALWAYS runs, regardless of whether an exception occurred or not — commonly used for cleanup tasks like closing files or database connections.

**Q3: Why would you create a custom exception instead of using a built-in one like `ValueError`?**
✅ A custom exception (e.g., `InsufficientBalanceError`) communicates the exact business problem clearly, making code and error logs far easier to understand and debug compared to a generic built-in exception.

**Q4: What are Python's five standard logging levels, in order of increasing severity?**
✅ `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` — from least severe (detailed debugging info) to most severe (a critical failure that may stop the program).

---

## 📝 Quick Summary

* 📝 Logging is the professional replacement for scattered `print()` debugging statements
* 🎚️ Python's `logging` module has 5 severity levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
* ⚙️ `logging.basicConfig()` lets you quickly configure level, format, and output file
* 🗂️ Custom loggers, handlers, and formatters give fine-grained control — e.g., logging everything to a file while only showing warnings+ in the console
* 💥 An exception is an error that occurs during program execution, disrupting normal flow
* 🛡️ `try/except` catches and gracefully handles exceptions instead of letting the program crash
* ✅ `else` runs only if NO exception occurred; 🔚 `finally` ALWAYS runs, regardless of success or failure
* 🏷️ Custom exceptions (`class MyError(Exception)`) let you create meaningful, application-specific error types
* 🎯 Combining logging with structured exception handling is essential for building stable, debuggable, real-world software

---

## 🎯 Class Activity

**"Build a Logged & Error-Safe Calculator" 🧮**

1. Set up a custom logger that writes DEBUG and above to a file called `calculator.log`, and WARNING and above to the console.
2. Write a `divide(a, b)` function wrapped in `try/except/else/finally`, that logs an `error` if division by zero occurs, and logs an `info` message showing the successful result otherwise.
3. Create a custom exception `NegativeNumberError` and raise it inside a `square_root(n)` function if `n` is negative, logging an `error` message when this happens.
4. Test your program with at least 3 different inputs (a valid division, a division by zero, and a negative square root) and check the contents of `calculator.log` afterward.
5. Bonus: Add a `finally` block that logs `"Calculation attempt finished"` every single time, regardless of success or failure.


---

# 📋 Assignments — Logging & Exception Handling

| Assignment |
|---|
| Set up basic logging using `logging.basicConfig()` with level set to `DEBUG`, and write one log message for each of the 5 severity levels. |
| Configure a logger that writes all log messages to a file called `activity.log`, using the format `"timestamp - level - message"`. |
| Write a program with a custom logger that logs to BOTH a file (all levels) and the console (WARNING and above only), and test it with several log calls. |
| Write a program that intentionally causes a `ZeroDivisionError`, and handle it using `try/except` with a friendly error message instead of crashing. |
| Write a program that asks the user for a number using `input()`, and handles a `ValueError` gracefully if they type letters instead of a number. |
| Write a `try/except/else/finally` block that opens a file, reads its content, and handles a `FileNotFoundError` if the file doesn't exist, always printing "Operation complete" in the `finally` block. |
| Create a custom exception `InvalidAgeError` and use it inside a function that registers a user, rejecting ages below 0 or above 120. |
| Create a custom exception `InsufficientStockError` for a simple inventory system, and raise it when someone tries to order more items than are in stock. |
| Combine logging and exception handling: whenever your `InsufficientStockError` is raised, log an `error`-level message with the details before showing a friendly message to the user. |
| Write a function that can raise THREE different exception types (`ValueError`, `ZeroDivisionError`, `TypeError`) depending on the input, and handle all three with separate `except` blocks. |
| Create a small custom exception hierarchy: a base `BankError`, with `InsufficientBalanceError` and `InvalidPinError` inheriting from it, and demonstrate catching the SPECIFIC error vs. the BASE error. |
| Write a program that logs every user login attempt (success or failure) to a file, including a timestamp and username, using the `logging` module. |
| Test what happens if you forget to add an `except` block for a specific exception, and let the program actually crash — copy the full traceback into a comment and explain what it means. |
| Write a `withdraw_money(balance, amount)` function that raises a custom `InsufficientBalanceError` with a clear message, and logs a `warning` every time a withdrawal attempt fails. |
| Write a short reflection (3–5 sentences) explaining, in your own words, why combining logging WITH exception handling is more powerful than using either one alone. |
