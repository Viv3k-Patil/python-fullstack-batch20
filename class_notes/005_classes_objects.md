# 📚 Object-Oriented Programming (OOP) Concepts (Part 1)

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand what Object-Oriented Programming is and why it's used
* 🎯 Create classes and objects in Python
* 🎯 Understand and use instance variables and instance methods
* 🎯 Get a basic understanding of class variables and how they differ from instance variables
* 🎯 Understand inner classes (classes inside classes) using real examples like College, Department, and Student
* 🎯 Understand the basics of inheritance and the "is-a" relationship between classes

---

## 📖 Introduction

Until now, you've written programs using variables, functions, and data structures like lists and dictionaries. But as real-world software grows bigger — think of a college management system, a banking app, or an e-commerce site — just using plain variables and functions becomes messy and hard to manage.

**Object-Oriented Programming (OOP)** is a way of writing code that models real-world things — like a `Student`, a `Car`, a `BankAccount` — as **objects**, each having their own **properties** (data) and **behaviors** (actions). 🧑‍🎓🚗🏦

### 🤔 Why does this topic exist?

* 🌍 The real world is made of "things" (objects) that have characteristics and actions — OOP lets code mirror reality closely
* 🧩 It helps organize large codebases into logical, manageable units
* ♻️ It promotes reusability — write a `Student` blueprint once, create hundreds of student objects from it
* 🔗 It naturally supports relationships between real-world entities — a College *has* Departments, a Department *has* Students

### 🤔 Where is it used?

* 🎮 Game development — every character, weapon, or enemy is an object
* 🏦 Banking software — each customer's account is an object with balance, deposit(), withdraw()
* 🛒 E-commerce — every product, cart, and order is modeled as an object
* 📱 Mobile apps — UI components (buttons, screens) are built using OOP
* 🐍 Python itself — even a simple string or list you've been using is secretly an **object**!

