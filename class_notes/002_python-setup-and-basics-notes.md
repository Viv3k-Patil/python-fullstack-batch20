# 📚 Why Python? Use Cases, Ecosystem, Installation & Your First Script

## 🎯 Learning Objectives

By the end of this class, you will be able to:

* 🐍 Explain why Python is one of the most popular languages in the industry today.
* 🌍 Identify real-world use cases and the ecosystem (libraries/frameworks) built around Python.
* 💻 Install Python correctly on your own system.
* 🛠️ Set up a proper development environment using VS Code and/or Jupyter Notebook.
* ▶️ Write and run your very first Python script successfully.

---

## 📖 Introduction

We've spent the last few classes understanding computers, operating systems, programming languages, and how compilers/interpreters work. Now it's finally time to get our hands dirty! 🙌

🤔 **Out of hundreds of programming languages that exist, why are we specifically learning Python in this course?**

Python was created by **Guido van Rossum** and released in 1991, with a core philosophy: **code should be easy to read and easy to write.** Unlike many languages that are packed with complicated symbols and strict formatting rules, Python reads almost like plain English.

**Why does this topic matter?**

Before writing any code, you need:

1. A clear understanding of *why* you're learning this particular language.
2. Python actually installed on your machine.
3. A comfortable place (IDE) to write and test your code.
4. The confidence of having successfully run your very first program.

This class is your **launchpad** — everything else in this course builds on top of what we set up today.

**Where is Python used?**

From Instagram's backend, to NASA's data analysis scripts, to the AI model that might be answering your questions elsewhere — Python is everywhere. We'll explore this in detail below.

---

## 🧠 Detailed Notes

### 🔹 Why Python?

Here's what makes Python stand out among programming languages:

| Reason | Explanation |
|---|---|
| 📖 **Readable Syntax** | Code looks close to English. No complicated curly braces `{}` or semicolons `;` required. |
| 🚀 **Beginner Friendly** | Very gentle learning curve compared to C++ or Java. |
| 📦 **Huge Ecosystem** | Massive collection of ready-made libraries for almost any task imaginable. |
| 🌐 **Versatile** | Used in Web Development, Data Science, AI/ML, Automation, Scripting, and more. |
| 🏢 **Strong Industry Demand** | Consistently ranked among the top languages in job postings and developer surveys. |
| 🤝 **Huge Community Support** | If you get stuck, chances are someone has already faced (and solved) your exact problem online. |

> 💡 **Tip**
>
> Python's official philosophy is captured in something called "The Zen of Python" — one famous line from it is: *"Simple is better than complex."* This mindset is baked into the language itself.

---

### 🔹 Use Cases & Ecosystem

Python isn't just *one* thing — it's an entire **ecosystem** of tools built around a simple core language.

```
                         PYTHON (Core Language)
                                │
        ┌───────────────┬───────┴────────┬────────────────┐
        ▼               ▼                ▼                ▼
  Web Development   Data Science    Automation/Scripting   AI / Machine Learning
  (Django, Flask)   (Pandas, NumPy)  (Selenium, os, shutil)  (TensorFlow, PyTorch)
```

| Use Case | Popular Libraries/Frameworks | Real Example |
|---|---|---|
| 🌐 **Web Development** | Django, Flask, FastAPI | Instagram's backend uses Django. |
| 📊 **Data Science & Analytics** | Pandas, NumPy, Matplotlib | Analysts use Pandas to process massive spreadsheets in seconds. |
| 🤖 **AI / Machine Learning** | TensorFlow, PyTorch, Scikit-learn | Netflix's recommendation engine research uses Python-based ML tools. |
| 🔁 **Automation/Scripting** | os, shutil, Selenium | Automating repetitive tasks like renaming 1000 files, or web scraping. |
| 🎮 **Game Development** | Pygame | Simple 2D games and prototypes. |
| 🔐 **Cybersecurity** | Scapy, Requests | Building penetration testing tools and security scripts. |

