# 📚 String Manipulation

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand what a "string" is in Python and why text needs its own data type
* 🎯 Perform basic string operations like concatenation and repetition
* 🎯 Use built-in string methods to clean, search, and transform text
* 🎯 Access individual characters and sub-parts of a string using indexing and slicing
* 🎯 Format strings dynamically using f-strings (the modern Python way)
* 🎯 Apply string skills to real-world tasks like validating user input, formatting reports, and cleaning data

---

## 📖 Introduction

Every time you type your name into a form, send a WhatsApp message, or search something on Google — you're working with **text**. In programming, we call text a **string**. 🧵

A string is simply a sequence of characters (letters, numbers, symbols) wrapped inside quotes.

```python
name = "Priya"
message = 'Hello, World!'
```

### 🤔 Why does this topic exist?

Almost every real-world application deals with text — usernames, passwords, emails, product names, addresses, chat messages, search queries. If you can't manipulate text confidently, you can't build real software.

### 🤔 Where is it used?

* 🌐 Websites — validating email format, showing usernames
* 📱 Apps — WhatsApp showing "typing..." status
* 🔍 Search engines — matching your search query to web pages
* 📊 Data Analysis — cleaning messy text data from Excel/CSV files
* 🤖 Chatbots — understanding and replying to user messages

> 💡 **Tip**
>
> In Python, strings are written using single quotes `' '`, double quotes `" "`, or triple quotes `''' '''` for multi-line text. All three work the same way for normal strings.

---

## 🧠 Detailed Notes

### 1️⃣ Basic String Operations

Strings support several simple but powerful operations.

| Operation | Symbol | Example | Result |
|---|---|---|---|
| Concatenation (joining) | `+` | `"Hello" + " " + "World"` | `"Hello World"` |
| Repetition | `*` | `"Ha" * 3` | `"HaHaHa"` |
| Membership check | `in` | `"e" in "Hello"` | `True` |
| Length | `len()` | `len("Hello")` | `5` |
| Comparison | `==`, `!=` | `"cat" == "cat"` | `True` |

```python
first_name = "Rahul"
last_name = "Sharma"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)          # Rahul Sharma

# Repetition
line = "-" * 20
print(line)                # --------------------

# Membership
print("Sharma" in full_name)   # True

# Length
print(len(full_name))      # 12
```

> ⚠️ **Important**
>
> You cannot add a string and a number directly. `"Age: " + 25` will throw an error. You must convert the number using `str(25)` first.

🤔 **Quick thinking question:** What will `print("Py" + "thon" * 2)` output?
✅ **Answer:** `Pythonthon` — because `*` (repetition) runs before `+` (concatenation), just like multiplication before addition in maths.

---

### 2️⃣ String Methods

Python strings come with many **built-in methods** — ready-made tools that help you transform or inspect text. A method is called using `variable.method()`.

| Method | What it does | Example | Output |
|---|---|---|---|
| `.upper()` | Converts to uppercase | `"hello".upper()` | `"HELLO"` |
| `.lower()` | Converts to lowercase | `"HELLO".lower()` | `"hello"` |
| `.strip()` | Removes extra spaces from both ends | `"  hi  ".strip()` | `"hi"` |
| `.replace(a, b)` | Replaces text `a` with `b` | `"cat".replace("c","b")` | `"bat"` |
| `.split(sep)` | Breaks string into a list | `"a,b,c".split(",")` | `['a','b','c']` |
| `.join(list)` | Joins a list into a string | `"-".join(['a','b'])` | `"a-b"` |
| `.find(x)` | Returns index of first match, or -1 | `"hello".find("l")` | `2` |
| `.count(x)` | Counts occurrences | `"banana".count("a")` | `3` |
| `.startswith(x)` | Checks starting text | `"hello".startswith("he")` | `True` |
| `.endswith(x)` | Checks ending text | `"hello".endswith("lo")` | `True` |
| `.isdigit()` | Checks if all characters are digits | `"123".isdigit()` | `True` |
| `.title()` | Capitalizes each word | `"john doe".title()` | `"John Doe"` |

```python
email = "  Priya.Sharma@GMAIL.com  "

cleaned = email.strip().lower()
print(cleaned)               # priya.sharma@gmail.com

username = cleaned.split("@")[0]
print(username)              # priya.sharma

is_gmail = cleaned.endswith("@gmail.com")
print(is_gmail)              # True
```

> 💡 **Tip**
>
> String methods **never change the original string**. They always return a **new** string. Strings in Python are *immutable* (cannot be changed in place).

🤔 **Quick thinking question:** After `x = "hello"` and `x.upper()`, what is the value of `x`?
✅ **Answer:** Still `"hello"` — because `.upper()` returns a new string; it doesn't modify `x` unless you reassign it: `x = x.upper()`.

---

### 3️⃣ Indexing and Slicing

Every character in a string has a **position number**, called an index, starting from `0`.

```
 String:   P    y    t    h    o    n
 Index:    0    1    2    3    4    5
 Negative: -6  -5   -4   -3   -2   -1
```

**Indexing** — accessing a single character:

```python
lang = "Python"
print(lang[0])     # P  (first character)
print(lang[5])     # n  (last character)
print(lang[-1])    # n  (last character, using negative index)
print(lang[-6])    # P  (first character, from the end)
```

