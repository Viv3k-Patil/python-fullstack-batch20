# 📚 FastAPI Introduction

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Explain why FastAPI exists and how it compares to Flask, Django, and DRF
* 🎯 Create and run a basic FastAPI application
* 🎯 Define and use path parameters and query parameters
* 🎯 Use Pydantic models to validate request and response data automatically
* 🎯 Build simple, type-safe request-response workflows

---

## 📖 Introduction

Up until now, you've built console-based Python projects — programs that run in a terminal and talk directly to a user typing on a keyboard. But most real-world software today is **web-based**: apps and websites talk to a **backend server** over the internet, sending and receiving data.

**FastAPI** is a modern Python framework specifically built for creating these backend servers — called **APIs** (Application Programming Interfaces) — quickly, safely, and with excellent built-in tooling. 🚀

### 🤔 Why does this topic exist?

* 🌐 Nearly every modern app (mobile apps, websites, other backend services) needs an API to talk to
* ⚡ FastAPI is one of the fastest-growing, most in-demand Python web frameworks in the industry right now
* 🛡️ It automatically validates incoming data and documents your API — two things that took a LOT of manual work in older frameworks

### 🤔 Where is it used?

* 🏢 Companies like Microsoft, Uber, and Netflix use FastAPI (or similar frameworks) for backend services
* 📱 Mobile app backends — the app on your phone talks to a FastAPI server to fetch/save data
* 🤖 AI/ML model serving — FastAPI is extremely popular for wrapping machine learning models into usable APIs
* 🔗 Microservices — many companies split large systems into small FastAPI-powered services that talk to each other

> 💡 **Tip**
>
> If you've ever used an app that shows live data (weather, prices, notifications), there's almost certainly an API like the ones you'll build today working behind the scenes.

---

## 🧠 Detailed Notes

### 1️⃣ Why FastAPI? Comparing with Flask, Django, and DRF

Python has several popular web frameworks. Each was built with different priorities in mind.

| Framework | What It's Best At | Key Trade-off |
|---|---|---|
| **Flask** | Lightweight, minimal, very flexible | You must add validation, docs, async support yourself |
| **Django** | "Batteries-included" full framework — admin panel, ORM, auth all built in | Heavier, more opinionated, slower to set up a simple API |
| **DRF (Django REST Framework)** | Adds REST API tooling on top of Django | Still carries Django's full weight, more boilerplate |
| **FastAPI** | Built specifically for APIs — fast, automatic validation, automatic docs, native async support | Newer ecosystem, fewer built-in extras than Django (no admin panel, no ORM) |

**What makes FastAPI stand out:**

* ⚡ **Speed** — Built on `Starlette` and `Pydantic`, FastAPI is one of the fastest Python frameworks available, comparable to Node.js and Go in benchmarks
* ✅ **Automatic data validation** — Using Python type hints, FastAPI checks incoming data automatically, rejecting invalid requests before your code even runs
* 📄 **Automatic interactive documentation** — Every FastAPI app automatically generates a live, testable API documentation page (via Swagger UI), with ZERO extra code
* 🔄 **Native async support** — FastAPI is designed from the ground up to handle asynchronous code efficiently, unlike Flask which needed retrofitting for this

```
        FRAMEWORK COMPARISON AT A GLANCE
        -----------------------------------
   Flask:    🧱 minimal building blocks — you assemble everything yourself
   Django:   🏢 a fully furnished building — great if you want everything included
   DRF:      🏢 + 🔌 Django with API-specific plugins added on top
   FastAPI:  🏎️  a purpose-built race car for APIs — fast, validated, documented, async-ready
```

> ⚠️ **Important**
>
> FastAPI is NOT a full replacement for Django — Django still wins for large, traditional web apps needing an admin panel and a built-in ORM. FastAPI shines specifically for building **APIs**, especially fast, modern, data-driven ones.

