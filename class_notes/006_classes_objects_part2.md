# 📚 OOP Advanced Concepts (Part 2)

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Understand Method Resolution Order (MRO) and how `super()` works in multi-level inheritance
* 🎯 Understand polymorphism in depth and implement method overriding correctly
* 🎯 Create and use abstract methods and abstract classes using Python's `abc` module
* 🎯 Understand and correctly use public, private, and protected class members
* 🎯 Make informed design decisions about when to use inheritance vs composition

---

## 📖 Introduction

In the previous OOP topic, you learned the fundamentals — classes, objects, inheritance, encapsulation basics. Now we go one level deeper 🔍. Real-world professional Python code uses some more advanced OOP tools to make programs safer, more flexible, and easier to maintain.

### 🤔 Why does this topic exist?

* 🧬 As inheritance chains grow longer (grandparent → parent → child classes), you need to understand exactly **which** method Python will actually run — this is MRO
* 🎭 Polymorphism becomes far more powerful once you understand **method overriding** properly
* 🚧 Sometimes you want to **force** every child class to implement certain methods — that's what abstract methods do
* 🔐 Real applications need proper data protection using public/private/protected access levels
* 🏗️ Every experienced developer eventually asks: "Should I use inheritance or composition here?" — this topic gives you the framework to decide

### 🤔 Where is it used?

* 🏦 Banking software — abstract `Account` class forces every account type (Savings, Current) to implement `calculate_interest()`
* 🎮 Game engines — method overriding lets different game characters have unique `attack()` behavior
* 📱 Framework design (like Django, Flask) — heavily relies on MRO and abstract base classes
* 🔒 Any secure system — public/private/protected members control what other developers can and cannot directly touch

> 💡 **Tip**
>
> These concepts are what separate "beginner OOP" from "professional OOP." They're commonly asked about in technical interviews too!

---

## 🧠 Detailed Notes

### 1️⃣ MRO (Method Resolution Order) and the `super()` Method

When a class inherits from multiple classes, or forms a long inheritance chain, Python needs a clear **order** to decide which class's method to actually run if multiple classes define a method with the same name. This order is called the **Method Resolution Order (MRO)**.

```python
class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):     # D inherits from BOTH B and C
    pass

d = D()
d.show()             # Which show() runs? Let's check the MRO!

print(D.mro())       # shows the exact order Python searches in
```

Output:
```
B's show method
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

Python uses an algorithm called **C3 Linearization** to compute MRO — but as a beginner, the key takeaway is: **Python searches left to right, depth-first, but never checks a parent before all its children have been checked.** You can always check the exact order using `ClassName.mro()` or `ClassName.__mro__`.

**`super()` in a multi-level inheritance chain:**

```python
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)          # calls Person's __init__
        self.course = course
        print("Student constructor called")

class GraduateStudent(Student):
    def __init__(self, name, course, thesis):
        super().__init__(name, course)   # calls Student's __init__
        self.thesis = thesis
        print("GraduateStudent constructor called")

g1 = GraduateStudent("Ananya", "MSc CS", "AI in Healthcare")
```

Output:
```
Person constructor called
Student constructor called
GraduateStudent constructor called
```

`super()` always calls the **next** class in the MRO chain — not necessarily the "immediate parent" in complicated multi-inheritance cases, but for simple single-parent chains (like above), it behaves exactly like calling the parent directly.

| Concept | Meaning |
|---|---|
| MRO | The specific order Python follows to search for a method across a class's inheritance chain |
| `ClassName.mro()` | Lets you see the exact MRO order for any class |
| `super()` | Calls the next class's version of a method, following the MRO — commonly used to call the parent's constructor |

> ⚠️ **Important**
>
> MRO becomes especially important with **multiple inheritance** (a class inheriting from more than one class at once) — a feature Python supports but many other languages (like Java) don't allow directly.

🤔 **Quick thinking question:** In the `D(B, C)` example above, why did `B`'s `show()` run instead of `C`'s, even though both `B` and `C` inherit from `A`?
✅ **Answer:** Because `D(B, C)` lists `B` before `C`, Python's MRO checks `B` first — since `B` has its own `show()` method, that version is used before Python even looks at `C`.

---

### 2️⃣ Polymorphism & Method Overriding

**Polymorphism** means "many forms" — the same method name can behave differently depending on which object calls it. **Method overriding** is the specific technique of a child class providing its **own version** of a method that already exists in its parent class.

```python
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):              # OVERRIDING the parent's method
        print("Woof! 🐕")