**Slicing** — accessing a range of characters using `string[start:stop:step]`. The `stop` index is **never included**.

```python
lang = "Python"

print(lang[0:3])     # Pyt   (index 0,1,2)
print(lang[2:])      # thon  (from index 2 to end)
print(lang[:4])      # Pyth  (from start to index 3)
print(lang[:])       # Python (entire string, creates a copy)
print(lang[::2])     # Pto   (every 2nd character)
print(lang[::-1])    # nohtyP (reversed string!)
```

| Slice | Meaning | Result |
|---|---|---|
| `s[2:5]` | From index 2 up to (not including) 5 | characters at 2,3,4 |
| `s[:3]` | From beginning to index 3 | first 3 characters |
| `s[3:]` | From index 3 to end | rest of the string |
| `s[::-1]` | Whole string, step -1 | reversed string |

> ⚠️ **Important**
>
> Trying to access an index that doesn't exist, like `lang[10]` on a 6-letter word, will raise an `IndexError`. Slicing, however, never gives an error even if the range is out of bounds — it just returns whatever is available.

🤔 **Quick thinking question:** What does `"Programming"[3:8]` return?
✅ **Answer:** `"gramm"` — characters at index 3, 4, 5, 6, 7 (index 8 is excluded).

---

### 4️⃣ Formatting Strings (f-strings)

Often you need to insert variable values inside a sentence. The modern, cleanest way to do this in Python is using **f-strings** (formatted string literals), introduced in Python 3.6+.

```python
name = "Ananya"
age = 22
city = "Bengaluru"

# f-string way (recommended)
print(f"My name is {name}, I am {age} years old and I live in {city}.")
```

Output:
```
My name is Ananya, I am 22 years old and I live in Bengaluru.
```

You simply put an `f` before the quotes, and wrap variables (or even expressions) inside `{ }`.

```python
price = 499
quantity = 3

print(f"Total bill: ₹{price * quantity}")     # Total bill: ₹1497
print(f"Name in caps: {name.upper()}")         # Name in caps: ANANYA
```

**Controlling decimal places and formatting numbers:**

```python
pi = 3.14159265

print(f"Pi rounded: {pi:.2f}")        # Pi rounded: 3.14
print(f"Percentage: {0.856:.1%}")     # Percentage: 85.6%

amount = 1234567
print(f"{amount:,}")                   # 1,234,567
```

**Older formatting methods (good to recognize in interviews/legacy code):**

```python
# %-formatting (very old style)
print("My name is %s and I am %d years old" % (name, age))

# .format() method
print("My name is {} and I am {} years old".format(name, age))
```

| Method | Style | Recommended? |
|---|---|---|
| f-strings | `f"{name}"` | ✅ Yes — modern, fast, readable |
| `.format()` | `"{}".format(name)` | ⚠️ Older, still used |
| `%` formatting | `"%s" % name` | ❌ Legacy, avoid in new code |

🤔 **Quick thinking question:** How would you print `"Score: 87.5%"` using an f-string, given `score = 0.875`?
✅ **Answer:** `f"Score: {score:.1%}"`

---

## 💡 Real-Life Analogy

Think of a **string as a train made of bogies (compartments)** 🚂. Each bogie holds one character, and every bogie has a seat number (index) painted on it, starting from 0.

* **Indexing** is like asking "who is sitting in bogie number 3?"
* **Slicing** is like saying "show me bogies 2 to 5"
* **String methods** are like train staff who can announce information (`.upper()` = announce loudly), clean the train (`.strip()`), or split the train into separate parts (`.split()`)
* **f-strings** are like a ticket printer that automatically fills in your name, seat number, and destination into a pre-designed ticket template

---

## 💻 Real-World Application

| Industry Use Case | How Strings Are Used |
|---|---|
| 📧 Gmail / Outlook | Validating email format (`.endswith("@gmail.com")`) |
| 🛒 Amazon | Formatting product prices, titles, and search queries |
| 🐦 Twitter/X | Counting characters in a tweet (`len()`) |
| 📰 News websites | Cleaning and formatting scraped article text |
| 🏦 Banking apps | Masking card numbers (`"**** **** **** " + card[-4:]`) |
| 🤖 Chatbots (like Claude, Siri) | Splitting user sentences into words to understand intent |
| 📊 Data Analysts | Cleaning messy Excel/CSV text data using `.strip()`, `.lower()` |

---

## 🔍 Industry Example

**Scenario:** When a new user signs up on **Instagram**, they type their email as `"  John.Smith@GMAIL.com  "` (with accidental spaces and mixed case).

Here's what happens internally, step by step:

1. The raw input is captured as a string: `"  John.Smith@GMAIL.com  "`
2. Instagram's backend calls `.strip()` to remove the accidental leading/trailing spaces
3. `.lower()` is applied so `"John.Smith@GMAIL.com"` and `"john.smith@gmail.com"` are treated as the **same** account (since emails are case-insensitive)
4. `.endswith("@gmail.com")` or similar checks validate the domain
5. `.split("@")` breaks it into `["john.smith", "gmail.com"]` to extract the username part
6. Finally, an f-string is used to generate a welcome message: `f"Welcome, {username}! 🎉"`