🤔 **Quick thinking question:** If Python can do so many different things, why do you think it's called a "General-Purpose" language?
✅ Answer: Because unlike some languages built for one narrow purpose (like SQL, which is only for databases), Python can be applied across **web, data, AI, automation, and more** — hence "general-purpose."

---

### 🔹 Installing Python

**Step-by-step installation process:**

1. 🌐 Go to the official website: `python.org/downloads`
2. ⬇️ Download the latest stable version for your OS (Windows/Mac/Linux).
3. ▶️ Run the installer.

> ⚠️ **Important**
>
> On **Windows**, make sure to check the box that says **"Add Python to PATH"** during installation. This step is skipped by beginners very often, and it causes the classic error: `'python' is not recognized as an internal or external command`.

4. ✅ Verify installation by opening your Terminal/Command Prompt and typing:

```bash
python --version
```
or on some systems:
```bash
python3 --version
```

If installed correctly, you'll see something like `Python 3.12.4`.

```
   Download Installer ──► Run Installer ──► Check "Add to PATH" ──► Verify with python --version
```

---

### 🔹 Setting Up an IDE (VS Code / Jupyter)

An **IDE (Integrated Development Environment)** is where you'll actually write, run, and debug your code — think of it as your "workshop."

| Feature | 🧩 VS Code | 📓 Jupyter Notebook |
|---|---|---|
| **Best For** | General-purpose coding, Web/App development, Full Stack projects | Data analysis, quick experiments, step-by-step exploration |
| **Interface** | Traditional file-based code editor | Cell-based notebook (run code in small chunks) |
| **Output Display** | Shows output in a terminal panel | Shows output directly below each cell (great for graphs/tables) |
| **Extensions** | Huge marketplace (Python, Git, Docker extensions, etc.) | Limited, but great built-in support for visualization |
| **Typical Use in This Course** | Writing Full Stack Python projects (Django/Flask apps) | Practicing Data Analysis, quick script testing |

**Setting up VS Code:**

1. Download from `code.visualstudio.com`.
2. Install it like any regular application.
3. Open VS Code → Go to Extensions (🧩 icon) → Search **"Python"** → Install the official Microsoft Python extension.
4. Open a folder, create a file `hello.py`, and you're ready to code!

**Setting up Jupyter Notebook:**

1. Open your Terminal/Command Prompt.
2. Run:
```bash
pip install notebook
```
3. Launch it by running:
```bash
jupyter notebook
```
4. This opens Jupyter in your web browser, where you can create a new notebook and start writing code in cells.

> 💡 **Tip**
>
> Many developers use **both** — VS Code for building real applications, and Jupyter for quick data experiments. You don't have to pick just one forever!

---

### 🔹 Writing & Running Your First Python Script

Let's finally write some real code! 🎉

**Step 1: Create a file**

Create a new file named `first_script.py`.

**Step 2: Write this code inside it**

```python
print("Hello, World! I just wrote my first Python program.")
```

**Step 3: Run it**

* **Using VS Code:** Open the file, click the ▶️ "Run" button (top-right), or right-click → "Run Python File in Terminal."
* **Using Terminal directly:**
```bash
python first_script.py
```
* **Using Jupyter Notebook:** Type the code into a cell and press `Shift + Enter`.

**Expected Output:**

```
Hello, World! I just wrote my first Python program.
```

🤔 **Quick thinking question:** Why do you think almost every programming course in the world starts with a "Hello, World!" program?
✅ Answer: Because it's the **simplest possible way to confirm** that your language, installation, and environment are all working correctly together — before you move on to anything complex.

---

## 💡 Real-Life Analogy

**Python Ecosystem = A Fully Stocked Toolbox** 🧰

Imagine Python's core language as a basic **hammer** — useful on its own. But the Python ecosystem gives you an entire **toolbox**: a screwdriver (Pandas for data), a drill (Django for web apps), a measuring tape (NumPy for calculations). You pick the right tool depending on the job at hand — but they're all part of the same toolbox, designed to work together.