class Cat(Animal):
    def make_sound(self):              # OVERRIDING the parent's method
        print("Meow! 🐈")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()      # each object calls ITS OWN version — this is polymorphism in action
```

Output:
```
Woof! 🐕
Meow! 🐈
Some generic animal sound
```

**Calling the parent's version too, using `super()`, inside an overridden method:**

```python
class Employee:
    def calculate_salary(self):
        print("Calculating base salary...")
        return 30000

class Manager(Employee):
    def calculate_salary(self):
        base = super().calculate_salary()     # reuse parent's logic first
        bonus = 5000
        print("Adding manager bonus...")
        return base + bonus

m1 = Manager()
print(m1.calculate_salary())    # 35000
```

**Method Overloading vs Method Overriding — a common point of confusion:**

| Concept | Meaning | Supported in Python? |
|---|---|---|
| Method Overriding | Child class redefines a method that already exists in the parent, with the SAME name | ✅ Yes — fully supported |
| Method Overloading (traditional, like in Java/C++) | Same method name with different parameter combinations | ❌ Not directly — Python allows only ONE version of a method with a given name (later definitions overwrite earlier ones); default parameters or `*args` are used instead |

```python
# Python does NOT support traditional method overloading:
class Demo:
    def greet(self):
        print("Hello!")

    def greet(self, name):        # this OVERWRITES the previous greet(), doesn't "overload" it
        print(f"Hello, {name}!")

d = Demo()
d.greet("Priya")     # works
# d.greet()          # ❌ TypeError — the no-argument version no longer exists!
```

> 💡 **Tip**
>
> In Python, if you want "overloading-like" flexibility, use **default parameter values** or `*args`/`**kwargs` instead of defining multiple methods with the same name.

🤔 **Quick thinking question:** What is the key difference between method overriding and method overloading?
✅ **Answer:** Overriding happens **across** a parent-child relationship (child redefines parent's method); overloading (in languages that support it) happens **within the same class**, having multiple versions of a method with different parameters — Python doesn't support true overloading.

---

### 3️⃣ Abstract Methods (Using the `abc` Module)

Sometimes you want to design a **base class** that defines *what* methods every child class MUST implement, without providing the actual implementation itself. This is done using **Abstract Base Classes (ABC)** from Python's built-in `abc` module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):                     # inherits from ABC — makes this an abstract class
    @abstractmethod
    def area(self):                    # abstract method — NO implementation here, just a rule
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):                     # MUST implement this, or Python will raise an error
        return self.length * self.width

    def perimeter(self):                 # MUST implement this too
        return 2 * (self.length + self.width)

r1 = Rectangle(5, 3)
print(r1.area())          # 15
print(r1.perimeter())      # 16

# s1 = Shape()   ❌ TypeError — Can't instantiate an abstract class directly!
```

**What happens if a child class forgets to implement an abstract method:**

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    # perimeter() is MISSING!

c1 = Circle(5)   # ❌ TypeError: Can't instantiate abstract class Circle with abstract method perimeter
```

| Concept | Meaning |
|---|---|
| Abstract class | A class that cannot be directly instantiated; meant only to be inherited from |
| `@abstractmethod` | A decorator marking a method that MUST be implemented by any child class |
| Purpose | Enforces a consistent structure/contract across all child classes |

> ⚠️ **Important**
>
> You cannot create an object directly from an abstract class (`Shape()` will fail). Abstract classes exist purely to be **inherited** from, forcing consistency across all their child classes.

🤔 **Quick thinking question:** Why would a developer deliberately design `Shape` as an abstract class instead of just letting `area()` and `perimeter()` have default (possibly wrong) implementations in the parent?
✅ **Answer:** Because every shape (Rectangle, Circle, Triangle) calculates area and perimeter completely differently — there's no sensible "default" implementation, so forcing each child class to provide its OWN correct version (via abstract methods) prevents bugs from an incorrect default being accidentally used.

---

### 4️⃣ Public, Private, and Protected Members

Python uses **naming conventions** (not strict enforced rules like Java) to indicate how "accessible" a class member (variable or method) should be from outside the class.

```python
class BankAccount:
    def __init__(self, holder, balance, pin):
        self.holder = holder            # PUBLIC — accessible from anywhere
        self._balance = balance           # PROTECTED — accessible, but signals "internal use, be careful"
        self.__pin = pin                   # PRIVATE — name-mangled, hard to access from outside

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return f"Balance: ₹{self._balance}"
        return "❌ Incorrect PIN"

acc = BankAccount("Priya", 50000, 1234)