🤔 **Quick thinking question:** Why might a team building a machine learning model's API choose FastAPI over Flask?
✅ **Answer:** FastAPI automatically validates the incoming data (e.g., ensuring an image size or a numeric input is in the correct format) and automatically generates interactive documentation for testing the model's API — both of which would need to be built manually in Flask, costing extra development time.

---

### 2️⃣ Creating a Basic FastAPI Application

**Installation:**

```bash
pip install fastapi uvicorn
```

`fastapi` is the framework itself; `uvicorn` is the **ASGI server** that actually runs your FastAPI app (similar to how a car needs an engine to actually move).

**The simplest possible FastAPI app:**

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

**Running the app:**

```bash
uvicorn main:app --reload
```

* `main` refers to the filename `main.py`
* `app` refers to the `FastAPI()` object we created
* `--reload` automatically restarts the server whenever you save a code change (great for development)

Once running, visiting `http://127.0.0.1:8000/` in a browser shows:
```json
{"message": "Hello, FastAPI!"}
```

**The automatic documentation — one of FastAPI's standout features:**

Visit `http://127.0.0.1:8000/docs` and you'll see a full, interactive **Swagger UI** page — automatically generated, with ZERO extra code written, letting you test your API directly from the browser.

```
              HOW A FASTAPI REQUEST FLOWS
              ------------------------------
   Browser/App  ──HTTP GET request──►  FastAPI app  ──► Python function runs
        ▲                                                        │
        └───────────────── JSON response ◄──────────────────────┘
```

| Concept | Meaning |
|---|---|
| `FastAPI()` | Creates the main application object |
| `@app.get("/")` | A **decorator** — registers this function to handle GET requests to the `/` URL |
| `uvicorn` | The server program that actually runs your FastAPI app and listens for requests |
| `/docs` | Auto-generated interactive documentation (Swagger UI) |

> 💡 **Tip**
>
> Notice `@app.get("/")` is a **decorator** — exactly the same concept you learned earlier in this course! FastAPI uses decorators extensively to connect URLs to the functions that handle them.

🤔 **Quick thinking question:** Why is `uvicorn` needed at all — why can't you just run `python main.py` directly?
✅ **Answer:** FastAPI itself only defines HOW to handle requests; it doesn't include the actual network server that listens for incoming HTTP connections. `uvicorn` is that server — it receives real network requests and hands them off to your FastAPI app to process.

---

### 3️⃣ Defining Path & Query Parameters

**Path parameters** are values embedded directly IN the URL itself — used to identify a SPECIFIC resource.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):          # the {user_id} in the URL maps to this parameter
    return {"user_id": user_id, "message": f"Fetching user {user_id}"}
```

Visiting `http://127.0.0.1:8000/users/42` returns:
```json
{"user_id": 42, "message": "Fetching user 42"}
```

Notice `user_id: int` — FastAPI automatically converts the URL text into an actual Python `int`, AND validates it. Try visiting `/users/abc` instead, and FastAPI automatically returns a clear validation error, WITHOUT you writing any check yourself!

```json
{"detail": [{"loc": ["path", "user_id"], "msg": "value is not a valid integer", ...}]}
```

**Query parameters** are optional (usually) values added AFTER a `?` in the URL, typically used for filtering, searching, or pagination.

```python
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):     # query params, with DEFAULT values
    return {"skip": skip, "limit": limit, "message": "Fetching items"}
```

Visiting `http://127.0.0.1:8000/items/?skip=5&limit=20` returns:
```json
{"skip": 5, "limit": 20, "message": "Fetching items"}
```

Visiting `http://127.0.0.1:8000/items/` (no query params at all) uses the DEFAULT values:
```json
{"skip": 0, "limit": 10, "message": "Fetching items"}
```

**Combining path AND query parameters together:**

```python
@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int, status: str = "all"):
    return {"user_id": user_id, "status_filter": status}
```

`http://127.0.0.1:8000/users/5/orders?status=pending` → `{"user_id": 5, "status_filter": "pending"}`