This entire pipeline — cleaning, validating, and formatting — happens in a fraction of a second, purely using string operations.

---

## 📊 Diagram

```
                STRING MANIPULATION PIPELINE
                -----------------------------

  Raw Input:  "  John.Smith@GMAIL.com  "
        │
        ▼
   .strip()   ───► removes extra spaces
        │
        ▼
   .lower()   ───► "john.smith@gmail.com"
        │
        ▼
   .split("@") ───► ["john.smith", "gmail.com"]
        │
        ▼
   f-string   ───► "Welcome, john.smith! 🎉"


   INDEXING vs SLICING
   --------------------
   String :   P   y   t   h   o   n
   Index  :   0   1   2   3   4   5

   lang[1]      →  y            (single character)
   lang[1:4]    →  y t h        (range, stop excluded)
   lang[::-1]   →  n o h t y P  (reversed)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "String methods change the original string."
  ✅ **Correct:** Strings are immutable. Methods always return a **new** string; you must reassign it: `x = x.strip()`.

* ❌ **Wrong belief:** "`string[stop]` index is included in slicing."
  ✅ **Correct:** The `stop` index is always **excluded**. `s[0:3]` gives characters at index 0, 1, 2 only.

* ❌ **Wrong belief:** "I can add numbers and strings directly using `+`."
  ✅ **Correct:** You must convert numbers to strings first using `str()`, or use f-strings instead.

* ❌ **Wrong belief:** "Single quotes and double quotes behave differently in Python."
  ✅ **Correct:** They are functionally identical; use double quotes when the string itself contains a single quote (e.g., `"It's fine"`).

* ❌ **Wrong belief:** "Negative indexing is an error."
  ✅ **Correct:** Negative indexing is valid and commonly used to access characters from the end (`-1` = last character).

---

## 💬 Interview Corner

**Q1: Are strings mutable or immutable in Python?**
✅ Immutable. Once created, a string's characters cannot be changed in place. Any "modification" actually creates a brand-new string.

**Q2: What is the difference between `.find()` and `.index()`?**
✅ Both search for a substring. `.find()` returns `-1` if not found, while `.index()` raises a `ValueError` if the substring isn't present.

**Q3: How do you reverse a string in Python?**
✅ Using slicing: `reversed_string = my_string[::-1]`

**Q4: Why are f-strings preferred over `%` formatting or `.format()`?**
✅ f-strings are more readable, faster in execution, and allow direct embedding of expressions inside `{ }`, e.g. `f"{price * qty}"`.

---

## 📝 Quick Summary

* 🧵 A string is a sequence of characters wrapped in quotes
* ➕ `+` joins strings, `*` repeats them
* 🛠️ String methods like `.upper()`, `.strip()`, `.split()` help transform text but never change the original string
* 🔢 Indexing (`s[i]`) accesses a single character; index starts at 0
* ✂️ Slicing (`s[start:stop:step]`) accesses a range; `stop` is always excluded
* ↩️ Negative indexing (`s[-1]`) counts from the end
* 🖨️ f-strings (`f"{variable}"`) are the modern, preferred way to insert values into text
* 📏 `.2f`, `.1%` inside f-strings control decimal/percentage formatting
* 🚫 Strings are immutable — methods return new strings, they don't edit in place

---

## 🎯 Class Activity

**"Build a Mini Profile Card Generator" 🪪**

1. Ask the student to create variables: `name`, `age`, `city`, `email` (with intentional extra spaces and mixed case in the email)
2. Clean the email using `.strip()` and `.lower()`
3. Extract the username from the email using `.split("@")`
4. Print a formatted profile card using an f-string, for example:
   ```
   ╔══════════════════════════╗
     Name: Ananya
     Age: 22
     City: Bengaluru
     Username: ananya.k
   ╚══════════════════════════╝
   ```
5. Bonus: Reverse the name using slicing and print it just for fun!


---

# 📋 Assignments — String Manipulation

| Assignment |
|---|
| Create a variable with your full name (with extra spaces before/after) and clean it using `.strip()`. Print before and after. |
| Take any sentence and count how many times the letter "a" appears using `.count()`. |
| Write a program that takes a user's email and checks whether it ends with `"@gmail.com"` using `.endswith()`. |
| Take a full name string and print the first name and last name separately using `.split()`. |
| Reverse any string of your choice using slicing (`[::-1]`) without using any built-in reverse function. |
| Given the string `"Python Full Stack Course"`, extract only the word `"Full"` using slicing. |
| Write a program using an f-string to print your name, age, and favorite programming language in one sentence. |
| Create a fake "bill receipt" using f-strings that shows item name, quantity, price per item, and total (quantity × price). |
| Take a paragraph of text and convert it fully to uppercase, then fully to lowercase, and count the total characters using `len()`. |
| Write a program to check if a given word is a palindrome (reads the same forward and backward) using slicing. |
| Replace all occurrences of the word "bad" with "good" in a given sentence using `.replace()`. |
| Take a comma-separated string of 5 fruit names and convert it into a list using `.split(",")`, then join it back using `" - "` as separator with `.join()`. |
| Mask a given 16-digit card number so only the last 4 digits are visible (e.g., `**** **** **** 1234`) using slicing and string concatenation. |
| Write a program that asks the user for their name and prints a personalized welcome message using an f-string, with the name in Title Case. |

---

# 📚 Data Structures in Python

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand what a "data structure" is and why we need different types for different situations
* 🎯 Create, Read, Update, Delete (CRUD), and iterate over **Lists**
* 🎯 Understand **Tuples** and why immutability matters
* 🎯 Create, Read, Update, Delete, and iterate over **Dictionaries**, including nested dictionaries
* 🎯 Create, Read, Update, Delete, and iterate over **Sets** and perform set operations
* 🎯 Compare all four data structures and know when to use which one in real projects

---

## 📖 Introduction

Imagine you need to store the marks of 40 students, or the details of one customer (name, email, phone), or a list of unique visitors to a website. A single variable like `x = 5` can only hold **one value**. That's not enough for real-world data. 📦

This is where **Data Structures** come in — they are containers that let you store, organize, and manage **multiple pieces of data together**.

Python gives us four major built-in data structures:

| Data Structure | Ordered? | Changeable? | Allows Duplicates? | Symbol |
|---|---|---|---|---|
| **List** | ✅ Yes | ✅ Yes | ✅ Yes | `[ ]` |
| **Tuple** | ✅ Yes | ❌ No | ✅ Yes | `( )` |
| **Dictionary** | ✅ Yes (insertion order) | ✅ Yes | ❌ No duplicate keys | `{key: value}` |
| **Set** | ❌ No | ✅ Yes (but items must be unique) | ❌ No | `{ }` |

### 🤔 Why does this topic exist?

Real applications don't deal with single numbers — they deal with **collections**: a shopping cart full of products, a contact list full of phone numbers, a database of employee records. Data structures are the foundation of literally every app, website, and AI system you've ever used.

### 🤔 Where is it used?

* 🛒 E-commerce — a shopping cart is a **list** of products
* 📇 Contacts app — each contact is a **dictionary** of name, phone, email
* 🎓 Attendance system — unique roll numbers stored using a **set**
* 📍 GPS coordinates — latitude & longitude stored as a **tuple** (fixed pair, shouldn't change)

> 💡 **Tip**
>
> Think of choosing a data structure like choosing the right container in your kitchen — you wouldn't store soup in a paper bag (list) or store rice in an open bowl outdoors (set with no order)! Choosing the right structure makes your code efficient and bug-free.

---

## 🧠 Detailed Notes

### 1️⃣ Lists and Their Methods

A **List** is an ordered, changeable collection that allows duplicate values. It is written using square brackets `[ ]`.

```python
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits)          # ['apple', 'banana', 'cherry', 'banana']
print(type(fruits))    # <class 'list'>
```

#### 🟢 CREATE (making a list)

```python
empty_list = []
numbers = [10, 20, 30]
mixed = ["Priya", 25, True, 5.5]      # lists can hold different data types
```

#### 🔵 READ (accessing list items)

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])       # apple  (first item)
print(fruits[-1])      # cherry (last item)
print(fruits[0:2])     # ['apple', 'banana']  (slicing works on lists too!)
print(len(fruits))     # 3
```

