# 📚 Advanced Decorators & Introduction to Generators

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Chain multiple decorators together confidently and predict their execution order
* 🎯 Build parameterized decorators that accept their own arguments
* 🎯 Understand what an iterator is, and how `__iter__` and `__next__` work internally
* 🎯 Understand generator functions and the `yield` keyword
* 🎯 Recognize when generators are a better choice than regular functions or lists

---

## 📖 Introduction

You've already learned the basics of decorators in the previous topic. Now we push further — combining multiple decorators, building decorators that accept their own custom arguments, and introducing a brand-new, closely related concept: **generators**. 🔄

Generators solve a very specific, very common problem: **What if you need to produce a huge (or even infinite) sequence of values, without storing them all in memory at once?** Think of Netflix streaming a movie — it doesn't download the entire film before you can watch the first second. That's the exact mindset behind generators.

### 🤔 Why does this topic exist?

* 🧱 Real-world applications often stack multiple decorators together (logging + validation + timing, all on one function)
* 🎛️ Sometimes a decorator itself needs configuration — like `@retry(times=3)` — this requires "parameterized" decorators
* 🔄 Iterators and generators are the backbone of how Python's `for` loops actually work internally
* 💾 Generators let you work with massive or infinite data streams without running out of memory

### 🤔 Where is it used?

* 📊 Data pipelines — processing huge CSV/log files one line at a time instead of loading everything into RAM
* 🎥 Streaming services (Netflix, YouTube) — data is generated/sent in chunks, not all at once
* 🌐 Web APIs with pagination — fetching results "page by page" instead of everything at once
* 🎮 Game development — generating infinite procedural levels or events on demand

> 💡 **Tip**
>
> If decorators are about **adding behavior**, generators are about **producing values lazily** (only when needed). They're different concepts, but this topic introduces both because generators also rely on some of the same "function as an object" thinking you learned with decorators.

---

## 🧠 Detailed Notes

### 1️⃣ Chaining Multiple Decorators

You already saw a glimpse of this in the previous topic — here we go deeper into **why order matters** and how to reason about chained decorators confidently.

```python
from functools import wraps

def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@uppercase_decorator
@exclaim_decorator
def get_message():
    return "hello world"

print(get_message())    # HELLO WORLD!!!
```

**How to trace the order, step by step:**

```
   @uppercase_decorator     ← applied SECOND (outer layer)
   @exclaim_decorator        ← applied FIRST (inner layer, closest to function)
   def get_message():
       return "hello world"

   Step 1: exclaim_decorator wraps get_message
           → "hello world" + "!!!" = "hello world!!!"

   Step 2: uppercase_decorator wraps THAT result
           → "hello world!!!".upper() = "HELLO WORLD!!!"
```

**Chaining decorators that print before/after (helps visualize execution order clearly):**

```python
def decorator_a(func):
    def wrapper(*args, **kwargs):
        print("A: before")
        result = func(*args, **kwargs)
        print("A: after")
        return result
    return wrapper

def decorator_b(func):
    def wrapper(*args, **kwargs):
        print("B: before")
        result = func(*args, **kwargs)
        print("B: after")
        return result
    return wrapper

@decorator_a
@decorator_b
def say_hi():
    print("Hi!")

say_hi()
```

Output:
```
A: before
B: before
Hi!
B: after
A: after
```

This nested "before-before-run-after-after" pattern is exactly like **opening layered boxes** — you open the outer box first (A: before), then the inner box (B: before), do the task inside, then close the inner box (B: after), then close the outer box (A: after).

| Decorator Order | Effect |
|---|---|
| `@A` on top, `@B` below, directly above function | `B` wraps first (closest to function), then `A` wraps around that |
| Execution order for "before" code | Top decorator's "before" code runs first |
| Execution order for "after" code | Top decorator's "after" code runs LAST |

🤔 **Quick thinking question:** In the `decorator_a`/`decorator_b` example, why does "A: after" print LAST, even though `decorator_a` is listed FIRST (on top)?
✅ **Answer:** Because `decorator_a` wraps around `decorator_b` (which wraps around the original function) — so `decorator_a`'s code runs on the very outside, meaning its "before" code runs first, but its "after" code has to wait for everything inside it (including `decorator_b` and the original function) to finish first.

---

### 2️⃣ Parameterized Decorators (`@decorator(arg)`)

Sometimes a decorator itself needs to accept **configuration** — for example, "retry up to N times" or "only allow role X." This requires an extra outer layer, making it a **decorator factory** — a function that returns a decorator.

```python
from functools import wraps

def repeat(times):                       # OUTER layer — accepts the decorator's OWN argument
    def decorator(func):                   # MIDDLE layer — the actual decorator
        @wraps(func)
        def wrapper(*args, **kwargs):       # INNER layer — wraps the original function call
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Priya")
```

Output:
```
Hello, Priya!
Hello, Priya!
Hello, Priya!
```

**Anatomy of a parameterized decorator (three layers):**

```
   def repeat(times):              ← Layer 1: captures the decorator's OWN argument
       def decorator(func):          ← Layer 2: the REAL decorator, receives the target function
           def wrapper(*args, **kwargs):  ← Layer 3: wraps the actual function call
               ...
           return wrapper
       return decorator
```

`@repeat(times=3)` first CALLS `repeat(3)`, which returns `decorator`. THEN `decorator` is applied to `greet`, exactly like a normal decorator.

**A practical parameterized decorator — retry on failure:**

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"⚠️ Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print("❌ All attempts failed.")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    print("✅ Success!")