**Installing Python + IDE Setup = Setting Up a Kitchen Before Cooking** 🍳

You wouldn't start cooking a dish without first having a stove (Python installed) and a clean countertop with your utensils laid out (IDE set up). Only once your kitchen is ready can you actually start cooking (writing real code)!

---

## 💻 Real-World Application

**Python's ecosystem is used in:**

* 📸 **Instagram** — Backend built primarily using Django (a Python framework).
* 🎬 **Netflix** — Uses Python extensively for backend services, data pipelines, and recommendation research.
* 🚀 **NASA** — Uses Python for scientific computing, data analysis, and even mission-critical calculations.
* 🏦 **Financial Institutions** — Use Python (Pandas, NumPy) for risk analysis and fraud detection modeling.
* 🧠 **AI Companies (like OpenAI, Anthropic)** — Use Python as the primary language for building and training AI models.

---

## 🔍 Industry Example

**"When a Data Analyst at Spotify wants to understand which songs are trending..."**

1. 🛠️ They open **Jupyter Notebook** (their preferred IDE for data exploration).
2. 📊 They use the **Pandas** library to load millions of rows of streaming data.
3. 🧮 They write a few lines of Python to calculate top trending songs by region.
4. 📈 They use **Matplotlib** to create a simple visual chart of the results.
5. 📤 These insights help Spotify decide what to feature on the "Trending Now" playlist — all powered by Python's ecosystem!

---

## 📊 Diagram

```
   Install Python
        │
        ▼
   Set Up IDE (VS Code / Jupyter)
        │
        ▼
   Write Code (hello.py)
        │
        ▼
   Run Code (python hello.py)
        │
        ▼
   See Output on Screen 🎉
```

---

## ⚠️ Common Mistakes

❌ "I installed Python, so I don't need an IDE — Notepad is enough."
✅ While technically possible, a proper IDE like **VS Code** gives you error highlighting, auto-completion, and easy running/debugging — massively improving productivity.

❌ "Forgetting to check 'Add Python to PATH' during installation doesn't matter."
✅ This is one of the **most common beginner errors** — without it, your terminal won't recognize the `python` command at all.

❌ "Jupyter Notebook and VS Code are competitors — I should only learn one."
✅ They serve **different purposes** and are often used together by the same developer, depending on the task.

❌ "Python 2 and Python 3 are basically the same, so it doesn't matter which I install."
✅ Python 2 is **officially discontinued** (end-of-life). Always install the latest **Python 3.x** version.

---

## 💬 Interview Corner

**Q1: Why is Python considered a good language for beginners?**
A: Its syntax is simple and close to plain English, it has extensive community support, and it removes a lot of the complexity found in languages like C++ or Java.

**Q2: Name two frameworks/libraries Python offers for web development and two for data science.**
A: Web Development — Django, Flask. Data Science — Pandas, NumPy.

**Q3: What is the difference between VS Code and Jupyter Notebook?**
A: VS Code is a general-purpose code editor best suited for building full applications, while Jupyter Notebook is a cell-based environment best suited for data analysis and quick experimentation.

---

## 📝 Quick Summary

* 🐍 Python is popular due to its **readable syntax, versatility, and huge ecosystem**.
* 🌍 Python is used across **Web Development, Data Science, AI/ML, Automation, and more**.
* 💻 Installing Python requires downloading from `python.org` and ensuring **"Add to PATH"** is checked (Windows).
* 🛠️ **VS Code** is great for general coding; **Jupyter Notebook** is great for data exploration.
* ▶️ Your first Python script uses the simple `print()` function to display output.
* ✅ Always verify your setup using `python --version` before moving forward.

---

## 🎯 Class Activity

1. Open your Terminal/Command Prompt and run `python --version` to confirm Python is installed.
2. Open VS Code (or Jupyter Notebook) and create a new file called `myfirstprogram.py`.
3. Write a line of code that prints your own name, e.g., `print("My name is Riya")`.
4. Run the file and confirm the output appears correctly.
5. Try changing the message and running it again — notice how quickly you can see results!

