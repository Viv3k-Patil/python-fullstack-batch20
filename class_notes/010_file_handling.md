# 📚 File Handling, Regular Expressions & Python Memory Management

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Read and write both text and JSON files in Python
* 🎯 Understand and correctly use different file modes (`r`, `w`, `a`, `rb`, `wb`)
* 🎯 Safely handle exceptions that occur during file operations
* 🎯 Understand what regular expressions (regex) are and why they're useful
* 🎯 Use Python's `re` module to search, match, and extract patterns in text
* 🎯 Apply regex to real validation tasks: names, phone numbers, emails, and PAN numbers
* 🎯 Understand the basics of how Python manages memory using reference counting and garbage collection

---

## 📖 Introduction

Today we cover three practical, "behind-the-scenes" skills every developer needs:

* 📁 **File Handling** — reading and writing data to actual files on disk, so your program's data doesn't disappear when it closes
* 🔍 **Regular Expressions (Regex)** — a powerful mini-language for finding, matching, and validating patterns in text
* 🧠 **Memory Management** — understanding how Python quietly manages memory behind the scenes, so your programs run efficiently

### 🤔 Why does this topic exist?

* 💾 Every real application needs to permanently save data — user profiles, settings, logs, reports — and that means writing to files
* ✅ Validating user input (emails, phone numbers, PAN cards) is something almost every form-based application needs, and regex is the standard tool for this
* 🧠 Understanding memory management helps you write more efficient code and debug tricky memory-related bugs later in your career

### 🤔 Where is it used?

* 📄 Any app that "saves" or "loads" data — text editors, games (save files), configuration files
* 🌐 APIs — almost all modern web APIs send and receive data in JSON format
* 📝 Form validation — signup forms checking your email/phone format before submitting
* 🧾 Government/finance apps — validating PAN numbers, Aadhaar formats, GST numbers using regex patterns
* 🐍 Every single Python program ever run — memory management happens automatically, whether you notice it or not!

> 💡 **Tip**
>
> These three topics might feel unrelated at first, but they're all "practical engineering" skills — the kind of things that separate someone who can write basic scripts from someone who can build real, production-ready software.

---

## 🧠 Detailed Notes

### 1️⃣ Reading and Writing Files (Text, JSON)

**Writing to a text file:**

```python
file = open("notes.txt", "w")     # "w" = write mode
file.write("Hello, this is my first line.\n")
file.write("This is the second line.\n")
file.close()                        # ALWAYS close the file when done!
```

**Reading from a text file:**

```python
file = open("notes.txt", "r")      # "r" = read mode
content = file.read()
print(content)
file.close()
```

**The recommended way — using `with` (automatically closes the file for you):**

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# file is AUTOMATICALLY closed here, even if an error occurs inside the 'with' block!
```

**Different ways to read a file:**

```python
with open("notes.txt", "r") as file:
    print(file.read())          # reads the ENTIRE file as one string

with open("notes.txt", "r") as file:
    print(file.readline())       # reads just ONE line

with open("notes.txt", "r") as file:
    print(file.readlines())       # reads ALL lines into a LIST of strings

with open("notes.txt", "r") as file:
    for line in file:               # loop through the file line by line (memory-efficient!)
        print(line.strip())          # .strip() removes the trailing newline character
```

**Working with JSON files** — JSON (JavaScript Object Notation) is the most common format for structured data, and Python's built-in `json` module makes it easy to work with:

```python
import json

# Writing a Python dictionary to a JSON file
student = {"name": "Priya", "age": 21, "course": "Python Full Stack"}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)     # indent=4 makes it nicely formatted/readable
```

This creates `student.json` with content:
```json
{
    "name": "Priya",
    "age": 21,
    "course": "Python Full Stack"
}
```

```python
import json

# Reading a JSON file back into a Python dictionary
with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])       # Priya
print(type(data))          # <class 'dict'>
```

**Converting between JSON strings and Python objects (without files):**

```python
import json