| Parameter Type | Where It Appears | Typical Use |
|---|---|---|
| Path parameter | Inside the URL path, e.g. `/users/{user_id}` | Identifying a SPECIFIC resource |
| Query parameter | After `?` in the URL, e.g. `?skip=5&limit=20` | Filtering, sorting, pagination, optional settings |

> ⚠️ **Important**
>
> FastAPI decides whether something is a path or query parameter based on WHERE it appears — parameters listed in the URL path string (inside `{}`) are path parameters; any OTHER function parameters automatically become query parameters.

🤔 **Quick thinking question:** In `get_user_orders(user_id: int, status: str = "all")`, why is `user_id` treated as a path parameter, but `status` is treated as a query parameter?
✅ **Answer:** Because `user_id` appears inside `{}` in the route string `/users/{user_id}/orders`, marking it explicitly as part of the URL path — `status` does NOT appear in the route string, so FastAPI automatically treats it as an optional query parameter instead.

---

### 4️⃣ Pydantic Models for Request/Response Validation

For simple values (numbers, strings), path/query parameters work great. But for more complex data — like a whole "new user" object with multiple fields — you need a **Pydantic model**: a class that describes the exact SHAPE of the data you expect, with automatic validation.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users/")
def create_user(user: User):        # FastAPI automatically parses & validates incoming JSON into a User object
    return {"message": f"User {user.name} created!", "user": user}
