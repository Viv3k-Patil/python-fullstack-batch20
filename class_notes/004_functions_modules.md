# 📚 Functions & Modules (Part 1)

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand what a function is and why we "wrap" code inside one
* 🎯 Define and call their own functions in Python
* 🎯 Use parameters to pass data into functions and `return` to get results back
* 🎯 Understand the difference between local and global variable scope
* 🎯 Get a basic understanding of higher-order functions (functions that work with other functions)
* 🎯 Import and use Python's built-in standard library modules

---

## 📖 Introduction

Imagine you had to make tea 🍵 five times a day, and every single time you had to explain, step by step, "boil water, add tea leaves, add milk, add sugar, strain it" — all over again. Wouldn't it be easier to just say **"make tea"** once you've taught someone the recipe?

That's exactly what a **function** is in programming — a **reusable block of code** that performs a specific task, which you can "call" (use) again and again without rewriting it.

### 🤔 Why does this topic exist?

As programs grow bigger, writing the same code repeatedly becomes messy, hard to read, and hard to fix. Functions let us:

* ♻️ Reuse code instead of copy-pasting
* 🧩 Break a big problem into smaller, manageable pieces
* 🐛 Debug faster (fix the function once, fixed everywhere it's used)
* 👥 Work in teams (different people can write different functions)

### 🤔 Where is it used?

* 🧮 Calculator apps — a `add()`, `subtract()` function for each operation
* 🏦 Banking software — a `withdraw_money()` function used every time someone withdraws
* 🎮 Games — a `check_score()` function called every time a player scores a point
* 🌐 Websites — a `send_email()` function called whenever a user signs up

> 💡 **Tip**
>
> A function is defined **once** but can be called (used) **hundreds of times** throughout a program.

---

## 🧠 Detailed Notes

### 1️⃣ Defining and Calling Functions

A function is created (defined) using the `def` keyword, followed by a name, parentheses `()`, and a colon `:`. The code inside it must be indented.

```python
def greet():
    print("Hello! Welcome to Python Full Stack Course 🎉")

# Calling the function
greet()
greet()   # can be called as many times as needed
```

Output:
```
Hello! Welcome to Python Full Stack Course 🎉
Hello! Welcome to Python Full Stack Course 🎉
```

**Anatomy of a function:**

```
   def   greet ( ) :
    │      │    │  │
    │      │    │  └── colon, marks start of function body
    │      │    └───── parentheses (can hold parameters)
    │      └────────── function name (should be meaningful!)
    └───────────────── keyword that starts a function definition
```

> ⚠️ **Important**
>
> Defining a function does **not** run its code. The code only runs when you **call** the function using `greet()`. Beginners often forget this and wonder why nothing happens after `def`.

🤔 **Quick thinking question:** If you write a `def` block but never call the function, will anything print?
✅ **Answer:** No — the function body only executes when it is explicitly called with `function_name()`.

---

### 2️⃣ Function Parameters and Return Values

**Parameters** let you send data INTO a function. **Return values** let a function send data BACK OUT to whoever called it.

```python
def greet_user(name):          # 'name' is a parameter
    print(f"Hello, {name}! 👋")

greet_user("Priya")             # "Priya" is the argument passed in
greet_user("Rahul")
```

**Multiple parameters:**

```python
def add_numbers(a, b):
    result = a + b
    print(f"The sum is {result}")

add_numbers(5, 3)     # The sum is 8
```

**Default parameter values** (used when caller doesn't provide a value):

```python
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Ananya")                  # Hello, Ananya!
greet_user("Ananya", "Good Morning")   # Good Morning, Ananya!
```

**Return values** — using `return` to send a result back, instead of just printing it:

```python
def add_numbers(a, b):
    return a + b        # sends the result back to the caller

total = add_numbers(10, 20)   # total now holds 30
print(total)                    # 30
print(add_numbers(5, 5) * 2)   # 20 — because you can use the returned value directly
```

| Concept | `print()` inside function | `return` inside function |
|---|---|---|
| What it does | Displays the value on screen | Sends the value back to be used further |
| Can you store the result in a variable? | ❌ No (prints `None`) | ✅ Yes |
| Function stops executing after this line? | ❌ No | ✅ Yes, immediately |

```python
def calculate_bill(price, quantity):
    total = price * quantity
    tax = total * 0.18
    return total + tax     # function stops here and sends back the final value

final_bill = calculate_bill(500, 2)
print(f"Final bill: ₹{final_bill:.2f}")   # Final bill: ₹1180.00
```

> 💡 **Tip**
>
> A function can also `return` multiple values at once, separated by commas — Python automatically packs them into a tuple.

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = get_min_max([4, 9, 1, 7])
print(smallest, largest)     # 1 7
```

🤔 **Quick thinking question:** What is printed if a function has no `return` statement at all, and you try to store its result in a variable?
✅ **Answer:** The variable will store `None` — Python functions return `None` by default if you don't explicitly `return` something.

---

### 3️⃣ Scope of Variables (Local vs Global)

**Scope** determines **where in your program a variable can be accessed**.

* 🏠 **Local variable** — created inside a function, only exists/accessible inside that function
* 🌍 **Global variable** — created outside all functions, accessible anywhere in the program

```python
message = "I am global"   # global variable

def show_message():
    local_message = "I am local"   # local variable
    print(message)          # ✅ can access global variable from inside
    print(local_message)     # ✅ can access local variable inside its own function

show_message()
print(message)              # ✅ works — global variable accessible outside too
# print(local_message)      # ❌ NameError — local variable doesn't exist outside the function
```

**Modifying a global variable from inside a function** requires the `global` keyword:

```python
counter = 0

def increment():
    global counter        # tells Python: "use the global counter, don't create a new local one"
    counter += 1

increment()
increment()
print(counter)    # 2
```

Without the `global` keyword, Python would create a brand-new **local** variable instead of touching the outer one, and you'd get an error or unexpected behavior.

```python
counter = 0

def increment_wrong():
    counter += 1     # ❌ UnboundLocalError — Python thinks 'counter' is local here
                       #    because you're assigning to it inside the function

increment_wrong()
```

| Scope Type | Where created | Where accessible | Keyword needed to modify from inside a function |
|---|---|---|---|
| Local | Inside a function | Only within that function | Not needed (default) |
| Global | Outside any function | Anywhere in the file | `global` keyword required to *modify* it inside a function |

> ⚠️ **Important**
>
> Relying too heavily on global variables is considered bad practice in real projects — it makes code harder to debug because any function could secretly change the value. Prefer passing values as parameters and getting results via `return`.

🤔 **Quick thinking question:** Why does Python give an `UnboundLocalError` when you try to do `counter += 1` inside a function without declaring `global counter`?
✅ **Answer:** Because the moment Python sees an assignment (`counter += 1`, which means `counter = counter + 1`) inside a function, it assumes `counter` is a **local** variable for the entire function — even before that line runs — so it doesn't know the "current" value yet.

---

### 4️⃣ Basic Idea of Higher-Order Functions

A **Higher-Order Function** is a function that either:

* 📥 Takes another function as an argument (input), OR
* 📤 Returns a function as its result

This is possible in Python because **functions are treated as values**, just like numbers or strings — they can be stored in variables, passed around, and returned.

```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_operation(func, value):    # 'func' is a parameter that expects a FUNCTION
    return func(value)

print(apply_operation(square, 5))     # 25
print(apply_operation(cube, 3))        # 27
```

**Real, commonly-used higher-order functions in Python:**

```python
numbers = [1, 2, 3, 4, 5]

# map() — applies a function to every item in a list
squared = list(map(square, numbers))
print(squared)          # [1, 4, 9, 16, 25]

# filter() — keeps only items where the function returns True
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)             # [2, 4]

# sorted() with a 'key' function — controls HOW sorting happens
words = ["banana", "kiwi", "apple", "fig"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)   # ['fig', 'kiwi', 'apple', 'banana']
```

**Lambda functions** — tiny, unnamed, "throwaway" functions, often used with higher-order functions:

```python
squared = list(map(lambda x: x * x, numbers))
print(squared)     # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)         # [2, 4]
```

| Function | Purpose | Example |
|---|---|---|
| `map(func, list)` | Apply a function to every element | `map(square, [1,2,3])` |
| `filter(func, list)` | Keep only elements where function returns `True` | `filter(is_even, [1,2,3,4])` |
| `sorted(list, key=func)` | Sort using custom logic | `sorted(words, key=len)` |
| `lambda` | Create a quick, unnamed function | `lambda x: x * 2` |

> 💡 **Tip**
>
> You don't need to master higher-order functions immediately — just understand the **idea**: functions can be passed around like any other value. We'll go deeper into this in later sessions.

🤔 **Quick thinking question:** In `sorted(words, key=len)`, what is `len` actually doing here?
✅ **Answer:** `len` (the length function) is being passed as an argument, and Python uses it to calculate a "sort value" for each word — sorting the words by their length instead of alphabetically.

---

### 5️⃣ Importing Modules, Using Standard Library

A **module** is simply a Python file full of pre-written functions that you can reuse, instead of writing everything from scratch. Python comes with a huge **Standard Library** of built-in modules — ready to use, no installation required.

```python
import math

print(math.sqrt(16))       # 4.0
print(math.pi)               # 3.141592653589793
print(math.factorial(5))    # 120
```

**Different ways to import:**

```python
import math                       # import the whole module
print(math.sqrt(25))               # must use math.functionname()

from math import sqrt              # import ONE specific function
print(sqrt(25))                     # can use it directly, no "math." needed

from math import sqrt, pi          # import multiple specific things
import math as m                   # import with a shorter nickname (alias)
print(m.sqrt(25))
```

**Some genuinely useful standard library modules for beginners:**

```python
import random
print(random.randint(1, 10))        # random whole number between 1 and 10
print(random.choice(["Rock", "Paper", "Scissors"]))  # random pick from a list

import datetime
today = datetime.date.today()
print(today)                          # e.g. 2026-08-15

import os
print(os.getcwd())                    # prints current working directory

import time
print("Starting...")
time.sleep(2)                         # pauses program for 2 seconds
print("2 seconds passed!")
```

| Module | Purpose | Example Use |
|---|---|---|
| `math` | Mathematical operations | `math.sqrt()`, `math.pi` |
| `random` | Generate random values | `random.randint()`, `random.choice()` |
| `datetime` | Work with dates and times | `datetime.date.today()` |
| `os` | Interact with the operating system | `os.getcwd()`, `os.listdir()` |
| `time` | Time-related functions, delays | `time.sleep()` |
| `statistics` | Statistical calculations | `statistics.mean()` |

> ⚠️ **Important**
>
> You do NOT need to install standard library modules using `pip` — they come bundled with Python automatically. Only third-party modules (like `pandas`, `requests`) need to be installed separately.

🤔 **Quick thinking question:** What's the difference between `import math` and `from math import sqrt`?
✅ **Answer:** `import math` requires you to prefix every function with `math.` (e.g., `math.sqrt()`), while `from math import sqrt` lets you use `sqrt()` directly — but only that specific function is available, not the whole module.

---

## 💡 Real-Life Analogy

* 🍳 **Function → A Recipe Card** — You write the recipe (steps) once. Every time you want to cook that dish, you just follow the card (call the function) — you don't rewrite the recipe each time.
* 📥 **Parameters → Ingredients you bring** — The recipe stays the same, but you can use different quantities/ingredients each time (different arguments).
* 📤 **Return Value → The finished dish handed back to you** — After following the recipe, you get something back that you can use elsewhere (eat it, serve it, photograph it).
* 🏠 **Local Scope → Your Own House** — What happens inside your house (local variables) usually stays inside your house, unless you deliberately share it with the outside world.
* 🌍 **Global Scope → A Public Notice Board** — Anyone (any function) can read what's posted there, but only certain people are allowed to officially update it (using the `global` keyword).
* 📚 **Module → A Toolbox Someone Already Built** — Instead of forging your own hammer (writing sqrt calculation from scratch), you just open the toolbox (`import math`) and grab the ready-made tool.

---

## 💻 Real-World Application

| Use Case | How Functions/Modules Are Used |
|---|---|
| 🏦 Banking apps | A `calculate_interest()` function reused for every account |
| 🛒 E-commerce checkout | A `calculate_total()` function that takes cart items and returns the final price |
| 🎲 Games | `random.randint()` used to roll virtual dice or generate loot |
| 📅 Calendar apps (Google Calendar) | `datetime` module used to calculate reminders and event times |
| 🤖 Chatbots | Higher-order functions used to apply the same "reply logic" to different types of messages |
| 📊 Data Science tools (Pandas, NumPy) | Built entirely as collections of reusable functions organized into modules |

---

## 🔍 Industry Example

**Scenario:** A **Backend Developer at Zomato** is building the "Order Total Calculator" for the checkout page.

1. Instead of writing the price calculation logic everywhere it's needed (cart page, checkout page, order confirmation email), the developer writes **one function**: `calculate_order_total(items, discount_percent=0)`.
2. This function takes **parameters**: the list of items (with prices) and an optional discount percentage (using a **default value** of 0 if no discount applies).
3. Inside the function, a **local variable** `subtotal` is calculated — it only exists during this function's execution and doesn't interfere with other parts of the app.
4. The function uses `return` to send back the final calculated total, which different parts of the app (cart summary, payment page, invoice generator) can all use.
5. To calculate delivery time, the developer uses the standard library's `datetime` module to add estimated minutes to the current time.
6. To apply a "Buy 1 Get 1" style logic across multiple items, the developer uses a **higher-order function** (`map()`) to apply the same offer-checking function to every item in the cart at once — instead of writing a separate loop each time.

This is exactly how real production backend code is structured: small, reusable, well-scoped functions, powered by both custom logic and Python's standard library.

---

## 📊 Diagram

```
                     ANATOMY OF A FUNCTION CALL
                     ---------------------------

     def calculate_bill(price, quantity):     ← DEFINITION (blueprint)
         total = price * quantity              ← LOCAL variable
         return total

     final = calculate_bill(500, 2)            ← CALL (using the blueprint)
       │                 │      │
       │                 └──────┴── Arguments passed IN (parameters)
       └── Return value captured OUT


                SCOPE VISUALIZATION
                --------------------
      ┌─────────────────────────────────────┐
      │   GLOBAL SCOPE (whole program)        │
      │   message = "I am global" 🌍           │
      │                                        │
      │   ┌───────────────────────────────┐   │
      │   │  FUNCTION SCOPE (local) 🏠      │   │
      │   │  local_message = "I am local"   │   │
      │   │  (dies once function ends)      │   │
      │   └───────────────────────────────┘   │
      └─────────────────────────────────────┘


          HIGHER-ORDER FUNCTION FLOW
          ----------------------------
     numbers  ──►  map(square, numbers)  ──►  squared list
     [1,2,3]        (function passed IN)       [1,4,9]
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Defining a function automatically runs it."
  ✅ **Correct:** A function only runs when it is explicitly **called** using its name and parentheses `function_name()`.

* ❌ **Wrong belief:** "`print()` and `return` do the same thing."
  ✅ **Correct:** `print()` only displays a value on screen; `return` sends the value back so it can be stored in a variable and used further in the program.

* ❌ **Wrong belief:** "A variable created inside a function can be used anywhere in the program."
  ✅ **Correct:** Variables created inside a function are **local** — they disappear once the function finishes running and cannot be accessed outside it.

* ❌ **Wrong belief:** "You can freely modify a global variable inside any function without any special keyword."
  ✅ **Correct:** You must use the `global` keyword inside the function if you intend to **modify** (not just read) a global variable.

* ❌ **Wrong belief:** "You need to install `pip install math` before using the `math` module."
  ✅ **Correct:** `math`, `random`, `datetime`, `os`, and `time` are all part of Python's **standard library** and come pre-installed — no `pip install` needed.

* ❌ **Wrong belief:** "Functions can only accept and work with numbers/strings, not other functions."
  ✅ **Correct:** In Python, functions are treated like any other value — they can be passed as arguments to other functions (higher-order functions like `map()` and `filter()`).

---

## 💬 Interview Corner

**Q1: What is the difference between a parameter and an argument?**
✅ A **parameter** is the variable name listed inside the function definition (`def greet(name):`). An **argument** is the actual value you pass when calling the function (`greet("Priya")` — `"Priya"` is the argument).

**Q2: What happens if a function doesn't have a `return` statement?**
✅ It automatically returns `None` by default.

**Q3: What is variable scope, and why does it matter?**
✅ Scope defines where a variable can be accessed in a program (local vs global). It matters because it prevents naming conflicts and keeps code organized — variables in one function don't accidentally interfere with variables in another.

**Q4: Can you give a simple example of a higher-order function?**
✅ `map()` is a classic example — it takes another function (like `square`) and applies it to every item in a list, e.g., `map(square, [1,2,3])`.

---

## 📝 Quick Summary

* 🍳 A function is a reusable block of code, defined once using `def` and reused via calling
* 📥 Parameters let you pass data into a function; arguments are the actual values passed
* 📤 `return` sends a result back to the caller; `print()` merely displays it
* 🏠 Local variables exist only inside their function; 🌍 global variables exist throughout the program
* 🔑 Use the `global` keyword to modify a global variable from inside a function
* 🧩 Higher-order functions accept or return other functions — e.g. `map()`, `filter()`, `sorted(key=...)`
* ⚡ `lambda` creates small, unnamed, throwaway functions
* 📦 Modules are pre-written Python files full of reusable functions
* 🛠️ Python's standard library (`math`, `random`, `datetime`, `os`, `time`) comes free, no installation needed
* 🎯 Well-designed functions with clear parameters and return values make code cleaner, reusable, and easier to debug

---

## 🎯 Class Activity

**"Build a Mini Utility Toolkit" 🧰**

1. Write a function `add(a, b)` that returns the sum of two numbers, and call it with 3 different pairs of numbers.
2. Write a function `is_even(n)` that returns `True` or `False`, then use it with `filter()` on a list of 10 numbers to get only the even ones.
3. Create a global variable `total_students = 0`. Write a function `add_student()` that increases it by 1 using the `global` keyword. Call it 5 times and print the final count.
4. Import the `random` module and write a function `roll_dice()` that returns a random number between 1 and 6. Call it 3 times and print the results.
5. Bonus: Use `map()` with a `lambda` to double every number in a list of your choice.


---

# 📋 Assignments — Functions & Modules (Part 1)

| Assignment |
|---|
| Write a function `greet(name)` that prints a personalized greeting, and call it with your own name and a friend's name. |
| Write a function `calculate_area(length, width)` that returns the area of a rectangle, and print the result for 3 different sets of dimensions. |
| Write a function `check_even_odd(number)` that returns `"Even"` or `"Odd"` depending on the number passed in. |
| Create a function with a default parameter: `apply_discount(price, discount=10)` that returns the discounted price. Call it once with a custom discount and once without. |
| Write a function that returns TWO values at once — the square and the cube of a number — and unpack both into separate variables when calling it. |
| Create a global variable `bank_balance = 1000`. Write two functions, `deposit(amount)` and `withdraw(amount)`, that correctly update this global variable using the `global` keyword. |
| Write a small program that demonstrates the `UnboundLocalError` by trying to modify a global variable inside a function WITHOUT using the `global` keyword, then fix it. |
| Write a function `apply_twice(func, value)` that applies a given function to a value two times in a row (a basic higher-order function). Test it with a `square` function. |
| Use `filter()` with a `lambda` to extract all words longer than 4 letters from a list of 10 words. |
| Use `sorted()` with a `key` function to sort a list of student names by their length. |
| Import the `math` module and write a program that calculates the area of a circle given its radius, using `math.pi`. |
| Import the `random` module and simulate a simple "Guess the Number" game where the computer picks a random number between 1–20. |
| Import the `datetime` module and write a program that prints today's date and calculates how many days are left until January 1st of next year. |
| Write a function `calculate_bill(price, quantity, tax_percent=18)` that returns the final bill including tax, and test it with at least 3 different inputs. |
| Create your own small "module": write 3 useful functions (e.g., `add`, `subtract`, `is_prime`) in a separate `.py` file, then import and use them in another script. |

# 📚 Project 1 — Hotel Management System (Console)

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand how to plan and structure a real console-based project from scratch
* 🎯 Break a big requirement down into smaller, manageable coding tasks
* 🎯 Design and implement a menu-driven program using loops and conditionals
* 🎯 Apply functions to organize booking, cancellation, and display logic
* 🎯 Use lists and dictionaries as simple "in-memory" data storage (like a mini database)
* 🎯 Test and debug a multi-feature console application systematically

---

## 📖 Introduction

So far, you've learned individual building blocks — variables, loops, conditionals, functions, data structures. Now it's time to combine **everything** into one real, working project: a **Hotel Management System** 🏨 that runs in the console (terminal).

This project will let a "hotel receptionist" (the user) book rooms, view existing bookings, cancel bookings, and check room availability — all through a simple text-based menu.

### 🤔 Why does this topic exist?

Learning syntax is not the same as building software. Real developers need to:

* 🧩 Take a vague requirement ("build a hotel system") and break it into concrete steps
* 🏗️ Structure code using functions instead of one giant messy script
* 💾 Manage data (even without a real database) using lists/dictionaries
* 🐞 Test their own code and fix bugs before showing it to anyone else

This project simulates exactly what happens in a real internship or junior developer job — except on a smaller, beginner-friendly scale.

### 🤔 Where is it used?

* 🏨 Real hotel booking systems (like the backend logic behind OYO, MakeMyTrip room booking)
* 🎬 Movie ticket booking systems (very similar logic — seats instead of rooms)
* 🚌 Bus/train reservation systems
* 🏫 Any "reserve a slot" style application (library book reservation, gym slot booking)

> 💡 **Tip**
>
> This is your first real project. It won't be perfect on the first try — and that's completely normal! Real software is built through repeated testing and fixing, not written perfectly in one go.

---

## 🧠 Detailed Notes

### 1️⃣ Project Overview

**Goal:** Build a console-based Hotel Management System that can:

* 🛏️ Show available rooms
* 📝 Book a room for a customer (store name, phone number, room number, number of days)
* ❌ Cancel an existing booking
* 📋 View all current bookings
* 🔍 Search a booking by customer name or room number
* 🚪 Exit the program cleanly

**Core requirement:** Everything should work through a **menu** — the user picks a number, and the program performs that action, repeatedly, until they choose to exit.

```
===== 🏨 HOTEL MANAGEMENT SYSTEM =====
1. View Available Rooms
2. Book a Room
3. Cancel a Booking
4. View All Bookings
5. Search Booking
6. Exit
=======================================
Enter your choice:
```

🤔 **Quick thinking question:** Why do we plan out the full menu and features BEFORE writing any code?
✅ **Answer:** Planning first prevents wasted effort — if you start coding immediately, you often realize halfway through that your data structure or logic doesn't support a feature you need, forcing you to rewrite everything.

---

### 2️⃣ Breaking Down Into Smaller Tasks (Control Flow, Loops, Functions)

A big project feels overwhelming if you look at it as one whole thing. The professional approach is to break it into **small, independent tasks**, and solve each one using the tools you already know:

| Big Requirement | Broken Down Into | Python Tool Used |
|---|---|---|
| Keep showing the menu until user exits | Repeat the menu display until choice = 6 | `while` loop |
| React differently based on user's choice | Check which number user entered | `if / elif / else` |
| Book a room | Take input, validate room availability, store details | Functions + Dictionaries |
| Show all bookings | Loop through stored bookings and print each | `for` loop |
| Prevent booking an already-booked room | Check room status before allowing booking | Conditional check on data structure |
| Cancel a booking | Find and remove/reset a specific booking | Dictionary/list operations |

**Step-by-step task breakdown:**

```python
# STEP 1: Set up initial data (rooms, bookings)
rooms = {101: "Available", 102: "Available", 103: "Available", 104: "Available"}
bookings = {}   # will store: {room_number: {"name": ..., "phone": ..., "days": ...}}

# STEP 2: Write a function for each menu action
def view_available_rooms():
    ...

def book_room():
    ...

def cancel_booking():
    ...

def view_all_bookings():
    ...

def search_booking():
    ...

# STEP 3: Build the main menu loop that calls these functions
def main():
    while True:
        print("1. View Rooms  2. Book  3. Cancel  4. View All  5. Search  6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            view_available_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            view_all_bookings()
        elif choice == "5":
            search_booking()
        elif choice == "6":
            print("Thank you for using Hotel Management System! 👋")
            break
        else:
            print("Invalid choice, please try again.")
```

> ⚠️ **Important**
>
> Notice that `main()` doesn't contain the actual booking logic — it just **calls** the right function. This separation makes the program much easier to read, test, and fix.

🤔 **Quick thinking question:** Why is it better to write `book_room()` as a separate function instead of writing all its logic directly inside the `while` loop?
✅ **Answer:** Separating it into its own function makes the code easier to test individually, easier to read, and reusable — you could call `book_room()` from another part of the program later without duplicating code.

---

### 3️⃣ Implementing Menus, Booking Logic, and In-Memory Data Structures

Let's now implement the actual logic, function by function.

**Data structures used:**

```python
rooms = {
    101: "Available",
    102: "Available",
    103: "Booked",
    104: "Available"
}

bookings = {
    103: {"name": "Rahul Sharma", "phone": "9876543210", "days": 3}
}
```

We use a **dictionary** for `rooms` because each room number (key) maps to a status (value) — quick and clear lookups. We use a **nested dictionary** for `bookings` because each room needs multiple related details (name, phone, days).

**Function: View Available Rooms**

```python
def view_available_rooms():
    print("\n--- Available Rooms ---")
    available_found = False
    for room_number, status in rooms.items():
        if status == "Available":
            print(f"Room {room_number} ✅")
            available_found = True
    if not available_found:
        print("No rooms available right now. 😔")
```

**Function: Book a Room**

```python
def book_room():
    view_available_rooms()
    room_number = int(input("\nEnter room number to book: "))

    if room_number not in rooms:
        print("❌ Invalid room number.")
        return

    if rooms[room_number] == "Booked":
        print("❌ This room is already booked!")
        return

    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    days = int(input("Enter number of days: "))

    rooms[room_number] = "Booked"
    bookings[room_number] = {"name": name, "phone": phone, "days": days}

    print(f"✅ Room {room_number} successfully booked for {name} ({days} days)!")
```

**Function: Cancel a Booking**

```python
def cancel_booking():
    room_number = int(input("Enter room number to cancel: "))

    if room_number in bookings:
        customer = bookings[room_number]["name"]
        del bookings[room_number]
        rooms[room_number] = "Available"
        print(f"✅ Booking for {customer} in Room {room_number} has been cancelled.")
    else:
        print("❌ No booking found for this room number.")
```

**Function: View All Bookings**

```python
def view_all_bookings():
    print("\n--- Current Bookings ---")
    if not bookings:
        print("No bookings yet. 📭")
        return

    for room_number, details in bookings.items():
        print(f"Room {room_number}: {details['name']} | {details['phone']} | {details['days']} days")
```

**Function: Search Booking**

```python
def search_booking():
    keyword = input("Enter customer name or room number to search: ")

    found = False
    for room_number, details in bookings.items():
        if keyword.lower() == details["name"].lower() or keyword == str(room_number):
            print(f"🔍 Found: Room {room_number} — {details['name']}, {details['phone']}, {details['days']} days")
            found = True

    if not found:
        print("❌ No matching booking found.")
```

> 💡 **Tip**
>
> Notice how every function has a **single, clear responsibility**: one books, one cancels, one searches. This principle (called "Single Responsibility") makes real-world software much easier to maintain.

🤔 **Quick thinking question:** In `book_room()`, why do we check `if rooms[room_number] == "Booked"` before allowing a new booking?
✅ **Answer:** To prevent **double-booking** — without this check, two different customers could accidentally be assigned to the same room, which is a serious real-world bug.

---

### 4️⃣ Thoroughly Testing and Debugging the Solution

Writing the code is only half the job — a professional developer always **tests** their program against different scenarios before considering it "done."

**A practical testing checklist for this project:**

| Test Case | Expected Behavior |
|---|---|
| Book an available room | Room status changes to "Booked", details saved correctly |
| Try to book an already-booked room | Program should show an error, NOT allow double booking |
| Try to book a room number that doesn't exist (e.g., 999) | Program should show "Invalid room number" |
| Cancel an existing booking | Room becomes "Available" again, booking removed |
| Cancel a booking for a room that was never booked | Program should show "No booking found" |
| View all bookings when there are none | Should show a friendly "No bookings yet" message, not crash |
| Search using a room number that exists | Should correctly display that booking's details |
| Search using a name that doesn't exist | Should show "No matching booking found" |
| Enter a non-numeric value where a number is expected (e.g., room number) | Program should ideally not crash (advanced: use try/except) |
| Enter an invalid main menu choice (e.g., "9" or "abc") | Should show "Invalid choice" and show the menu again |

**Common debugging technique — adding print statements temporarily:**

```python
def book_room():
    room_number = int(input("Enter room number: "))
    print(f"DEBUG: room_number entered = {room_number}")   # temporary debug line
    ...
```

> ⚠️ **Important**
>
> Always **remove or comment out** debug `print()` statements before considering your project finished — they shouldn't appear in the final, polished version shown to users.

**Basic error handling to make the project more robust:**

```python
def book_room():
    try:
        room_number = int(input("Enter room number to book: "))
    except ValueError:
        print("❌ Please enter a valid number for room number.")
        return
    ...
```

🤔 **Quick thinking question:** Why should you specifically test "edge cases" like cancelling a booking that doesn't exist, instead of only testing the "happy path" (everything working correctly)?
✅ **Answer:** Real users don't always follow the expected flow — they make typos, enter wrong values, or try invalid actions. If you only test the ideal scenario, your program will crash or behave incorrectly the moment a real user does something unexpected.

---

## 💡 Real-Life Analogy

Think of this project like **managing a real hotel reception desk** using just a **notebook and a whiteboard** 📓:

* The **whiteboard** (the `rooms` dictionary) shows, at a glance, which rooms are "Available" or "Booked"
* The **notebook** (the `bookings` dictionary) has detailed entries — guest name, phone number, number of days — for each occupied room
* The **menu loop** is like the receptionist repeatedly asking "What would you like to do next?" until their shift ends (`Exit`)
* **Testing and debugging** is like a manager double-checking the notebook and whiteboard at the end of the day to make sure nothing was recorded incorrectly — no room double-booked, no missing entries

---

## 💻 Real-World Application

| Real System | Similarity to This Project |
|---|---|
| 🏨 OYO / MakeMyTrip (hotel booking backend) | Room availability tracking + booking storage logic, at a much larger scale with a real database |
| 🎬 BookMyShow | Same core idea — "seats" instead of "rooms", checking availability before confirming booking |
| 🚌 RedBus | Bus seat booking follows an identical availability-check + booking-storage pattern |
| 🏥 Hospital appointment systems | Doctor "slots" behave exactly like hotel "rooms" — available vs booked |
| 📚 Library management systems | Book "copies" behave like rooms — available vs issued/booked |

---

## 🔍 Industry Example

**Scenario:** A **Junior Full-Stack Developer** joins a startup building a boutique hotel chain's booking software.

1. On day one, their manager asks them to build a **prototype** exactly like this console project — no database, no website yet — just to validate the core booking logic works correctly.
2. The developer starts by **breaking down the requirement** into smaller functions: `check_availability()`, `create_booking()`, `cancel_booking()` — exactly like this project's structure.
3. They use **dictionaries** to temporarily simulate what will later become real database tables (`rooms` table, `bookings` table).
4. They build a **simple menu-driven console app** first, to confirm the business logic (no double-booking, correct cancellation) works before any fancy website design is added.
5. Before showing it to their manager, they go through a **testing checklist** — trying invalid room numbers, double-booking attempts, and empty searches — to catch bugs early.
6. Only after this console prototype works flawlessly does the team move on to connecting it with a real website and database — proving that **this exact beginner project mirrors real early-stage software development**.

---

## 📊 Diagram

```
                 HOTEL MANAGEMENT SYSTEM — PROGRAM FLOW
                 ----------------------------------------

        ┌─────────────────────────────┐
        │   Show Main Menu (loop)      │◄────────────────┐
        └───────────────┬─────────────┘                  │
                         │                                 │
                 User enters choice                        │
                         │                                 │
        ┌────────────────┼────────────────┬──────────┬─────┴────┐
        ▼                ▼                ▼          ▼          ▼
  View Rooms       Book Room       Cancel Booking  View All   Search
        │                │                │           │          │
        ▼                ▼                ▼           ▼          ▼
   Loop rooms{}    Check availability  Find in     Loop       Match name/
   print Available  → Save to          bookings{}  bookings{} room number
                     bookings{}         → delete    → print    → print
                                         → free room


              DATA STRUCTURE SNAPSHOT
              -------------------------
   rooms = { 101: "Available", 102: "Booked", 103: "Available" }
                                   │
                                   ▼
   bookings = { 102: {"name": "Rahul", "phone": "98765...", "days": 3} }
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "I should write the entire project in one giant block of code without functions."
  ✅ **Correct:** Breaking the project into small functions (`book_room()`, `cancel_booking()`, etc.) makes it far easier to read, test, and fix.

* ❌ **Wrong belief:** "I don't need to check if a room is already booked before booking it again."
  ✅ **Correct:** Always validate the current status before allowing an action — this prevents serious bugs like double-booking.

* ❌ **Wrong belief:** "Testing only the normal, expected flow (happy path) is enough."
  ✅ **Correct:** You must also test edge cases — invalid inputs, non-existent rooms, empty bookings list — because real users make mistakes.

* ❌ **Wrong belief:** "Data will magically persist even after the program is closed and reopened."
  ✅ **Correct:** Since we're using in-memory lists/dictionaries (no file or database), all data is lost once the program stops — this is a beginner-level limitation, later solved using files/databases.

* ❌ **Wrong belief:** "The `while True` loop with a menu will run forever no matter what."
  ✅ **Correct:** It runs forever until the `break` statement is triggered (usually via the "Exit" choice) — without a `break`, users would be stuck in an infinite loop.

---

## 💬 Interview Corner

**Q1: Why is it a good practice to break a large project into multiple functions instead of writing everything in `main()`?**
✅ It improves readability, makes each piece independently testable, avoids code duplication, and makes debugging much faster since issues can be isolated to a specific function.

**Q2: How would you prevent double-booking of the same room in this kind of system?**
✅ Before confirming a booking, check the current status of the room in the `rooms` dictionary (or database in real systems) — only proceed if it's marked "Available".

**Q3: Why use a dictionary instead of a list to store room bookings?**
✅ A dictionary allows instant lookup by room number (the key), which is much faster and cleaner than searching through a list item by item to find a matching room.

**Q4: What is the difference between testing the "happy path" and testing "edge cases"?**
✅ The happy path tests normal, expected usage (correct inputs, valid actions). Edge cases test unusual, invalid, or boundary situations (wrong input types, non-existent data, empty collections) that real users might trigger by mistake.

---

## 📝 Quick Summary

* 🏨 This project combines loops, conditionals, functions, and dictionaries into one real console application
* 🧩 Big requirements should always be broken into smaller, independent tasks before coding begins
* 🔁 A `while True` loop with a `break` on "Exit" powers the repeating menu system
* 🗂️ Dictionaries (`rooms`, `bookings`) act as simple in-memory data storage, simulating a database
* 🛠️ Each feature (booking, cancelling, searching) is implemented as its own dedicated function
* 🚫 Always validate data (e.g., check room availability) before performing an action, to avoid bugs like double-booking
* 🧪 Testing must cover both the "happy path" and unexpected edge cases
* 🐞 Debugging often involves temporary `print()` statements — remove them before the final version
* 💾 In-memory data structures don't persist after the program closes — that's expected at this learning stage
* 🎯 This project structure mirrors how real, early-stage software prototypes are actually built in the industry

---

## 🎯 Class Activity

**"Extend the Hotel Management System" 🏨💪**

1. Run the base version of the Hotel Management System code shown in this topic on your own machine.
2. Try to intentionally "break" it — attempt to book an already-booked room, cancel a non-existent booking, and enter invalid menu choices. Note down what happens.
3. Add a new feature: a function `total_revenue()` that calculates and prints the total earnings so far, assuming each room costs ₹1500 per day (`price_per_day * days` for each booking).
4. Add basic input validation using `try/except` so the program doesn't crash if a user types letters instead of a room number.
5. Bonus: Add a new menu option to "Update Customer Details" for an existing booking (change phone number or number of days).


---

# 📋 Assignments — Project 1 — Hotel Management System (Console)

| Assignment |
|---|
| Build the complete base Hotel Management System from this topic on your own machine and confirm all 6 menu options work correctly. |
| Add a 7th menu option: "Check Total Available Rooms" that counts and prints how many rooms are currently "Available". |
| Modify the `rooms` dictionary to include 10 rooms instead of 4, and re-test booking and cancellation with the larger dataset. |
| Add a `price_per_day` value for each room type (e.g., Standard = ₹1200, Deluxe = ₹2000) and update `book_room()` to calculate and display the total cost for the stay. |
| Write a function `total_revenue()` that loops through all current bookings and prints the total money earned so far. |
| Add input validation using `try/except` so that entering a non-numeric room number does not crash the program. |
| Add a feature to update an existing booking's number of days without cancelling and re-booking it from scratch. |
| Test the system by attempting to book a room that doesn't exist (e.g., room 999) and confirm the correct error message appears. |
| Test the system by cancelling a booking for a room that was never booked, and confirm it shows an appropriate message instead of crashing. |
| Add a feature to list only "Booked" rooms (the opposite of the existing "View Available Rooms" feature). |
| Write down (as comments in your code) at least 5 edge cases you tested and what the expected vs actual output was for each. |
| Add a simple "receptionist login" step at the start of the program — a fixed username/password check — before the main menu is shown. |
| Refactor the `search_booking()` function to also allow partial name matches (e.g., searching "raj" should match "Rajesh Kumar"). |
| Add a confirmation step before cancelling a booking (e.g., "Are you sure? (yes/no)") so bookings aren't accidentally cancelled. |
| Write a short reflection (3–5 sentences) on what part of this project was hardest for you to build, and how you debugged it. |