student = {"name": "Rahul", "age": 22}

json_string = json.dumps(student)      # Python dict → JSON string
print(json_string)                       # '{"name": "Rahul", "age": 22}'

python_dict = json.loads(json_string)   # JSON string → Python dict
print(python_dict["name"])                # Rahul
```

| Function | Purpose |
|---|---|
| `json.dump(obj, file)` | Write a Python object AS JSON, directly to a file |
| `json.load(file)` | Read JSON FROM a file, into a Python object |
| `json.dumps(obj)` | Convert a Python object INTO a JSON string (no file) |
| `json.loads(string)` | Convert a JSON string INTO a Python object (no file) |

> 💡 **Tip**
>
> Remember the naming pattern: functions with an **"s"** (`dumps`, `loads`) work with **s**trings; functions without it (`dump`, `load`) work directly with **file** objects.

🤔 **Quick thinking question:** Why is `with open(...) as file:` generally preferred over manually calling `open()` and `file.close()`?
✅ **Answer:** The `with` statement automatically closes the file for you, even if an error/exception occurs while working with it — manually calling `.close()` risks the file staying open if an error happens before reaching that line.

---

### 2️⃣ Working with Different File Modes (r, w, a, rb, wb)

The second argument to `open()` tells Python HOW you intend to use the file:

| Mode | Meaning | Behavior |
|---|---|---|
| `"r"` | Read (default) | File must already exist; error if it doesn't |
| `"w"` | Write | Creates a new file, OR **completely overwrites** an existing one |
| `"a"` | Append | Adds new content to the END of the file, without erasing existing content |
| `"rb"` | Read binary | For reading non-text files, like images or PDFs |
| `"wb"` | Write binary | For writing non-text files, like images or PDFs |
| `"r+"` | Read AND write | File must exist; allows both reading and writing |

```python
# "w" mode — OVERWRITES the entire file every time!
with open("log.txt", "w") as file:
    file.write("First run\n")

with open("log.txt", "w") as file:      # this ERASES "First run" completely!
    file.write("Second run\n")

# result: log.txt only contains "Second run"
```

```python
# "a" mode — ADDS to the file without erasing previous content
with open("log.txt", "a") as file:
    file.write("First run\n")

with open("log.txt", "a") as file:
    file.write("Second run\n")

# result: log.txt contains BOTH "First run" AND "Second run"
```

**Working with binary files (e.g., copying an image):**

```python
with open("photo.jpg", "rb") as source_file:      # "rb" = read binary
    data = source_file.read()

with open("photo_copy.jpg", "wb") as dest_file:     # "wb" = write binary
    dest_file.write(data)
```

```
                 FILE MODE COMPARISON
                 ------------------------
   "w" mode:  [old content] ──► ❌ ERASED ──► [new content only]

   "a" mode:  [old content] ──► [old content][new content]  ✅ preserved + added
```

> ⚠️ **Important**
>
> The most common beginner mistake is using `"w"` mode when you actually meant `"a"` — accidentally wiping out important existing data. Always double-check which mode you actually need!

🤔 **Quick thinking question:** If you run a program using `"w"` mode to write a log entry every time it starts, what will happen to your log file over multiple program runs?
✅ **Answer:** Each run will COMPLETELY ERASE the previous log content, since `"w"` mode overwrites the file from scratch every time — you'd only ever see the log from the MOST RECENT run, not a full history. You'd need `"a"` (append) mode to preserve history across runs.

---

### 3️⃣ Exception Handling in File Operations

File operations are especially prone to errors — the file might not exist, you might not have permission to access it, or the disk might be full. Always wrap file operations in proper exception handling.

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ Error: The file 'data.txt' does not exist.")
except PermissionError:
    print("❌ Error: You don't have permission to access this file.")
else:
    print("✅ File read successfully!")
finally:
    print("🔚 File operation attempt finished.")
```