#### 🟡 UPDATE (changing list items)

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"          # replace a single item
print(fruits)                 # ['apple', 'mango', 'cherry']

fruits.append("orange")       # add item at the end
print(fruits)                 # ['apple', 'mango', 'cherry', 'orange']

fruits.insert(1, "grapes")    # insert at a specific index
print(fruits)                 # ['apple', 'grapes', 'mango', 'cherry', 'orange']

fruits.extend(["kiwi", "fig"])  # add multiple items at once
print(fruits)
```

#### 🔴 DELETE (removing list items)

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")     # removes the FIRST matching value
print(fruits)                # ['apple', 'cherry', 'banana']

popped = fruits.pop()        # removes and returns the LAST item
print(popped, fruits)        # banana ['apple', 'cherry']

del fruits[0]                 # removes item at a specific index
print(fruits)                 # ['cherry']

fruits.clear()                 # empties the entire list
print(fruits)                  # []
```

#### 🔁 ITERATE (looping through a list)

```python
fruits = ["apple", "banana", "cherry"]

# Simple loop
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

**Common list methods:**

| Method | Purpose |
|---|---|
| `.append(x)` | Add item at the end |
| `.insert(i, x)` | Add item at index `i` |
| `.remove(x)` | Remove first occurrence of value `x` |
| `.pop(i)` | Remove and return item at index `i` (default: last) |
| `.sort()` | Sort the list in place |
| `.reverse()` | Reverse the list in place |
| `.count(x)` | Count occurrences of `x` |
| `.index(x)` | Find the index of the first occurrence of `x` |
| `.copy()` | Create a shallow copy of the list |

```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)          # [1, 2, 5, 8, 9]