---

# 📋 Assignments — Why Python? Installation & First Script

| Assignment |
|---|
| Install Python on your personal laptop and verify the version using `python --version` in the terminal. |
| Install VS Code and the official Python extension. Take a screenshot of the extension installed. |
| Write a Python script that prints your full name, city, and career goal — each on a separate line. |
| Install Jupyter Notebook using pip and successfully launch it in your browser. |
| Research and list 3 real companies that use Python in their tech stack, other than the ones mentioned in class. |
| Write a Python script using `print()` that displays a small ASCII art or pattern of your choice. |
| Try running the same Python script using three different methods: VS Code Run button, Terminal command, and Jupyter Notebook cell. Note any differences you observed. |
| Research what "PATH" means in the context of installing software, and explain it in 3-4 lines in your own words. |
| Find out the latest stable version of Python available today, and compare it with the version you installed. |
| List 5 Python libraries (other than the ones mentioned in class) and briefly research what each one is used for. |
| Intentionally create an error in your Python script (e.g., misspell `print` as `pint`) and note down the exact error message Python shows you. |

---

# 📚 Basic Python Syntax & Control Flow (Introduction)

## 🎯 Learning Objectives

By the end of this class, you will be able to:

* 🏷️ Understand identifiers, variables, and Python's reserved keywords.
* 📦 Identify Python's basic data types.
* 🔄 Perform type casting between different data types.
* ➕ Use arithmetic, comparison, and logical operators confidently.
* 🔀 Write simple `if` conditions to make decisions in code.
* 🔁 Write basic loops to repeat actions automatically.

---

## 📖 Introduction

Now that Python is installed and you've run your first script, it's time to learn the actual **building blocks** of the language — the vocabulary and grammar you'll use in every single Python program you ever write.

🤔 **Think about it — every single app, website, or AI model, no matter how complex, is ultimately built using a handful of basic building blocks: storing data, making decisions, and repeating actions.**

That's exactly what we'll learn today:

* How to **store information** (variables and data types).
* How to **convert information** from one form to another (type casting).
* How to **perform operations** on data (operators).
* How to **make decisions** (`if` conditions).
* How to **repeat actions** (loops).

**Why is this important?**

These concepts are the absolute foundation of programming. Skipping or rushing through this topic will make everything else in this course — web development, APIs, databases — much harder to understand later.

**Where is this used?**

Every single feature of every app you use relies on these basics. When Instagram decides whether to show you a "like" notification (a decision/condition) or when it loops through hundreds of posts to display your feed (a loop) — it's built on exactly these fundamentals.

---

## 🧠 Detailed Notes

### 🔹 Identifiers

> An identifier is simply the **name** you give to things in your program — like variables, functions, or classes.

**Rules for naming identifiers in Python:**

| Rule | Example (Valid ✅) | Example (Invalid ❌) |
|---|---|---|
| Must start with a letter or underscore `_` | `age`, `_name` | `1name` |
| Can contain letters, numbers, and underscores | `student_1`, `total_marks` | `student-1` (hyphens not allowed) |
| Cannot use reserved keywords | `total` | `for`, `if` (these are reserved) |
| Case-sensitive | `Age` and `age` are different | — |
| No spaces allowed | `first_name` | `first name` |

> 💡 **Tip**
>
> Python developers commonly use **snake_case** for variable names (e.g., `student_name`, `total_marks`) rather than camelCase — it's considered the standard, readable convention in Python.

---

### 🔹 Variables

> A variable is a **named container** used to store data in memory, which can be used and changed later in your program.

```python
name = "Riya"          # storing text
age = 21                # storing a number
is_student = True       # storing True/False
```

Unlike many other languages, Python does **not** require you to declare the data type in advance — this is called **dynamic typing**.