unstable_function()
```

| Decorator Type | Syntax | Number of Nested Layers |
|---|---|---|
| Simple decorator | `@my_decorator` | 2 layers (`decorator` → `wrapper`) |
| Parameterized decorator | `@my_decorator(arg)` | 3 layers (`factory` → `decorator` → `wrapper`) |

> ⚠️ **Important**
>
> A common beginner mistake is forgetting the parentheses: `@repeat` (without calling it) vs `@repeat(times=3)` (correctly calling the factory first). Since `repeat` takes an argument, you MUST call it with `()` even if passing default values.

🤔 **Quick thinking question:** Why does `@repeat(times=3)` require three nested function layers, while a normal decorator like `@my_decorator` only needs two?
✅ **Answer:** The outermost layer exists specifically to accept and "remember" (via closure) the decorator's own custom argument (`times=3`) before it can return the actual 2-layer decorator that will be applied to the target function.

---

### 3️⃣ Understanding Iterators & `__iter__`, `__next__`

Every time you write a `for` item in a_list loop, Python is secretly using something called an **iterator** behind the scenes.

* An **iterable** is anything you can loop over (lists, strings, tuples, dictionaries, etc.) — it has an `__iter__()` method.
* An **iterator** is the actual "worker" object that produces one value at a time — it has both `__iter__()` and `__next__()` methods.

```python
numbers = [10, 20, 30]

# Behind the scenes, a for loop does roughly this:
iterator = iter(numbers)         # calls numbers.__iter__(), gets an iterator object

print(next(iterator))    # 10   — calls iterator.__next__()
print(next(iterator))    # 20
print(next(iterator))    # 30
print(next(iterator))    # ❌ StopIteration error — no more items!
```

**Building your own custom iterator class:**

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):              # makes this object ITERABLE — must return an iterator (itself, here)
        return self

    def __next__(self):               # defines HOW to get the next value
        if self.current > self.end:
            raise StopIteration         # signals "no more items" — REQUIRED to stop the loop
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 5)

for num in counter:
    print(num)    # 1 2 3 4 5
```

**What actually happens in a `for` loop, step by step:**

```
   for num in counter:
       print(num)

           is roughly equivalent to:

   iterator = iter(counter)          # calls counter.__iter__()
   while True:
       try:
           num = next(iterator)       # calls iterator.__next__()
           print(num)
       except StopIteration:
           break                        # loop ends automatically
```

| Method | Purpose |
|---|---|
| `__iter__(self)` | Returns the iterator object itself (usually `return self`) — makes the object usable in a `for` loop |
| `__next__(self)` | Returns the next value each time it's called; raises `StopIteration` when there are no more values |

> ⚠️ **Important**
>
> Forgetting to `raise StopIteration` when your custom iterator runs out of values will cause an **infinite loop** — Python will keep calling `__next__()` forever, expecting it to eventually signal the end.

🤔 **Quick thinking question:** What would happen if `CountUp.__next__()` never raised `StopIteration`, even after `self.current` passed `self.end`?
✅ **Answer:** The `for` loop (and any code calling `next()` repeatedly) would run forever, since Python only knows to stop when it receives a `StopIteration` exception — without it, the loop has no way of knowing the sequence has ended.

---

### 4️⃣ Introduction to Generator Functions and `yield`

Writing a full iterator class (like `CountUp` above) works, but it's verbose. Python offers a much simpler shortcut: **generator functions**, using the `yield` keyword instead of `return`.

```python
def count_up(start, end):
    current = start
    while current <= end:
        yield current       # PAUSES here, sends back 'current', remembers where it left off
        current += 1

for num in count_up(1, 5):
    print(num)    # 1 2 3 4 5
```

This does **exactly** what our `CountUp` class did — but in just 4 lines, with no `__iter__`/`__next__` boilerplate needed at all!

**What makes `yield` special — a function becomes a generator the moment it uses `yield`:**

```python
def simple_generator():
    print("First part")
    yield 1
    print("Second part")
    yield 2
    print("Third part")
    yield 3

gen = simple_generator()      # calling it does NOT run any code yet! Just creates a generator object

print(next(gen))     # First part      1
print(next(gen))     # Second part      2
print(next(gen))     # Third part        3
# print(next(gen))   # ❌ StopIteration — generator is exhausted
```

Notice how execution **pauses** at each `yield` and **resumes exactly where it left off** on the next `next()` call — this is fundamentally different from a normal function, which runs start-to-finish every single time it's called.

| Regular Function (`return`) | Generator Function (`yield`) |
|---|---|
| Runs completely, then returns ONE final value | Pauses at each `yield`, can produce MANY values over time |
| Calling it again re-runs everything from scratch | Calling `next()` resumes exactly where it paused |
| Uses `return` | Uses `yield` |
| Stores entire result in memory (e.g., building a full list) | Produces values one at a time — much more memory-efficient |

```python
# Comparing memory approach: a LIST-building function vs a GENERATOR
def get_squares_list(n):            # builds and stores the ENTIRE list in memory
    return [i**2 for i in range(n)]

def get_squares_generator(n):        # produces ONE value at a time, on demand
    for i in range(n):
        yield i**2

squares_list = get_squares_list(5)       # [0, 1, 4, 9, 16] — all computed and stored immediately
squares_gen = get_squares_generator(5)    # <generator object> — nothing computed yet!

for square in squares_gen:
    print(square)     # 0 1 4 9 16 — computed one at a time, as the loop asks for each value
```

> 💡 **Tip**
>
> You can also use a **generator expression** — a compact, one-line generator, similar to a list comprehension but with `()` instead of `[]`: `squares_gen = (i**2 for i in range(5))`.