numbers.reverse()
print(numbers)          # [9, 8, 5, 2, 1]
```

🤔 **Quick thinking question:** What is the difference between `.remove()` and `.pop()`?
✅ **Answer:** `.remove(value)` deletes based on the **value** you provide, while `.pop(index)` deletes based on **position** and also returns the removed item.

> ⚠️ **Important**
>
> Lists are **mutable** — you can change them after creation, unlike strings and tuples.

---

### 2️⃣ Tuples and Immutability

A **Tuple** looks similar to a list but is written with round brackets `( )` and, most importantly, is **immutable** — once created, it cannot be changed.

```python
coordinates = (28.6139, 77.2090)   # latitude, longitude of Delhi
print(coordinates)
print(type(coordinates))            # <class 'tuple'>
```

#### 🟢 CREATE (making a tuple)

```python
empty_tuple = ()
single_item_tuple = (5,)     # ⚠️ comma is required, else it's just treated as int
colors = ("red", "green", "blue")
```

#### 🔵 READ (accessing tuple items)

```python
colors = ("red", "green", "blue")

print(colors[0])        # red
print(colors[-1])       # blue
print(colors[0:2])      # ('red', 'green')

for color in colors:    # ITERATE — works just like lists
    print(color)
```

#### 🟡 UPDATE — ❌ Not Directly Possible!

```python
colors = ("red", "green", "blue")

# colors[0] = "purple"   ❌ This will raise: TypeError: 'tuple' object does not support item assignment
```

If you truly need to "update" a tuple, the workaround is to **convert it to a list, modify it, and convert it back**:

```python
colors = ("red", "green", "blue")

colors_list = list(colors)     # convert tuple → list
colors_list[0] = "purple"       # now it's editable
colors = tuple(colors_list)     # convert back list → tuple

print(colors)   # ('purple', 'green', 'blue')
```

#### 🔴 DELETE — Item-level deletion ❌ Not Possible

```python
colors = ("red", "green", "blue")

# del colors[0]   ❌ TypeError

del colors        # ✅ This works — deletes the ENTIRE tuple, not a single item
```

> 💡 **Tip**
>
> You cannot delete a single element from a tuple. You can only delete the whole tuple variable itself using `del`.

**Why does immutability even matter?**

* 🔒 It protects important, fixed data (like GPS coordinates, RGB color codes, days of the week) from accidental changes
* ⚡ Tuples are slightly faster and use less memory than lists
* 🔑 Tuples can be used as dictionary keys (lists cannot, because keys must be unchangeable)

🤔 **Quick thinking question:** Why would a developer choose a tuple over a list for storing a birthdate `(2000, 5, 14)`?
✅ **Answer:** Because a birthdate should never accidentally change once recorded — immutability protects it from being modified by mistake anywhere in the code.

---

### 3️⃣ Dictionaries: Key-Value Pairs, Methods, Nested Dicts

A **Dictionary** stores data as **key-value pairs**, like a real-world dictionary where a "word" (key) maps to its "meaning" (value). Written using curly braces `{ }`.

```python
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python Full Stack"
}
print(student)
print(type(student))   # <class 'dict'>
```

#### 🟢 CREATE (making a dictionary)

```python
empty_dict = {}
person = {"name": "Ananya", "city": "Bengaluru"}
using_dict_function = dict(name="Kabir", age=30)
```

#### 🔵 READ (accessing values)

```python
student = {"name": "Rahul", "age": 21, "course": "Python Full Stack"}

print(student["name"])            # Rahul
print(student.get("age"))          # 21
print(student.get("grade", "N/A")) # N/A  (default value if key doesn't exist — avoids errors!)

print(student.keys())     # dict_keys(['name', 'age', 'course'])
print(student.values())   # dict_values(['Rahul', 21, 'Python Full Stack'])
print(student.items())    # dict_items([('name','Rahul'), ('age',21), ('course','Python Full Stack')])
```

#### 🟡 UPDATE (changing / adding values)

```python
student = {"name": "Rahul", "age": 21}

student["age"] = 22                  # update existing key
student["course"] = "Python"         # add new key-value pair
print(student)                        # {'name': 'Rahul', 'age': 22, 'course': 'Python'}

student.update({"city": "Pune", "age": 23})   # update multiple keys at once
print(student)
```

#### 🔴 DELETE (removing values)

```python
student = {"name": "Rahul", "age": 22, "course": "Python", "city": "Pune"}

del student["city"]              # delete a specific key
print(student)

removed_value = student.pop("age")   # remove and return the value
print(removed_value, student)

student.clear()                   # remove everything
print(student)                     # {}
```

#### 🔁 ITERATE (looping through a dictionary)

```python
student = {"name": "Rahul", "age": 22, "course": "Python"}

for key in student:                      # loops through keys by default
    print(key)

for key, value in student.items():        # loops through key-value pairs
    print(f"{key} -> {value}")
```

#### 🪆 Nested Dictionaries

A dictionary can contain **another dictionary** as a value — very useful for representing complex, real-world records like a database row.

```python
students = {
    "student1": {"name": "Rahul", "age": 21, "marks": [85, 90, 78]},
    "student2": {"name": "Ananya", "age": 22, "marks": [92, 88, 95]}
}

print(students["student1"]["name"])          # Rahul
print(students["student2"]["marks"][0])        # 92

# Iterating through a nested dictionary
for student_id, details in students.items():
    print(f"{student_id}: {details['name']}, Age: {details['age']}")
