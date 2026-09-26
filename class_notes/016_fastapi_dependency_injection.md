# 📚 FastAPI Dependency Injection

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Explain what dependency injection is and why FastAPI is built around it
* 🎯 Use `Depends()` to share logic across multiple endpoints
* 🎯 Build a reusable database-session dependency using `yield`
* 🎯 Build a reusable authentication dependency
* 🎯 Build a configurable, class-based dependency for role-based checks

---

## 📖 Introduction

Every API you build will have SOME logic that many different endpoints need: connecting to a database, checking who's logged in, applying pagination. Without a proper mechanism for this, you end up copy-pasting the same setup code into every single endpoint function.

FastAPI's answer to this is **Dependency Injection (DI)** — a way for an endpoint to simply DECLARE what it needs, and let FastAPI supply it automatically.

### 🤔 Why does this topic exist?

* 🔁 Almost every real endpoint needs SOMETHING shared — a DB connection, the current user, common query parameters
* 🧹 Without DI, that shared logic gets duplicated everywhere, and any change means editing every single endpoint
* 🏗️ Dependency injection is the single feature that most shapes how real FastAPI applications are structured

### 🤔 Where is it used?

* 🗄️ Database-backed APIs — a `get_db()` dependency hands a fresh connection to any endpoint that needs one
* 🔐 Authentication — a `get_current_user()` dependency checks login status before allowing access
* 📄 Pagination/filtering — shared query-parameter logic reused across many "list" endpoints

> 💡 **Tip**
>
> If this reminds you of the `@requires_permission` decorator from the earlier RBAC project — good instinct. Both solve the same problem (avoiding repeated logic), just using a mechanism native to each framework.

---

## 🧠 Detailed Notes

### 1️⃣ Understanding Dependency Injection in FastAPI

**Dependency Injection** means: instead of a function creating what it needs internally, that "what it needs" is supplied from outside.

```python
# WITHOUT dependency injection — the endpoint builds everything itself
@app.get("/users/{user_id}")
def get_user(user_id: int):
    db = connect_to_database()      # tightly coupled to ONE specific setup
    user = db.query_user(user_id)
    db.close()
    return user


# WITH dependency injection — the endpoint just DECLARES what it needs
@app.get("/users/{user_id}")
def get_user(user_id: int, db=Depends(get_db)):
    return db.query_user(user_id)
```

`Depends()` tells FastAPI: "before running this endpoint, call `get_db()` first, and pass its result in as `db`."

**A simple reusable dependency — shared pagination logic:**

```python
from fastapi import FastAPI, Depends

app = FastAPI()

def pagination_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/users/")
def list_users(pagination: dict = Depends(pagination_params)):
    return {"pagination": pagination, "users": ["Priya", "Rahul"]}

@app.get("/products/")
def list_products(pagination: dict = Depends(pagination_params)):
    return {"pagination": pagination, "products": ["Laptop", "Mouse"]}
```

Both endpoints share the EXACT SAME pagination logic — write it once, reuse it everywhere.

```
             HOW Depends() WORKS
             -----------------------
   Request arrives
        │
        ▼
   FastAPI sees `Depends(pagination_params)`
        │
        ▼
   Calls pagination_params() FIRST
        │
        ▼
   Result injected into list_users(pagination=...)
        │
        ▼
   Your endpoint function runs, using the injected value
```

| Without Dependency Injection | With `Depends()` |
|---|---|
| Every endpoint repeats the same setup code | Setup logic written once, reused everywhere |
| Changes to shared logic mean editing every endpoint | Changes happen in ONE place |
| Harder to keep behavior consistent across endpoints | Every endpoint using the dependency behaves identically |

> ⚠️ **Important**
>
> A dependency can be ANY callable — a plain function, a generator function, or even a class — FastAPI figures out how to call it correctly based on what it is.

🤔 **Quick thinking question:** If `list_users()` and `list_products()` each wrote their OWN pagination-handling code instead of sharing `pagination_params()`, what happens if the team later decides to cap `limit` at 100?
✅ **Answer:** Every endpoint that duplicated the pagination logic would need to be found and edited individually — with a shared dependency, the cap is added ONCE inside `pagination_params()`, and every endpoint using it is automatically updated.

---

### 2️⃣ Creating Reusable Dependencies (DB Session, Auth Stub, etc.)

**A database session dependency, using `yield`** — this is the standard FastAPI pattern for anything that needs setup AND guaranteed cleanup.