🤔 **Quick thinking question:** If you call `simple_generator()` but never call `next()` on the result, does any of the code inside the function run?
✅ **Answer:** No — calling a generator function only creates a generator object; none of the function's code actually executes until you start calling `next()` (or iterate over it with a `for` loop) — this "lazy" behavior is a core feature of generators.

---

## 💡 Real-Life Analogy

* 🥪 **Chained Decorators → Layers of a Sandwich** — Each layer (decorator) adds its own effect, and you experience them in a specific order — the outermost layer (top slice of bread) is the first thing you notice and the last thing you finish.
* 🎛️ **Parameterized Decorators → A Custom Settings Dial Before Wrapping a Gift** — Before wrapping the gift (decorator), you first choose settings like "wrap it in red paper" or "add 3 ribbons" (the decorator's own arguments) — the wrapping behavior changes based on what you configure.
* 🎫 **Iterators → A Ticket Dispenser Machine at a Bakery** — Each time you press the button (`next()`), it gives you exactly ONE ticket number, remembering where it left off — until it runs out of tickets (`StopIteration`).
* 🎬 **Generators → Netflix Streaming a Show** — Instead of downloading an entire season (a full list) before you can watch anything, Netflix sends you one episode (one `yield`ed value) at a time, exactly when you need it — saving massive amounts of storage/memory.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Chained decorators | Flask routes commonly stack `@app.route()` with `@login_required` together |
| Parameterized decorators | Django's `@permission_required('can_edit')`, retry libraries like `@retry(max_attempts=3)` |
| Custom iterators | Database cursor objects (like in `sqlite3` or `psycopg2`) let you iterate through query results row by row |
| Generators | Pandas' `chunk` reading for huge CSV files; Python's own `range()` object behaves like a generator internally |
| Infinite generators | Log-monitoring tools that continuously watch and process new log lines as they're written |

---

## 🔍 Industry Example

**Scenario:** A **Data Engineer at a fintech company** needs to process a **10 GB transaction log file** — far too large to load entirely into memory at once.

1. Instead of writing `all_lines = file.readlines()` (which would try to load the ENTIRE file into RAM), they write a **generator function** `read_large_file(filepath)` that uses `yield` to return one line at a time.
2. Their processing pipeline then uses this generator with a simple `for line in read_large_file(...)` loop — at any given moment, only ONE line is actually in memory, no matter how huge the file is.
3. To add monitoring, they stack **multiple decorators** on their processing function: `@log_activity` (records what's happening) and `@retry(max_attempts=3)` (a parameterized decorator that automatically retries if a network call to save results temporarily fails).
4. They also build a **custom iterator class** for a specialized data source (like a live sensor feed) where `__next__()` fetches the next reading directly from a hardware device, only when requested.
5. This combination — decorators for cross-cutting behavior, generators for memory-efficient data processing — is exactly how real large-scale data engineering pipelines are built in production.

---

## 📊 Diagram

```
             CHAINED & PARAMETERIZED DECORATORS
             -------------------------------------
     @decorator_a               ← "before" runs 1st, "after" runs LAST
     @decorator_b               ← "before" runs 2nd, "after" runs 2nd-last
     @repeat(times=3)           ← parameterized: factory → decorator → wrapper
     def my_function(): ...


              ITERATOR PROTOCOL
              --------------------
     iterable  ──►  iter(iterable)  ──►  iterator object
                                              │
                              ┌───────────────┼───────────────┐
                              ▼               ▼               ▼
                        next() → val1   next() → val2   next() → StopIteration
                                                                  (loop ends)


          GENERATOR EXECUTION — PAUSE & RESUME
          ----------------------------------------
     def count_up(start, end):
         current = start
         while current <= end:
             yield current   ◄── PAUSES here, remembers state
             current += 1     ◄── RESUMES here on next next() call

     gen = count_up(1, 3)
       next(gen) → 1  (paused after first yield)
       next(gen) → 2  (resumed, paused again)
       next(gen) → 3  (resumed, paused again)
       next(gen) → StopIteration (loop condition now false)


         LIST vs GENERATOR — MEMORY COMPARISON
         ------------------------------------------
     LIST:      [🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎]  ← ALL items exist in memory at once
     GENERATOR:  🍎 → (next item made only when asked) → 🍎 → ...  ← ONE at a time
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Chained decorators are applied top-to-bottom, so the top one's code runs completely first, then the next one."
  ✅ **Correct:** They're nested — the "before" code of each decorator runs top-to-bottom, but the "after" code runs in REVERSE order (bottom-to-top), since each decorator must wait for everything inside it to finish first.

* ❌ **Wrong belief:** "`@repeat` and `@repeat()` behave the same way."
  ✅ **Correct:** `@repeat` (without parentheses) tries to use `repeat` itself as the decorator, which will error if `repeat` is designed as a decorator factory expecting arguments — you must call it: `@repeat(times=3)`.

* ❌ **Wrong belief:** "You need `__iter__` and `__next__` to make any looping code — that's the only way."
  ✅ **Correct:** Generator functions (`yield`) achieve the exact same result far more simply, without ever needing to manually define `__iter__`/`__next__`.

* ❌ **Wrong belief:** "Calling a generator function immediately runs all of its code."
  ✅ **Correct:** Calling a generator function only creates a generator object — none of the code inside runs until you call `next()` on it (or loop over it).

* ❌ **Wrong belief:** "A generator can be looped over multiple times, just like a list."
  ✅ **Correct:** Once a generator is exhausted (fully looped through), it cannot be reset or reused — you'd need to call the generator function again to create a fresh one.

---

## 💬 Interview Corner

**Q1: In what order do chained decorators execute their "before" and "after" code?**
✅ "Before" code runs top-to-bottom (outer decorator's before-code first); "after" code runs bottom-to-top (inner decorator's after-code first) — like nested boxes opening and closing in reverse order.

**Q2: What is a parameterized decorator, and why does it need an extra layer of nesting?**
✅ It's a decorator that accepts its own configuration arguments (e.g., `@retry(max_attempts=3)`). It needs an extra outer layer specifically to capture and remember that argument via closure, before returning the actual decorator function.

**Q3: What is the difference between an iterable and an iterator?**
✅ An iterable is any object you can loop over and has an `__iter__()` method (like a list). An iterator is the object actually returned by `iter()`, which has both `__iter__()` and `__next__()`, and produces values one at a time.

**Q4: What is the key advantage of a generator over a function that returns a full list?**
✅ Memory efficiency — a generator produces values one at a time, on demand ("lazily"), instead of computing and storing an entire collection in memory all at once, which is critical for very large or infinite sequences.

---

## 📝 Quick Summary

* 🥪 Chained decorators execute "before" code top-to-bottom and "after" code bottom-to-top, like nested layers
* 🎛️ Parameterized decorators (`@decorator(arg)`) require an extra outer layer to capture their own custom argument, making them "decorator factories"
* 🔄 An iterable has `__iter__()`; an iterator has both `__iter__()` and `__next__()`, producing one value at a time
* 🛑 A custom iterator MUST `raise StopIteration` when it runs out of values, or it will loop forever
* ⏸️ `yield` turns a regular function into a generator function — execution pauses at each `yield` and resumes exactly there on the next call
* 💾 Generators are far more memory-efficient than building full lists, since values are only produced when actually needed
* 🚫 Generators can only be looped through ONCE — once exhausted, you must create a new one to loop again
* 🎯 Both decorators and generators rely on Python's ability to treat functions as flexible, "pausable" building blocks

---

## 🎯 Class Activity

**"Build a Chained Decorator + Generator Mini Toolkit" 🧰**

1. Write two decorators, `@bold` and `@shout`, that both modify a string returned by a function. Stack them in both possible orders and compare the outputs.
2. Write a parameterized decorator `@repeat(times)` and apply it to a function that prints a motivational quote, testing with `times=2` and `times=5`.
3. Build a custom iterator class `EvenNumbers(start, end)` that yields only even numbers in a range, correctly implementing `__iter__` and `__next__`, including `StopIteration`.
4. Rewrite the same `EvenNumbers` logic as a simple generator function using `yield`, and compare how much shorter the code is.
5. Bonus: Write a generator function `infinite_counter()` that yields numbers forever (no end condition), and use a `for` loop with a manual `break` after printing the first 10 values.


---

# 📋 Assignments — Advanced Decorators & Introduction to Generators

| Assignment |
|---|
| Write two decorators, `@add_prefix` and `@add_suffix`, and stack them on a function returning a string. Test both possible stacking orders and compare results. |
| Write a parameterized decorator `@multiply_result(factor)` that multiplies a function's numeric return value by `factor`, and test it with different factor values. |
| Write a parameterized decorator `@retry(max_attempts=3)` that retries a function if it raises an exception, using a function that randomly fails to test it. |
| Build a custom iterator class `Countdown(start)` that counts down from `start` to 0, correctly implementing `__iter__`, `__next__`, and `StopIteration`. |
| Rewrite the `Countdown` logic as a generator function using `yield`, and confirm both versions produce identical output. |
| Write a generator function `even_numbers(limit)` that yields only even numbers from 0 up to `limit`. |
| Write a generator function `fibonacci_sequence(n)` that yields the first `n` Fibonacci numbers, one at a time. |
| Create a custom iterator class `Alphabet` that iterates through the English alphabet from 'a' to 'z'. |
| Compare memory behavior: write a function that returns a LIST of the first 1 million square numbers, and a generator version that yields them one at a time — explain (in comments) why the generator is more memory-efficient. |
| Write a generator expression (one-liner, using `()`) that generates the cubes of numbers from 1 to 10, and print each value using a loop. |
| Stack three decorators (`@log_activity`, `@measure_time`, and a parameterized `@repeat(times=2)`) on a single function, and predict the full output order before running it. |
| Write a generator function `infinite_even_numbers()` with no end condition, and safely print only the first 15 values using a loop with a counter and `break`. |
| Try calling `next()` on an already-exhausted generator and observe the exact error message Python shows. |
| Write a custom iterator class `WordSplitter(sentence)` that iterates through a sentence one word at a time (using `.split()` internally). |
| Write a short reflection (3–5 sentences) comparing when you would choose to write a full iterator class vs. a simple generator function for the same task. |
# 📚 Generators & Mini Project — Dynamic Ticket Pricing System

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Confidently create custom iterators and generators for practical use cases
* 🎯 Recognize real-life scenarios where generators are the right tool (infinite sequences, data streams)
* 🎯 Build a working ticket sales simulator using a custom iterator
* 🎯 Use a generator to dynamically calculate ticket prices based on live demand
* 🎯 Clearly demonstrate and explain how generators optimize memory usage for large sequences

---

## 📖 Introduction

You've learned the theory behind iterators and generators — now let's apply it to something everyone can relate to: **buying event tickets** 🎟️. Ever noticed how concert or flight ticket prices seem to increase as more people buy them, or as the event date gets closer? That's **dynamic pricing** — and it's a perfect real-world use case for generators, since prices need to be calculated **on-the-fly**, one ticket at a time, based on constantly changing demand.

### 🤔 Why does this topic exist?

* 🎫 Dynamic/surge pricing is used everywhere — concert tickets, flights, Uber rides, hotel bookings
* 🔄 This is a genuinely practical, portfolio-worthy mini project that showcases both iterators AND generators together
* 💾 It clearly demonstrates memory efficiency — something abstract in theory becomes obvious once you simulate thousands of ticket sales

### 🤔 Where is it used?

* ✈️ Airlines (IndiGo, Air India) — ticket prices increase as seats fill up or the flight date approaches
* 🎫 BookMyShow, Ticketmaster — concert ticket prices can rise based on demand
* 🚕 Uber/Ola — surge pricing during high-demand periods
* 🏨 Hotel booking sites (MakeMyTrip, Booking.com) — room prices fluctuate based on occupancy and dates

> 💡 **Tip**
>
> This project is a great one to mention in interviews or put on your resume — it combines OOP (custom iterator), functional concepts (generators), and a genuinely realistic business problem (dynamic pricing).

---

## 🧠 Detailed Notes

### 1️⃣ Creating Custom Iterators and Generators

Let's start by building a **custom iterator** that represents a batch of tickets being sold, one by one.

```python
class TicketBatch:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.sold = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.sold >= self.total_tickets:
            raise StopIteration

        self.sold += 1
        return f"🎟️ Ticket #{self.sold} sold"

batch = TicketBatch(5)

for ticket_status in batch:
    print(ticket_status)
```

Output:
```
🎟️ Ticket #1 sold
🎟️ Ticket #2 sold
🎟️ Ticket #3 sold
🎟️ Ticket #4 sold
🎟️ Ticket #5 sold
```

**Now let's build the equivalent as a simpler generator function:**

```python
def ticket_batch_generator(total_tickets):
    sold = 0
    while sold < total_tickets:
        sold += 1
        yield f"🎟️ Ticket #{sold} sold"

for ticket_status in ticket_batch_generator(5):
    print(ticket_status)
```

Both approaches produce identical output — but notice how much shorter the generator version is.

| Approach | Code Length | Best Used When |
|---|---|---|
| Custom iterator class | Longer, more boilerplate | You need extra methods/state beyond just iteration (e.g., `cancel_sale()`, `get_summary()`) |
| Generator function | Shorter, simpler | You just need to produce a sequence of values, nothing more |

🤔 **Quick thinking question:** If `TicketBatch` needed an extra method like `refund_ticket()` that other code could call directly on the object, would a generator function still be a good fit?
✅ **Answer:** Not as easily — generators are focused purely on producing a sequence of values and don't naturally support extra custom methods the way a full class does; a custom iterator class would be the better choice here.

---

### 2️⃣ Real-Life Generator Use-Cases (Infinite Sequences, Streams)

Generators genuinely shine in situations where either:

* 🌀 The sequence is **infinite** (or unknown length) — you can't build a full list because it might never end
* 🌊 The data is a **stream** — arriving continuously, and you want to process it as it comes, not all at once

**Infinite sequence example — a ticket ID generator that never "runs out":**

```python
def ticket_id_generator():
    ticket_id = 1000
    while True:                    # infinite loop — but that's OK, because it's a generator!
        yield f"TCKT-{ticket_id}"
        ticket_id += 1

id_gen = ticket_id_generator()

print(next(id_gen))    # TCKT-1000
print(next(id_gen))    # TCKT-1001
print(next(id_gen))    # TCKT-1002
# ... this could keep going literally forever, without ever running out of memory
```

**Stream-like example — simulating live ticket demand updates:**

```python
import random
import time

def live_demand_stream():
    while True:
        demand_level = random.choice(["low", "medium", "high"])
        yield demand_level
        time.sleep(1)          # simulates a new demand reading arriving every second

demand_gen = live_demand_stream()

for i in range(5):                     # only look at the first 5 "live updates" for this demo
    current_demand = next(demand_gen)
    print(f"📡 Live demand update: {current_demand}")
```

> ⚠️ **Important**
>
> An infinite generator is only safe because it produces values **one at a time, on demand**. If you tried to do `list(ticket_id_generator())`, Python would try to build an infinitely long list and eventually crash — always be careful to only pull the number of values you actually need from an infinite generator.

🤔 **Quick thinking question:** Why is it perfectly safe to write `while True:` inside a generator function, when it would be dangerous inside a normal function?
✅ **Answer:** Because a generator's code only runs UP TO the next `yield`, then pauses — it doesn't try to complete the entire infinite loop at once. A normal function with `while True` (and no `yield`) would try to run forever immediately upon being called, crashing or freezing the program.

---

### 3️⃣ Implementing a Ticket Sales Simulator with a Custom Iterator

Let's build a more realistic version — a ticket sales simulator that tracks available seats and stops correctly once sold out.

```python
class TicketSalesSimulator:
    def __init__(self, event_name, total_seats):
        self.event_name = event_name
        self.total_seats = total_seats
        self.seats_sold = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.seats_sold >= self.total_seats:
            raise StopIteration

        self.seats_sold += 1
        remaining = self.total_seats - self.seats_sold
        return {
            "event": self.event_name,
            "ticket_number": self.seats_sold,
            "seats_remaining": remaining
        }

simulator = TicketSalesSimulator("Coldplay Live in Mumbai 🎸", 5)

for sale in simulator:
    print(f"Sold ticket #{sale['ticket_number']} for {sale['event']} — {sale['seats_remaining']} seats left")
```

Output:
```
Sold ticket #1 for Coldplay Live in Mumbai 🎸 — 4 seats left
Sold ticket #2 for Coldplay Live in Mumbai 🎸 — 3 seats left
Sold ticket #3 for Coldplay Live in Mumbai 🎸 — 2 seats left
Sold ticket #4 for Coldplay Live in Mumbai 🎸 — 1 seats left
Sold ticket #5 for Coldplay Live in Mumbai 🎸 — 0 seats left
```

**Adding a "sold out" check as an extra method (something a generator alone couldn't do as cleanly):**

```python
class TicketSalesSimulator:
    def __init__(self, event_name, total_seats):
        self.event_name = event_name
        self.total_seats = total_seats
        self.seats_sold = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_sold_out():
            raise StopIteration
        self.seats_sold += 1
        return self.seats_sold

    def is_sold_out(self):                   # extra method — easy to add to a CLASS, harder in a pure generator
        return self.seats_sold >= self.total_seats

    def seats_remaining(self):
        return self.total_seats - self.seats_sold
```

🤔 **Quick thinking question:** Why does this project use a custom iterator CLASS (not just a plain generator function) for the ticket sales simulator?
✅ **Answer:** Because the simulator needs extra supporting methods like `is_sold_out()` and `seats_remaining()` that other parts of the program can call directly — a class naturally supports this, while a plain generator function only supports producing the next value.

---

### 4️⃣ Using a Generator to Dynamically Calculate Ticket Prices Based on Demand

Now for the core "dynamic pricing" logic — a **generator function** that calculates and yields a new ticket price each time, based on how many tickets have already been sold (simulating rising demand).

```python
def dynamic_price_generator(base_price, total_seats):
    seats_sold = 0
    while seats_sold < total_seats:
        seats_sold += 1
        demand_ratio = seats_sold / total_seats          # how "full" the event is, from 0.0 to 1.0

        if demand_ratio < 0.5:
            price = base_price                               # low demand — base price
        elif demand_ratio < 0.8:
            price = base_price * 1.2                          # medium demand — 20% increase
        else:
            price = base_price * 1.5                           # high demand — 50% increase

        yield {
            "ticket_number": seats_sold,
            "price": round(price, 2),
            "demand_ratio": round(demand_ratio, 2)
        }

pricing = dynamic_price_generator(base_price=1000, total_seats=10)

for ticket in pricing:
    print(f"Ticket #{ticket['ticket_number']}: ₹{ticket['price']} (demand: {ticket['demand_ratio']*100:.0f}%)")
```

Output (prices rise as more tickets sell):
```
Ticket #1: ₹1000.0 (demand: 10%)
Ticket #2: ₹1000.0 (demand: 20%)
...
Ticket #6: ₹1200.0 (demand: 60%)
...
Ticket #9: ₹1500.0 (demand: 90%)
Ticket #10: ₹1500.0 (demand: 100%)
```

**Combining the custom iterator (sales tracking) with the generator (dynamic pricing) — putting it ALL together:**

```python
def run_ticket_sale(event_name, total_seats, base_price):
    pricing_generator = dynamic_price_generator(base_price, total_seats)

    print(f"🎫 Ticket Sale Started: {event_name}\n")

    total_revenue = 0
    for ticket in pricing_generator:
        total_revenue += ticket["price"]
        print(f"Sold Ticket #{ticket['ticket_number']} → ₹{ticket['price']} (demand {ticket['demand_ratio']*100:.0f}%)")

    print(f"\n💰 Total Revenue: ₹{total_revenue}")

run_ticket_sale("Coldplay Live in Mumbai 🎸", total_seats=10, base_price=1000)
```

> 💡 **Tip**
>
> Notice that at NO point did we build a full list of all 10 ticket prices in advance — each price is calculated fresh, exactly when needed, based on the CURRENT demand at that moment. This is dynamic pricing done the "generator way."

🤔 **Quick thinking question:** Why is a generator (rather than pre-calculating all prices into a list upfront) the more realistic approach for dynamic pricing?
✅ **Answer:** Real-world demand changes unpredictably and continuously as tickets sell — a generator calculates each price fresh, based on the CURRENT state at that exact moment, which mirrors how real dynamic pricing systems work (unlike a pre-computed list, which would need to know all future demand in advance).

---

### 5️⃣ Demonstrating How Generators Optimize Memory for Large Sequences

Let's make the memory benefit concrete using Python's `sys.getsizeof()` to actually MEASURE memory usage.

```python
import sys

def get_prices_list(total_seats, base_price):
    return [base_price * 1.1 for _ in range(total_seats)]     # builds and stores EVERYTHING immediately

def get_prices_generator(total_seats, base_price):
    for _ in range(total_seats):
        yield base_price * 1.1                                    # produces ONE value at a time

# Comparing memory for 1 MILLION tickets
prices_list = get_prices_list(1_000_000, 1000)
prices_gen = get_prices_generator(1_000_000, 1000)

print(f"List size in memory: {sys.getsizeof(prices_list):,} bytes")
print(f"Generator size in memory: {sys.getsizeof(prices_gen):,} bytes")
```

Typical output:
```
List size in memory: 8,448,728 bytes    (roughly 8 MB!)
Generator size in memory: 200 bytes      (basically nothing!)
```

The **list** must physically store all 1 million calculated prices in memory at once. The **generator**, on the other hand, only stores the tiny bit of "state" needed to calculate the NEXT value when asked — regardless of whether you need 10 prices or 10 million.

| Sequence Size | List Memory Usage | Generator Memory Usage |
|---|---|---|
| 10 tickets | Small, negligible difference | Small, negligible difference |
| 1,000,000 tickets | Several MB, grows with size | Stays constant, tiny (just a few hundred bytes) |
| Infinite sequence | ❌ Impossible — would crash | ✅ Works perfectly fine |

> ⚠️ **Important**
>
> This is exactly why real large-scale ticket-selling platforms (handling millions of transactions) rely on generator-style, "process one at a time" logic internally — trying to hold every single calculation in memory at once simply wouldn't scale.

🤔 **Quick thinking question:** For a real platform selling tickets to a stadium with 80,000 seats, why would using a generator for price calculations be a smarter engineering choice than pre-building a full list of 80,000 prices?
✅ **Answer:** A generator only ever holds the current calculation in memory, regardless of how many seats there are, keeping memory usage constant and predictable — a pre-built list would consume increasingly large amounts of memory as the venue size grows, and wastefully calculates prices for seats that may never even sell.

---

## 💡 Real-Life Analogy

* 🎟️ **Custom Iterator (TicketSalesSimulator) → A Physical Ticket Booth with a Counter** — Each time someone buys a ticket, the booth clerk (the iterator) updates the "seats remaining" counter and hands out the next ticket, one at a time, stopping once the counter hits zero.
* 📈 **Dynamic Pricing Generator → An Airline's Live Fare Display** — The price shown for a flight seat isn't pre-calculated for the whole year and stored somewhere — it's recalculated in real-time based on current demand, exactly when you check.
* 💾 **Memory Optimization → Cooking Meals to Order vs. Pre-Cooking Everything** — A restaurant that cooks each dish fresh as it's ordered (generator) uses far less storage/fridge space than one that pre-cooks and stores a year's worth of every possible dish in advance (list).

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Custom iterators for sales tracking | Event ticketing platforms (BookMyShow, Ticketmaster) internally track seat inventory using similar stateful objects |
| Dynamic pricing generators | Uber/Ola surge pricing, airline fare engines, hotel booking platforms — prices recalculated based on live demand |
| Infinite ID generators | Order ID / Ticket ID generation systems in e-commerce and ticketing platforms |
| Memory-efficient streaming | Spotify/YouTube — processing and delivering data streams without loading entire files into memory |
| Live demand data streams | Stock trading platforms — continuously processing live price ticks without storing the entire day's data in memory upfront |

---

## 🔍 Industry Example

**Scenario:** An engineer at **BookMyShow** is building the backend for a high-demand concert ticket sale (e.g., a major artist's India tour), where thousands of users may try to buy tickets within seconds of sales opening.

1. They use a **custom iterator class**, `TicketSalesSimulator`, to represent each event's seat inventory — tracking `seats_sold`, checking `is_sold_out()`, and safely stopping (`StopIteration`) once the venue is full.
2. To handle **dynamic pricing** (common for high-demand shows), they use a **generator function** that recalculates the current price based on the live demand ratio — ensuring the displayed price always reflects real-time scarcity, without pre-computing prices for every possible scenario in advance.
3. For generating unique ticket/order IDs at massive scale, they use an **infinite generator** (`ticket_id_generator()`) — since they have no way of knowing in advance exactly how many tickets will ultimately be sold.
4. When benchmarking their system, the engineering team specifically measures memory usage using tools similar to `sys.getsizeof()`, confirming that their generator-based approach keeps memory usage flat and predictable even during massive traffic spikes — critical for a system that must not crash during a high-profile ticket sale.
5. This combination of stateful iterators (for tracking) and generators (for calculation) mirrors exactly how real, large-scale ticketing platforms are engineered to handle extreme demand efficiently.

---

## 📊 Diagram

```
          DYNAMIC TICKET PRICING SYSTEM — ARCHITECTURE
          ------------------------------------------------

    🎫 TicketSalesSimulator (custom iterator)
       ├── seats_sold, total_seats
       ├── __next__() → sells one ticket, raises StopIteration when sold out
       └── is_sold_out(), seats_remaining()   ← extra methods only a CLASS can offer


    💰 dynamic_price_generator (generator function)
       ├── tracks seats_sold internally
       ├── calculates demand_ratio = seats_sold / total_seats
       └── yields a NEW price each time, based on CURRENT demand
                 │
        ┌────────┼────────┐
        ▼         ▼         ▼
   demand<50%  demand<80%  demand≥80%
   base price   ×1.2         ×1.5


         MEMORY COMPARISON — 1 MILLION TICKETS
         ------------------------------------------
    LIST approach:
    [₹1000, ₹1000, ..., ₹1500]  ← ALL 1,000,000 prices stored at once 🐘 (huge memory)

    GENERATOR approach:
    ₹1000 → (calculate next only when asked) → ₹1000 → ...  🐜 (tiny, constant memory)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "It's fine to pre-calculate a full list of prices for every possible ticket in advance, since it's simpler."
  ✅ **Correct:** Pre-calculating everything wastes memory (especially at scale) and doesn't reflect real, live-changing demand — a generator recalculates each price fresh, based on current conditions.

* ❌ **Wrong belief:** "An infinite generator like `ticket_id_generator()` will eventually crash the program since it never stops."
  ✅ **Correct:** It's perfectly safe as long as you only pull the values you actually need (e.g., using `next()` a limited number of times) — the generator itself uses almost no memory regardless of how "infinite" it is.

* ❌ **Wrong belief:** "A custom iterator class and a generator function are interchangeable in every situation."
  ✅ **Correct:** Use a class when you need extra supporting methods and state (like `is_sold_out()`); use a generator function when you simply need to produce a sequence of values with minimal code.

* ❌ **Wrong belief:** "Once a ticket sale generator reaches `StopIteration`, you can just call it again to restart the sale."
  ✅ **Correct:** A generator, once exhausted, cannot be reused — you'd need to call the generator function again to create a completely fresh one for a new sale.

* ❌ **Wrong belief:** "Memory savings from generators only matter for truly massive datasets, not smaller ones."
  ✅ **Correct:** While the difference is most dramatic at large scale, it's still good practice to default to generators whenever you don't need the entire sequence stored at once — it's a habit that scales well as your projects grow.

---

## 💬 Interview Corner

**Q1: Why would you choose a custom iterator class over a generator function for the ticket sales simulator?**
✅ Because the simulator needs additional supporting methods (like `is_sold_out()` and `seats_remaining()`) that other code needs to call directly — a class supports this naturally, while a generator function only produces a sequence of values.

**Q2: How does the dynamic pricing generator ensure prices reflect real, current demand instead of pre-calculated guesses?**
✅ It recalculates the `demand_ratio` and resulting price fresh, every single time a new value is requested, based on the CURRENT `seats_sold` count at that exact moment — not from a list computed in advance.

**Q3: Why is memory usage roughly constant for a generator, regardless of how many values it eventually produces?**
✅ A generator only stores the minimal internal state needed to compute the NEXT value — it never stores the entire sequence of past or future values at once, unlike a list.

**Q4: Give a real-world example (other than ticket pricing) where an infinite generator would be genuinely useful.**
✅ Generating unique, ever-increasing order IDs or transaction IDs for an e-commerce platform — since there's no fixed upper limit on how many orders might eventually be placed, an infinite generator handles this naturally without pre-allocating a fixed range.

---

## 📝 Quick Summary

* 🎟️ A custom iterator class is ideal when you need extra methods/state beyond just producing values (like `is_sold_out()`)
* 🌀 Infinite generators (`while True: yield ...`) are safe because they only compute one value at a time, on demand
* 🌊 Generators are perfect for stream-like data that arrives continuously or is too large to hold in memory
* 💰 A dynamic pricing generator recalculates ticket prices fresh, based on the CURRENT demand ratio each time
* 🧩 Combining a custom iterator (sales tracking) with a generator (price calculation) mirrors real ticketing platform architecture
* 💾 `sys.getsizeof()` can concretely demonstrate that generators use dramatically less memory than fully-built lists, especially at scale
* 🚫 Generators can only be iterated through once — they cannot be reset or reused after exhaustion
* 🎯 This project proves that iterators and generators aren't just abstract theory — they solve real, practical business problems like dynamic pricing at scale

---

## 🎯 Class Activity

**"Build a Complete Dynamic Ticket Pricing Simulator" 🎫💰**

1. Build the `TicketSalesSimulator` custom iterator class shown in this topic, and run it for an event with 8 total seats, printing each sale.
2. Build the `dynamic_price_generator()` function, and run it for the same event with a base price of your choice, printing each ticket's price and demand percentage.
3. Combine both into a single `run_ticket_sale()` function (like the example shown) that prints a full sales report AND the total revenue collected.
4. Use `sys.getsizeof()` to compare the memory size of a list of 100,000 pre-calculated prices vs. a generator producing the same 100,000 prices, and print both results.
5. Bonus: Modify the pricing logic to add a 4th demand tier — "SOLD OUT WARNING" (demand > 95%) — that applies a 2x price multiplier for the last few tickets.


---

# 📋 Assignments — Generators & Mini Project — Dynamic Ticket Pricing System

| Assignment |
|---|
| Build the `TicketSalesSimulator` custom iterator class exactly as shown, and run it for an event with 12 seats, printing every ticket sold. |
| Build the `dynamic_price_generator()` function and test it with 3 different base prices (₹500, ₹1500, ₹3000) for a 20-seat event. |
| Combine the iterator and generator into a single `run_ticket_sale()` function that prints a full sales report and total revenue collected. |
| Add a 4th demand tier to the pricing logic: when demand exceeds 95%, apply a 2x "surge" multiplier instead of the usual 1.5x. |
| Write an infinite generator `order_id_generator()` that yields unique order IDs starting from "ORD-5000", and print the first 10 values. |
| Use `sys.getsizeof()` to compare memory usage between a list and a generator, each producing 500,000 ticket prices, and print both results clearly. |
| Add an `is_sold_out()` and `seats_remaining()` method to your `TicketSalesSimulator` class, and use them in a message printed after each ticket sale. |
| Simulate a "live demand stream" generator that yields a random demand level ("low", "medium", "high") every time it's called, and print the first 8 updates. |
| Modify the dynamic pricing generator to also apply a "last-minute" price increase if fewer than 3 seats remain, regardless of the demand ratio. |
| Write a generator function `batch_ticket_sales(total_seats, batch_size)` that yields tickets in GROUPS (e.g., 5 tickets at a time) instead of one at a time. |
| Build a custom iterator for a "waitlist" system — once the main event is sold out, additional `next()` calls should return `"Added to waitlist"` instead of raising `StopIteration` immediately. |
| Write a program that uses your dynamic pricing generator to calculate and print the TOTAL cost for a group booking of exactly 4 tickets bought together. |
| Test what happens when you try to iterate through an already-exhausted `TicketSalesSimulator` object a second time, and explain the result in a comment. |
| Create a generator `flash_sale_prices(base_price, discount_percent, total_seats)` that applies a special discount ONLY to the first 20% of tickets sold, then reverts to normal dynamic pricing. |
| Write a short reflection (3–5 sentences) explaining how this project demonstrates real memory-saving advantages of generators, using specific numbers from your own testing. |
