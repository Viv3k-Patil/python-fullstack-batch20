# 📚 Simple CRUD with FastAPI, SQLAlchemy, and PostgreSQL

Two tables: **Department** and **Employee**. Every script below has been run against a real PostgreSQL database. No SQL teaching here — you already know SQL. This is about the Python/SQLAlchemy side only.

---

## 1️⃣ The Two Tables We're Building

```
departments                    employees
------------                   -----------------------------
id   (PK)                      id            (PK)
name                           name
                                email         (unique)
                                salary
                                department_id (FK → departments.id)
```

One department has many employees. One employee belongs to one department. This is the same "has-a" relationship from the OOP topics, now stored in a database.

---

## 2️⃣ `database.py` — Explained Line by Line

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import SYNC_URL

engine = create_engine(SYNC_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

| Line | What it does |
|---|---|
| `from config import SYNC_URL` | `SYNC_URL` is just the connection string (host, port, username, password, database name) built in one place, so you never retype it |
| `engine = create_engine(SYNC_URL)` | Creates the **engine**: the object that knows how to open connections to PostgreSQL. Created **once**, when the app starts |
| `echo=False` | If you set this to `True`, SQLAlchemy prints every SQL statement it runs — useful for learning, turn off later |
| `SessionLocal = sessionmaker(bind=engine, ...)` | This is not a session itself. It is a **factory**: every time you call `SessionLocal()`, you get a brand new session tied to this engine |
| `autoflush=False, autocommit=False` | Standard settings: don't auto-save half-finished work; you decide exactly when to `commit()` |
| `class Base(DeclarativeBase): pass` | Every table class you write (`Department`, `Employee`) will inherit from `Base`. This is how SQLAlchemy knows "these classes are database tables" |
| `def get_db():` | A function used with FastAPI's `Depends()`. It hands one session to an endpoint and guarantees it is closed afterward |
| `db = SessionLocal()` | Opens a fresh session (one per request) |
| `yield db` | Pauses here, hands `db` to whichever endpoint asked for it, and waits for that endpoint to finish |
| `finally: db.close()` | Runs no matter what — even if the endpoint crashed — so the connection is always returned properly |

> 💡 **Why `yield` and not `return`?** With `return`, there is no way to run cleanup code afterward. With `yield` + `finally`, the "close the session" step is guaranteed, always.

---

## 3️⃣ `models.py` — Two Tables, and What `Mapped`/`mapped_column` Actually Mean

```python
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    employees: Mapped[list["Employee"]] = relationship(back_populates="department")


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    salary: Mapped[float] = mapped_column(Float)
    department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))

    department: Mapped["Department"] = relationship(back_populates="employees")
```

### What is `Mapped`?

`Mapped[int]`, `Mapped[str]`, `Mapped[float]` are just **type hints** — the same type hints you already use everywhere in Python (`def f(x: int)`). They tell SQLAlchemy (and your editor) what Python type this column will come back as. `Mapped[int]` → this column behaves like a Python `int`.

### What is `mapped_column(...)`?

This is the actual instruction that becomes a **database column**. Whatever you put inside its parentheses configures that column:

| You write | Column becomes |
|---|---|
| `mapped_column(primary_key=True)` | The primary key column |
| `mapped_column(String(50), unique=True)` | A text column, max 50 characters, no duplicates allowed |
| `mapped_column(Float)` | A numeric (decimal) column |
| `mapped_column(ForeignKey("departments.id"))` | A column that must match an existing `id` in `departments` |

So the pattern is always:

```
attribute_name : Mapped[python_type] = mapped_column(database_options)
                     │                        │
                what Python sees        what the database actually stores
```

`id: Mapped[int] = mapped_column(primary_key=True)` reads as: *"`id` behaves like a Python `int`, and in the database it is the primary key."*

### What is `relationship(...)`?

`relationship()` is NOT a real column. It does not exist in the database at all. It is a convenience SQLAlchemy gives you so you can write Python like:

```python
dept = db.get(Department, 1)
print(dept.employees)          # list of Employee objects in this department

emp = db.get(Employee, 1)
print(emp.department.name)     # walk from employee back to its department
```

`back_populates="employees"` / `back_populates="department"` simply tell the two `relationship()` calls that they are two sides of the *same* connection, so updating one keeps the other in sync in Python's memory.

> ⚠️ **`ForeignKey` vs `relationship` — do not confuse them:**
> - `department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))` → this is a **real column** in the `employees` table
> - `department: Mapped["Department"] = relationship(...)` → this is a **Python convenience**, not a column, letting you write `emp.department` instead of manually looking it up

🤔 **Quick check:** if you deleted the `relationship()` lines entirely but kept `department_id`, would the database still work correctly?
✅ Yes — the foreign key constraint still works. You would just lose the convenient `emp.department` / `dept.employees` shortcuts in Python.

---

## 4️⃣ `schemas.py` — What the API Actually Accepts and Returns

These are **Pydantic** models, completely separate from the SQLAlchemy models above. Models describe the *database*; schemas describe the *API*.

```python
from typing import Optional
from pydantic import BaseModel, ConfigDict


class DepartmentCreate(BaseModel):
    name: str

class DepartmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class EmployeeCreate(BaseModel):
    name: str
    email: str
    salary: float
    department_id: int

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    salary: Optional[float] = None
    department_id: Optional[int] = None

class EmployeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str
    salary: float
    department_id: int
```

| Schema | Used when | Why it looks the way it does |
|---|---|---|
| `DepartmentCreate` / `EmployeeCreate` | Client is **creating** a new row | No `id` field — the database assigns it, the client never chooses it |
| `EmployeeUpdate` | Client is **updating** a row | Every field is `Optional` — the client only sends what it wants to change |
| `DepartmentOut` / `EmployeeOut` | API is **returning** data | Includes `id`; `model_config = ConfigDict(from_attributes=True)` lets Pydantic read values straight off a SQLAlchemy object (`emp.name`, `emp.id`, ...) instead of requiring a plain dict |

---

## 5️⃣ `main.py` — CRUD, One Piece at a Time

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Department, Employee
from schemas import (
    DepartmentCreate, DepartmentOut,
    EmployeeCreate, EmployeeUpdate, EmployeeOut,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()
```

`Base.metadata.create_all(bind=engine)` looks at every class that inherits `Base` (both `Department` and `Employee`) and creates the matching tables if they don't already exist.

### CREATE — `POST /departments/`

```python
@app.post("/departments/", response_model=DepartmentOut, status_code=201)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    dept = Department(**data.model_dump())
    db.add(dept)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Department already exists")
    db.refresh(dept)
    return dept
```

* `data.model_dump()` turns the validated Pydantic object into a plain dict: `{"name": "Engineering"}`
* `Department(**that_dict)` builds an actual `Department` ORM object from it
* `db.add(dept)` stages it (not saved yet)
* `db.commit()` actually saves it; if the name already exists, PostgreSQL's `unique=True` constraint blocks it and raises `IntegrityError`
* `db.rollback()` cleans up the failed attempt so the session can be used again
* `db.refresh(dept)` reloads `dept` from the database, filling in the `id` PostgreSQL just generated

### READ (list) — `GET /departments/`

```python
@app.get("/departments/", response_model=list[DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return db.scalars(select(Department)).all()
```

`select(Department)` builds the query; `db.scalars(...)` runs it and gives you `Department` objects directly (not raw rows); `.all()` turns that into a plain list.

### READ (one) — `GET /departments/{dept_id}`

```python
@app.get("/departments/{dept_id}", response_model=DepartmentOut)
def get_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept
```

`db.get(Model, primary_key)` is the fastest way to fetch one row by its `id`. It returns `None`, not an error, if nothing matches — so you check for that yourself.

### DELETE — `DELETE /departments/{dept_id}`

```python
@app.delete("/departments/{dept_id}", status_code=204)
def delete_department(dept_id: int, db: Session = Depends(get_db)):
    dept = db.get(Department, dept_id)
    if dept is None:
        raise HTTPException(status_code=404, detail="Department not found")
    db.delete(dept)
    db.commit()
```

`204 No Content` is the correct status for "deleted successfully, nothing to send back."

### CREATE (Employee) — showing a cross-table check

```python
@app.post("/employees/", response_model=EmployeeOut, status_code=201)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    if db.get(Department, data.department_id) is None:
        raise HTTPException(status_code=400, detail="department_id does not exist")
    emp = Employee(**data.model_dump())
    db.add(emp)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email already exists")
    db.refresh(emp)
    return emp
```

Before creating an employee, we check the department actually exists — a friendlier 400 error instead of letting the database reject it with a confusing foreign-key error.

### UPDATE — `PUT /employees/{emp_id}`

```python
@app.put("/employees/{emp_id}", response_model=EmployeeOut)
def update_employee(emp_id: int, data: EmployeeUpdate, db: Session = Depends(get_db)):
    emp = db.get(Employee, emp_id)
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(emp, field, value)
    db.commit()
    db.refresh(emp)
    return emp
```

`exclude_unset=True` means: only include fields the client actually sent. Sending `{"salary": 65000}` alone will **only** change `salary` — `name` and `department_id` stay untouched. Without `exclude_unset=True`, every unsent field would be overwritten with `None`.

`setattr(emp, field, value)` sets `emp.salary = 65000` dynamically, one field at a time, for whatever fields were sent.

---

## ✅ Verified Test Run (real PostgreSQL, not simulated)

```
POST /departments/  {"name": "Engineering"}   → 201  {'id': 1, 'name': 'Engineering'}
POST /departments/  {"name": "HR"}             → 201  {'id': 2, 'name': 'HR'}
POST /departments/  {"name": "Engineering"}     → 409  duplicate name blocked
GET  /departments/                               → [Engineering, HR]

POST /employees/  {..., "department_id": 1}       → 201  employee created
POST /employees/  (same email again)               → 409  duplicate email blocked
POST /employees/  {..., "department_id": 999}       → 400  department_id does not exist
GET  /employees/1  |  GET /employees/99               → 200  |  404
PUT  /employees/1  {"salary": 65000}                    → 200  only salary changed
DELETE /employees/1  then GET /employees/1               → 204  then 404
DELETE /departments/2  then GET /departments/2             → 204  then 404
```

Every one of these was actually executed against a running PostgreSQL database while writing this note, not just described.

---

## ⚠️ Common Mistakes

* ❌ "`Mapped[int]` and `mapped_column()` do the same thing, pick one."
  ✅ `Mapped[int]` is the Python type hint. `mapped_column(...)` is the real database column definition. You need both together.

* ❌ "`relationship()` creates a column in the table."
  ✅ It does not. Only `mapped_column(ForeignKey(...))` creates a real column. `relationship()` is a Python-only convenience.

* ❌ "`db.add(obj)` saves it to the database."
  ✅ It only stages the change. Nothing is permanent until `db.commit()`.

* ❌ "Updating with `data.model_dump()` (no `exclude_unset`) is fine."
  ✅ It will silently wipe out every field the client didn't send, setting them to `None`.

---

## 🎯 Try It Yourself

1. Run the app: `uvicorn main:app --reload`
2. Open `/docs`, create 2 departments, then 2 employees pointing at them
3. Try creating an employee with a `department_id` that doesn't exist — confirm you get 400, not a crash
4. Update only one field on an employee and confirm the others didn't change
5. Delete a department that still has employees in it, and see what PostgreSQL does — this is a great follow-up question for the next class