**A practical, safe file-writing function:**

```python
def save_data_safely(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
    except PermissionError:
        print(f"❌ Cannot write to '{filename}' — permission denied.")
        return False
    except OSError as e:                    # catches other OS-level file errors (disk full, invalid path, etc.)
        print(f"❌ An OS error occurred: {e}")
        return False
    else:
        print(f"✅ Data saved successfully to '{filename}'.")
        return True

save_data_safely("report.txt", "Sales increased by 15% this quarter.")
```

**Safe JSON reading with corrupted/invalid file handling:**

```python
import json

def load_json_safely(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ '{filename}' not found. Returning empty data.")
        return {}
    except json.JSONDecodeError:                # raised if the file contains INVALID JSON
        print(f"❌ '{filename}' contains invalid JSON. Returning empty data.")
        return {}

data = load_json_safely("student.json")
print(data)
```

> 💡 **Tip**
>
> Since `with open(...)` already handles closing the file automatically, your `try/except` around it only needs to worry about catching errors related to OPENING, READING, or WRITING — not about remembering to close it.

🤔 **Quick thinking question:** Why is it especially important to handle exceptions around file operations, compared to, say, simple arithmetic operations?
✅ **Answer:** File operations depend on factors OUTSIDE your program's control — whether the file exists, whether you have permission, whether the disk has space — making them far more likely to fail unpredictably at runtime than something like basic arithmetic, which only depends on the values you provide.

---

### 4️⃣ Understanding Regular Expressions (Regex)

A **regular expression** (regex) is a special text pattern used to search, match, or validate strings against a set of rules. Instead of writing complicated manual character-by-character checks, regex lets you describe a PATTERN once.

**Why not just use `.startswith()`, `.endswith()`, `in`, etc.?** Those work for simple, exact checks — but regex handles much more COMPLEX patterns, like "a valid email format" or "exactly 10 digits," in a single, compact expression.

**Basic regex symbols:**

| Symbol | Meaning | Example | Matches |
|---|---|---|---|
| `.` | Any single character | `a.c` | "abc", "axc", "a1c" |
| `\d` | Any digit (0-9) | `\d\d\d` | "123", "456" |
| `\w` | Any word character (letters, digits, underscore) | `\w+` | "hello", "abc_123" |
| `\s` | Any whitespace character | `a\sb` | "a b" |
| `*` | Zero or more of the previous | `ab*` | "a", "ab", "abbb" |
| `+` | One or more of the previous | `ab+` | "ab", "abbb" (NOT "a") |
| `?` | Zero or one of the previous (optional) | `colou?r` | "color", "colour" |
| `{n}` | Exactly n repetitions | `\d{3}` | exactly 3 digits |
| `{n,m}` | Between n and m repetitions | `\d{2,4}` | 2 to 4 digits |
| `^` | Start of string | `^Hello` | must START with "Hello" |
| `$` | End of string | `bye$` | must END with "bye" |
| `[]` | A set of allowed characters | `[aeiou]` | any single vowel |
| `\|` | OR (alternatives) | `cat\|dog` | "cat" or "dog" |

```
      HOW TO READ A REGEX PATTERN
      ------------------------------
      ^   [A-Za-z]+   \s   \d{3}   $
      │       │         │      │      │
      │       │         │      │      └── must END here
      │       │         │      └── exactly 3 digits
      │       │         └── a single whitespace
      │       └── one or more letters (name)
      └── must START here

      Example match: "John 123"
```

> 💡 **Tip**
>
> Regex looks intimidating at first — but you don't need to memorize every symbol. Most developers look up or reuse common patterns (like email validation) rather than writing complex regex from scratch every time.

🤔 **Quick thinking question:** What is the difference between `\d*` and `\d+` in a regex pattern?
✅ **Answer:** `\d*` matches ZERO or more digits (so it would even match an empty string with no digits at all), while `\d+` requires AT LEAST ONE digit to match successfully.