```python
class FakeDBSession:
    def __init__(self):
        print("🔌 DB session opened")

    def close(self):
        print("🔒 DB session closed")

    def get_user(self, user_id: int):
        return {"id": user_id, "name": "Priya"}


def get_db():
    db = FakeDBSession()
    try:
        yield db          # this is a GENERATOR dependency — connects back to the generators topic!
    finally:
        db.close()          # guaranteed to run after the request finishes, even if an error occurred


@app.get("/users/{user_id}")
def read_user(user_id: int, db: FakeDBSession = Depends(get_db)):
    return db.get_user(user_id)
```

Code BEFORE `yield` runs at the START of the request; code AFTER `yield` (inside `finally`) runs at the END — guaranteeing the connection is always closed, even if the endpoint raises an error.

```
       GENERATOR DEPENDENCY LIFECYCLE
       ---------------------------------
   Request starts
        │
        ▼
   get_db() runs up to yield  →  "🔌 DB session opened"
        │
        ▼
   db object injected into the endpoint
        │
        ▼
   Endpoint function runs
        │
        ▼
   Request finishes (success OR error)
        │
        ▼
   get_db() resumes after yield  →  "🔒 DB session closed"
```

**An authentication "stub" dependency** — checking whether a user is logged in, without building a full login system yet:

```python
from fastapi import Header, HTTPException

def get_current_user(authorization: str = Header(None)):
    if authorization != "Bearer secret-token-123":     # a STUB — a real app verifies a proper token
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"username": "priya", "role": "admin"}


@app.get("/profile")
def read_profile(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user['username']}!"}
```

Any request to `/profile` without the correct header is automatically rejected — BEFORE `read_profile()`'s own code even runs.

**A class-based dependency, for when the check itself needs configuration:**

```python
class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user


admin_only = RoleChecker(allowed_roles=["admin"])

@app.get("/admin-dashboard")
def admin_dashboard(user: dict = Depends(admin_only)):
    return {"message": f"Welcome to the admin dashboard, {user['username']}!"}
```

This mirrors the `@requires_permission(action)` decorator factory from the earlier RBAC project — same underlying idea (a configurable, reusable check), implemented FastAPI's way.

| Dependency Type | Example | When to Use |
|---|---|---|
| Plain function | `pagination_params()` | Simple, stateless logic |
| Generator function (`yield`) | `get_db()` | Anything needing setup AND guaranteed cleanup |
| Callable class | `RoleChecker` | A check that needs its OWN configuration |

> 💡 **Tip**
>
> Dependencies can also depend on OTHER dependencies — notice `RoleChecker.__call__` itself uses `Depends(get_current_user)`. FastAPI resolves this chain automatically, in the correct order.

🤔 **Quick thinking question:** Why does `get_db()` use `yield` and a `finally` block instead of just `return db`?
✅ **Answer:** Using `yield` with `finally` guarantees the database session is closed EVERY time, even if the endpoint raises an unexpected error — with a plain `return`, there'd be no natural place to guarantee that cleanup step runs.

---

## 💡 Real-Life Analogy

* 🔌 **Dependency Injection → Hotel Room Service, Not a Mini-Kitchen in Every Room** — Instead of every room (endpoint) needing its own kitchen (setup code), room service (FastAPI) delivers exactly what's needed directly to the room.
* 🗄️ **`get_db()` with yield/finally → Borrowing a Library Book with an Automatic Return** — You get the book when you need it, and no matter what happens while you have it, the system guarantees it's properly returned afterward.
* 🎫 **`RoleChecker` → A Configurable Bouncer** — The SAME bouncer logic checks IDs at the door, but you can configure different bouncers for different rooms ("VIP only" vs "staff only") using the same underlying mechanism.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Shared pagination dependency | Nearly every "list" endpoint across real-world APIs (e-commerce product listings, search results) |
| DB session dependency | Standard pattern with SQLAlchemy + FastAPI, used across countless production APIs |
| Auth dependency | Used to protect endpoints in apps ranging from banking APIs to internal admin tools |
| Class-based role dependency | Common in any API with multiple user roles (admin/staff/customer) needing different access levels |

---

## 🔍 Industry Example

**Scenario:** A team at a **fintech startup** is building a FastAPI backend for a lending platform.