print(acc.holder)              # ✅ Priya — public, freely accessible
print(acc._balance)             # ⚠️ 50000 — works, but you're NOT supposed to touch this directly
print(acc.check_balance(1234))   # ✅ Balance: ₹50000 — correct, controlled access

# print(acc.__pin)             # ❌ AttributeError — private, cannot access directly like this
print(acc._BankAccount__pin)     # 1234 — accessible ONLY via "name mangling" trick (not recommended!)
```

| Access Level | Syntax | Convention Meaning | Actually Enforced by Python? |
|---|---|---|---|
| Public | `self.variable` | Freely accessible from anywhere | N/A — always accessible |
| Protected | `self._variable` | "Internal use — don't touch from outside unless you know what you're doing" | ❌ Not enforced, just a convention (single underscore) |
| Private | `self.__variable` | "Strongly discourage outside access" | ⚠️ Partially enforced via **name mangling** (double underscore) |

**What is "name mangling"?**

When you write `self.__pin`, Python internally renames it to `self._ClassName__pin` — this makes accidental access harder (but not impossible, as shown above), mainly to prevent naming conflicts in inheritance.

```python
class Parent:
    def __init__(self):
        self.__secret = "Parent's secret"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__secret = "Child's secret"     # this does NOT overwrite Parent's __secret!

c = Child()
print(c._Parent__secret)    # Parent's secret
print(c._Child__secret)      # Child's secret
```

> 💡 **Tip**
>
> Python's philosophy is often summarized as **"we're all consenting adults here"** — private variables are a strong *hint* not to touch them directly, not an unbreakable lock. Real professional teams still respect these conventions strictly, even though Python allows working around them.

🤔 **Quick thinking question:** Why is a single underscore (`_balance`) called "protected" while a double underscore (`__pin`) is called "private," even though Python doesn't strictly block access to either?
✅ **Answer:** It's purely a **naming convention** difference in strength: single underscore is a soft warning ("internal, but accessible if truly needed"), while double underscore triggers actual name-mangling, making accidental access significantly harder and clearly signaling "do not touch this from outside."

---

### 5️⃣ Basic Design Discussion: When to Use Inheritance vs Composition

Both inheritance ("is-a") and composition ("has-a") let you reuse code and organize objects — but choosing the wrong one for a situation leads to confusing, hard-to-maintain code.

**Use INHERITANCE when:**
* ✅ There's a genuine "is-a" relationship (`Dog` **is an** `Animal`, `Manager` **is an** `Employee`)
* ✅ The child class needs to reuse AND potentially override the parent's behavior
* ✅ The relationship is unlikely to need to change at runtime

**Use COMPOSITION when:**
* ✅ There's a "has-a" relationship (`Car` **has an** `Engine`, `Department` **has** `Doctors`)
* ✅ You want more flexibility — swap out one component for another easily
* ✅ You want to avoid deep, fragile inheritance chains

```python
# ❌ Poor design — using inheritance for a "has-a" relationship
class Engine:
    def start(self):
        print("Engine starting...")

class Car(Engine):        # WRONG — a Car is NOT a type of Engine!
    pass


# ✅ Good design — using composition for a "has-a" relationship
class Engine:
    def start(self):
        print("Engine starting... 🔧")

class Car:
    def __init__(self):
        self.engine = Engine()      # Car HAS an Engine

    def start_car(self):
        self.engine.start()
        print("Car is now running! 🚗")