---

### 5️⃣ Using the `re` Module in Python

Python's built-in `re` module lets you actually USE regex patterns in your code.

```python
import re

text = "My phone number is 9876543210"

# re.search() — finds the FIRST match anywhere in the string
match = re.search(r"\d{10}", text)
if match:
    print("Found:", match.group())    # Found: 9876543210
```

**Key `re` module functions:**

| Function | Purpose |
|---|---|
| `re.match(pattern, string)` | Checks for a match ONLY at the very BEGINNING of the string |
| `re.search(pattern, string)` | Finds the FIRST match ANYWHERE in the string |
| `re.findall(pattern, string)` | Returns a LIST of ALL matches found in the string |
| `re.sub(pattern, replacement, string)` | Replaces all matches with a new string |
| `re.split(pattern, string)` | Splits a string wherever the pattern matches |

```python
import re

text = "Contact us at priya@email.com or rahul@email.com for support."

# findall() — get ALL matching emails
emails = re.findall(r"\w+@\w+\.\w+", text)
print(emails)     # ['priya@email.com', 'rahul@email.com']

# sub() — replace all phone numbers with "[HIDDEN]"
text2 = "Call 9876543210 or 9123456789"
masked = re.sub(r"\d{10}", "[HIDDEN]", text2)
print(masked)      # Call [HIDDEN] or [HIDDEN]

# split() — split a string using multiple possible delimiters
data = "apple, banana; cherry mango"
fruits = re.split(r"[,;\s]+", data)
print(fruits)        # ['apple', 'banana', 'cherry', 'mango']
```

**Using "raw strings" (the `r` prefix) — always recommended for regex patterns:**

```python
# WITHOUT raw string — Python might misinterpret backslashes
pattern1 = "\d+"      # risky — \d isn't a recognized Python escape sequence

# WITH raw string — Python passes backslashes through EXACTLY as written
pattern2 = r"\d+"      # correct, recommended way
```

> ⚠️ **Important**
>
> ALWAYS prefix your regex patterns with `r` (e.g., `r"\d{10}"`) to create a "raw string" — this prevents Python from trying to interpret backslashes as its OWN special escape characters before regex even sees them.

🤔 **Quick thinking question:** What is the key difference between `re.match()` and `re.search()`?
✅ **Answer:** `re.match()` only checks for a match at the very BEGINNING of the string, while `re.search()` looks for a match ANYWHERE within the string — `re.search()` would still find a match even if the pattern appears in the middle or end.

---

### 6️⃣ Practical Regex Applications: Name, Phone, Email, PAN Validation

**Name validation** (only letters and spaces, no numbers/symbols):

```python
import re

def is_valid_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return bool(re.match(pattern, name))

print(is_valid_name("Priya Sharma"))    # True
print(is_valid_name("Priya123"))          # False
print(is_valid_name("Rahul_Kumar"))        # False (underscore not allowed here)
```

**Phone number validation** (Indian 10-digit mobile numbers, optionally starting with +91):

```python
import re

def is_valid_phone(phone):
    pattern = r"^(\+91)?[6-9]\d{9}$"      # optional +91, then a digit 6-9, then 9 more digits
    return bool(re.match(pattern, phone))

print(is_valid_phone("9876543210"))      # True
print(is_valid_phone("+919876543210"))    # True
print(is_valid_phone("1234567890"))        # False (Indian mobile numbers start with 6-9)
print(is_valid_phone("98765"))              # False (too short)
```

**Email validation:**

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

print(is_valid_email("priya.sharma@gmail.com"))    # True
print(is_valid_email("invalid-email"))                # False
print(is_valid_email("test@site"))                     # False (missing proper domain extension)
```

**PAN card validation** (Indian format: 5 letters, 4 digits, 1 letter — e.g., ABCDE1234F):

```python
import re

