# 📚 Decorators in Python

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand first-class functions and how Python treats functions as values
* 🎯 Understand closures and how inner functions can "remember" outer variables
* 🎯 Understand what a decorator is and why it's useful
* 🎯 Create and use simple custom decorators
* 🎯 Apply decorators to real practical use cases like logging and validation

---

## 📖 Introduction

Imagine you have 10 different functions in your app, and you suddenly need to add "logging" (recording when each function runs) to **all** of them. Would you go into each function and add a `print()` statement manually? That's repetitive and messy. 😩

**Decorators** solve exactly this problem — they let you **add extra behavior to a function without changing its actual code**, by "wrapping" it with another function.

### 🤔 Why does this topic exist?

* ♻️ Decorators let you reuse cross-cutting behavior (logging, timing, validation, access control) across many functions without duplicating code
* 🧹 They keep your core business logic clean and separate from repetitive "extra" tasks
* 🏗️ Nearly every professional Python framework (Flask, Django, FastAPI) is built heavily around decorators

### 🤔 Where is it used?

* 🌐 Web frameworks — `@app.route('/home')` in Flask defines a URL route using a decorator
* 🔐 Authentication systems — `@login_required` decorators protect certain pages/functions
* ⏱️ Performance monitoring — `@measure_time` decorators log how long a function takes to run
* 📝 Logging systems — `@log_activity` decorators record every function call automatically

> 💡 **Tip**
>
> Decorators can feel a bit abstract at first — but once the "aha moment" clicks, you'll start seeing them as one of Python's most elegant and powerful features.

---

## 🧠 Detailed Notes

### 1️⃣ Understanding First-Class Functions & Closures

**First-class functions** means functions in Python are treated just like any other value (numbers, strings, lists) — they can be:

* Assigned to a variable
* Passed as an argument to another function
* Returned from another function
* Stored inside lists/dictionaries

```python
def greet():
    return "Hello! 👋"

# Assigning a function to a variable (without calling it — no parentheses!)
say_hello = greet
print(say_hello())        # Hello! 👋

# Passing a function as an argument
def call_function(func):
    return func()

print(call_function(greet))    # Hello! 👋

# Storing functions inside a list
functions_list = [greet, print]
print(functions_list[0]())      # Hello! 👋
```

> ⚠️ **Important**
>
> `greet` (no parentheses) refers to the **function itself** as an object. `greet()` (with parentheses) actually **calls/runs** the function. This distinction is essential for understanding decorators.

**Closures** — an inner (nested) function that "remembers" the variables from its outer function's scope, even after the outer function has finished running.

```python
def outer_function(greeting):
    def inner_function(name):              # inner_function is defined INSIDE outer_function
        print(f"{greeting}, {name}!")       # it can access 'greeting' from the outer scope
    return inner_function                    # returning the FUNCTION itself, not calling it

say_hello = outer_function("Hello")     # outer_function runs once, returns inner_function
say_hello("Priya")                        # Hello, Priya!
say_hello("Rahul")                        # Hello, Rahul!

say_namaste = outer_function("Namaste")
say_namaste("Ananya")                     # Namaste, Ananya!
```

Notice that even though `outer_function("Hello")` finished running long ago, `say_hello` still "remembers" that `greeting = "Hello"` — this memory is exactly what a **closure** is.

```
   outer_function("Hello")
         │
         ▼
   creates inner_function, which "closes over" greeting="Hello"
         │
         ▼
   returns inner_function  ──►  stored in say_hello
         │
         ▼
   say_hello("Priya")  ──►  still remembers greeting="Hello"!
```

🤔 **Quick thinking question:** Why does `say_hello("Priya")` still know the value of `greeting`, even though `outer_function` already finished executing?
✅ **Answer:** Because `inner_function` forms a **closure** — it "closes over" (captures and remembers) the variables from its enclosing scope at the time it was created, keeping them alive even after the outer function has returned.

---

### 2️⃣ What is a Decorator and Why We Use It

A **decorator** is a function that takes another function as input, adds some extra behavior around it, and returns a new, "enhanced" function — all without modifying the original function's actual code.

```python
def my_decorator(func):
    def wrapper():
        print("Something happens BEFORE the function runs 🔵")
        func()                                                # call the original function
        print("Something happens AFTER the function runs 🔴")
    return wrapper

def say_hello():
    print("Hello! 👋")

decorated_function = my_decorator(say_hello)    # manually "decorating"
decorated_function()
```

Output:
```
Something happens BEFORE the function runs 🔵
Hello! 👋
Something happens AFTER the function runs 🔴
```