> 💡 **Tip**
>
> Almost every major programming language (Java, C++, Python, C#, JavaScript) supports OOP because it mirrors how humans naturally think about the world — in terms of "things" with properties and actions.

---

## 🧠 Detailed Notes

### 1️⃣ Classes and Objects

A **class** is a **blueprint** or **template** — it defines what properties and behaviors something will have, but it is not the actual thing itself.

An **object** is a real **instance** created from that blueprint — the actual "thing" with real data.

```python
class Student:          # class definition (the blueprint)
    pass

s1 = Student()           # object (an actual instance)
s2 = Student()           # another separate object

print(type(s1))           # <class '__main__.Student'>
print(s1)                  # <__main__.Student object at 0x...>
```

**A more useful class, with a constructor:**

```python
class Student:
    def __init__(self, name, age, course):    # constructor — runs automatically when object is created
        self.name = name
        self.age = age
        self.course = course

# Creating objects (instances) of the Student class
s1 = Student("Priya", 20, "Python Full Stack")
s2 = Student("Rahul", 22, "Data Science")

print(s1.name, s1.age, s1.course)    # Priya 20 Python Full Stack
print(s2.name, s2.age, s2.course)    # Rahul 22 Data Science
```

**Anatomy of `__init__`:**

```
   def   __init__ ( self, name, age, course ):
    │        │        │      │
    │        │        │      └── parameters (data to set up the object)
    │        │        └───────── refers to the CURRENT object being created
    │        └────────────────── special "constructor" method name (double underscores)
    └─────────────────────────── keyword to define any function/method
```

> ⚠️ **Important**
>
> `__init__` is called a **constructor**. It runs **automatically** the moment you create an object using `ClassName(...)`. You never call `__init__` directly.

🤔 **Quick thinking question:** If `s1 = Student("Priya", 20, "Python")` and `s2 = Student("Rahul", 22, "Java")`, are `s1` and `s2` the same object?
✅ **Answer:** No — they are two completely separate objects, each with their own independent copy of `name`, `age`, and `course`, even though both were created from the same `Student` class blueprint.

---

### 2️⃣ Instance Variables, Instance Methods

**Instance variables** are variables that belong to a **specific object** — each object gets its own independent copy. They are usually created inside `__init__` using `self.variable_name`.

**Instance methods** are functions defined inside a class that operate on a specific object's data. They always take `self` as their first parameter, which refers to the object calling the method.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name          # instance variable
        self.marks = marks         # instance variable

    def display_info(self):        # instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

    def is_passed(self):            # another instance method
        return self.marks >= 40

s1 = Student("Ananya", 85)
s2 = Student("Kabir", 30)

s1.display_info()      # Name: Ananya, Marks: 85
s2.display_info()      # Name: Kabir, Marks: 30

print(s1.is_passed())   # True
print(s2.is_passed())   # False
```

**Modifying instance variables after object creation:**

```python
s1.marks = 90            # directly update
print(s1.marks)           # 90

s1.display_info()          # Name: Ananya, Marks: 90
```

**Methods can also update the object's own data:**

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_bonus_marks(self, bonus):
        self.marks += bonus              # updates THIS object's marks

s1 = Student("Ananya", 85)
s1.add_bonus_marks(5)
print(s1.marks)     # 90
```

| Concept | Meaning | Example |
|---|---|---|
| Instance variable | Data unique to each object | `self.name`, `self.marks` |
| Instance method | Function that acts on an object's own data | `display_info(self)` |
| `self` | Refers to "this particular object" | Always first parameter of instance methods |

> 💡 **Tip**
>
> Think of `self` as the class saying "I'm talking about **this specific object**, not any other object of the same class."

🤔 **Quick thinking question:** Why does every instance method need `self` as its first parameter?
✅ **Answer:** Because Python needs to know **which object's** data the method should work with. When you call `s1.display_info()`, Python automatically passes `s1` as `self` behind the scenes.

---

### 3️⃣ Class Variables (Basic Idea)

Unlike instance variables (unique per object), a **class variable** is **shared by ALL objects** of that class. It's defined directly inside the class, but outside any method.

```python
class Student:
    college_name = "ABC Institute of Technology"    # class variable — SHARED by all objects

    def __init__(self, name, marks):
        self.name = name        # instance variable — unique per object
        self.marks = marks       # instance variable — unique per object

s1 = Student("Ananya", 85)
s2 = Student("Kabir", 60)

print(s1.college_name)    # ABC Institute of Technology
print(s2.college_name)    # ABC Institute of Technology  (SAME for both!)

print(s1.name, s2.name)    # Ananya Kabir  (DIFFERENT for each)
```

**A common real use case — counting how many objects have been created:**

```python
class Student:
    total_students = 0     # class variable, starts at 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1    # increases the SHARED counter every time a new object is made

s1 = Student("Ananya")
s2 = Student("Kabir")
s3 = Student("Rahul")

print(Student.total_students)    # 3  — shared across all objects
```

| Type | Belongs to | How to access | Shared? |
|---|---|---|---|
| Instance variable | Each individual object | `self.variable` | ❌ No — unique per object |
| Class variable | The class itself | `ClassName.variable` or `self.variable` (read-only) | ✅ Yes — same for all objects |

> ⚠️ **Important**
>
> If you do `s1.college_name = "XYZ College"`, it does **not** change the class variable for everyone — it actually creates a **new instance variable** for `s1` only, which "shadows" (hides) the class variable just for that one object.

🤔 **Quick thinking question:** In the `total_students` example, why do we write `Student.total_students += 1` inside `__init__` instead of `self.total_students += 1`?
✅ **Answer:** Using `Student.total_students` clearly updates the shared class-level counter. Using `self.total_students += 1` would actually create a brand-new **instance** variable for that object instead of updating the shared class variable — a very common beginner mistake.

---

### 4️⃣ Inner Classes with Real Examples (College, Department, Student)

An **inner class** (or nested class) is simply a class defined **inside another class**. This is useful for modeling real-world "has-a" relationships — for example, a **College** *has* **Departments**, and a **Department** *has* **Students**.

```python
class College:
    def __init__(self, college_name):
        self.college_name = college_name

    class Department:                        # INNER CLASS inside College
        def __init__(self, dept_name, hod):
            self.dept_name = dept_name
            self.hod = hod

        class Student:                        # INNER CLASS inside Department
            def __init__(self, name, roll_no):
                self.name = name
                self.roll_no = roll_no

            def display(self):
                print(f"Student: {self.name}, Roll No: {self.roll_no}")


# Creating a College object
c1 = College("ABC Institute of Technology")

# Creating a Department object (using College.Department)
d1 = College.Department("Computer Science", "Dr. Mehta")
print(d1.dept_name, "-", d1.hod)

# Creating a Student object (using College.Department.Student)
s1 = College.Department.Student("Priya", 101)
s1.display()
```

Output:
```
Computer Science - Dr. Mehta
Student: Priya, Roll No: 101
```

**A more realistic, connected version — where objects actually contain other objects:**

```python
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Department:
    def __init__(self, dept_name, hod):
        self.dept_name = dept_name
        self.hod = hod
        self.students = []          # a Department HAS students (a list of Student objects)

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"\nStudents in {self.dept_name} Department:")
        for student in self.students:
            print(f"  - {student.name} (Roll No: {student.roll_no})")

class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.departments = []        # a College HAS departments (a list of Department objects)

    def add_department(self, department):
        self.departments.append(department)

    def show_college_structure(self):
        print(f"🏫 {self.college_name}")
        for dept in self.departments:
            print(f" └── 🏢 {dept.dept_name} (HOD: {dept.hod})")
            for student in dept.students:
                print(f"      └── 🧑‍🎓 {student.name} (Roll No: {student.roll_no})")


# Building the structure
cs_dept = Department("Computer Science", "Dr. Mehta")
cs_dept.add_student(Student("Priya", 101))
cs_dept.add_student(Student("Rahul", 102))

college = College("ABC Institute of Technology")
college.add_department(cs_dept)
college.show_college_structure()
```

Output:
```
🏫 ABC Institute of Technology
 └── 🏢 Computer Science (HOD: Dr. Mehta)
      └── 🧑‍🎓 Priya (Roll No: 101)
      └── 🧑‍🎓 Rahul (Roll No: 102)
```

> 💡 **Tip**
>
> In real professional Python code, this second approach (separate classes connected via "has-a" relationships) is used **far more often** than truly nested inner classes — it's cleaner and more flexible. True inner classes (like the first example) are shown here mainly to build conceptual understanding.

🤔 **Quick thinking question:** In the College-Department-Student example, is the relationship between a Department and its Students a "has-a" or an "is-a" relationship?
✅ **Answer:** It's a **"has-a"** relationship — a Department *has* Students; a Student is not *a type of* Department. ("is-a" relationships are handled through inheritance, covered next!)

---

### 5️⃣ Inheritance Basics (is-a Relationship)

**Inheritance** allows one class (called the **child** or **subclass**) to reuse the properties and methods of another class (called the **parent** or **superclass**) — while also being able to add its own new features.

This models an **"is-a" relationship**: for example, "a Student *is a* Person", "a Manager *is an* Employee".

```python
class Person:                    # PARENT class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):            # CHILD class — Student "is a" Person
    def __init__(self, name, age, course):
        super().__init__(name, age)    # calls the PARENT's __init__ to set up name & age
        self.course = course             # Student-specific extra attribute

    def display_course(self):
        print(f"{self.name} is studying {self.course}")


s1 = Student("Ananya", 21, "Python Full Stack")

s1.display_info()       # Name: Ananya, Age: 21     ← inherited from Person!
s1.display_course()      # Ananya is studying Python Full Stack   ← Student's own method
```

**What's happening with `super()`:**

```
   class Student(Person):
                  │
                  └── Student INHERITS everything from Person

   super().__init__(name, age)
       │
       └── calls Person's constructor to set up 'name' and 'age',
           so Student doesn't need to repeat that code
```

**Multiple child classes sharing one parent:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

s1 = Student("Priya", 20, "Python")
t1 = Teacher("Dr. Mehta", 45, "Computer Science")

s1.display_info()    # Name: Priya, Age: 20        ← reused from Person
t1.display_info()    # Name: Dr. Mehta, Age: 45     ← reused from Person
```

| Term | Meaning |
|---|---|
| Parent class / Superclass | The original class being reused (e.g., `Person`) |
| Child class / Subclass | The new class that inherits from the parent (e.g., `Student`) |
| `super()` | Used to call the parent class's methods/constructor from inside the child |
| "is-a" relationship | Describes inheritance — "a Student **is a** Person" |

> ⚠️ **Important**
>
> Don't confuse "is-a" (inheritance) with "has-a" (composition, like College having Departments). A `Student` **is a** `Person` (inheritance), but a `Department` **has** `Students` (composition) — they are different relationships and are modeled differently in code.

🤔 **Quick thinking question:** Why do we call `super().__init__(name, age)` inside `Student`'s constructor instead of just rewriting `self.name = name` and `self.age = age` again?
✅ **Answer:** Reusing the parent's constructor via `super()` avoids duplicating code — if `Person`'s setup logic ever changes, `Student` (and every other child class) automatically benefits without needing to be modified separately.

---

## 💡 Real-Life Analogy

* 🏗️ **Class → An Architect's Blueprint for a House** — The blueprint itself isn't a house you can live in; it just defines what every house built from it *will* have (rooms, doors, windows).
* 🏠 **Object → An Actual House Built From That Blueprint** — Many houses (objects) can be built from the same blueprint (class), each with their own address, paint color, and furniture (instance variables).
* 🧬 **Instance Variable → A Family Living in a Specific House** — Every house has its *own* family; one house's residents don't affect another's.
* 🏛️ **Class Variable → The Housing Society's Shared Rule Board** — A single rule (like "gate closes at 10 PM") applies to *every* house in the society equally, unless one house specifically decides to ignore it.
* 🏫 **Inner Classes (College → Department → Student) → A Company's Organization Chart** — A Company *has* Departments, and each Department *has* Employees — a nested, "contains" structure.
* 👨‍👩‍👧 **Inheritance → A Child Inheriting Traits From a Parent** — A child inherits the parent's surname and basic traits (inherited methods/variables), but also develops their own unique personality (their own extra methods/variables).

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| **Classes & Objects** | Instagram — every user profile is an object created from a `User` class |
| **Instance Variables** | Amazon — each product object has its own `price`, `stock`, `rating` |
| **Class Variables** | A game like PUBG/BGMI — a shared "max players per match" value used by every `Match` object |
| **Inner Classes / Composition** | LinkedIn — a `Company` object contains multiple `Department` objects, each containing `Employee` objects |
| **Inheritance** | Uber — `Driver` and `Rider` classes might both inherit shared attributes from a common `User` parent class |

---

## 🔍 Industry Example

**Scenario:** A **Software Engineer at a college ERP company** (like the systems used by universities to manage students, faculty, and courses) is designing the core data model.

1. They start by creating a `Person` class with common attributes shared by everyone in the system: `name`, `age`, `email`.
2. They create a `Student` class and a `Faculty` class, both **inheriting** from `Person` using `super()` — since "a Student *is a* Person" and "a Faculty member *is a* Person" (is-a relationship, inheritance).
3. They design a `Department` class that **contains** a list of `Student` objects and `Faculty` objects — since "a Department *has* Students and Faculty" (has-a relationship, composition).
4. They design a `College` class that **contains** a list of `Department` objects — again a has-a relationship.
5. They add a **class variable** `College.total_colleges_registered` to track how many college branches are using their ERP software system-wide — a single shared counter, not tied to any one college.
6. Each `Student` object has its own **instance variables**: `roll_no`, `marks`, `attendance_percentage` — completely independent from every other student.

This exact structure — inheritance for "is-a" relationships and composition for "has-a" relationships — is the backbone of real enterprise software design.

---

## 📊 Diagram

```
              CLASS vs OBJECT
              -----------------
   class Student:            s1 = Student("Priya", 20)
   (BLUEPRINT — no data)      (OBJECT — real data)

        📐                         🧑‍🎓 Priya, 20
                                    🧑‍🎓 Rahul, 22   ← s2
                                    🧑‍🎓 Kabir, 19    ← s3


         INSTANCE VARIABLE vs CLASS VARIABLE
         --------------------------------------
    ┌───────────────────────────────────────────┐
    │  class Student:                             │
    │      college_name = "ABC Institute"  🏫      │ ← CLASS variable (SHARED)
    │                                              │
    │      def __init__(self, name):               │
    │          self.name = name  🧑‍🎓                │ ← INSTANCE variable (UNIQUE per object)
    └───────────────────────────────────────────┘
       s1.college_name  ──┐
       s2.college_name  ──┼──►  SAME value: "ABC Institute"
       s3.college_name  ──┘

       s1.name = "Priya"   ┐
       s2.name = "Rahul"    ├──►  DIFFERENT for each object
       s3.name = "Kabir"   ┘


      "HAS-A" (Composition)              "IS-A" (Inheritance)
      -------------------------          -------------------------
      🏫 College                          👤 Person
        └── 🏢 Department                    ▲
              └── 🧑‍🎓 Student                 │  (inherits from)
                                          🧑‍🎓 Student   👨‍🏫 Teacher
      (College HAS Departments)          (Student IS-A Person)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "A class and an object are the same thing."
  ✅ **Correct:** A class is just a blueprint/template; an object is an actual instance created from that blueprint, with real data.

* ❌ **Wrong belief:** "You need to call `__init__()` manually to create an object."
  ✅ **Correct:** `__init__` runs **automatically** whenever you create an object using `ClassName(...)` — you never call it directly.

* ❌ **Wrong belief:** "Instance variables are shared between all objects of a class."
  ✅ **Correct:** Instance variables are unique to each object; only **class variables** are shared across all objects.

* ❌ **Wrong belief:** "Changing a class variable through one object (`s1.college_name = 'XYZ'`) updates it for every object."
  ✅ **Correct:** Doing this actually creates a new **instance** variable for that one object only — it does NOT change the shared class variable for others.

* ❌ **Wrong belief:** "Inheritance and composition (has-a) are the same thing."
  ✅ **Correct:** Inheritance models "is-a" relationships (Student is a Person), while composition models "has-a" relationships (Department has Students) — they solve different design problems.

* ❌ **Wrong belief:** "You must rewrite all the parent class's code inside the child class."
  ✅ **Correct:** Using `super().__init__(...)`, the child class can reuse the parent's existing setup logic without duplicating any code.

---

## 💬 Interview Corner

**Q1: What is the difference between a class and an object?**
✅ A class is a blueprint that defines properties and behaviors; an object is a concrete instance of that class with actual, real data stored in it.

**Q2: What is the purpose of the `self` keyword in a class?**
✅ `self` refers to the specific object that a method is being called on, allowing the method to access and modify that particular object's own instance variables.

**Q3: What is the difference between an instance variable and a class variable?**
✅ An instance variable is unique to each object (`self.variable`), while a class variable is shared across **all** objects of that class (`ClassName.variable`).

**Q4: What does the "is-a" relationship mean in the context of inheritance, and how is it different from "has-a"?**
✅ "Is-a" means a subclass is a specialized type of its parent class (e.g., `Student` is a `Person`) — implemented via inheritance. "Has-a" means one class contains or owns instances of another class (e.g., `Department` has `Students`) — implemented via composition (storing objects as attributes).

---

## 📝 Quick Summary

* 🏗️ A **class** is a blueprint; an **object** is a real instance created from it
* 🛠️ `__init__` is the constructor — it runs automatically when an object is created
* 🧑‍🎓 **Instance variables** (`self.variable`) are unique to each object
* ⚙️ **Instance methods** operate on a specific object's data and always take `self` as the first parameter
* 🏛️ **Class variables** are shared across ALL objects of a class, defined outside any method
* 🏫 **Inner classes** (or composition) model "has-a" relationships — e.g., College has Departments has Students
* 👨‍👩‍👧 **Inheritance** models "is-a" relationships — a child class reuses a parent class's code using `super()`
* 🔗 Composition ("has-a") and Inheritance ("is-a") solve different real-world modeling problems — know when to use which
* 🎯 OOP helps organize large, real-world software into clean, reusable, logically connected building blocks

---

## 🎯 Class Activity

**"Build a Mini College Management Model" 🏫**

1. Create a `Person` class with `name` and `age` as instance variables, and a method `display_info()`.
2. Create a `Student` class that **inherits** from `Person` (is-a relationship) and adds its own `roll_no` and `course` attributes, using `super()` correctly.
3. Add a **class variable** `Student.total_students` that increases by 1 every time a new `Student` object is created. Create 4 student objects and print the final count.
4. Create a `Department` class that **has** a list of `Student` objects (has-a relationship), with a method `show_students()` to display all students in that department.
5. Create a `College` class that **has** a list of `Department` objects, with a method `show_college_structure()` to display the full college → department → student hierarchy (like the example in this topic).
6. Bonus: Add a `Teacher` class that also inherits from `Person`, and add teachers to your `Department` object too.


---

# 📋 Assignments — Object-Oriented Programming (OOP) Concepts (Part 1)

| Assignment |
|---|
| Create a `Car` class with instance variables `brand`, `model`, and `year`. Create 3 different car objects and print their details. |
| Add an instance method `start_engine()` to the `Car` class that prints `"<brand> <model> engine started 🚗"`. |
| Create a `BankAccount` class with instance variables `account_holder` and `balance`. Add instance methods `deposit(amount)` and `withdraw(amount)` that correctly update the balance. |
| Add a class variable `bank_name = "State Bank"` to the `BankAccount` class and confirm it is the same across multiple account objects. |
| Add a class variable `total_accounts` to `BankAccount` that increases by 1 every time a new account object is created. Create 5 accounts and print the final count. |
| Create a `Book` class with `title`, `author`, and `price`. Create a list of 5 `Book` objects and write a loop to print all book titles. |
| Build the College → Department → Student structure shown in this topic, but for a different scenario: a `Hospital` containing `Department`s (like Cardiology, Neurology) containing `Doctor` objects. |
| Create a `Vehicle` parent class with `brand` and `speed`. Create `Car` and `Bike` child classes that inherit from `Vehicle` and each add one unique attribute of their own. |
| Create an `Animal` parent class with a method `make_sound()` that prints a generic sound. Create `Dog` and `Cat` child classes that inherit from `Animal` and override `make_sound()` with their own specific sound. |
| Create a `Person` class and a `Student` class (inheriting from `Person`) as shown in the topic. Then create a `GraduateStudent` class that inherits from `Student` (a 3-level inheritance chain) and add a `thesis_title` attribute. |
| Write a program that demonstrates the difference between changing an instance variable vs. accidentally creating a new one when trying to modify a class variable through an object. |
| Create an `Employee` class with `name` and `salary`. Add a class variable `company_name`. Create 3 employee objects and print each one's salary along with the shared company name. |
| Build a `School` class that contains a list of `Teacher` objects and a list of `Student` objects (has-a relationship), with a method to display counts of each. |
| Create a `Shape` base concept using classes: a `Rectangle` class with `length` and `width`, and add a method `area()` that returns length × width. Create 3 rectangle objects with different dimensions. |
| Write a short paragraph (in comments) explaining, in your own words, the difference between "is-a" and "has-a" relationships, using 2 original examples of your own (not from the notes). |