def is_valid_pan(pan):
    pattern = r"^[A-Z]{5}\d{4}[A-Z]{1}$"
    return bool(re.match(pattern, pan))

print(is_valid_pan("ABCDE1234F"))    # True
print(is_valid_pan("abcde1234f"))      # False (lowercase not allowed in this pattern)
print(is_valid_pan("ABC1234XYZ"))       # False (wrong format)
```

**Putting it all together — a mini form validator:**

```python
import re

def validate_form(name, phone, email, pan):
    errors = []

    if not re.match(r"^[A-Za-z\s]+$", name):
        errors.append("❌ Invalid name")
    if not re.match(r"^(\+91)?[6-9]\d{9}$", phone):
        errors.append("❌ Invalid phone number")
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        errors.append("❌ Invalid email")
    if not re.match(r"^[A-Z]{5}\d{4}[A-Z]{1}$", pan):
        errors.append("❌ Invalid PAN number")

    if errors:
        for error in errors:
            print(error)
        return False
    else:
        print("✅ All fields are valid!")
        return True

validate_form("Priya Sharma", "9876543210", "priya@gmail.com", "ABCDE1234F")
```

| Validation | Pattern | Meaning |
|---|---|---|
| Name | `^[A-Za-z\s]+$` | Only letters and spaces, start to end |
| Phone (India) | `^(\+91)?[6-9]\d{9}$` | Optional +91, then digit 6-9, then 9 more digits |
| Email | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | username@domain.extension format |
| PAN (India) | `^[A-Z]{5}\d{4}[A-Z]{1}$` | 5 uppercase letters, 4 digits, 1 uppercase letter |

🤔 **Quick thinking question:** Why does the phone validation pattern use `[6-9]` for the first digit specifically, instead of just `\d`?
✅ **Answer:** Indian mobile numbers are only issued starting with digits 6, 7, 8, or 9 — using `[6-9]` ensures the pattern only accepts REALISTIC Indian mobile numbers, rejecting numbers that start with 0-5 even if they're otherwise 10 digits long.

---

### 7️⃣ Overview of Python Memory Management: Reference Counting, Garbage Collection

Every time you create a variable, object, or data structure in Python, it needs to be stored somewhere in your computer's memory (RAM). Python automatically manages this memory for you — you rarely need to think about it, but understanding the basics helps you write more efficient code and debug memory-related issues.

**Reference Counting** — Python keeps track of HOW MANY variables/references currently point to a given object in memory. When that count drops to ZERO, Python knows the object is no longer needed and can safely free that memory.

```python
import sys

a = [1, 2, 3]                  # a new list object is created; 1 reference (a)
print(sys.getrefcount(a))       # shows reference count (usually 2, due to how getrefcount itself counts)

b = a                            # b now ALSO points to the SAME list; reference count increases
print(sys.getrefcount(a))         # count increased

del b                              # removing one reference; count decreases
print(sys.getrefcount(a))           # back down
```

```
        REFERENCE COUNTING VISUALIZATION
        ------------------------------------
   a = [1, 2, 3]        [1,2,3] object  ← 1 reference (from 'a')

   b = a                [1,2,3] object  ← 2 references (from 'a' AND 'b')

   del b                [1,2,3] object  ← 1 reference (only 'a' remains)

   del a                [1,2,3] object  ← 0 references → 🗑️ memory automatically freed!
```

**Garbage Collection** — handles a tricky situation that reference counting ALONE can't solve: **circular references**, where two objects reference each other, so their reference counts never naturally drop to zero, even though nothing outside actually uses them anymore.

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.reference = None

a = Node("A")
b = Node("B")

a.reference = b       # A points to B
b.reference = a         # B points to A — a CIRCULAR reference!

del a
del b
# Even after deleting both variables, A and B still reference EACH OTHER internally
# Reference counting alone can't clean this up — Python's separate Garbage Collector handles it!
```