```

**Common dictionary methods:**

| Method | Purpose |
|---|---|
| `.get(key, default)` | Safely fetch a value without crashing if key is missing |
| `.keys()` | Get all keys |
| `.values()` | Get all values |
| `.items()` | Get all key-value pairs |
| `.update(dict2)` | Merge/update with another dictionary |
| `.pop(key)` | Remove a key and return its value |
| `.setdefault(key, default)` | Get a key's value, or set it if it doesn't exist |

🤔 **Quick thinking question:** Why is `.get()` safer than using `student["grade"]` directly?
✅ **Answer:** If `"grade"` doesn't exist as a key, `student["grade"]` throws a `KeyError` and crashes the program, while `.get("grade")` simply returns `None` (or a default value you specify) without crashing.

> ⚠️ **Important**
>
> Dictionary **keys** must be unique and immutable (strings, numbers, or tuples). Dictionary **values** can be anything — including lists, other dictionaries, or even functions.

---

### 4️⃣ Sets and Set Operations

A **Set** is an unordered collection that automatically removes duplicate values. Written using curly braces `{ }` (like dictionaries, but without key-value pairs).

```python
numbers = {1, 2, 3, 3, 2, 1}
print(numbers)          # {1, 2, 3}   — duplicates automatically removed!
print(type(numbers))    # <class 'set'>
```

#### 🟢 CREATE (making a set)

```python
empty_set = set()          # ⚠️ NOT {} — that creates an empty dictionary!
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3, 3, 3])   # converting a list to a set removes duplicates
print(from_list)            # {1, 2, 3}
```

#### 🔵 READ (checking membership — sets don't support indexing!)

```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)         # True
print("mango" in fruits)         # False
print(len(fruits))                # 3

# fruits[0]   ❌ TypeError — sets are unordered, so NO indexing allowed
```

#### 🟡 UPDATE (adding items)

```python
fruits = {"apple", "banana"}

fruits.add("cherry")               # add a single item
print(fruits)

fruits.update(["mango", "grapes"])  # add multiple items
print(fruits)
```

#### 🔴 DELETE (removing items)

```python
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")     # removes item; raises error if not found
print(fruits)

fruits.discard("mango")      # removes item; NO error even if not found (safer)
print(fruits)

popped = fruits.pop()         # removes a RANDOM item (sets are unordered!)
print(popped, fruits)

fruits.clear()                 # empties the set
print(fruits)                  # set()
```

#### 🔁 ITERATE (looping through a set)

```python
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)   # order is NOT guaranteed!
```

**Set Operations (this is where sets truly shine — mathematical set theory!):**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))             # {1,2,3,4,5,6}  — all elements from both
print(a.intersection(b))       # {3, 4}         — common elements only
print(a.difference(b))         # {1, 2}         — in a but NOT in b
print(a.symmetric_difference(b))  # {1,2,5,6}   — everything EXCEPT common elements

print(a.issubset(b))            # False — is 'a' entirely inside 'b'?
print(a.issuperset({1,2}))      # True — does 'a' contain all of {1,2}?
```

| Operation | Symbol | Method | Meaning |
|---|---|---|---|
| Union | `\|` | `.union()` | Combine both sets, no duplicates |
| Intersection | `&` | `.intersection()` | Common elements only |
| Difference | `-` | `.difference()` | Elements in first set but not second |
| Symmetric Difference | `^` | `.symmetric_difference()` | Elements in either, but not both |

🤔 **Quick thinking question:** Why would you use a set instead of a list to store the roll numbers of students who attended a college event?
✅ **Answer:** Because a set automatically prevents duplicate entries — even if a roll number gets scanned twice at the entry gate, the set will only keep one copy of it.

> ⚠️ **Important**
>
> Sets are unordered — you can never rely on the position of an item in a set, and `.pop()` removes a **random** element, not a specific one.

---

### 5️⃣ Methods and Their Use Cases (Choosing the Right Data Structure)

Now that we've seen all four, here's a practical decision guide:

| Situation | Best Data Structure | Why |
|---|---|---|
| Shopping cart items (order matters, can add/remove) | **List** | Ordered, changeable, allows duplicates (2x same item) |
| Latitude-longitude of a location | **Tuple** | Fixed pair of values that should never change |
| Storing a user's profile (name, email, age) | **Dictionary** | Labeled data accessed by meaningful keys |
| Removing duplicate email addresses from a marketing list | **Set** | Automatically eliminates duplicates |
| Days of the week (fixed, constant list) | **Tuple** | Should not be accidentally modified |
| Storing multiple student records with nested details | **Nested Dictionary** | Represents structured, labeled, hierarchical data |
| Checking if a username already exists quickly | **Set** | Very fast membership checking (`in`) |

```python
# Real combined example
cart = ["Laptop", "Mouse", "Laptop"]              # List: order + duplicates matter
location = (28.6139, 77.2090)                       # Tuple: fixed coordinate pair
user = {"name": "Dev", "email": "dev@mail.com"}     # Dictionary: labeled profile data
visited_pages = {"home", "cart", "home", "profile"}  # Set: unique pages only

print(cart)             # ['Laptop', 'Mouse', 'Laptop']
print(location)         # (28.6139, 77.209)
print(user)             # {'name': 'Dev', 'email': 'dev@mail.com'}
print(visited_pages)    # {'home', 'cart', 'profile'}  (duplicate 'home' removed)
```