```

**Testing this with a POST request** (e.g., sending this JSON body):
```json
{"name": "Priya", "age": 21, "email": "priya@example.com"}
```

Returns:
```json
{"message": "User Priya created!", "user": {"name": "Priya", "age": 21, "email": "priya@example.com"}}
```

**What happens with INVALID data** — e.g., sending `{"name": "Priya", "age": "not-a-number", "email": "priya@example.com"}`:

```json
{
  "detail": [
    {
      "loc": ["body", "age"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

FastAPI automatically rejected the request and explained EXACTLY what was wrong — no manual validation code needed!

**Pydantic models can also add extra validation rules:**

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)              # gt = greater than, lt = less than
    email: EmailStr                                     # automatically validates proper email format!
```

**Using a Pydantic model for the RESPONSE too — controlling exactly what data goes OUT:**

```python
class UserResponse(BaseModel):
    name: str
    age: int
    # 'email' is deliberately left out — never send it back in responses!

@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    return user     # even though 'user' has an email field, the RESPONSE only shows name and age
```

| Concept | Purpose |
|---|---|
| `BaseModel` | Base class for defining a Pydantic data shape |
| Type hints (`str`, `int`, `EmailStr`) | Define what type each field must be — validated automatically |
| `Field(...)` | Add extra constraints (min/max length, value ranges) |
| `response_model=` | Controls exactly what fields are sent back in the response |

> 💡 **Tip**
>
> Think of a Pydantic model as a **contract** — "any data coming in (or going out) MUST match this exact shape." FastAPI enforces that contract automatically, on every single request.

🤔 **Quick thinking question:** Why would a developer deliberately use a DIFFERENT Pydantic model for the response (`UserResponse`) than for the request (`User`)?
✅ **Answer:** To control exactly what data is exposed to the client — for example, hiding sensitive fields like a password or email that were needed to CREATE the user, but should never be sent back out in the API's response.

---

### 5️⃣ Simple Request-Response Workflows with Type-Safe Inputs & Outputs

Let's put everything together into one small, complete, type-safe API.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    age: int

# a simple in-memory "database" for this example
users_db: dict[int, User] = {}
next_id = 1


@app.post("/users/", response_model=UserResponse)
def create_user(user: User):
    global next_id
    user_id = next_id
    users_db[user_id] = user
    next_id += 1
    return UserResponse(id=user_id, name=user.name, age=user.age)


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(id=user_id, name=user.name, age=user.age)


@app.get("/users/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10):
    all_users = [
        UserResponse(id=uid, name=u.name, age=u.age)
        for uid, u in users_db.items()
    ]
    return all_users[skip: skip + limit]
```

**What makes this "type-safe" end to end:**

```
     INCOMING REQUEST                          OUTGOING RESPONSE
     ------------------                        --------------------
     JSON body                                  Python object
        │                                              │
        ▼                                              ▼
   Validated against `User`                  Converted using `UserResponse`
   (name: str, age: int,                     (only id, name, age —
    email: EmailStr)                          email deliberately excluded)
        │                                              │
        ▼                                              ▼
   ❌ Invalid → automatic 422 error           ✅ Guaranteed correct shape,
   ✅ Valid → function runs                      every single time
```

Notice: at NO point did we manually write `if not isinstance(...)` checks, or manually build JSON responses — FastAPI and Pydantic handle validation and serialization automatically, based purely on the TYPE HINTS we wrote.

> ⚠️ **Important**
>
> Using `HTTPException` (rather than a normal Python exception) is how you correctly signal an HTTP-specific error — like "404 Not Found" — from inside a FastAPI route. FastAPI catches it and turns it into a proper HTTP error response.

🤔 **Quick thinking question:** Why does `list_users()` use `list[UserResponse]` as its `response_model`, instead of just `UserResponse`?
✅ **Answer:** Because this endpoint returns MULTIPLE users (a list), not just one — `response_model` must match the actual shape of the data being returned, so a list of users needs `list[UserResponse]` to correctly validate and document that the response is an array of user objects.

---

## 💡 Real-Life Analogy

* 🍽️ **FastAPI → A Restaurant with a Very Strict, Very Fast Waiter** — You (the client) place an order (a request) in a specific format (the menu/Pydantic model). If your order doesn't match the menu's format, the waiter immediately tells you exactly what's wrong, before it ever reaches the kitchen (your function).
* 📋 **Pydantic Model → An Official Form With Required Fields** — Just like a government form rejects your application if you leave the "age" field blank or write letters instead of numbers, a Pydantic model rejects incoming data that doesn't match its expected shape.
* 🔑 **Path Parameter → An Apartment Number** — `/users/42` is like walking directly to apartment "42" — you're identifying ONE specific thing.
* 🔍 **Query Parameter → Filters at a Search Counter** — `?skip=5&limit=20` is like telling a librarian "skip the first 5 books, show me the next 20" — refining a broader search, not pointing to one specific item.
* 📖 **Automatic `/docs` → A Restaurant Menu That Lets You Actually Order From It** — Instead of just describing the dishes, FastAPI's auto-generated docs let you actually "place a test order" directly from the documentation page.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| FastAPI in production | Microsoft, Uber, Netflix, and Cred have publicly discussed using FastAPI for backend services |
| Path parameters | Almost every REST API — e.g., `/products/{product_id}` on an e-commerce site |
| Query parameters | Search/filter features — e.g., `/search?query=shoes&category=men` |
| Pydantic validation | Any API that accepts user-submitted data — signup forms, payment details, order details |
| Automatic docs (`/docs`) | Used by API teams to let OTHER developers (frontend, mobile) explore and test the API without needing separate documentation tools |
| AI/ML model serving | Data science teams commonly wrap trained models in a FastAPI endpoint for other services to call |

---

## 🔍 Industry Example

**Scenario:** A **backend developer at a food delivery startup** (similar to Zomato) is building the API that the mobile app will use to fetch restaurant details and place orders.

1. They choose **FastAPI** specifically because the team needs to move fast, and automatic request validation + automatic documentation saves significant development time compared to Flask.
2. The endpoint to fetch a specific restaurant uses a **path parameter**: `GET /restaurants/{restaurant_id}` — identifying ONE specific restaurant.
3. The endpoint to search restaurants uses **query parameters**: `GET /restaurants/?cuisine=chinese&min_rating=4` — filtering a broader list.
4. When a user places an order, the mobile app sends a JSON body matching an `OrderRequest` **Pydantic model** — FastAPI automatically rejects malformed orders (e.g., missing item IDs, negative quantities) before the order-processing logic ever runs.
5. The API's responses use a SEPARATE `OrderResponse` Pydantic model, ensuring sensitive internal details (like a restaurant's internal cost pricing) are never accidentally leaked to the mobile app.
6. The frontend/mobile team uses the **auto-generated `/docs` page** to explore and test the API themselves, without needing the backend team to write separate documentation.

This exact combination — path/query parameters, Pydantic-validated requests and responses, and automatic docs — is standard practice for real, modern API development.

---

## 📊 Diagram

```
              FASTAPI REQUEST LIFECYCLE
              ----------------------------

   Client (browser/app/Postman)
          │
          ▼  HTTP request (GET/POST/etc.)
   ┌─────────────────────────────┐
   │  FastAPI routes the request  │
   │  based on URL + method        │
   └─────────────────────────────┘
          │
          ▼
   Path/Query params + Pydantic model
   automatically parsed & validated
          │
     ┌────┴────┐
     ▼           ▼
   ❌ Invalid   ✅ Valid
     │             │
     ▼             ▼
  422 error    Your function runs
  returned      (business logic)
                    │
                    ▼
             response_model
             validates OUTGOING data
                    │
                    ▼
             JSON response sent back


        PATH vs QUERY PARAMETER
        ---------------------------
   /users/{user_id}/orders ? status=pending
              │                    │
         PATH param            QUERY param
       (identifies WHICH)    (filters/refines)
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "FastAPI replaces Django/Flask entirely — you should always use it instead."
  ✅ **Correct:** FastAPI is purpose-built for APIs; Django remains a strong choice for full websites needing an admin panel, ORM, and templating out of the box.

* ❌ **Wrong belief:** "You need to manually validate incoming JSON data in FastAPI, just like in Flask."
  ✅ **Correct:** FastAPI automatically validates incoming data based on your Pydantic model's type hints — manual `if` checks for basic type/shape validation are unnecessary.

* ❌ **Wrong belief:** "Path parameters and query parameters are interchangeable — it doesn't matter which you use."
  ✅ **Correct:** Path parameters identify a SPECIFIC resource (`/users/42`); query parameters filter/refine a broader request (`?skip=5&limit=20`) — using the wrong one leads to confusing, non-RESTful API design.

* ❌ **Wrong belief:** "You should just return your internal data model directly from an endpoint, without a separate response model."
  ✅ **Correct:** Using a dedicated `response_model` lets you control exactly what data is exposed, keeping sensitive/internal fields from accidentally leaking into API responses.

* ❌ **Wrong belief:** "Running `python main.py` is the standard way to start a FastAPI app."
  ✅ **Correct:** FastAPI apps are run using an ASGI server like `uvicorn` (`uvicorn main:app --reload`), since FastAPI itself doesn't include a built-in server.

---

## 💬 Interview Corner

**Q1: What are the main advantages of FastAPI over Flask?**
✅ Automatic request/response validation using Python type hints and Pydantic, automatically generated interactive documentation (Swagger UI), and native support for asynchronous code — all of which require extra manual setup in Flask.

**Q2: What is the difference between a path parameter and a query parameter in FastAPI?**
✅ A path parameter is embedded directly in the URL (e.g., `/users/{user_id}`) and typically identifies a specific resource. A query parameter appears after a `?` in the URL (e.g., `?skip=5&limit=10`) and is typically used for optional filtering, sorting, or pagination.

**Q3: What role does a Pydantic model play in a FastAPI application?**
✅ It defines the exact expected shape (fields and types) of incoming request data or outgoing response data, and FastAPI uses it to automatically validate and serialize that data — rejecting anything that doesn't match, without requiring manual validation code.

**Q4: Why might a FastAPI endpoint use a different Pydantic model for its response than for its request?**
✅ To control exactly which fields are exposed in the response — for example, accepting a password or email as part of a request model, but deliberately excluding them from the response model so they're never sent back to the client.

---

## 📝 Quick Summary

* 🏎️ FastAPI is a modern Python framework purpose-built for creating fast, validated, well-documented APIs
* ⚖️ Compared to Flask (minimal), Django (full-featured), and DRF (Django + REST tooling), FastAPI trades some built-in extras for speed, automatic validation, and native async support
* 🚀 A basic FastAPI app is created with `FastAPI()` and run using `uvicorn main:app --reload`
* 📄 Every FastAPI app automatically generates interactive documentation at `/docs`, with zero extra code
* 🔑 Path parameters (`/users/{user_id}`) identify a specific resource; query parameters (`?skip=5&limit=10`) filter or refine a request
* 🛡️ Pydantic models (`BaseModel`) define the expected shape of request/response data, and FastAPI validates against them automatically
* 📤 `response_model` controls exactly what fields are sent back, letting you hide sensitive/internal data
* 🎯 Together, these features let you build type-safe, self-documenting APIs with far less manual validation code than older frameworks required

---

## 🎯 Class Activity

**"Build Your First Type-Safe API" 🚀**

1. Install `fastapi` and `uvicorn`, and create a basic app with a single `GET /` endpoint returning a welcome message.
2. Add a `GET /students/{student_id}` endpoint using a path parameter, returning a message that includes the student ID.
3. Add a `GET /students/` endpoint using two query parameters (`skip` and `limit`, with default values), and test it with different URL combinations.
4. Create a Pydantic model `Student` with `name`, `age`, and `email` (using `EmailStr`), and build a `POST /students/` endpoint that accepts and returns this model.
5. Run your app with `uvicorn main:app --reload`, open `/docs` in your browser, and test all four endpoints directly from the interactive documentation page.
6. Bonus: Try sending INVALID data (like a string for `age`) through the `/docs` page, and observe FastAPI's automatic validation error message.


---

# 📋 Assignments — FastAPI Introduction

| Assignment |
|---|
| Install `fastapi` and `uvicorn`, and create a basic app with a `GET /` endpoint returning your name and course name as JSON. |
| Write a short comparison table (in your own words) of Flask vs Django vs FastAPI, listing one clear use case for each. |
| Create a `GET /books/{book_id}` endpoint using a path parameter, and test what happens when you visit it with a non-numeric ID. |
| Create a `GET /books/` endpoint with two query parameters, `genre` (string, default "all") and `limit` (int, default 5), and test several different URL combinations. |
| Create a Pydantic model `Product` with `name`, `price`, and `in_stock` (bool), and build a `POST /products/` endpoint that accepts and returns it. |
| Add validation constraints to the `Product` model using `Field()` — price must be greater than 0, and name must be between 2 and 100 characters. |
| Create a separate `ProductResponse` model that excludes an internal `cost_price` field, and use it as the `response_model` for your `POST /products/` endpoint. |
| Build a small in-memory "book store" API with `POST /books/`, `GET /books/{book_id}`, and `GET /books/` (list all), using proper Pydantic request and response models throughout. |
| Add an `HTTPException` with a 404 status code to your `GET /books/{book_id}` endpoint for when a book ID doesn't exist, and test it. |
| Visit your running app's `/docs` page and manually test EVERY endpoint you've built directly from the Swagger UI, taking a screenshot of at least one successful and one failed (validation error) request. |
| Add an `EmailStr` field to a `Customer` Pydantic model, and test what happens when you submit an invalid email format through `/docs`. |
| Create a `GET /search/` endpoint with THREE optional query parameters (`keyword`, `min_price`, `max_price`), all with sensible defaults, and print/return which filters were applied. |
| Combine a path parameter AND multiple query parameters in one endpoint, e.g. `GET /users/{user_id}/orders?status=pending&limit=10`, and test it thoroughly. |
| Try removing all type hints from one of your endpoint functions and observe how FastAPI's behavior and automatic docs change (or don't) — write your observations as a comment. |
| Write a short reflection (3–5 sentences) on what surprised you most about FastAPI's automatic validation and documentation, compared to how you might have built the same thing without it. |