Python has a built-in **garbage collector** (in the `gc` module) that periodically scans for these circular reference situations and cleans them up, even when simple reference counting fails to catch them.

```python
import gc

print(gc.isenabled())    # True — garbage collection is on by default

gc.collect()               # manually trigger a garbage collection cycle (rarely needed, but possible)
```

| Concept | What It Does |
|---|---|
| Reference counting | Tracks how many references point to each object; frees memory when count hits 0 |
| Circular reference | Two (or more) objects reference each other, preventing reference count from EVER reaching 0 naturally |
| Garbage collector (`gc` module) | Periodically scans for and cleans up circular references that reference counting alone would miss |

> 💡 **Tip**
>
> You almost NEVER need to manually manage memory in Python — this happens automatically. Understanding it is more about knowing WHY your program behaves the way it does, rather than something you need to actively control day-to-day.

🤔 **Quick thinking question:** Why can't simple reference counting alone clean up two objects that reference each other in a circular way?
✅ **Answer:** Because each object still has AT LEAST one reference pointing to it (from the OTHER object in the circle), so its reference count never naturally drops to zero — even though nothing OUTSIDE the circle actually uses either object anymore. This is exactly why Python needs a separate garbage collector to detect and clean up these cases.

---

## 💡 Real-Life Analogy

* 📁 **File Handling → Writing in a Physical Notebook** — Opening a file is like opening the notebook; writing/reading is like writing or reading pages; closing the file is like closing the notebook so no one else damages it while you're not using it.
* 🔄 **File Modes (`w` vs `a`) → Starting a Fresh Notebook vs. Continuing an Existing One** — "w" mode is like tearing out all the old pages and starting completely fresh; "a" mode is like simply turning to the next blank page and continuing to write.
* 🔍 **Regex → A Very Specific Bouncer at a Club's Entrance** — Instead of checking IDs one detail at a time manually, the bouncer has one clear rule card ("must be exactly 10 digits, starting with 6-9") and instantly checks anyone against it.
* 🗑️ **Reference Counting → Counting How Many People Are Still Reading a Shared Library Book** — As long as at least ONE person still has the book checked out (a reference exists), the book stays "in use." Once EVERYONE returns it (reference count hits 0), the library can put it back on the shelf (free the memory).
* ♻️ **Garbage Collection → A Cleanup Crew for a Room Where Two People Keep Pointing at Each Other** — If two people insist they're each "waiting for the other one" to leave (circular reference), a simple headcount won't clear the room — you need someone to specifically notice this deadlock and intervene (the garbage collector).

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Text/JSON file handling | Config files for almost every app; APIs (like Twitter, Instagram) return data in JSON format |
| File modes | Log rotation systems that append new entries daily using "a" mode |
| Exception handling in file ops | Cloud storage apps (Google Drive, Dropbox) handle missing/corrupted files gracefully without crashing |
| Regex email/phone validation | Every signup form you've ever filled out — Amazon, Instagram, banking apps |
| PAN/Aadhaar-style validation | Indian fintech apps (PhonePe, Paytm, ClearTax) validating KYC documents |
| Memory management | Python interpreters/runtimes (CPython) rely on reference counting + garbage collection to avoid memory leaks in long-running apps like web servers |

---

## 🔍 Industry Example

**Scenario:** A **Full-Stack Developer at a fintech startup** is building the KYC (Know Your Customer) verification form for a new banking app.