```python
x = 10        # x is currently an integer
x = "hello"   # now x is a string - Python allows this!
```

🤔 **Quick thinking question:** If Python doesn't require specifying data types upfront, how does it know what type of data a variable holds?
✅ Answer: Python automatically detects the type **at the moment you assign a value** — this is called **dynamic typing**, and it's one reason Python code looks so clean and simple.

---

### 🔹 Reserved Keywords

> Reserved keywords are **special words** that Python has already reserved for its own use. You cannot use them as variable names.

| Category | Examples |
|---|---|
| Conditionals | `if`, `elif`, `else` |
| Loops | `for`, `while`, `break`, `continue` |
| Logical | `and`, `or`, `not` |
| Values | `True`, `False`, `None` |
| Functions/Classes | `def`, `class`, `return` |
| Others | `import`, `try`, `except`, `pass`, `in`, `is` |

> ⚠️ **Important**
>
> Trying to write `for = 5` will give you a **SyntaxError**, because `for` is a reserved keyword, not an available variable name.

---

### 🔹 Data Types

| Data Type | Example | Description |
|---|---|---|
| 🔢 **int** | `age = 21` | Whole numbers (no decimal). |
| 🔢 **float** | `price = 99.99` | Numbers with decimal points. |
| 🔤 **str** | `name = "Riya"` | Text data, written inside quotes. |
| ✅ **bool** | `is_active = True` | Only two values: `True` or `False`. |
| 📋 **list** | `marks = [90, 85, 78]` | An ordered, changeable collection of items. |
| 📦 **tuple** | `coordinates = (10, 20)` | An ordered, unchangeable collection of items. |
| 🗂️ **dict** | `student = {"name": "Riya", "age": 21}` | Key-value pairs, like a mini-database. |
| 🚫 **NoneType** | `result = None` | Represents "no value" or "empty." |

```
       Python Data Types
              │
   ┌──────────┼───────────┬─────────────┐
   ▼          ▼            ▼             ▼
 Numeric   Text (str)   Boolean     Collections
(int,float)              (True/False) (list, tuple, dict, set)
```

---

### 🔹 Type Casting

> Type casting means **converting one data type into another.**

```python
age = "21"          # this is currently a string
age = int(age)      # now converted to an integer -> 21

price = 99           # this is currently an integer
price = float(price) # now converted to a float -> 99.0

marks = 85
marks = str(marks)   # now converted to a string -> "85"
```

| Function | Converts To |
|---|---|
| `int()` | Integer |
| `float()` | Float (decimal) |
| `str()` | String (text) |
| `bool()` | Boolean (True/False) |

> 💡 **Tip**
>
> Type casting is extremely common when taking user input, because Python's `input()` function **always returns a string** — even if the user types a number!

```python
age = input("Enter your age: ")   # this is a string, even if user types "21"
age = int(age)                     # now it's usable as a number for calculations
```

---

### 🔹 Basic Operators

**1. Arithmetic Operators** (for calculations)

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponent (power) | `5 ** 2` | `25` |

**2. Comparison Operators** (compare two values, return True/False)

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

**3. Logical Operators** (combine multiple conditions)

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True only if BOTH are true | `(5>3) and (2>1)` | `True` |
| `or` | True if AT LEAST ONE is true | `(5>3) or (1>2)` | `True` |
| `not` | Reverses the result | `not(5>3)` | `False` |

🤔 **Quick thinking question:** What's the difference between `/` and `//` in Python?
✅ Answer: `/` always gives a **decimal (float) result**, while `//` gives only the **whole number part**, discarding any remainder — this is called floor division.

---

### 🔹 Simple `if` Conditions

> `if` statements let your program **make decisions** based on conditions.

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
```

**With multiple conditions using `elif`:**

```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")
```

> ⚠️ **Important**
>
> Python uses **indentation (spaces)** instead of curly braces `{}` to define code blocks. Incorrect indentation will cause an `IndentationError` — this is very different from languages like Java or C++.

---

### 🔹 Basic Loops

Loops let your program **repeat an action** multiple times without rewriting the same code again and again.

**1. `for` loop** — used when you know how many times to repeat, or want to go through a collection:

```python
for i in range(5):
    print("Hello, this is loop number", i)