1. Every endpoint that touches the database uses a shared `get_db()` **dependency** (with `yield`/`finally`), guaranteeing database connections are never leaked, even under heavy load.
2. Protected endpoints (like viewing loan details) depend on `get_current_user()`, and admin-only endpoints ADDITIONALLY depend on a configurable `RoleChecker` — reusing the SAME authentication dependency across dozens of endpoints.
3. When the pagination rules change (say, a new maximum page size), the team updates ONE `pagination_params()` function, and every "list" endpoint across the API picks up the change automatically.

This is exactly how dependency injection is used in real, production FastAPI systems — not for one endpoint, but as an organizing principle across the whole API.

---

## 📊 Diagram

```
            A REALISTIC DEPENDENCY CHAIN
            --------------------------------

   GET /admin-dashboard
          │
          ▼
   admin_only  (RoleChecker instance)
          │
          needs → get_current_user
                       needs → Header("Authorization")
          │
          ▼
   All resolved automatically, in order
          │
          ▼
   Endpoint function finally runs
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Dependencies can only be simple functions with no parameters of their own."
  ✅ **Correct:** Dependencies can be generator functions (`yield`) or configurable classes — FastAPI resolves all of these automatically.

* ❌ **Wrong belief:** "It's fine to open a database connection with `return db` instead of `yield db`."
  ✅ **Correct:** `yield` with `finally` guarantees cleanup happens even if the endpoint raises an error — `return` alone provides no such guarantee.

* ❌ **Wrong belief:** "Comparing a header string to a hardcoded value IS how real authentication works."
  ✅ **Correct:** This is a useful STUB for learning the pattern — real systems verify properly issued tokens, not a fixed string.

---

## 💬 Interview Corner

**Q1: What problem does dependency injection solve in FastAPI?**
✅ It avoids repeating shared setup logic (database connections, auth checks) inside every endpoint — dependencies are written once and injected into any endpoint that declares it needs them.

**Q2: Why do database dependencies typically use `yield` instead of `return`?**
✅ `yield` with a `finally` block allows code to run both before the request (opening the session) and after it completes (closing it) — guaranteeing cleanup even on error.

**Q3: What advantage does a class-based dependency like `RoleChecker` have over a plain function?**
✅ It can be CONFIGURED at creation time (`RoleChecker(allowed_roles=["admin"])`), letting you reuse the same underlying check with different rules for different endpoints.

---

## 📝 Quick Summary

* 🔌 Dependency Injection lets endpoints DECLARE what they need instead of building it themselves
* ♻️ `Depends()` shares logic (like pagination) across many endpoints — written once, reused everywhere
* 🗄️ Generator dependencies (`yield` + `finally`) guarantee setup AND cleanup, even on error
* 🔐 A simple header-check dependency is a useful STUB for authentication before building a full login system
* 🏷️ Class-based dependencies (`RoleChecker`) allow configurable, reusable checks — similar in spirit to parameterized decorators

---

## 🎯 Class Activity

**"Build Your First Shared Dependencies" 🔧**

1. Build a `pagination_params()` dependency and use it in two different "list" endpoints.
2. Build a `get_db()` generator dependency (using the `FakeDBSession` pattern) and inject it into an endpoint, confirming (via the print statements) that it opens and closes correctly.
3. Build a `get_current_user()` header-based auth dependency and protect one endpoint with it, testing both a valid and a missing header.
4. Build a `RoleChecker` class-based dependency and use two differently-configured instances (`allow_admin`, `allow_staff`) on two different endpoints.


---

# 📋 Assignments — FastAPI Dependency Injection

| Assignment |
|---|
| Build a `pagination_params()` dependency (with `skip` and `limit`) and use it in two different endpoints, confirming both share the same logic. |
| Build a `get_db()` generator dependency using the `FakeDBSession` pattern, and inject it into a `GET /orders/{order_id}` endpoint. |
| Add print statements to your `get_db()` dependency to confirm the session opens BEFORE the endpoint runs and closes AFTER — even when you deliberately raise an error inside the endpoint. |
| Build a `get_current_user()` dependency that checks an `Authorization` header, and protect a `/dashboard` endpoint with it, testing both valid and missing/incorrect headers. |
| Build a `RoleChecker` class-based dependency and create at least 2 differently-configured instances (`allow_admin`, `allow_editor`), applying each to a different endpoint. |
| Combine dependencies: build an endpoint that requires BOTH a `get_db()` session AND a `get_current_user()` check. |
| Write a short comparison (3–4 sentences) explaining, in your own words, when you'd choose a plain function dependency vs. a class-based one. |