# 📚 FastAPI Custom Exception Handlers & Middleware

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Write custom exception handlers that return clean, consistent error responses
* 🎯 Understand why global exception handling matters for a real API
* 🎯 Understand what middleware is and how it wraps every request
* 🎯 Build basic middleware for logging, timing, and simple security checks

---

## 📖 Introduction

Two things separate a "toy" API from a real one: how it handles things going WRONG, and what it does for EVERY request regardless of which endpoint is hit. Today covers both — **custom exception handlers** (clean, controlled error responses) and **middleware** (logic that wraps the entire request-response cycle).

### 🤔 Why does this topic exist?

* 🚨 By default, an unhandled error in FastAPI returns a generic, unhelpful response — real APIs need clear, predictable errors
* 📊 Every production API needs SOME cross-cutting behavior — logging, timing, basic security — applied globally, not endpoint-by-endpoint
* 🔗 Both ideas connect directly to earlier topics: custom exceptions (from the banking project) and decorators (chained execution order)

### 🤔 Where is it used?

* 💳 Payment APIs — known for clean, well-structured error responses that client apps can rely on
* 📝 Production logging — middleware records every request automatically, without touching individual endpoints
* 🛡️ Basic security — middleware can block requests missing required headers before they reach any business logic

> 💡 **Tip**
>
> If chained decorators made sense to you earlier, middleware will feel familiar — it's the SAME "before/after" wrapping idea, just applied to the whole application instead of one function.

---

## 🧠 Detailed Notes

### 1️⃣ Custom Exception Handlers

By default, an unhandled error in FastAPI returns a generic 500 response. A **custom exception handler** lets you catch a SPECIFIC exception type globally and control exactly how it looks to the client.

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class InsufficientBalanceError(Exception):
    def __init__(self, balance: float, requested: float):
        self.balance = balance
        self.requested = requested


@app.exception_handler(InsufficientBalanceError)
def insufficient_balance_handler(request: Request, exc: InsufficientBalanceError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "InsufficientBalance",
            "message": f"You requested ₹{exc.requested} but only have ₹{exc.balance}",
        },
    )


@app.get("/withdraw/{amount}")
def withdraw(amount: float):
    balance = 1000
    if amount > balance:
        raise InsufficientBalanceError(balance=balance, requested=amount)
    return {"message": f"Withdrew ₹{amount}"}
```

Visiting `/withdraw/5000` now returns a CLEAN, controlled response instead of a generic error:
```json
{"error": "InsufficientBalance", "message": "You requested ₹5000.0 but only have ₹1000"}
```

This connects directly to the custom exceptions topic from earlier — the SAME idea (custom, meaningful exceptions) now plugged into FastAPI's error-handling system, so every endpoint benefits automatically without repeating `try/except`.

```
        WITHOUT a custom handler                 WITH a custom handler
        ----------------------------             ----------------------------
   raise InsufficientBalanceError(...)      raise InsufficientBalanceError(...)
              │                                          │
              ▼                                          ▼
     Generic 500 error                         @app.exception_handler catches it
     (unhelpful, exposes internals)              │
                                                  ▼
                                          Clean, controlled JSON response
```

**You can register handlers for multiple exception types**, each with its own response:

```python
class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id


@app.exception_handler(ItemNotFoundError)
def item_not_found_handler(request: Request, exc: ItemNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"error": "ItemNotFound", "message": f"Item {exc.item_id} does not exist"},
    )
```

| Concept | Purpose |
|---|---|
| `@app.exception_handler(ExceptionType)` | Registers a handler that runs whenever that exception is raised, anywhere in the app |
| `JSONResponse(status_code=..., content=...)` | Lets you fully control the status code and body of the error response |

> ⚠️ **Important**
>
> Custom exception handlers are registered ONCE, globally, on the `app` object — you do NOT need `try/except` in every endpoint that might raise that exception.

🤔 **Quick thinking question:** Why is returning a generic 500 error for a business-logic problem like "insufficient balance" considered bad API design?
✅ **Answer:** A 500 error signals an UNEXPECTED server bug, not a normal, anticipated situation like insufficient funds — the client needs a clear, specific error (like a 400 with a descriptive message) so it can show the user something helpful, instead of a generic "something went wrong."

---

### 2️⃣ Middleware Basics for Logging, Timing, and Security

**Middleware** is code that runs on EVERY request — before it reaches your endpoint, and again after the response is generated — wrapping the entire request-response cycle, application-wide.

```python
import time
from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)          # this actually runs the endpoint
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"⏱️ {request.method} {request.url.path} took {process_time:.4f}s")
    return response