🤔 **Quick thinking question:** You're building a system to store exam seat numbers where each seat number must be unique and order doesn't matter. Which data structure fits best?
✅ **Answer:** A **Set** — because it automatically enforces uniqueness and we don't care about order.


## 💡 Real-Life Analogy

* 📝 **List → A Shopping List on Paper** — You can add items, cross out items, rearrange the order, and even write the same item twice ("milk" appearing twice by mistake is fine).
* 🔒 **Tuple → Your Date of Birth on a Government ID** — It's fixed. Once printed, it shouldn't be — and can't be — casually changed.
* 📇 **Dictionary → A Real Physical Dictionary / Phonebook** — You look up a "word" (key) to get its "meaning" (value). You don't search page-by-page; you go directly to the word.
* 🎟️ **Set → Entry Wristbands at a Concert** — Every wristband is unique; the system won't let two people use the exact same wristband ID, and the order in which people entered doesn't matter for the guest list.

---

## 💻 Real-World Application

| Data Structure | Real Company / Product Usage |
|---|---|
| **List** | Instagram — the list of photos in your feed (ordered, can have similar posts) |
| **List** | Amazon — items in your shopping cart |
| **Tuple** | Google Maps — storing fixed (latitude, longitude) coordinate pairs |
| **Tuple** | Banking systems — storing (account_number, IFSC_code) as an unchangeable pair |
| **Dictionary** | LinkedIn — a user profile object: `{name, headline, company, location}` |
| **Dictionary** | Any REST API (like weather apps) — JSON responses are essentially Python dictionaries |
| **Set** | Spotify — ensuring no duplicate songs in a "Liked Songs" collection |
| **Set** | Cybersecurity systems — storing a set of blocked IP addresses for fast lookup |

---

## 🔍 Industry Example

**Scenario:** A **Backend Developer at Swiggy** (a food delivery app) is building the "Add to Cart" and "Nearby Restaurants" features.

1. When you add food items to your cart, Swiggy stores them in a **List** — because order matters (items shown in the order you added them) and you might add "2 Butter Naan" twice, which should count as 2 separate additions.
2. Each restaurant's exact location is stored as a **Tuple**: `(latitude, longitude)` — because this shouldn't accidentally change once the restaurant is registered.
3. Your delivery address details are stored as a **Dictionary**: `{"house_no": "12A", "area": "Koramangala", "city": "Bengaluru", "pincode": "560034"}` — because each piece of data has a clear label.
4. When Swiggy wants to know all the **unique cuisines** available in your area (to show filter options like "Chinese", "Italian", "South Indian"), it collects them into a **Set** — automatically removing duplicate cuisine names even if 50 restaurants serve "Chinese" food.
5. Finally, all of this combines into a **nested dictionary** structure like:

```python
order = {
    "user": {"name": "Aditi", "address": {"area": "Koramangala", "city": "Bengaluru"}},
    "items": ["Butter Naan", "Paneer Tikka", "Butter Naan"],
    "restaurant_location": (12.9352, 77.6146),
    "available_cuisines": {"Chinese", "Italian", "South Indian"}
}
```

This single example uses **all four data structures together** — exactly how it happens in real production code!

---

## 📊 Diagram