Python provides a much cleaner shortcut for this using the `@` symbol:

```python
def my_decorator(func):
    def wrapper():
        print("Something happens BEFORE the function runs 🔵")
        func()
        print("Something happens AFTER the function runs 🔴")
    return wrapper

@my_decorator          # this is EXACTLY equivalent to: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello! 👋")

say_hello()             # calling say_hello now actually runs the WRAPPED version
```

The output is identical to before — but the syntax is much cleaner and doesn't require manually reassigning the function.

| Without `@` syntax | With `@` syntax |
|---|---|
| `say_hello = my_decorator(say_hello)` written manually below the function | `@my_decorator` written directly above the function definition |
| Works the same way | Cleaner, more readable, the "Pythonic" way |

> 💡 **Tip**
>
> A decorator doesn't change what's inside the original function — it just wraps EXTRA behavior around it, before and/or after it runs.

🤔 **Quick thinking question:** What does `@my_decorator` placed directly above `def say_hello():` actually do behind the scenes?
✅ **Answer:** It's shorthand for `say_hello = my_decorator(say_hello)` — Python automatically passes `say_hello` into `my_decorator`, and reassigns `say_hello` to be the returned `wrapper` function.

---

### 3️⃣ Creating and Using Simple Decorators

**Handling functions that take arguments** — using `*args` and `**kwargs` so the decorator works with ANY function, regardless of how many parameters it has:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):       # accepts any number of positional/keyword arguments
        print("Before the function runs...")
        result = func(*args, **kwargs)    # pass them along to the original function
        print("After the function runs...")
        return result                       # don't forget to return the original result!
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print(add(5, 3))                # Before... 8  After...
greet_user("Priya")              # Before... Hello, Priya!  After...
greet_user("Rahul", greeting="Hi")   # Before... Hi, Rahul!  After...
```

**Stacking multiple decorators** — you can apply more than one decorator to the same function:

```python
def bold_decorator(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic_decorator(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold_decorator
@italic_decorator
def get_text():
    return "Hello!"

print(get_text())    # <b><i>Hello!</i></b>
```

Decorators are applied **bottom to top** — `italic_decorator` wraps first, then `bold_decorator` wraps the result.

**Using `functools.wraps` to preserve the original function's identity:**

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)              # preserves func's original __name__, docstring, etc.
    def wrapper(*args, **kwargs):
        print("Wrapping...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """This function greets someone."""
    print("Hello!")

print(greet.__name__)     # greet   (WITHOUT @wraps, this would incorrectly show 'wrapper')
print(greet.__doc__)       # This function greets someone.
```

> ⚠️ **Important**
>
> Without `*args, **kwargs` in your `wrapper()`, your decorator will ONLY work on functions that take zero arguments — always use `*args, **kwargs` to make decorators flexible and reusable across different functions.

🤔 **Quick thinking question:** In the stacked decorator example, why does `@bold_decorator` end up wrapping the OUTSIDE (bold tags on the outer edge), even though it's written on TOP?
✅ **Answer:** Decorators apply bottom-to-top: the one closest to the function (`@italic_decorator`) wraps first, and then `@bold_decorator` wraps around that already-wrapped result — so its effect appears on the outside.

---

### 4️⃣ Practical Applications of Decorators (Logging, Validation)

**Logging decorator** — automatically records when a function is called and with what arguments:

```python
from functools import wraps
import datetime

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"📝 [{timestamp}] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📝 [{timestamp}] '{func.__name__}' finished, returned: {result}")
        return result
    return wrapper

@log_activity
def calculate_total(price, quantity):
    return price * quantity

calculate_total(500, 3)
```

Output:
```
📝 [14:32:10] Calling 'calculate_total' with args=(500, 3), kwargs={}
📝 [14:32:10] 'calculate_total' finished, returned: 1500
```

**Validation decorator** — checks input data before allowing the actual function to run:

```python
from functools import wraps

def validate_positive_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, (int, float)) and value < 0:
                print(f"❌ Invalid input: {value}. All numbers must be positive.")
                return None
        return func(*args, **kwargs)
    return wrapper

@validate_positive_numbers
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))      # ✅ 15
print(calculate_area(-5, 3))      # ❌ Invalid input: -5. All numbers must be positive.  → None
```

**A timing decorator** (very common in real projects, to measure performance):

```python
import time
from functools import wraps

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ '{func.__name__}' took {end - start:.4f} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1)
    print("Done sleeping!")

slow_function()
```

| Real Decorator Use Case | What It Does |
|---|---|
| `@log_activity` | Records every function call, its inputs, and its output |
| `@validate_positive_numbers` | Blocks a function from running if invalid data is passed in |
| `@measure_time` | Tracks how long a function takes to execute |
| `@login_required` (common in web apps) | Blocks access to a function/page unless the user is logged in |
| `@cache` (common for performance) | Stores previous results so expensive calculations aren't repeated |

🤔 **Quick thinking question:** Why is a validation decorator considered better practice than putting the same validation `if` check inside every single function that needs it?
✅ **Answer:** Writing the validation logic once inside a decorator and reusing it across multiple functions avoids code duplication — if the validation rule ever changes, you only need to update it in ONE place (the decorator), not in every function individually.

---

## 💡 Real-Life Analogy

* 🎁 **Decorator → Gift Wrapping Paper** — The actual gift (original function) stays exactly the same inside; the wrapping paper (decorator) just adds something extra around it (a nice appearance, a ribbon) without changing the gift itself.
* 🍔 **Closures → A Sandwich Recipe Card That Remembers Your Custom Order** — Once you tell the chef "no onions" (outer function variable), every sandwich (inner function call) they make for you afterward automatically remembers and applies that preference.
* 🛂 **Validation Decorator → An Airport Security Checkpoint** — Before you (the function) are allowed to board the plane (execute), security (the decorator) checks your documents first. If something's invalid, you're stopped before you ever reach your seat.
* 📋 **Logging Decorator → A Visitor Sign-In Register at an Office** — Every time someone enters a room (calls a function), the register automatically records the time and their name — without the visitor having to do anything extra themselves.

---

## 💻 Real-World Application

| Use Case | Real Company / Framework Usage |
|---|---|
| Web routing | Flask's `@app.route('/login')` decorator maps URLs to functions |
| Authentication | Django's `@login_required` decorator restricts page access to logged-in users |
| Caching | Python's built-in `@functools.lru_cache` speeds up repeated expensive function calls |
| API rate limiting | Many REST APIs use decorators like `@rate_limit` to control how often a function can be called |
| Testing frameworks | Pytest uses decorators like `@pytest.fixture` and `@pytest.mark.parametrize` extensively |
| Timing/Profiling | Performance monitoring tools often use custom `@measure_time`-style decorators in production code |

---

## 🔍 Industry Example

**Scenario:** A **Backend Developer at Zomato** needs to add logging AND input validation to dozens of existing functions (like `place_order()`, `cancel_order()`, `update_address()`) — without touching each function's internal logic.

1. Instead of manually adding `print()` statements and `if` validation checks inside every single function, the developer writes **one** reusable `@log_activity` decorator and **one** reusable `@validate_input` decorator.
2. They simply add `@log_activity` above each function they want to track — instantly, every order placement, cancellation, and address update gets automatically logged with timestamps, without changing a single line inside those functions.
3. For functions that require positive numeric values (like order quantity), they apply `@validate_positive_numbers` — protecting the business logic from ever running with invalid data.
4. When the team later needs to add **caching** to a slow, frequently-called function (like `get_restaurant_menu()`), they simply add Python's built-in `@functools.lru_cache` decorator — instantly improving performance with just one line, no logic rewrite needed.
5. Because decorators are reusable, the exact same `@log_activity` decorator ends up being used across hundreds of functions throughout Zomato's codebase — a perfect real-world demonstration of the DRY principle ("Don't Repeat Yourself").

---

## 📊 Diagram

```
              HOW A DECORATOR WORKS
              ------------------------

    @my_decorator
    def say_hello():
        print("Hello!")

           is EXACTLY equivalent to:

    def say_hello():
        print("Hello!")

    say_hello = my_decorator(say_hello)


         WRAPPER FUNCTION FLOW
         ------------------------
    Calling say_hello()
           │
           ▼
    ┌─────────────────────────────┐
    │  wrapper() runs               │
    │   ┌─────────────────────┐    │
    │   │ BEFORE code runs 🔵  │    │
    │   │                       │    │
    │   │  func() ── original   │    │
    │   │  function actually    │    │
    │   │  runs here             │    │
    │   │                       │    │
    │   │ AFTER code runs 🔴   │    │
    │   └─────────────────────┘    │
    └─────────────────────────────┘


         STACKED DECORATORS (bottom-to-top)
         --------------------------------------
    @bold_decorator        ← applied 2nd (outer layer)
    @italic_decorator      ← applied 1st (inner layer)
    def get_text():
        return "Hello!"

    Result:  <b><i>Hello!</i></b>
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "A decorator modifies the actual source code of the original function."
  ✅ **Correct:** A decorator wraps the original function with extra behavior — it never touches or changes the original function's internal code.

* ❌ **Wrong belief:** "My decorator's `wrapper()` doesn't need `*args, **kwargs` since my function doesn't take arguments right now."
  ✅ **Correct:** Always include `*args, **kwargs` in `wrapper()` so your decorator remains flexible and reusable for ANY function, even ones with different parameter counts, now or in the future.

* ❌ **Wrong belief:** "Forgetting to `return result` inside `wrapper()` is fine as long as the function prints something."
  ✅ **Correct:** If `wrapper()` doesn't `return` the original function's result, the decorated function will always return `None` — silently breaking any code that depends on the actual return value.

* ❌ **Wrong belief:** "Stacked decorators are applied top to bottom."
  ✅ **Correct:** They're applied **bottom to top** — the decorator closest to the function definition wraps first.

* ❌ **Wrong belief:** "Using `@wraps(func)` is optional and doesn't really matter."
  ✅ **Correct:** Without `@wraps(func)` from `functools`, the decorated function loses its original name and docstring (both become `wrapper`'s), which can break debugging tools, documentation generators, and testing frameworks.

---

## 💬 Interview Corner

**Q1: What is a decorator in Python, and why is it useful?**
✅ A decorator is a function that takes another function, adds extra behavior around it, and returns a new function — without modifying the original function's code. It's useful for reusable cross-cutting tasks like logging, validation, timing, and access control.

**Q2: What is a closure, and how does it relate to decorators?**
✅ A closure is an inner function that remembers variables from its enclosing (outer) function's scope even after the outer function has finished executing. Decorators rely on closures — the `wrapper()` function "remembers" the original `func` passed into the decorator.

**Q3: Why do decorator `wrapper()` functions typically use `*args, **kwargs`?**
✅ To make the decorator generic and reusable across ANY function, regardless of how many positional or keyword arguments that function accepts.

**Q4: What does `@functools.wraps(func)` do, and why is it recommended?**
✅ It preserves the original function's metadata (like `__name__` and docstring) on the wrapped version, which would otherwise be overwritten by the wrapper function's own metadata — important for debugging and documentation.

---

## 📝 Quick Summary

* 🧩 First-class functions mean functions can be assigned to variables, passed as arguments, and returned from other functions — just like any other value
* 🔒 Closures let an inner function "remember" variables from its enclosing outer function, even after that outer function has finished running
* 🎁 A decorator wraps a function with extra behavior, without modifying the original function's actual code
* ✨ `@decorator_name` syntax is shorthand for `func = decorator_name(func)`
* 🧮 Always use `*args, **kwargs` in your `wrapper()` so your decorator works with any function signature
* 🔁 Always `return` the original function's result from inside `wrapper()`, or you'll silently lose it
* 🥪 Multiple decorators can be stacked — they apply bottom to top
* 🏷️ Use `@functools.wraps(func)` to preserve the original function's name and docstring
* 📝 Real practical decorators include logging, input validation, timing/performance measurement, and access control

---

## 🎯 Class Activity

**"Build Your Own Decorator Toolkit" 🧰**

1. Write a simple decorator `@shout` that converts a function's returned string to uppercase, and apply it to a function that returns a greeting.
2. Write a `@log_activity` decorator (like the one shown in this topic) and apply it to 3 different functions of your choice with different parameter counts.
3. Write a `@validate_positive_numbers` decorator and apply it to a `calculate_discL_price(price, discount)` function, testing it with both valid and invalid (negative) inputs.
4. Write a `@measure_time` decorator using the `time` module, and apply it to a function that deliberately takes 2 seconds using `time.sleep(2)`.
5. Bonus: Stack two of your own decorators on a single function and predict the output order before running the code.


---

# 📋 Assignments — Decorators in Python

| Assignment |
|---|
| Write a function `outer_multiplier(factor)` that returns an inner function which multiplies any number passed to it by `factor` — demonstrating closures. Test it with factor=2 and factor=5. |
| Create a simple decorator `@add_exclamation` that adds "!" to the end of any string a function returns, and apply it to a `get_message()` function. |
| Write a `@log_activity` decorator and apply it to a `withdraw_money(account, amount)` function, confirming it logs both the call and the result correctly. |
| Write a `@validate_positive_numbers` decorator and apply it to a `calculate_area(length, width)` function, testing with both valid and negative inputs. |
| Write a `@measure_time` decorator and use it on a function that loops 1 million times, printing how long the loop took. |
| Create a decorator `@count_calls` that keeps track of (and prints) how many times a decorated function has been called so far, across multiple calls. |
| Stack two decorators — `@uppercase` and `@add_exclamation` — on a single function that returns a greeting, and predict the final output before running it. |
| Write a decorator `@require_non_empty` that checks if a string argument passed to a function is non-empty before allowing the function to run. |
| Use `functools.wraps` in a custom decorator and prove (using `.__name__`) that the original function's name is preserved correctly. |
| Write a decorator `@retry` that automatically calls a function up to 3 times if it raises an exception (hint: use try/except inside the wrapper). |
| Apply Python's built-in `@functools.lru_cache` to a slow recursive Fibonacci function and compare execution time with and without the cache. |
| Write a decorator `@currency_formatter` that formats a function's numeric return value as `"₹X,XXX.XX"` before returning it. |
| Create a decorator `@check_even` that only allows a function to run if a number argument passed to it is even, otherwise prints an error message. |
| Write your own real-world use case (different from the notes) where a decorator would be genuinely useful, and implement a working example of it. |
| Combine a `@log_activity` and a `@validate_positive_numbers` decorator on the same `process_payment(amount)` function, and test with both valid and invalid inputs. |
# 📚 Mini Project — Role-Based Access Control using Decorators

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand the difference between authentication and authorization
* 🎯 Design a role-based permission system using employee data
* 🎯 Build custom decorators that enforce access control on business logic functions
* 🎯 Use `@decorator` syntax to dynamically allow or deny access based on a user's role
* 🎯 Apply everything learned about functions, closures, and decorators into one complete, realistic mini project

---

## 📖 Introduction

Every real application needs to answer two important security questions: **"Who are you?"** and **"What are you allowed to do?"** 🔐 In this mini project, we'll build a simplified **Role-Based Access Control (RBAC)** system — exactly like the permission systems used in real company software (like an HR portal or admin dashboard) — using nothing but functions and decorators.

### 🤔 Why does this topic exist?

* 🏢 Nearly every business application has different user roles (Admin, Manager, Employee) with different permissions
* 🔐 Access control is one of the most important, non-negotiable parts of real-world software security
* 🎓 This project ties together everything learned in the previous topic — closures, decorators, `*args/**kwargs` — into one cohesive, practical build

### 🤔 Where is it used?

* 🏢 HR software (like Zoho People, Darwinbox) — only Managers/HR can approve leave requests
* 💰 Banking dashboards — only certain staff roles can approve large transactions
* 🛠️ Admin panels of any website — only Admins can delete users or change site settings
* 🏥 Hospital systems — only Doctors can prescribe medicine; Nurses have different permissions

> 💡 **Tip**
>
> This exact pattern — decorators enforcing role checks — is used in real frameworks like Flask (`@login_required`, `@roles_required`) and Django (`@permission_required`).

---

## 🧠 Detailed Notes

### 1️⃣ Enforcing Access Control Based on User Roles and Permissions

We start by setting up a simple **employee database** (a dictionary), where each employee has a role.

```python
employees = {
    "priya": {"password": "priya123", "role": "admin"},
    "rahul": {"password": "rahul123", "role": "manager"},
    "ananya": {"password": "ananya123", "role": "employee"},
}
```

We then define which roles are allowed to perform which actions:

```python
permissions = {
    "view_reports": ["admin", "manager", "employee"],
    "approve_leave": ["admin", "manager"],
    "delete_employee": ["admin"],
}
```

**A decorator that checks role-based permission before allowing a function to run:**

```python
from functools import wraps

current_user = None    # tracks who is currently "logged in"

def requires_permission(action):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user is None:
                print("❌ Access Denied: No user is logged in.")
                return None

            user_role = employees[current_user]["role"]

            if user_role not in permissions.get(action, []):
                print(f"❌ Access Denied: '{current_user}' ({user_role}) cannot perform '{action}'.")
                return None

            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Notice this is a **decorator that takes an argument** (`action`) — it's actually a "decorator factory": a function that returns a decorator, customized for a specific permission check.

```
   requires_permission("approve_leave")
              │
              ▼
      returns a REAL decorator, customized to check for "approve_leave" permission
              │
              ▼
   @requires_permission("approve_leave")
   def approve_leave_request(...): ...
```

🤔 **Quick thinking question:** Why does `requires_permission` need THREE nested functions (`requires_permission` → `decorator` → `wrapper`) instead of the usual two we saw in the previous topic?
✅ **Answer:** Because `requires_permission` needs to accept an **argument** (`action`) before it can even become a decorator — the extra outer layer captures that argument via closure, and the resulting `decorator` function then behaves like the normal 2-layer decorators from before.

---

### 2️⃣ Difference Between Authentication and Authorization (Using Employee Data)

These two terms are often confused, but they answer **different** questions:

| Concept | Question It Answers | Example in This Project |
|---|---|---|
| **Authentication** | "Who are you?" (verifying identity) | Checking username + password match during login |
| **Authorization** | "What are you allowed to do?" (verifying permission) | Checking if the logged-in user's role can perform a specific action |

```python
def login(username, password):
    global current_user

    if username not in employees:
        print("❌ Login failed: User not found.")
        return False

    if employees[username]["password"] != password:
        print("❌ Login failed: Incorrect password.")
        return False

    current_user = username         # AUTHENTICATION successful
    print(f"✅ Welcome, {username}! You are logged in as '{employees[username]['role']}'.")
    return True


def logout():
    global current_user
    print(f"👋 Goodbye, {current_user}!")
    current_user = None
```

```python
login("priya", "priya123")     # AUTHENTICATION step — verifying identity

# Later, when priya tries an action:
# → AUTHORIZATION step — checking if her ROLE allows this specific action
```

> ⚠️ **Important**
>
> Authentication happens **once**, at login. Authorization happens **every time** a protected action is attempted — even a successfully authenticated user might still be denied access to certain actions if their role doesn't permit it.

**A visual example of the difference:**

```python
login("ananya", "ananya123")   # ✅ AUTHENTICATION succeeds — Ananya IS a real, verified employee

# But when Ananya (an "employee" role) tries to delete another employee:
delete_employee("rahul")        # ❌ AUTHORIZATION fails — she's verified, but NOT permitted for this action
```

🤔 **Quick thinking question:** Can a user pass authentication but still fail authorization? Give a real example.
✅ **Answer:** Yes — for example, Ananya successfully logs in (authentication succeeds, she's a real, verified employee), but when she tries to `delete_employee()`, authorization fails because her role ("employee") isn't in the allowed roles list for that specific action.

---

### 3️⃣ Using `@decorator` Syntax to Wrap Business Logic and Dynamically Allow/Deny Access

Now let's apply our `@requires_permission(...)` decorator to actual business logic functions:

```python
@requires_permission("view_reports")
def view_reports():
    print("📊 Displaying company reports...")

@requires_permission("approve_leave")
def approve_leave_request(employee_name):
    print(f"✅ Leave approved for {employee_name}.")

@requires_permission("delete_employee")
def delete_employee(employee_name):
    if employee_name in employees:
        del employees[employee_name]
        print(f"🗑️ Employee '{employee_name}' has been removed.")
    else:
        print("❌ Employee not found.")
```

**Testing the full system, with different roles:**

```python
# Test 1: Admin (priya) — should be able to do EVERYTHING
login("priya", "priya123")
view_reports()                   # ✅ works
approve_leave_request("ananya")   # ✅ works
delete_employee("rahul")           # ✅ works
logout()

# Test 2: Manager (rahul) — should approve leave & view reports, but NOT delete employees
login("rahul", "rahul123")
view_reports()                    # ✅ works
approve_leave_request("ananya")    # ✅ works
delete_employee("ananya")           # ❌ Access Denied
logout()

# Test 3: Employee (ananya) — should ONLY view reports
login("ananya", "ananya123")
view_reports()                    # ✅ works
approve_leave_request("rahul")     # ❌ Access Denied
delete_employee("rahul")            # ❌ Access Denied
logout()

# Test 4: No one logged in
approve_leave_request("priya")     # ❌ Access Denied: No user is logged in.
```

This demonstrates the **entire access control flow**: authentication (login) happens once, and then every protected function automatically checks authorization via the decorator — the actual function code (`view_reports`, `approve_leave_request`, `delete_employee`) never needs to contain any permission-checking logic itself!

> 💡 **Tip**
>
> Notice how clean the business logic functions stay — `delete_employee()` just focuses on deleting an employee. All the security checking is handled separately and automatically by the decorator. This is a great real-world example of "separation of concerns."

🤔 **Quick thinking question:** Why is it good design that `delete_employee()` itself contains ZERO permission-checking code?
✅ **Answer:** It follows the "separation of concerns" principle — the function focuses purely on its core job (deleting an employee), while the decorator handles security separately. This makes the code cleaner, easier to test, and means the same permission logic can be reused consistently across many different functions.

---

## 💡 Real-Life Analogy

Think of this system like a **corporate office building with keycard access** 🏢:

* **Authentication** is like swiping your keycard at the main entrance — the security guard checks "is this a real, registered employee?" (verifying identity)
* **Authorization** is like specific doors inside the building only opening for certain keycards — even though you got through the main entrance, the "Server Room" door only opens for IT staff, and the "Executive Floor" only opens for senior management
* The **`requires_permission` decorator** is like the electronic lock mechanism itself — it doesn't care WHO you are personally, it just checks "does this keycard's access level match what this door requires?" every single time, automatically

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Authentication | Every login page (Gmail, Instagram, banking apps) — verifying username/password before granting access |
| Authorization / RBAC | Zoho People, Darwinbox (HR software) — different dashboards and actions for HR, Managers, and Employees |
| `@requires_permission`-style decorators | Django's `@permission_required`, Flask-Login's `@login_required` |
| Role-based dashboards | AWS IAM (Identity and Access Management) — controls exactly which cloud actions each user/role can perform |
| Banking systems | Only certain bank employee roles can approve large fund transfers, enforced through similar permission-checking logic |

---

## 🔍 Industry Example

**Scenario:** A team at a **HR-tech startup** is building an internal employee management portal.

1. They design an `employees` data structure (similar to our dictionary) storing each employee's role: `hr_admin`, `manager`, or `staff`.
2. They implement **authentication** first — a `login()` function that verifies username and password, setting a `current_user` session variable upon success.
3. They define a `permissions` mapping, listing exactly which roles can perform which business actions (`approve_leave`, `view_salary_reports`, `terminate_employee`, etc.) — this is their **authorization** rulebook.
4. They build a reusable `@requires_permission("action_name")` decorator (a "decorator factory," since it needs to accept an argument) and apply it directly above every sensitive business function.
5. When a `staff`-level employee tries to call `terminate_employee()`, the decorator automatically blocks the action and logs the attempted violation — without the `terminate_employee()` function itself ever needing to contain permission-checking code.
6. As the company grows and adds new roles (like `payroll_officer`), the team simply updates the `permissions` dictionary — no changes needed to the actual business logic functions, since the decorator handles everything centrally.

This exact pattern — decorators enforcing centralized, role-based access control — is standard practice in real production HR, banking, and enterprise software.

---

## 📊 Diagram

```
           ROLE-BASED ACCESS CONTROL FLOW
           ---------------------------------

     login("rahul", "rahul123")
              │
              ▼
     🔐 AUTHENTICATION CHECK
     "Is this really Rahul?"  ──► ✅ Yes → current_user = "rahul"
                                └► ❌ No  → Access Denied, stop here


     rahul calls: approve_leave_request("ananya")
              │
              ▼
     @requires_permission("approve_leave")
              │
              ▼
     🔑 AUTHORIZATION CHECK
     "Is 'manager' role allowed to approve_leave?"
              │
        ┌─────┴─────┐
        ▼             ▼
      ✅ YES          ❌ NO
   run actual       print "Access Denied"
   function          return None


        PERMISSION MAP
        -----------------
   "view_reports"     → [admin, manager, employee]  (everyone)
   "approve_leave"    → [admin, manager]              (not employee)
   "delete_employee"  → [admin]                          (only admin)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Authentication and authorization mean the same thing."
  ✅ **Correct:** Authentication verifies WHO you are (login); authorization verifies WHAT you're allowed to do (permissions) — a user can be authenticated but still not authorized for a specific action.

* ❌ **Wrong belief:** "Once a user logs in successfully, they should be able to do anything in the system."
  ✅ **Correct:** Successful login only confirms identity — every sensitive action should still separately check the user's role-based permissions.

* ❌ **Wrong belief:** "The permission-checking logic should be written directly inside each business function (like `delete_employee()`)."
  ✅ **Correct:** Centralizing permission checks in a reusable decorator keeps business logic clean and ensures consistent, easily-updatable security rules across the entire application.

* ❌ **Wrong belief:** "`requires_permission("approve_leave")` is written the same way as a normal 2-layer decorator."
  ✅ **Correct:** Since it needs to accept an argument (`action`), it requires an extra outer layer — making it a 3-layer "decorator factory" instead of the usual 2-layer decorator.

* ❌ **Wrong belief:** "It's fine to skip checking `if current_user is None` before checking permissions."
  ✅ **Correct:** Without this check, trying to look up a non-logged-in user's role would cause an error — always verify a user IS logged in before checking what they're authorized to do.

---

## 💬 Interview Corner

**Q1: What is the difference between authentication and authorization?**
✅ Authentication verifies a user's identity (are you who you claim to be?), typically through login credentials. Authorization determines what an authenticated user is permitted to do, based on their role or permissions.

**Q2: Why use a decorator for access control instead of writing permission checks inside each function?**
✅ Using a decorator centralizes the security logic in one reusable place, keeping business logic functions clean and focused on their core task, and making permission rules easier to maintain and update consistently.

**Q3: Why does `requires_permission(action)` need three levels of nested functions instead of two?**
✅ Because it needs to accept a custom argument (`action`) before becoming a usable decorator — the outermost function captures `action` via closure, and returns the actual decorator function, which in turn returns the `wrapper`.

**Q4: In this project, can a fully authenticated user still be denied access to a function? Give an example.**
✅ Yes — for example, "ananya" (role: employee) successfully logs in (authentication succeeds) but is denied when calling `delete_employee()`, because her role isn't included in the permissions list for that specific action (authorization fails).

---

## 📝 Quick Summary

* 🔐 Authentication answers "Who are you?" — verified through login credentials
* 🔑 Authorization answers "What are you allowed to do?" — verified through role-based permissions
* 🧑‍💼 Employee data (username, password, role) forms the foundation of the access control system
* 📋 A `permissions` dictionary maps each action to the list of roles allowed to perform it
* 🏭 `requires_permission(action)` is a "decorator factory" — a function that returns a customized decorator based on the action passed in
* ✅ The decorator checks both that a user is logged in AND that their role has permission, before allowing the actual function to run
* 🧹 Business logic functions (like `delete_employee()`) stay clean and contain zero security-checking code — separation of concerns
* 🔄 This exact centralized, decorator-based pattern mirrors real frameworks like Flask and Django
* 🎯 This project combines closures, decorator factories, and role-based logic into one complete, realistic mini system

---

## 🎯 Class Activity

**"Build and Break Your Own Access Control System" 🔐**

1. Build the complete employee database, permissions map, `login()`/`logout()` functions, and the `requires_permission()` decorator factory shown in this topic.
2. Apply `@requires_permission(...)` to at least 3 business functions of your choice, and test each one with all 3 roles (admin, manager, employee).
3. Add a NEW role called `"intern"` with very limited permissions (only `view_reports`), and update the `permissions` dictionary accordingly — without changing any business logic function.
4. Intentionally try calling a protected function WITHOUT logging in first, and confirm the correct "No user is logged in" message appears.
5. Bonus: Add a new action `"edit_salary"` that only `admin` can perform, and write a new function `edit_salary(employee_name, new_salary)` protected by your decorator.


---

# 📋 Assignments — Mini Project — Role-Based Access Control using Decorators

| Assignment |
|---|
| Build the complete employee database, permissions map, login/logout system, and `requires_permission()` decorator exactly as shown in this topic, and confirm it works for all 3 roles. |
| Add a 4th role called `"guest"` with permission to ONLY view reports, and test that guests are denied access to all other actions. |
| Write a function `add_employee(username, password, role)` protected so that only `"admin"` can add new employees. |
| Add a new permission `"edit_salary"` allowed only for `"admin"`, and build a matching `edit_salary(employee_name, new_amount)` function protected by the decorator. |
| Test what happens when a logged-out user (no one logged in) tries to call a protected function, and confirm the correct error message displays. |
| Modify the system so that after 3 failed login attempts with the wrong password, the account is temporarily "locked" (print a lock message and refuse further attempts). |
| Write a function `list_my_permissions()` that shows the currently logged-in user exactly which actions they ARE allowed to perform, based on their role. |
| Create a manager-only function `generate_team_report()` and test it with all three existing roles to confirm correct access control behavior. |
| Add a `"read_only_admin"` role that can view everything but cannot delete or edit anything, and update the permissions dictionary accordingly. |
| Write a short program demonstrating the DIFFERENCE between authentication failure (wrong password) and authorization failure (correct login, wrong role) with clear printed messages for each case. |
| Add logging to the `requires_permission` decorator so that every DENIED access attempt is printed with the username, role, and action attempted (a simple security audit log). |
| Refactor the `login()` function to store MULTIPLE currently logged-in users (a dictionary of active sessions) instead of a single `current_user` variable, allowing multi-user testing in the same run. |
| Test the full system end-to-end: log in as each of the 3 roles, attempt every protected function, and write down (as comments) which succeeded and which were denied for each. |
| Add a new business function `view_salary_reports()` that only `admin` and a new `payroll_officer` role can access, and test it thoroughly. |
| Write a short reflection (3–5 sentences) explaining, in your own words, why centralizing access control in a decorator is better than checking permissions inside every single function. |