```

Every single request through this app now automatically logs its timing — without touching any individual endpoint's code.

**Logging middleware:**

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"📥 Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"📤 Response status: {response.status_code}")
    return response
```

**A simple security middleware — blocking requests missing a required header:**

```python
from fastapi.responses import JSONResponse

@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.url.path.startswith("/admin") and request.headers.get("X-API-Key") != "secret-key":
        return JSONResponse(status_code=403, content={"error": "Missing or invalid API key"})
    return await call_next(request)
```

**Multiple middleware — order matters, exactly like chained decorators:**

```
     Request
        │
        ▼
   Middleware 1 (logging) — runs BEFORE
        │
        ▼
   Middleware 2 (security check) — runs BEFORE
        │
        ▼
   Your endpoint function runs
        │
        ▼
   Middleware 2 — runs AFTER
        │
        ▼
   Middleware 1 — runs AFTER
        │
        ▼
     Response sent to client
```

This "before-before-run-after-after" pattern is the SAME chained-decorator execution order you learned earlier — middleware is really decorators applied at the whole-application level instead of one function at a time.

| Middleware Use Case | What It Does |
|---|---|
| Timing | Measures and logs how long each request takes |
| Logging | Records every incoming request and outgoing response status |
| Security | Blocks requests missing required headers before they reach any endpoint |

> 💡 **Tip**
>
> Use `Depends()` for logic SPECIFIC to certain endpoints (like "this endpoint needs a DB session"). Use middleware for logic that applies to LITERALLY EVERY request, regardless of which endpoint it hits.

🤔 **Quick thinking question:** Why would request logging be implemented as middleware rather than as a `Depends()` dependency added to every endpoint?
✅ **Answer:** Middleware automatically applies to EVERY request across the entire application without needing to remember to add the dependency to every single endpoint — it's the correct tool specifically because the behavior needs to be truly global.

---

## 💡 Real-Life Analogy

* 🚨 **Custom Exception Handlers → A Company's Standard Complaint Response Template** — Instead of every rep improvising their own reply, there's ONE standard, polished response used company-wide for that exact situation.
* 📹 **Middleware → CCTV Cameras Covering an Entire Building** — Instead of installing a camera in each individual room separately, one set of cameras watches EVERY room's entrances and exits automatically.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Custom exception handlers | Payment APIs (Razorpay, Stripe-style integrations) return clean, structured error codes using this exact pattern |
| Timing middleware | Performance monitoring dashboards often rely on similar request-timing instrumentation |
| Logging middleware | Standard practice for any API that needs to debug issues after the fact |
| Security middleware | API gateways and internal tools commonly enforce simple API-key checks this way |

---

## 🔍 Industry Example

**Scenario:** A team at a **fintech company** is building a FastAPI-based backend for a lending platform.

1. Business-specific errors like `LoanNotEligibleError` are registered as **custom exception handlers**, so the mobile app always receives a clean, predictable error instead of a raw server error.
2. **Timing middleware** logs how long every request takes, feeding a dashboard the team uses to catch slow endpoints before customers complain.
3. **Security middleware** checks for a valid internal token on any request hitting `/internal/*` routes, blocking unauthorized access before it reaches sensitive logic.

This combination — clean custom errors plus simple, global middleware — is a big part of what makes an API feel production-ready rather than like a class exercise.

---

## 📊 Diagram