```
                    PYTHON DATA STRUCTURES OVERVIEW
                    --------------------------------

  LIST  [ ]                  TUPLE  ( )
  ┌───┬───┬───┬───┐          ┌───┬───┬───┐
  │ A │ B │ C │ B │  ✅edit   │ X │ Y │ Z │  🔒locked
  └───┴───┴───┴───┘          └───┴───┴───┘
  ordered, duplicates OK      ordered, IMMUTABLE


  DICTIONARY  {key: value}         SET  { }
  ┌─────────────────────┐          ┌───────────────┐
  │ "name"  → "Rahul"    │          │  🔵 🔴 🟢      │
  │ "age"   → 21         │          │  (no order,    │
  │ "course"→ "Python"   │          │   no dupes)    │
  └─────────────────────┘          └───────────────┘
  key → value pairs                unique items only


        CRUD FLOW APPLICABLE TO EACH STRUCTURE
        ---------------------------------------
        CREATE  →  READ  →  UPDATE  →  DELETE  →  ITERATE
           │         │         │          │           │
        list=[]   list[0]  list[0]=x   list.pop()   for x in list
        {}        d["k"]   d["k"]=x    del d["k"]   for k,v in d.items()
        set()     "x" in s s.add(x)    s.remove(x)  for x in s
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Lists, tuples, and sets are basically the same thing."
  ✅ **Correct:** Lists are ordered & mutable, tuples are ordered & immutable, sets are unordered & only store unique items. Each has a distinct purpose.

* ❌ **Wrong belief:** "`{}` creates an empty set."
  ✅ **Correct:** `{}` creates an **empty dictionary**. To create an empty set, you must use `set()`.

* ❌ **Wrong belief:** "You can access set items using an index like `my_set[0]`."
  ✅ **Correct:** Sets are unordered, so indexing is **not allowed**. Use membership checks (`in`) instead.

* ❌ **Wrong belief:** "Dictionary keys can be duplicated."
  ✅ **Correct:** If you assign the same key twice, the second value simply **overwrites** the first — there's no error, but also no duplicate.

* ❌ **Wrong belief:** "Tuples can never be modified in any way."
  ✅ **Correct:** You cannot modify individual elements directly, but you *can* convert a tuple to a list, modify it, then convert it back to a tuple.

* ❌ **Wrong belief:** "`.remove()` and `.discard()` on a set behave identically."
  ✅ **Correct:** `.remove()` raises an error if the item doesn't exist; `.discard()` silently does nothing if the item isn't found.

---

## 💬 Interview Corner

**Q1: What is the key difference between a list and a tuple?**
✅ Lists are mutable (changeable) and slightly slower; tuples are immutable (fixed) and slightly faster and more memory-efficient. Tuples are used for data that shouldn't change.

**Q2: Why can't a list be used as a dictionary key, but a tuple can?**
✅ Dictionary keys must be immutable/hashable. Lists can change after creation (not hashable), while tuples cannot change, so they're allowed as keys.

**Q3: How does a set ensure there are no duplicate values?**
✅ Internally, a set uses a hashing mechanism — when you try to add an item that already has the same hash/value present, it's simply ignored, keeping only one copy.

**Q4: What is a nested dictionary and when would you use one?**
✅ A dictionary where a value itself is another dictionary. It's used to represent structured, hierarchical data — like a student record containing an address which itself has multiple fields (street, city, pincode).

---

## 📝 Quick Summary

* 📝 **List** `[ ]` — ordered, mutable, allows duplicates — use `.append()`, `.remove()`, `.pop()`, `.sort()`
* 🔒 **Tuple** `( )` — ordered, immutable — great for fixed data like coordinates or dates
* 📇 **Dictionary** `{key: value}` — stores labeled data as key-value pairs; supports nesting for complex records
* 🎟️ **Set** `{ }` — unordered, no duplicates allowed; perfect for uniqueness checks and set math (union, intersection)
* 🔁 All four structures support **iteration** using `for` loops
* ✏️ CRUD operations (Create, Read, Update, Delete) apply differently to each — tuples restrict Update/Delete at the item level
* 🧮 Sets support powerful operations: `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`
* 🪆 Nested dictionaries let you model real-world, structured data like database records or API responses
* 🎯 Choosing the right data structure is a core software engineering skill — it affects performance and code clarity

---

## 🎯 Class Activity

**"Build a Mini Student Record System" 🎓**

1. Create a **list** called `subjects` with 5 subject names; add one more subject using `.append()`, then remove one using `.remove()`.
2. Create a **tuple** called `dob` storing a birthdate as `(year, month, day)`. Try to change one value directly and observe the error — then show the correct workaround using list conversion.
3. Create a **dictionary** called `student` with keys: `name`, `age`, `subjects` (use the list from step 1), and a nested dictionary `address` with `city` and `pincode`.
4. Create a **set** called `unique_grades` by adding grades like `"A", "B", "A", "C", "B"` and observe how duplicates disappear.
5. Write a loop to iterate through the `student` dictionary and print every key and value, including the nested address details.
6. Bonus: Use set operations to find common subjects between your list and a friend's list (converted to sets).

---

# 📋 Assignments — Data Structures in Python

| Assignment |
|---|
| Create a list of 6 of your favorite movies. Add a new movie, update one movie name, remove one movie, and print the final list. |
| Write a program to sort a list of numbers in ascending and then descending order using `.sort()` and `.reverse()`. |
| Create a tuple of 5 Indian states. Try to change one value and note the error message. Then show the correct way to "update" it using list conversion. |
| Write a program that stores your weekly class timetable as a tuple of tuples: `(("Monday","Python"), ("Tuesday","DSA"), ...)` and iterate through it to print each day and subject. |
| Create a dictionary representing your own profile: name, age, city, and hobbies (as a list). Print each key-value pair using `.items()`. |
| Create a nested dictionary storing details of 3 employees, each having name, department, and salary. Print the department of the 2nd employee. |
| Write a program using `.get()` to safely check for a key that may not exist in a dictionary, and print a default message if it's missing. |
| Create a set of 10 numbers where at least 4 are duplicates. Print the set and explain in a comment why the duplicates disappeared. |
| Take two sets of your 5 favorite fruits and your friend's 5 favorite fruits (with some overlap). Find their union, intersection, and difference. |
| Write a program to remove duplicate values from a list of email addresses using a set, and print the cleaned list. |
| Build a "Library Catalog" using a list of dictionaries, where each dictionary has `title`, `author`, and `available` (True/False). Iterate and print only the available books. |
| Create an empty dictionary and, using a loop, add 5 key-value pairs where the key is a roll number and the value is a student name. |
| Write a program to check whether a given tuple of coordinates exists as a key in a dictionary of `{coordinates: place_name}`. |
| Combine all 4 data structures in one program: create a shopping list (list), a fixed store location (tuple), a customer profile (dictionary), and a set of unique product categories — then print all of them neatly using f-strings. |
| Write a program to count how many times each word appears in a sentence using a dictionary (word frequency counter). |