1. When a user submits their details, the form fields (name, phone, email, PAN number) are validated using **regex patterns** exactly like the ones covered in this topic — rejecting invalid formats immediately, before any data even reaches the backend.
2. Once validated, the user's data is saved as a **JSON file** (or sent to a database that stores JSON-like documents), using `json.dump()` to preserve the exact structure of the submitted form.
3. Every file operation — reading existing user records, writing new ones — is wrapped in **try/except** blocks, since file access can fail due to permission issues, missing files, or disk problems, and the app must NEVER crash during a critical KYC submission.
4. The developer chooses `"a"` (append) mode for a running audit log file that tracks every KYC submission attempt, ensuring historical records are never accidentally erased.
5. As the application runs continuously as a live web server for months, Python's automatic **reference counting and garbage collection** silently manage memory in the background — ensuring that old, no-longer-needed user session objects are properly cleaned up, preventing the server from slowly running out of memory (a "memory leak") over time.

---

## 📊 Diagram

```
              FILE HANDLING WORKFLOW
              --------------------------
    open(file, mode)  ──►  read/write operations  ──►  close (or auto-close via 'with')


              REGEX PATTERN MATCHING FLOW
              -------------------------------
    Input string:  "9876543210"
    Pattern:       r"^[6-9]\d{9}$"
                          │
                 ┌────────┴────────┐
                 ▼                   ▼
             ✅ MATCH             ❌ NO MATCH
          (valid phone)         (invalid format)


              PYTHON MEMORY MANAGEMENT
              ----------------------------
     a = [1,2,3]  ──►  🧠 Object created, ref count = 1
     b = a         ──►  🧠 SAME object, ref count = 2
     del a          ──►  🧠 ref count = 1 (still exists, 'b' points to it)
     del b           ──►  🧠 ref count = 0 → 🗑️ FREED automatically

     Circular reference (needs Garbage Collector):
     A ──points to──► B
     B ──points to──► A
     (ref count never reaches 0 naturally — gc module cleans this up)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Forgetting to close a file doesn't really matter."
  ✅ **Correct:** Leaving files open can lead to data not being properly saved, memory/resource leaks, and file-locking issues — always use `with open(...) as file:` to guarantee proper closing.

* ❌ **Wrong belief:** "`\"w\"` mode adds new content to a file, just like `\"a\"` mode."
  ✅ **Correct:** `"w"` mode COMPLETELY OVERWRITES existing file content; only `"a"` mode preserves existing content and adds new content at the end.

* ❌ **Wrong belief:** "Regex patterns don't need the `r` prefix — regular strings work just as well."
  ✅ **Correct:** Without the `r` prefix (raw string), Python may misinterpret backslash sequences BEFORE the regex engine even processes the pattern, leading to unexpected bugs — always use raw strings for regex patterns.

* ❌ **Wrong belief:** "`re.match()` and `re.search()` behave identically."
  ✅ **Correct:** `re.match()` only checks the BEGINNING of a string, while `re.search()` checks the ENTIRE string for a match anywhere within it.

* ❌ **Wrong belief:** "Python developers need to manually manage and free memory, like in some other programming languages."
  ✅ **Correct:** Python handles memory management automatically through reference counting and garbage collection — manual memory management (like in C) is not something Python developers typically need to do.

---

## 💬 Interview Corner

**Q1: What is the difference between `json.dump()` and `json.dumps()`?**
✅ `json.dump()` writes a Python object DIRECTLY to a file, while `json.dumps()` converts a Python object into a JSON-formatted STRING (without touching any file).

**Q2: What's the difference between `"w"` and `"a"` file modes?**
✅ `"w"` (write) mode creates a new file or completely overwrites an existing one, erasing any previous content. `"a"` (append) mode adds new content to the end of the file, keeping existing content intact.

**Q3: Why should you use raw strings (with the `r` prefix) for regex patterns in Python?**
✅ To prevent Python from interpreting backslash characters as its OWN special escape sequences before the regex engine gets to process the pattern — ensuring the regex pattern is passed through exactly as written.

**Q4: What is a circular reference, and why does Python need a separate garbage collector to handle it?**
✅ A circular reference occurs when two or more objects reference each other, so their reference counts never naturally drop to zero, even when nothing outside the circle uses them. Python's garbage collector specifically scans for and cleans up these situations, since simple reference counting alone cannot detect them.