```

**2. `while` loop** — used when you want to repeat until a condition becomes false:

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count = count + 1
```

```
   FOR LOOP FLOW:                    WHILE LOOP FLOW:
   ┌─────────────┐                   ┌─────────────┐
   │ Start Loop  │                   │  Check       │
   └──────┬──────┘                   │  Condition   │◄────┐
          ▼                          └──────┬──────┘      │
   ┌─────────────┐                          │ True         │
   │ Run for each │                         ▼              │
   │  item/range  │                  ┌─────────────┐      │
   └──────┬──────┘                   │  Run Code    │──────┘
          ▼                          └──────┬──────┘
   ┌─────────────┐                          │ False
   │  Loop Ends   │                         ▼
   └─────────────┘                  ┌─────────────┐
                                     │  Loop Ends   │
                                     └─────────────┘
```

🤔 **Quick thinking question:** What would happen if you forgot to write `count = count + 1` inside the `while` loop example above?
✅ Answer: The condition `count <= 5` would **never become false**, causing an **infinite loop** — your program would run forever until you manually stop it!

---

## 💡 Real-Life Analogy

**Variables = Labeled Boxes** 📦

Imagine labeled boxes in your room: a box labeled "Books," another labeled "Clothes." You can put things inside, take them out, or even replace the contents entirely — that's exactly what a variable does with data.

**`if` Conditions = A Traffic Signal** 🚦

"IF the signal is green, THEN go. ELSE, stop." Your program checks a condition, just like a driver checks the traffic light, and takes a specific action based on the result.

**Loops = A Washing Machine Cycle** 🔄

A washing machine repeats the same wash-rinse-spin cycle a set number of times (like a `for` loop with a fixed count), or keeps repeating until the clothes are clean enough (like a `while` loop with a condition) — then it stops.

---

## 💻 Real-World Application

**These basics are used in:**

* 🛒 **E-commerce Websites** — `if` conditions check stock availability before allowing a purchase ("if quantity > 0: allow order").
* 🎓 **Result Processing Systems** — Loops go through hundreds of student records to calculate grades automatically.
* 🏧 **ATM Machines** — `if` conditions check whether your entered PIN is correct and whether your balance is sufficient.
* 📱 **Social Media Feeds** — Loops repeatedly fetch and display each post in your feed, one after another.

---

## 🔍 Industry Example

**"When you try to withdraw ₹5000 from an ATM..."**

1. 🔢 The system stores your account balance in a **variable**.
2. 🔁 It **type-casts** your entered amount from text input into a number.
3. ⚖️ It uses a **comparison operator** (`>=`) to check if your balance is sufficient.
4. 🔀 An **`if` condition** decides: "If balance >= 5000, dispense cash. Else, show 'Insufficient Balance.'"
5. This entire decision — something that feels instant to you — is literally just an `if` condition running behind the scenes!

---

## 📊 Diagram

```
         Start
           │
           ▼
   Take Input (age)
           │
           ▼
   Type Cast to int
           │
           ▼
      if age >= 18? ──── No ──► Print "Not eligible"
           │
          Yes
           │
           ▼
   Print "Eligible to vote"
           │
           ▼
          End
```

---

## ⚠️ Common Mistakes

❌ "Variable names can start with a number, like `1name`."
✅ Identifiers **must start with a letter or underscore**, never a number.

❌ "I can use `for` or `if` as a variable name since it's just a name."
✅ These are **reserved keywords** — Python will throw a `SyntaxError` if you try.

❌ "`input()` returns a number if the user types a number."
✅ `input()` **always returns a string** — you must manually type-cast it using `int()` or `float()` if you need a number.