c1 = Car()
c1.start_car()
```

Output:
```
Engine starting... 🔧
Car is now running! 🚗
```

**A famous design principle:** *"Favor composition over inheritance"* — many experienced developers prefer composition by default because it's more flexible, and only reach for inheritance when there's a clear, genuine is-a relationship.

| Question to Ask Yourself | If "Yes" → Likely Choice |
|---|---|
| Is X truly a specialized type of Y? | Inheritance |
| Does X simply use/contain/own Y as a component? | Composition |
| Might I need to swap out this component later (e.g., different engine types)? | Composition |
| Do I want the child to inherit AND be able to override shared behavior? | Inheritance |

> ⚠️ **Important**
>
> A common beginner mistake is using inheritance just to "reuse some code," even when there's no real is-a relationship. This leads to confusing hierarchies (e.g., `Car(Engine)`) that don't reflect reality and become hard to maintain as the project grows.

🤔 **Quick thinking question:** Why is `class Car(Engine)` considered bad design, even though it technically lets `Car` reuse `Engine`'s `start()` method?
✅ **Answer:** Because a Car is not a specialized type of Engine — it simply **contains** an engine as one of its parts. Using inheritance here misrepresents the real-world relationship and would confuse other developers reading the code.

---

## 💡 Real-Life Analogy

* 🧬 **MRO → Following a Family Tree for a Surname Dispute** — If both your father's side and mother's side have a family recipe with the same name, MRO is like the agreed-upon family rule for whose recipe you follow first when there's a conflict.
* 🎭 **Polymorphism & Overriding → Ordering "The Special" at Different Restaurants** — Asking for "today's special" gives you a completely different dish depending on which restaurant (object) you're at, even though the request (method call) is identical.
* 📜 **Abstract Methods → A Franchise Agreement** — A pizza franchise headquarters (abstract class) requires every franchise branch (child class) to have a "made_pizza()" process — but HOW exactly they make it is up to each branch, as long as they provide their own version.
* 🔐 **Public/Private/Protected → Levels of Access in a Company** — Public info is on the company website (anyone can see), protected info is in internal memos (employees can see, outsiders shouldn't), and private info is in the CEO's locked personal drawer (heavily restricted, though a master key technically exists).
* 🏗️ **Inheritance vs Composition → Building a House vs Buying Furniture** — Inheritance is like saying "this new house design **is a type of** the original house blueprint." Composition is like saying "this house **contains** furniture that could be swapped out anytime" — the furniture isn't a "type of" house.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| MRO & `super()` | Django (web framework) — heavily relies on multiple inheritance and MRO for its class-based views |
| Method Overriding | Game engines (Unity via C#, or Python-based games) — different enemy types override a shared `attack()` method |
| Abstract Methods | Payment gateway SDKs (Razorpay, Stripe) — abstract `PaymentMethod` class forcing `CreditCard`, `UPI`, `NetBanking` to each implement `process_payment()` |
| Public/Private/Protected | Banking and fintech apps — account balances and transaction PINs are always protected/private in real systems |
| Inheritance vs Composition | Modern app architecture (e.g., React components) — favors composition (building UI from small reusable pieces) over deep inheritance chains |

---

## 🔍 Industry Example

**Scenario:** A team at a **fintech startup** is designing their payment processing system.

1. They create an **abstract base class** `PaymentMethod` using the `abc` module, with an abstract method `process_payment(amount)` — ensuring every payment type (Credit Card, UPI, Net Banking) MUST implement this method.
2. Each specific payment class (`CreditCardPayment`, `UPIPayment`) **overrides** `process_payment()` with its own logic — this is **polymorphism**, allowing the checkout system to call `.process_payment()` on any payment object without caring which type it is.
3. Sensitive data like card numbers and CVVs are stored as **private** members (`self.__card_number`), only accessible through carefully controlled, secure methods.
4. Their `Wallet` class **composes** a `TransactionHistory` object (has-a) rather than inheriting from it — since a Wallet is not "a type of" transaction history, it simply owns/uses one.
5. When their system grows to have multiple inheritance for shared "Loggable" and "Auditable" behaviors across classes, the team carefully checks the **MRO** using `ClassName.mro()` to make sure the correct logging/auditing method actually gets called in complex cases.

This exact combination of abstract classes, polymorphism, encapsulation, and careful inheritance-vs-composition decisions is standard practice in real, production-grade Python systems.

---

## 📊 Diagram

```
              MRO IN MULTIPLE INHERITANCE
              -----------------------------
                        A
                       ▲ ▲
                      /   \
                     B     C
                      ▲   ▲
                       \ /
                        D

     D.mro() → [D, B, C, A, object]
     (Python checks D first, then B, then C, then A)


         ABSTRACT CLASS ENFORCEMENT
         -----------------------------
     Shape (ABC)  🚫 cannot create Shape() directly
      ├── area()        (@abstractmethod — no body)
      └── perimeter()   (@abstractmethod — no body)
           │
           ▼ (must implement BOTH, or error!)
     Rectangle(Shape)  ✅ implements area() & perimeter()
     Circle(Shape)     ✅ implements area() & perimeter()


        ACCESS LEVEL VISIBILITY
        --------------------------
     ┌─────────────────────────────────────┐
     │  PUBLIC     self.name        🌍 open  │
     │  PROTECTED  self._balance     ⚠️ caution│
     │  PRIVATE    self.__pin         🔒 locked│
     └─────────────────────────────────────┘


      INHERITANCE (is-a)         COMPOSITION (has-a)
      -----------------------    -----------------------
        🐾 Animal                     🚗 Car
          ▲                            │ contains
          │                            ▼
        🐕 Dog                      🔧 Engine
      (Dog IS-A Animal)          (Car HAS-A Engine)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "`super()` always calls the direct parent class, no matter what."
  ✅ **Correct:** `super()` calls the **next class in the MRO chain**, which is usually the direct parent in simple single-inheritance cases, but can be different in complex multiple-inheritance situations.