---

## 📝 Quick Summary

* 📁 Use `with open(filename, mode) as file:` for safe, automatically-closed file handling
* 🔤 File modes: `"r"` (read), `"w"` (write/overwrite), `"a"` (append), `"rb"`/`"wb"` (binary read/write)
* 📦 `json.dump()`/`json.load()` work with files; `json.dumps()`/`json.loads()` work with strings
* 🛡️ Always wrap file operations in `try/except` to handle missing files, permission errors, and corrupted data gracefully
* 🔍 Regex is a compact pattern language for searching, matching, and validating text
* 🧰 Key `re` functions: `match()`, `search()`, `findall()`, `sub()`, `split()` — always use raw strings (`r"..."`) for patterns
* ✅ Regex is commonly used to validate names, phone numbers, emails, and identifiers like PAN numbers
* 🧠 Python automatically manages memory using reference counting — objects are freed once nothing references them anymore
* ♻️ The garbage collector specifically handles circular references, which reference counting alone cannot clean up
* 🎯 These three skills — file handling, regex, and memory awareness — are foundational for building real, reliable Python applications

---

## 🎯 Class Activity

**"Build a Mini KYC Form Validator with File Logging" 📋**

1. Write a program that takes name, phone number, email, and PAN number as input, and validates each one using the regex patterns shown in this topic.
2. If ALL fields are valid, save the data as a JSON file named `kyc_data.json` using `json.dump()`.
3. If any field is invalid, log an `error`-level message (using the `logging` module from the previous topic!) describing which field failed, and do NOT save the file.
4. Wrap all file operations in proper `try/except` blocks to handle any file-related errors gracefully.
5. Bonus: Use `"a"` mode to maintain a running `audit_log.txt` file that records EVERY submission attempt (valid or invalid) with a timestamp, without ever erasing previous entries.


---

# 📋 Assignments — File Handling, Regular Expressions & Python Memory Management

| Assignment |
|---|
| Write a program that writes 5 lines of text to a file using `"w"` mode, then reads and prints the entire file content back. |
| Write a program that appends a new line to an existing file every time it runs, using `"a"` mode, and run it 3 times to confirm all lines are preserved. |
| Create a Python dictionary representing a product (name, price, stock), save it to a JSON file using `json.dump()`, then read it back using `json.load()` and print it. |
| Write a program that safely attempts to open a non-existent file, catching the `FileNotFoundError` with a friendly message instead of crashing. |
| Copy an image file (or any binary file) from one location to another using `"rb"` and `"wb"` modes. |
| Write a program that reads a text file line by line using a `for` loop (not `.readlines()`), and prints only the lines containing more than 5 words. |
| Write a regex pattern to validate Indian PIN codes (exactly 6 digits), and test it against at least 5 valid and 5 invalid examples. |
| Write a function `extract_hashtags(text)` that uses `re.findall()` to extract all hashtags (words starting with #) from a given sentence. |
| Write a function `mask_email(email)` that uses `re.sub()` to partially hide an email address (e.g., `pr***@gmail.com`). |
| Build a complete form validator function that checks name, phone, email, and PAN number together, and prints a list of all validation errors found (if any). |
| Write a program demonstrating reference counting using `sys.getrefcount()` — create a list, assign it to a second variable, then delete one reference and observe the count change. |
| Write a short program (in comments, explain the concept) that intentionally creates a circular reference between two custom objects, similar to the example in this topic. |
| Write a regex pattern to validate a strong password (at least 8 characters, containing at least one uppercase letter, one lowercase letter, and one digit). |
| Combine file handling and regex: read a text file containing multiple email addresses (one per line, possibly with some invalid ones), and write only the VALID emails to a new file called `valid_emails.txt`. |
| Write a short reflection (3–5 sentences) on which of the three topics (file handling, regex, or memory management) felt the most challenging, and what part specifically you'd like more practice with. |