```
          REQUEST FLOW WITH ERRORS & MIDDLEWARE
          -----------------------------------------

   Request
      │
      ▼
   MIDDLEWARE (before) — logging, timing starts, security check
      │
      ▼
   ENDPOINT function runs
      │
      ├── ❌ raises a custom exception ──► @app.exception_handler catches it
      │                                          │
      │                                          ▼
      │                                   Clean JSON error response
      │
      └── ✅ returns normally ──► response built
                                        │
                                        ▼
   MIDDLEWARE (after) — add timing header, log final status
      │
      ▼
   Response sent to client
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "Unhandled exceptions in FastAPI automatically return helpful, clear error messages to the client."
  ✅ **Correct:** By default they return a generic 500 error — you must register custom exception handlers to control error responses for specific exception types.

* ❌ **Wrong belief:** "Middleware and `Depends()` solve the same problem, so it doesn't matter which you use."
  ✅ **Correct:** `Depends()` is for logic specific to certain endpoints; middleware is for logic that must apply to EVERY request, regardless of endpoint.

* ❌ **Wrong belief:** "You need to add `try/except` in every endpoint that might raise a specific custom exception."
  ✅ **Correct:** Registering a custom exception handler ONCE automatically applies to every endpoint that raises that exception type — no repeated `try/except` needed.

---

## 💬 Interview Corner

**Q1: What is the benefit of registering a custom exception handler instead of using `try/except` in every endpoint?**
✅ It's registered ONCE, globally, and automatically applies to every endpoint that raises that exception type — producing consistent error responses without duplicating error-handling code.

**Q2: What is the key difference in scope between a FastAPI dependency and middleware?**
✅ A dependency only applies to endpoints that explicitly declare it via `Depends()`. Middleware automatically applies to EVERY request across the entire application.

**Q3: Give a real-world reason to use timing middleware.**
✅ To automatically measure and log how long every request takes, without adding timing code to each individual endpoint — useful for spotting slow endpoints in production.

---

## 📝 Quick Summary

* 🚨 Custom exception handlers (`@app.exception_handler(...)`) turn specific exceptions into clean, consistent JSON error responses, registered once for the whole app
* 📹 Middleware runs on EVERY request, both before and after your endpoint code — ideal for logging, timing, and security checks
* ⚖️ Use `Depends()` for endpoint-specific shared logic; use middleware for truly global, application-wide behavior
* 🔗 These patterns mirror earlier ideas — custom exception handlers ≈ custom exceptions from the banking project; middleware ≈ decorators applied at the whole-app level

---

## 🎯 Class Activity

**"Add Clean Errors and Basic Middleware to Your API" 🔧**

1. Create a custom exception (e.g., `OutOfStockError`) and register a handler for it, returning a clean, structured JSON error.
2. Add timing middleware that logs how long each request takes, and test it with an artificial `time.sleep()` delay inside one endpoint.
3. Add security middleware that blocks any request to a path starting with `/admin` unless a specific header is present, and test both allowed and blocked cases.
4. Register two middleware together (logging + timing) and add print statements to confirm the before/after execution order.


---

# 📋 Assignments — FastAPI Custom Exception Handlers & Middleware

| Assignment |
|---|
| Create a custom exception `OutOfStockError` and register a global exception handler for it that returns a clean 400 response with a custom message. |
| Create a second custom exception (e.g., `ItemNotFoundError`) with its own handler returning a 404, and test both exceptions from different endpoints. |
| Write timing middleware that adds an `X-Process-Time` header to every response, and verify it using your browser's developer tools or Postman. |
| Write logging middleware that logs every request's method, path, and response status code to the console. |
| Write security middleware that blocks any request to a path starting with `/internal` unless a specific header/API key is present, and test both allowed and blocked cases. |
| Chain two middleware functions together (logging + timing) and add print statements to confirm the "before/after" execution order matches the chained-decorator pattern from earlier. |
| Combine both topics: build one endpoint that can raise a custom exception, is covered by your logging middleware, and confirm the log still records the failed request correctly. |
| Write a short reflection (3–4 sentences) comparing custom exception handlers here to the `BankingError` hierarchy from the earlier banking project — what's the same, what's different? |