* ❌ **Wrong belief:** "Python supports traditional method overloading like Java, where you define multiple methods with the same name but different parameters."
  ✅ **Correct:** Python does NOT support true method overloading — defining a method with the same name twice simply overwrites the earlier one. Use default parameters or `*args` instead.

* ❌ **Wrong belief:** "You can create an object directly from an abstract class as long as you don't call its abstract methods."
  ✅ **Correct:** Python will raise a `TypeError` immediately upon trying to instantiate any class that has unimplemented abstract methods — you cannot create the object at all.

* ❌ **Wrong belief:** "Private variables (`__variable`) in Python are completely impossible to access from outside the class."
  ✅ **Correct:** They are only "name-mangled" (renamed internally to `_ClassName__variable`), making accidental access harder — but technically still possible if someone deliberately looks for it.

* ❌ **Wrong belief:** "Inheritance is always the better choice for code reuse."
  ✅ **Correct:** Composition is often the more flexible, maintainable choice unless there's a genuine "is-a" relationship — "favor composition over inheritance" is a widely respected design principle.

---

## 💬 Interview Corner

**Q1: What is MRO in Python, and how can you check it?**
✅ MRO (Method Resolution Order) is the specific order Python follows to search through a class's inheritance hierarchy when looking for a method or attribute. You can check it using `ClassName.mro()` or `ClassName.__mro__`.

**Q2: What is the difference between method overriding and method overloading, and does Python support both?**
✅ Overriding is when a child class redefines a parent class's method — Python fully supports this. Overloading (multiple methods with the same name but different parameters) is NOT truly supported in Python; the last-defined version simply replaces earlier ones.

**Q3: What is an abstract method, and why would you use one?**
✅ An abstract method (defined using `@abstractmethod` from the `abc` module) is a method declared in a base class with no implementation, forcing every child class to provide its own implementation — ensuring consistency across all subclasses.

**Q4: How does Python implement private variables, and are they truly private?**
✅ Python uses "name mangling" — a variable like `self.__pin` is internally renamed to `self._ClassName__pin`. This isn't truly private (it can still be accessed if you know the mangled name), but it strongly discourages accidental outside access.

---

## 📝 Quick Summary

* 🧬 MRO determines the exact order Python searches through an inheritance chain to find a method — check it with `ClassName.mro()`
* 🔗 `super()` calls the next class in the MRO, most commonly used to reuse a parent class's constructor or method
* 🎭 Polymorphism lets the same method call behave differently depending on the object's actual class
* ✏️ Method overriding = child redefines parent's method (supported); method overloading = same method, different parameters (NOT truly supported in Python)
* 🚧 Abstract methods (via the `abc` module) force every child class to implement specific methods, enforcing consistency
* 🚫 You cannot create an object directly from a class containing unimplemented abstract methods
* 🌍 Public members (`self.var`) are freely accessible; 🔶 protected (`self._var`) is a soft warning; 🔒 private (`self.__var`) uses name-mangling for stronger protection
* 🏗️ Use inheritance for genuine "is-a" relationships; use composition for "has-a" relationships and greater flexibility
* 🎯 "Favor composition over inheritance" is a widely respected professional design principle

---

## 🎯 Class Activity

**"Design and Defend Your Class Structure" 🏗️**

1. Create an abstract class `PaymentMethod` using the `abc` module, with an abstract method `process_payment(amount)`. Create at least two child classes (`CreditCardPayment`, `UPIPayment`) that implement it differently.
2. Create a small 3-level inheritance chain (`A → B → C`) where each class overrides a shared method, and use `super()` in each `__init__` to properly chain constructor calls. Print `C.mro()` and explain the order out loud to a classmate.
3. Build a `BankAccount` class with a public `holder_name`, a protected `_balance`, and a private `__pin`. Write a method that safely checks the pin before revealing the balance.
4. Take the earlier `Car`/`Engine` example and intentionally design it the "wrong way" (inheritance) first, then refactor it to use composition correctly — write a one-line comment explaining why the composition version is better design.
5. Bonus: Try creating a class with multiple inheritance (two parent classes each having a method with the same name) and predict — before running the code — which version will execute, then verify using `.mro()`.