❌ "Using `=` and `==` means the same thing."
✅ `=` is used for **assignment** (storing a value), while `==` is used for **comparison** (checking equality). Mixing these up is one of the most common beginner bugs.

❌ "Indentation in Python is just for looks — it doesn't affect the code."
✅ Indentation in Python is **mandatory and functional** — it defines which lines belong inside a loop, if-condition, or function.

---

## 💬 Interview Corner

**Q1: What is the difference between `=` and `==` in Python?**
A: `=` is the assignment operator, used to store a value in a variable. `==` is the comparison operator, used to check if two values are equal.

**Q2: Why is Python called a "dynamically typed" language?**
A: Because you don't need to declare a variable's data type in advance — Python automatically determines it based on the value assigned, and the type can even change later.

**Q3: What is the difference between a `for` loop and a `while` loop?**
A: A `for` loop is typically used when the number of iterations is known or when iterating over a collection. A `while` loop repeats as long as a specified condition remains true, useful when the number of iterations isn't known in advance.

**Q4: Why does `input()` require type casting when working with numbers?**
A: Because Python's `input()` function always returns the entered value as a string, regardless of what the user types, so it must be explicitly converted using `int()` or `float()` for numeric operations.

---

## 📝 Quick Summary

* 🏷️ **Identifiers** are names for variables/functions — must start with a letter/underscore, no spaces, can't be reserved keywords.
* 📦 **Variables** store data and don't require a fixed data type in Python (dynamic typing).
* 🚫 **Reserved keywords** (like `if`, `for`, `True`) cannot be used as variable names.
* 🔢 Python's basic **data types** include int, float, str, bool, list, tuple, dict, and NoneType.
* 🔄 **Type casting** converts data from one type to another using functions like `int()`, `float()`, `str()`.
* ➕ **Operators** include Arithmetic (`+`, `-`, `*`, `/`), Comparison (`==`, `>`, `<`), and Logical (`and`, `or`, `not`).
* 🔀 **`if` conditions** allow your program to make decisions based on logic.
* 🔁 **Loops** (`for`, `while`) allow your program to repeat actions automatically.
* ⚠️ Python uses **indentation**, not curly braces, to define code blocks.

---

## 🎯 Class Activity

1. Open your IDE (VS Code or Jupyter Notebook).
2. Create variables for your `name`, `age`, and `is_student` status.
3. Write an `if` condition that checks if your age is greater than 18, and prints an appropriate message.
4. Write a `for` loop that prints "I am learning Python" 5 times.
5. Discuss with a classmate: "What happens if you remove the indentation from inside the if block?" Try it and observe the error!

---

# 📋 Assignments — Basic Python Syntax & Control Flow

| Assignment |
|---|
| Write a Python script that stores your name, age, and city in three separate variables and prints them using a single `print()` statement. |
| Write a program that takes a number as input from the user and prints whether it is even or odd (using `if-else` and the modulus operator). |
| Write a program that uses `input()` to take a user's age as text, type-casts it into an integer, and prints "Eligible to vote" or "Not eligible" accordingly. |
| Create 5 variables of 5 different data types (int, float, str, bool, list) and print each variable along with its data type using the `type()` function. |
| Write a `for` loop that prints all numbers from 1 to 10. |
| Write a `while` loop that prints all even numbers from 2 to 20. |
| Write a program using `if-elif-else` that takes marks as input and prints the correct grade (A, B, C, or Fail). |
| Try naming a variable using a reserved keyword (e.g., `for = 5`) and note down the exact error Python shows. |
| Write a program that demonstrates all 3 logical operators (`and`, `or`, `not`) using simple comparison examples. |
| Research and list 5 more reserved keywords in Python that were not covered in class, along with what each one is used for. |
| Write a program that calculates the area of a rectangle by taking length and width as input from the user (remember to type-cast!). |
| Intentionally write a loop without updating the condition variable (creating an infinite loop), run it, and note down how you stopped it (e.g., Ctrl+C). |
