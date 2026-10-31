# 📚 useEffect and Fetching Data from FastAPI

## 🎯 Learning Objectives

- ⚡ Explain what a **side effect** is and why React needs `useEffect`
- 🔁 Use the **dependency array** correctly (`none`, `[]`, `[x]`)
- 🚫 Recognize and avoid **infinite loops**
- 🧹 Write a **cleanup function**
- 🌐 Fetch data from a **FastAPI** backend (GET and POST) with loading and error states

---

## 📖 Introduction

Until now, our React apps used **mock data**. Real apps load data from a **server**. But fetching data is not part of "drawing the screen", it is an **extra action** that happens *because* the screen appeared. React calls these extra actions **side effects**, and `useEffect` is the hook to run them.

**Where is it used?** Loading a patient list when a page opens, setting a page title, starting a timer, listening to window resize.

---

## 🧠 Detailed Notes

### ⚡ 1. What Is a Side Effect?

A component's main job is to **return JSX** from props and state. Anything else it does to the outside world is a side effect:

| Side effect | Example |
|---|---|
| 🌐 Network request | `fetch("/patients")` |
| ⏱️ Timer | `setInterval` |
| 🏷️ Changing the page | `document.title = "Patients"` |
| 👂 Event listener | `window.addEventListener("resize", ...)` |

> ⚠️ **Important**
>
> Never call `fetch` directly in the component body. It would run on **every render**, and a state update after it would cause an endless loop.

---

### 🪝 2. `useEffect` Syntax

```jsx
import { useEffect } from "react"

useEffect(() => {
  // 1. the effect code runs AFTER the screen is drawn
  return () => {
    // 2. (optional) cleanup runs before the next effect, or when the component disappears
  }
}, [dependencies])  // 3. when should it run again?
```

---

### 🔁 3. Dependency Array Patterns

| Pattern | When the effect runs | Typical use |
|---|---|---|
| `useEffect(fn)` (no array) | After **every** render | Almost never |
| `useEffect(fn, [])` | **Once**, when the component first appears | Load initial data |
| `useEffect(fn, [id])` | Once, and again **whenever `id` changes** | Load details when the URL id changes |

```jsx
// Runs once, on first appearance
useEffect(() => {
  console.log("Page opened")
}, [])

// Runs on first appearance AND every time search changes
useEffect(() => {
  console.log("Search is now", search)
}, [search])
```

**Rule:** list every **prop or state value used inside the effect** in the array.

🤔 **Quick thinking question:** What happens if you forget `id` in `[id]` while fetching `/patients/${id}`?

✅ **Answer:** The page keeps showing the **first** patient even after the URL id changes, because the effect never runs again.

---

### 🚫 4. Avoiding Infinite Loops

```jsx
// ❌ INFINITE LOOP
useEffect(() => {
  fetch(url).then(r => r.json()).then(setPatients)   // changes state
})                                                    // no array → runs after every render

// ✅ FIXED
useEffect(() => {
  fetch(url).then(r => r.json()).then(setPatients)
}, [url])
```

The loop: render → effect → `setPatients` → render → effect → ...

**Other loop traps:**

| Trap | Why it loops | Fix |
|---|---|---|
| Missing array while setting state | Effect runs after every render | Add `[]` or the right dependencies |
| Putting an **object or array created in the component** in the array (`[{a: 1}]`) | A new object every render means "changed" | Use primitive values (`id`, `url`) instead |
| Putting a state value that the effect itself keeps changing | Effect changes it, which re-triggers the effect | Use a functional update, or remove it from the array |

---

### 🧹 5. Cleanup Function

Anything you start, you should stop:

```jsx
useEffect(() => {
  const timer = setInterval(() => console.log("tick"), 1000)
  return () => clearInterval(timer)     // cleanup
}, [])
```

For fetch, the cleanup **cancels the old request** when the URL changes or the page closes, using `AbortController`:

```jsx
useEffect(() => {
  const controller = new AbortController()

  fetch(url, { signal: controller.signal })
    .then(res => res.json())
    .then(setData)
    .catch(err => {
      if (err.name !== "AbortError") console.error(err)
    })

  return () => controller.abort()
}, [url])
```

> ℹ️ **Note**
>
> In development, `<StrictMode>` runs every effect **twice** (mount, cleanup, mount) to help you find missing cleanups. You will see two requests in the Network tab. This does **not** happen in production.

---

### 🌐 6. Fetching with Loading and Error States

Every request has **three possible screens**: waiting, failed, or done.

```jsx
function PatientsPage() {
  const [patients, setPatients] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    fetch("http://127.0.0.1:8000/patients")
      .then(res => {
        if (!res.ok) throw new Error("Server error " + res.status)
        return res.json()
      })
      .then(data => setPatients(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>⏳ Loading patients...</p>
  if (error) return <p style={{ color: "red" }}>❌ {error}</p>

  return (
    <ul>
      {patients.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  )
}
```

> 💡 **Tip**
>
> `fetch` does **not** throw on 404 or 500. Always check `res.ok` yourself.

---

### 🐍 7. Consuming FastAPI Endpoints

The hospital API (full code in the final project) offers:

| Method | URL | Purpose |
|---|---|---|
| GET | `/patients` | List all patients |
| GET | `/patients/{id}` | One patient (404 if missing) |
| POST | `/patients` | Add a patient (201 on success, 422 if invalid) |
| POST | `/login` | Check username and password |

**GET** is what we did above. **POST** sends JSON in the body, usually from an event handler (not from an effect):

```jsx
async function addPatient(newPatient) {
  const res = await fetch("http://127.0.0.1:8000/patients", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newPatient),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.detail?.[0]?.msg || data.detail || "Failed")
  return data
}
```

**Must-know for FastAPI:**

- 🔓 **CORS:** the browser blocks calls from `localhost:5173` to `127.0.0.1:8000` unless FastAPI adds `CORSMiddleware`.
- 🧾 **Errors:** validation errors (422) return `detail` as a **list** of objects with `msg`. Other errors return `detail` as a **string**.
- ▶️ **Two terminals:** one runs `uvicorn main:app --reload`, the other runs `npm run dev`.

---

## 💡 Real-Life Analogy

🍽️ **A restaurant order.**

Showing the menu (rendering) is instant. Ordering food (fetch) takes time. While you wait, the waiter shows **"Your food is on the way" (loading)**. If the kitchen is closed, you get a **message (error)**. When the food arrives, the table is **updated (state)**. If you change your order before it arrives, the waiter **cancels the old order (cleanup)**.

---

## 💻 Real-World Application

| Where | Effect used for |
|---|---|
| 🏥 Hospital portal | Load patients and appointments when a page opens |
| 🛒 Flipkart | Load product details when the URL id changes |
| 🎵 Spotify | Fetch the playlist, then start playback |
| 📈 Trading apps | Poll prices with a timer, clear it on exit |
| 💬 Chat apps | Open and close a WebSocket |

---

## 🔍 Industry Example

📘 **Scenario: Opening the patient list in a hospital portal**

1. 🖥️ React renders the page first, with `loading = true`, so the user instantly sees "Loading...".
2. 🪝 After the first draw, `useEffect(..., [])` runs and calls `fetch("/patients")`.
3. 🐍 FastAPI reads the database and returns JSON.
4. ✅ `setPatients(data)` and `setLoading(false)` run, and React re-renders the table.
5. 🚪 If the nurse leaves the page early, the cleanup cancels the request.

---

## 📊 Diagram

```
   Component renders (loading = true)
              │
              ▼
      Screen is drawn  ──► user sees "Loading..."
              │
              ▼
   useEffect runs  ──► fetch("/patients") ───► FastAPI ──► database
                                                   │
        setPatients(data) ◄──────── JSON ◄─────────┘
        setLoading(false)
              │
              ▼
      Re-render ──► table shown

   Dependency array:   []     = run once
                       [id]   = run when id changes
                       none   = run every render ⚠️
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Call `fetch` straight in the component." | Put it in `useEffect` (or an event handler for POST). |
| "No dependency array is fine." | It runs after every render and can loop forever. |
| "`fetch` throws an error on 404." | It doesn't. Check `res.ok`. |
| "`useEffect(async () => ...)` is OK." | The effect function can't be `async`. Write an inner async function or use `.then`. |
| "Two requests in the Network tab means a bug." | StrictMode runs effects twice in development only. |
| "Skip the loading and error screens." | Users need feedback. Always handle all three states. |
| "CORS is a React problem." | It is fixed in the **backend** with `CORSMiddleware`. |

---

## 💬 Interview Corner

**Q1. What is `useEffect` used for?**
To run side effects such as fetching data, timers, or event listeners after a component renders.

**Q2. What does an empty dependency array mean?**
The effect runs only once, after the first render.

**Q3. How do you avoid an infinite loop in `useEffect`?**
Provide the right dependency array and don't update a state value that is itself in the array without a condition.

**Q4. What is the cleanup function for?**
It undoes the effect (clear timers, remove listeners, abort requests) before the next run or when the component unmounts.

---

## 📝 Quick Summary

- ⚡ Side effects (fetch, timers, listeners) belong in `useEffect`.
- 🔁 `[]` = run once, `[x]` = run when `x` changes, no array = every render.
- 🚫 State update + no array = **infinite loop**.
- 🧹 Return a cleanup function to stop timers and abort requests.
- ⏳ Always keep `loading`, `error`, and `data` states.
- ✅ Check `res.ok` yourself.
- 🐍 FastAPI needs **CORS**. 422 errors have `detail` as a list.
- 📮 POST requests go in event handlers, not effects.

---

## 🎯 Class Activity

**🛠️ Activity: "Fetch and break it"**

1. Open `https://jsonplaceholder.typicode.com/users` in the browser to see JSON.
2. In a Vite React app, fetch this URL in `useEffect(..., [])` and show the names with loading and error states.
3. **Break it:** remove the dependency array and watch the Network tab. Then put it back.
4. Change the URL to a wrong one and confirm your error message appears.
5. Add a `useEffect` that sets `document.title` to the number of users loaded.

---

# 📋 Assignments — useEffect and Fetching Data from FastAPI

| Assignment |
|---|
| Fetch users from `jsonplaceholder.typicode.com/users` and show them in a list with proper keys. |
| Add loading and error screens, and test the error by using a wrong URL. |
| Remove the dependency array on purpose, take a screenshot of the Network tab, and explain what you saw. |
| Create a component with a counter that logs "count changed" using `useEffect` with `[count]`. Test with two other state values to prove they don't trigger it. |
| Build a clock that updates every second with `setInterval` and a cleanup function. Prove the cleanup works by hiding and showing the component. |
| Fetch one user by id from a text input (`/users/${id}`) and show the details, re-fetching when the id changes. |
| In your browser console, call a fetch to a 404 URL and show that it does not throw. Write the code that handles it. |
| Write down the steps to remove a CORS error between React and FastAPI, then try it with your hotel API. |

---
---

# 📚 React Router: Pages Without Reloading

## 🎯 Learning Objectives

- 🧭 Explain what **client-side routing** is
- 🧱 Use `BrowserRouter`, `Routes`, `Route`, and `Link`
- 🔗 Create **dynamic routes** and read them with `useParams`
- 🚦 Move between pages in code with `useNavigate`
- 🏥 Build hospital-style pages (patients list and patient details)

---

## 📖 Introduction

A React app is a **single page**. But users expect different URLs: `/patients`, `/patients/3`, `/login`. They also want the **Back button** to work and want to **bookmark** pages.

**React Router** shows different components for different URLs **without reloading the page**.

---

## 🧠 Detailed Notes

### 📦 1. Install and Set Up

```bash
npm install react-router-dom
```

Wrap the app once in `main.jsx`:

```jsx
import { BrowserRouter } from "react-router-dom"

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
)
```

---

### 🧱 2. The Four Building Blocks

| Piece | Job |
|---|---|
| `BrowserRouter` | Watches the browser URL and makes it available to the app |
| `Routes` | Looks at the URL and shows the **first matching** `Route` |
| `Route` | Says "this **path** shows this **element**" |
| `Link` | A clickable link that changes the URL **without reloading** |

```jsx
import { Routes, Route, Link } from "react-router-dom"

function App() {
  return (
    <>
      <nav>
        <Link to="/">Home</Link> | <Link to="/patients">Patients</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h1>Welcome</h1>} />
        <Route path="/patients" element={<PatientsPage />} />
        <Route path="*" element={<h1>404 - Page not found</h1>} />
      </Routes>
    </>
  )
}
```

> 💡 **Tip**
>
> Use `<Link>` instead of `<a href>`. A normal `<a>` reloads the whole page and **wipes your React state**.

`path="*"` matches everything else, so it is the **404 page**. Use `NavLink` instead of `Link` when you want the active link highlighted.

---

### 🔗 3. Dynamic Routes and `useParams`

A **colon** makes part of the path a variable:

```jsx
<Route path="/patients/:id" element={<PatientDetailsPage />} />
```

```jsx
import { useParams } from "react-router-dom"

function PatientDetailsPage() {
  const { id } = useParams()          // from /patients/7 → id is "7"
  return <h2>Details for patient #{id}</h2>
}
```

> ⚠️ **Important**
>
> Route params are always **strings**. `"7"` is not `7`. Use `Number(id)` when comparing with numbers.

Combine with `useEffect` to load the right record:

```jsx
useEffect(() => {
  fetch(`http://127.0.0.1:8000/patients/${id}`).then(...)
}, [id])          // re-fetch when the URL id changes
```

🤔 **Quick thinking question:** On `/patients/3` the user clicks a link to `/patients/4`. Does React create a new component or reuse the old one?

✅ **Answer:** It **reuses** it. Only `id` changes. This is why `[id]` in the dependency array matters.

---

### 🚦 4. Navigating in Code with `useNavigate`

```jsx
import { useNavigate } from "react-router-dom"

const navigate = useNavigate()

navigate("/patients")                   // go to a page
navigate("/patients", { replace: true }) // replace history (Back won't return here)
navigate(-1)                            // go back
```

Typical use: after a successful login or after saving a form.

---

### 🏥 5. Hospital Page Map

```
 URL                  Page                      Data
 /login               LoginPage                 POST /login
 /patients            PatientsPage (list)       GET /patients
 /patients/:id        PatientDetailsPage        GET /patients/{id}
 *                    NotFoundPage              none
```

In the list, link each row to its details page:

```jsx
<Link to={`/patients/${p.id}`}>View</Link>
```

---

### ⭐ 6. Handy Extras

| Feature | Use |
|---|---|
| `<Navigate to="/patients" replace />` | Redirect when a component is rendered |
| `useLocation()` | Read the current URL (and the `state` that was passed) |
| `useSearchParams()` | Read `?department=Cardiology` from the URL |
| Nested routes and `<Outlet />` | Shared layouts (a later topic) |

---

## 💡 Real-Life Analogy

🏨 **A hotel's floor directory.**

The building is **one structure** (a single page). The directory sign says *"Room 101 → Reception, Room 205 → Pharmacy"*. Following a sign takes you to a different **room** (component) **without leaving the building**. A **room number** like `/patients/7` is just a **variable** in the sign.

---

## 💻 Real-World Application

| Where | Routing |
|---|---|
| 🛒 Amazon | `/product/B09XYZ` loads a product by id |
| 🏥 Hospital portals | `/patients/102`, `/appointments`, `/billing` |
| ▶️ YouTube | `/watch?v=abc` |
| 💼 LinkedIn | `/in/username` |
| ⚙️ Admin dashboards | `/users`, `/reports`, `/settings` |

---

## 🔍 Industry Example

📘 **Scenario: A doctor opens a patient record**

1. 🖱️ The doctor clicks **View** on row 7. `Link to="/patients/7"` changes the URL without reloading.
2. 🧭 `Routes` finds the match `/patients/:id` and renders `PatientDetailsPage`.
3. 🔗 `useParams()` gives `id = "7"`.
4. 🪝 `useEffect(..., [id])` calls `GET /patients/7`.
5. 📋 The details appear. The doctor copies the URL and sends it to a colleague, who lands on the same page after logging in.
6. ⬅️ The **Back** button returns to `/patients`, and the list's search state may have been kept if it lives higher up.

---

## 📊 Diagram

```
   Browser URL           Routes                   Component shown
  ─────────────      ──────────────────         ──────────────────
   /                 path="/"                   Home
   /patients         path="/patients"           PatientsPage
   /patients/7       path="/patients/:id"       PatientDetailsPage  (id = "7")
   /xyz              path="*"                   NotFound

    <Link to="/patients/7">  ──►  URL changes  ──►  Routes re-match  ──►  new page
                                   (no page reload, React state stays)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Use `<a href>` for navigation." | Use `<Link to>`, or the page reloads. |
| "`useParams` gives a number." | It gives a **string**. |
| "I can use `<Link>` without `BrowserRouter`." | It must be inside a router, or you get an error. |
| "Forgot `[id]` in `useEffect`." | The details won't update when the URL changes. |
| "Imported from `react-router`." | In this course, import from `react-router-dom`. |
| "Refreshing `/patients/7` gives 404." | Not in Vite dev. In production hosting, configure a fallback to `index.html`. |

---

## 💬 Interview Corner

**Q1. What is the difference between `<a>` and `<Link>`?**
`<a>` triggers a full page reload. `<Link>` changes the URL and renders the matching component without reloading.

**Q2. How do you read a dynamic URL value?**
Define `path="/patients/:id"` and call `const { id } = useParams()`.

**Q3. What does `path="*"` do?**
It matches any URL that no other route matched, so it is used for a 404 page.

**Q4. How do you navigate programmatically?**
With the `useNavigate` hook, for example `navigate("/patients")`.

---

## 📝 Quick Summary

- 🧭 Client-side routing changes pages **without reloading**.
- 🧱 `BrowserRouter` wraps the app, `Routes` and `Route` map URLs to components.
- 🔗 `Link` replaces `<a>`.
- 🔢 `:id` in the path and `useParams()` give you the value as a **string**.
- 🚦 `useNavigate` changes the page from code.
- 🪝 Use `[id]` in `useEffect` for pages that depend on the URL.
- 🕳️ `path="*"` handles unknown URLs.

---

## 🎯 Class Activity

**🛠️ Activity: "Three-page site"**

1. Install `react-router-dom` and wrap the app in `BrowserRouter`.
2. Create `Home`, `PatientsPage` (a mock list with View links), and `PatientDetailsPage`.
3. Add routes `/`, `/patients`, `/patients/:id`, and a `*` 404 page.
4. In the details page, find the patient from the mock array using `Number(id)`.
5. Add a **Back** button using `navigate(-1)`.
6. Type a wrong URL and confirm the 404 page shows.

---

# 📋 Assignments — React Router

| Assignment |
|---|
| Create a navbar with `NavLink` so the active page link is highlighted, and show three pages. |
| Prove the difference between `<a>` and `<Link>`: type text in an input, click each one, and describe what happens to the text. |
| Add a `/doctors` list and `/doctors/:id` details page using mock data. |
| Show a patient's details by finding them in the array using `useParams`. Handle "patient not found" with a friendly message. |
| Add a "Back to list" button using `useNavigate`. |
| Make a custom 404 page with a link back to Home. |
| Use `useSearchParams` to read `?department=Cardiology` and filter the patients list. |
| Open your app on `/patients/5`, refresh the page, and explain why it works in Vite dev but needs configuration on real hosting. |

---
---

# 📚 Context API and Custom Hooks

## 🎯 Learning Objectives

- 🕳️ Explain the **prop drilling** problem
- 🌍 Create and use a context (`createContext`, `Provider`, `useContext`)
- 🔐 Structure an **AuthContext** with `user`, `login`, and `logout`
- 🪝 Write **custom hooks** (`useAuth`, `useFetch`)
- ♻️ Know when to use context and when not to

---

## 📖 Introduction

Some data is needed **everywhere**: the logged-in user, the theme, the language. Passing it as props through five layers of components is painful. This is called **prop drilling**.

**Context** lets a parent publish data and **any descendant** read it directly. **Custom hooks** let you package repeated logic (like fetching) into one reusable function.

---

## 🧠 Detailed Notes

### 🕳️ 1. The Prop Drilling Problem

```
 App (has user)
   └── Layout        ← must pass user
        └── Sidebar  ← must pass user
             └── ProfileBadge  ← finally uses user
```

`Layout` and `Sidebar` don't need `user`. They are just **delivery boys**.

---

### 🌍 2. Context in Three Steps

```jsx
// 1. CREATE
import { createContext } from "react"
export const AuthContext = createContext(null)

// 2. PROVIDE (wrap the part of the tree that needs it)
<AuthContext.Provider value={{ user, login, logout }}>
  <App />
</AuthContext.Provider>

// 3. CONSUME (any component inside)
import { useContext } from "react"
const { user } = useContext(AuthContext)
```

When the Provider's `value` changes, every component that **uses** the context re-renders.

---

### 🔐 3. AuthContext Structure

A provider component that holds the auth state:

```jsx
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)

  async function login(username, password) {
    // call POST /login, then:
    setUser(dataFromServer.user)
  }

  function logout() {
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
```

| Piece | Purpose |
|---|---|
| `user` | `null` when logged out, otherwise `{ username, role }` |
| `login()` | Calls the API and stores the user |
| `logout()` | Clears the user |
| `children` | Everything inside the provider |

> ℹ️ **Note**
>
> To stay logged in after a refresh, also save the user in `localStorage` and read it as the **initial state** (shown in the final project).

---

### 🪝 4. Custom Hooks

A **custom hook** is a normal function that:

- has a name starting with **`use`**
- calls other hooks inside it
- returns whatever the component needs

**Rules of hooks** (apply to custom hooks too):

1. Call hooks only at the **top level** (not inside `if`, loops, or nested functions).
2. Call hooks only from **components or other hooks**.

---

### 🔑 5. `useAuth`

Instead of writing `useContext(AuthContext)` everywhere:

```jsx
export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error("useAuth must be used inside <AuthProvider>")
  return ctx
}

// In any component:
const { user, logout } = useAuth()
```

It is shorter and gives a **clear error** if you forget the provider.

---

### 🌐 6. `useFetch` (Reusable API Hook)

Every page repeats `data`, `loading`, `error`, and a `useEffect`. Put them in one hook:

```jsx
export function useFetch(url) {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    const controller = new AbortController()
    setLoading(true)
    setError("")

    fetch(url, { signal: controller.signal })
      .then(res => {
        if (!res.ok) throw new Error("Server error " + res.status)
        return res.json()
      })
      .then(setData)
      .catch(err => { if (err.name !== "AbortError") setError(err.message) })
      .finally(() => setLoading(false))

    return () => controller.abort()
  }, [url])

  return { data, loading, error }
}

// Usage: one line replaces ~15
const { data: patients, loading, error } = useFetch(`${API}/patients`)
```

🤔 **Quick thinking question:** Two components both call `useFetch`. Do they share the same `data` state?

✅ **Answer:** No. Each call creates its **own** separate state. A custom hook shares **logic**, not **data**. To share data, use context.

---

### ⚖️ 7. When to Use Context

| ✅ Good for | ❌ Not for |
|---|---|
| Logged-in user | Data used by just two components (use props) |
| Theme and language | Frequently changing values (re-renders every consumer) |
| App-wide settings | Server data that needs caching (later: libraries like TanStack Query) |

---

## 💡 Real-Life Analogy

📢 **A hospital PA system.**

Prop drilling is like passing a note from person to person across ten desks. **Context** is the hospital loudspeaker: the announcement ("the logged-in doctor is Dr. Rao") is made once, and anyone who tunes in (`useContext`) can hear it.

A **custom hook** is a **recipe card**: "How to fetch data: steps 1 to 5." Each chef (component) follows the same card but cooks their **own dish** (own state).

---

## 💻 Real-World Application

| Where | Context or custom hooks |
|---|---|
| 🔐 Every login-based app | `AuthContext` for the current user |
| 🌙 YouTube, GitHub | Theme (dark/light) context |
| 🌍 Netflix | Language/locale context |
| 🛒 E-commerce | Cart context |
| 🧰 Company codebases | `useFetch`, `useDebounce`, `useLocalStorage` hooks |

---

## 🔍 Industry Example

📘 **Scenario: Showing the doctor's name in a hospital app's header**

1. 🔑 The doctor logs in. `login()` sends `POST /login`, and `setUser({ username: "admin", role: "admin" })` runs inside `AuthProvider`.
2. 🌍 The provider's `value` changes, so React re-renders components that called `useAuth()`.
3. 🧭 The `Navbar` (deep in the tree) reads `user` and shows "👤 admin", with no props passed through other layers.
4. 🛡️ The route guard (next topic) reads the same `user` to decide whether to show the patients page.
5. 🚪 Logout calls `setUser(null)`, and the navbar and routes update everywhere at once.

---

## 📊 Diagram

```
              <AuthProvider>  (user, login, logout)
                    │
                  <App>
        ┌───────────┼───────────────┐
     Navbar     PatientsPage    ProtectedRoute
        │            │                │
   useAuth()     useAuth()        useAuth()
   → user         → user           → user
      (all read the same value directly, no props)

   Custom hook:  useFetch(url) ─► { data, loading, error }
                 (logic is shared, state is separate per component)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Context is a replacement for all props." | Use props for local data and context for app-wide data. |
| "Components outside the Provider can read it." | They get the default value (`null`), so wrap enough of the app. |
| "A custom hook shares state between components." | It shares logic. Each call has its own state. |
| "Custom hook names can be anything." | They must start with `use`. |
| "Call hooks inside `if` statements." | Hooks must run in the same order every render. |
| "Putting everything in one giant context." | Split by purpose (auth, theme). Changes re-render all consumers. |

---

## 💬 Interview Corner

**Q1. What problem does Context solve?**
Prop drilling: passing data through many levels of components that don't use it.

**Q2. How do you create and use a context?**
`createContext()`, wrap with `<Context.Provider value={...}>`, and read it with `useContext(Context)`.

**Q3. What is a custom hook?**
A function starting with `use` that uses other hooks to package reusable logic.

**Q4. Do two components using the same custom hook share state?**
No. Each call has its own state. A custom hook reuses logic only.

---

## 📝 Quick Summary

- 🕳️ **Prop drilling** = passing props through components that don't need them.
- 🌍 Context = `createContext` + `Provider` + `useContext`.
- 🔐 `AuthContext` holds `user`, `login`, and `logout`.
- 🪝 Custom hooks are `use...` functions that reuse logic.
- 🔑 `useAuth` wraps `useContext` with a helpful error.
- 🌐 `useFetch` bundles `data`, `loading`, `error`, and the effect.
- 📏 Follow the **rules of hooks**.
- ⚖️ Use context only for data needed in many places.

---

## 🎯 Class Activity

**🛠️ Activity: "Theme and login switch"**

1. Create `ThemeContext` with `theme` and `toggleTheme`.
2. Wrap the app in a `ThemeProvider` and show a toggle button in a deeply nested component.
3. Create a `useTheme` hook that wraps `useContext`.
4. Move your fetch code into a `useFetch(url)` hook and use it in two pages.
5. Show that two components using `useFetch` have **separate** data by logging inside them.

---

# 📋 Assignments — Context API and Custom Hooks

| Assignment |
|---|
| Build a 4-level component tree and pass a username using props. Then rewrite it with context and compare. |
| Create a `ThemeContext` with a toggle and apply different background colors based on the theme. |
| Create `AuthContext` with mock `login(username)` and `logout()`. Show the username in a navbar. |
| Write a `useAuth` hook that throws an error if used outside the provider. Trigger that error on purpose and note the message. |
| Write a `useFetch(url)` hook and use it in two different pages. |
| Write a `useLocalStorage(key, initial)` hook that works like `useState` but remembers values after refresh. |
| Write a `useToggle()` hook that returns `[value, toggle]`. Use it for show/hide of a panel. |
| Explain in 5 lines why `useFetch` called in two components makes two separate requests, and how you could share data. |

---
---

# 📚 Protected Routes

## 🎯 Learning Objectives

- 🛡️ Explain what a **protected route** is and why apps need it
- 🧱 Build a `ProtectedRoute` component
- ↪️ Redirect to login and return the user to the page they wanted
- 👥 Restrict pages by **role**
- 🔒 Understand why frontend protection is **not real security**

---

## 📖 Introduction

Some pages must only be visible to logged-in users: the patients list, billing, reports. If someone types `/patients` without logging in, they should be sent to `/login`.

A **protected route** checks the **auth state** (from `useAuth`) before showing a page.

---

## 🧠 Detailed Notes

### 🧱 1. The `ProtectedRoute` Component

```jsx
import { Navigate, useLocation } from "react-router-dom"
import { useAuth } from "../hooks/useAuth"

function ProtectedRoute({ children }) {
  const { user } = useAuth()
  const location = useLocation()

  if (!user) {
    return <Navigate to="/login" replace state={{ from: location }} />
  }

  return children
}
```

- `<Navigate>` redirects when rendered.
- `replace` removes the protected URL from history, so **Back** doesn't bounce the user in a loop.
- `state={{ from: location }}` remembers the page the user wanted.

---

### 🛣️ 2. Using It in Routes

```jsx
<Routes>
  <Route path="/login" element={<LoginPage />} />

  <Route path="/patients" element={
    <ProtectedRoute><PatientsPage /></ProtectedRoute>
  } />

  <Route path="/patients/:id" element={
    <ProtectedRoute><PatientDetailsPage /></ProtectedRoute>
  } />
</Routes>
```

Public pages (`/login`) stay unwrapped.

---

### ↪️ 3. Returning to the Wanted Page After Login

```jsx
function LoginPage() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const from = location.state?.from?.pathname || "/patients"

  async function handleSubmit(e) {
    e.preventDefault()
    await login(username, password)
    navigate(from, { replace: true })
  }
  // ...
}
```

A user who opened `/patients/7` while logged out logs in and lands on **`/patients/7`**, not on a generic home page.

---

### 👥 4. Restricting by Role

```jsx
function ProtectedRoute({ children, roles }) {
  const { user } = useAuth()
  const location = useLocation()

  if (!user) return <Navigate to="/login" replace state={{ from: location }} />
  if (roles && !roles.includes(user.role)) return <p>🚫 You are not allowed to view this page.</p>

  return children
}

<Route path="/billing" element={
  <ProtectedRoute roles={["admin"]}><BillingPage /></ProtectedRoute>
} />
```

Also hide **menu links** a user can't use (`{user.role === "admin" && <Link ...>}`).

---

### 🔒 5. The Honest Truth About Security

> ⚠️ **Important**
>
> Everything in React runs in the **user's browser**, and users can change it. Protected routes only improve **user experience**. The **backend must check permissions** on every API call (tokens, FastAPI dependencies, roles). Never trust the frontend.

| Layer | Job |
|---|---|
| React `ProtectedRoute` | Hide pages, redirect nicely |
| FastAPI | **Actually** allow or deny the data |

🤔 **Quick thinking question:** A user edits `localStorage` to pretend to be an admin and opens `/billing`. What should still protect the data?

✅ **Answer:** The backend. The API must verify the real token and role before returning billing data.

---

## 💡 Real-Life Analogy

🏥 **A hospital ward gate with a security guard.**

The guard (`ProtectedRoute`) checks your **visitor pass (user)** before letting you in. No pass means you're sent to the **reception desk (`/login`)**, and after getting a pass you're taken **straight to the ward you wanted**. Some wards (ICU) need a **special badge (role)**. But the guard is only the first line: **locked cabinets inside (backend permissions)** protect real records.

---

## 💻 Real-World Application

| Where | Protected routes |
|---|---|
| 🏦 Net banking | Dashboard only after login |
| 🏥 Hospital portal | Patient records for staff only |
| 🛒 Amazon | `/orders` needs login, `/product/...` is public |
| 🧑‍💼 Admin panels | `/users` for admins only |
| 💼 LinkedIn | Messaging needs a signed-in user |

---

## 🔍 Industry Example

📘 **Scenario: A nurse opens a saved link to a patient record**

1. 🔗 The nurse clicks `/patients/7` from an email, but her session has expired (`user = null`).
2. 🛡️ `ProtectedRoute` sees no user and renders `<Navigate to="/login" state={{ from }} />`.
3. 🔑 She logs in. `login()` stores the user.
4. ↪️ `LoginPage` reads `location.state.from` and navigates to `/patients/7`.
5. 📋 The page loads the patient from the API, where FastAPI checks her token again.
6. 🚪 If she logs out, `user` becomes `null` and every protected page redirects.

---

## 📊 Diagram

```
   User opens /patients/7
            │
     ┌──────▼───────┐
     │ ProtectedRoute│
     └──────┬───────┘
      logged in? ── YES ──► (role allowed?) ── YES ──► show PatientDetailsPage
            │                       │
            NO                      NO
            ▼                       ▼
   <Navigate to="/login">     "🚫 not allowed"
   remember where from
            │
        Login success
            │
   navigate(from) ──► back to /patients/7
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Protected routes make my app secure." | Only the backend can truly secure data. |
| "I can redirect with `navigate()` in the render body." | Use `<Navigate>` when rendering, and `useNavigate` in handlers/effects. |
| "No need for `replace`." | Without it, **Back** returns to the protected URL and redirects again. |
| "Logged-out flash of content." | Check the stored user **before** rendering (use it as initial state). |
| "Only hide the link and the route is safe." | The URL can still be typed, so guard the route too. |
| "Store passwords in `localStorage`." | Never. Store only a token or basic user info. |

---

## 💬 Interview Corner

**Q1. What is a protected route?**
A route that checks authentication (and maybe role) before rendering a page, and redirects to login otherwise.

**Q2. How does React Router redirect?**
Render `<Navigate to="/login" />`, or call `navigate()` from `useNavigate` in an event handler.

**Q3. Is hiding routes in React enough for security?**
No. Users control the browser, so the API must enforce permissions.

**Q4. How do you send the user back to the page they originally wanted?**
Pass `state={{ from: location }}` in `<Navigate>`, then read `location.state.from` after login.

---

## 📝 Quick Summary

- 🛡️ `ProtectedRoute` wraps pages that need login.
- 🔁 `<Navigate replace>` sends logged-out users to `/login`.
- ↪️ Pass `from` in state and return after login.
- 👥 Add a `roles` prop for role-based access.
- 🔒 Frontend protection is **UX only**. The backend decides.
- 👁️ Hide menu links the user can't use.
- 🧠 Auth state comes from `useAuth()`.

---

## 🎯 Class Activity

**🛠️ Activity: "Lock the doors"**

1. Using your `AuthContext`, create a `ProtectedRoute`.
2. Protect `/patients` and `/patients/:id`, and leave `/login` public.
3. Try opening `/patients` while logged out and confirm the redirect.
4. Log in and confirm you return to the page you wanted.
5. Add a `/billing` route only for role `admin`, and test with a `staff` user.
6. Open DevTools and try to change `localStorage` to fake a role. Discuss what should stop you.

---

# 📋 Assignments — Protected Routes

| Assignment |
|---|
| Build `ProtectedRoute` and protect two pages. Show screenshots of the logged-out redirect and logged-in access. |
| Add `replace` to the `Navigate` and compare how the Back button behaves with and without it. |
| Implement "return to the page I wanted" after login using `location.state`. |
| Add a role-based route (`/billing`) that only `admin` can open, with a friendly "not allowed" message for others. |
| Hide the Billing link in the navbar for non-admin users. Explain why you should still protect the route. |
| Add a logout button that clears the user and returns to `/login`. |
| Make the login persist after refresh using `localStorage`, and confirm protected pages don't flash the login page. |
| Write 6 to 8 lines on what the FastAPI backend should do to truly protect `GET /patients`. |

---
---

# 📚 Performance Basics: Re-renders, `React.memo`, `useCallback`, `useMemo`

## 🎯 Learning Objectives

- 🔄 Explain **when React re-renders** a component
- 🧊 Use `React.memo` to skip unnecessary child renders
- 🔗 Use `useCallback` to keep function props stable
- 🧮 Use `useMemo` to avoid repeating expensive calculations
- ⚖️ Know **when not to optimize**

---

## 📖 Introduction

React is fast by default. But when a page has **thousands of rows** or heavy calculations, typing in a search box can feel laggy. Understanding re-renders helps you fix this **only where needed**.

> ⚠️ **Important**
>
> **Measure first, optimize later.** Most components don't need `memo`, `useCallback`, or `useMemo`.

---

## 🧠 Detailed Notes

### 🔄 1. When Does React Re-render?

A component re-renders when:

1. Its **own state** changes
2. Its **parent re-renders** (even if its props are the same!)
3. A **context** it uses changes

```jsx
function Parent() {
  const [search, setSearch] = useState("")
  return (
    <>
      <input value={search} onChange={e => setSearch(e.target.value)} />
      <HugeTable />        {/* re-renders on EVERY keystroke */}
    </>
  )
}
```

Re-rendering means "React runs your function again". It does not always mean the screen changes, but it costs time.

> 💡 **Tip**
>
> Add `console.log("Row rendered", patient.id)` inside a component to **see** re-renders.

---

### 🧊 2. `React.memo`: Skip Re-render if Props Are the Same

```jsx
import { memo } from "react"

function PatientRow({ patient }) {
  console.log("render row", patient.id)
  return <tr><td>{patient.name}</td></tr>
}

export default memo(PatientRow)
```

With `memo`, React compares the **old and new props**. If every prop is equal, the component is **skipped**.

Comparison is **shallow**: numbers and strings compare by value, but **objects, arrays, and functions compare by reference**. A new object or function created on each parent render is "different", and memo won't help.

---

### 🔗 3. `useCallback`: Keep a Function the Same

```jsx
function PatientsPage() {
  const [search, setSearch] = useState("")

  // ❌ new function every render, so memo(PatientRow) is useless
  const handleSelect = (id) => console.log(id)

  // ✅ same function between renders
  const handleSelect2 = useCallback((id) => console.log(id), [])

  return rows.map(p => <PatientRow key={p.id} patient={p} onSelect={handleSelect2} />)
}
```

`useCallback(fn, deps)` returns the **same function** until a dependency changes. It is useful **only when** the function goes to a `memo` child or into a dependency array.

---

### 🧮 4. `useMemo`: Keep a Calculated Value

```jsx
const visible = useMemo(() => {
  return transactions.filter(t =>
    t.patientName.toLowerCase().includes(search.toLowerCase())
  )
}, [transactions, search])

const total = useMemo(
  () => visible.reduce((sum, t) => sum + t.amount, 0),
  [visible]
)
```

The calculation reruns **only when** `transactions` or `search` changes. If some **unrelated** state (like a "dark mode" toggle) causes a re-render, the old result is reused.

| Hook | Remembers | Use when |
|---|---|---|
| `React.memo` | A **component's output** | A child re-renders with the same props |
| `useCallback` | A **function** | Passing a function to a memoized child |
| `useMemo` | A **calculated value** | Calculation is slow, or you need a stable object/array |

---

### 🧪 5. Real Scenario: Filtering Hospital Transactions

The billing page has **5,000 transactions**, a search box, and a theme toggle.

```jsx
function BillingPage({ transactions }) {
  const [search, setSearch] = useState("")
  const [dark, setDark] = useState(false)

  const visible = useMemo(
    () => transactions.filter(t => t.patientName.toLowerCase().includes(search.toLowerCase())),
    [transactions, search]
  )

  const total = useMemo(() => visible.reduce((s, t) => s + t.amount, 0), [visible])

  return (
    <div className={dark ? "dark" : ""}>
      <button onClick={() => setDark(!dark)}>Toggle theme</button>
      <input value={search} onChange={e => setSearch(e.target.value)} />
      <p>Total: ₹{total}</p>
      {visible.map(t => <TransactionRow key={t.id} transaction={t} />)}
    </div>
  )
}

const TransactionRow = memo(function TransactionRow({ transaction }) {
  return <p>{transaction.patientName}: ₹{transaction.amount}</p>
})
```

- Toggling the theme re-renders `BillingPage`, but filtering and summing are **skipped** (`useMemo`) and the rows are **skipped** (`memo`).
- Typing in the search recalculates, which is **correct**.

🤔 **Quick thinking question:** Should you wrap a 3-item list filter in `useMemo`?

✅ **Answer:** No. The calculation takes microseconds, and `useMemo` itself costs a little. Use it for **heavy** work or for **stable references**.

---

### 🧰 6. Other Easy Wins

| Technique | Benefit |
|---|---|
| Stable `key={id}` | Correct, efficient list updates |
| Keep state **close to where it's used** | Fewer components re-render |
| Don't create components inside components | They would be rebuilt every render |
| React DevTools **Profiler** | Shows what rendered and how long it took |
| Pagination or virtualized lists | Don't render 5,000 rows at once |

> ℹ️ **Note**
>
> Newer React versions have an optional **React Compiler** that adds much of this memoization automatically. Understanding the concepts still matters for interviews and older code.

---

## 💡 Real-Life Analogy

🧑‍🍳 **A chef with a notebook.**

- `React.memo` = "If the **same order** comes again, serve the **previous dish** without cooking."
- `useMemo` = "I already **calculated the bill total**. If the items haven't changed, I won't add them again."
- `useCallback` = "I keep the **same phone number card** for the delivery guy. If I print a fresh card each time, he thinks it's a new number."

But writing everything in the notebook takes effort too, so use it only for **dishes that take long**.

---

## 💻 Real-World Application

| Where | Optimization |
|---|---|
| 📊 Dashboards with big tables | `memo` rows and `useMemo` for totals |
| 💬 Chat apps | Memoized message items |
| 🔍 Search-as-you-type | Debounce plus `useMemo` filtering |
| 🛒 Product grids | Memoized cards that don't re-render on cart change |
| 🏥 Billing and reports | Heavy filtering and summing |

---

## 🔍 Industry Example

📘 **Scenario: A lagging billing screen**

1. 🐢 Accountants say typing in the search box is slow. The page has 5,000 rows.
2. 🔬 A developer opens the React **Profiler** and sees every row re-rendering on each keystroke.
3. 🧊 She wraps `TransactionRow` in `memo`, and rows with unchanged data are skipped.
4. 🧮 She moves the filtering and total into `useMemo`.
5. 🔗 A `handleSelect` function passed to rows is wrapped in `useCallback` so `memo` isn't defeated.
6. 📄 Finally she adds pagination (50 rows per page), the biggest improvement of all.

---

## 📊 Diagram

```
   Parent state changes
           │
   Parent re-renders
           │
   ┌───────┴────────────────────────────┐
   │ Plain child        → re-renders    │
   │ memo child         → props same?   │
   │       ├─ YES (primitives, stable   │
   │       │   refs via useCallback /   │
   │       │   useMemo) → SKIPPED ✅    │
   │       └─ NO (new object/function) │
   │              → re-renders ❌       │
   └────────────────────────────────────┘

   useMemo:  deps same? ──YES──► reuse old value
                      └──NO───► recalculate
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Wrap everything in `memo` and `useMemo`." | They have a cost. Optimize only measured problems. |
| "`memo` works even if I pass a new function each time." | A new function is a new reference, so use `useCallback`. |
| "`useCallback` makes the function faster." | It only keeps the same reference. |
| "A re-render means the DOM is rebuilt." | Re-render means the function re-runs. React updates the DOM only where output changed. |
| "Wrong dependency arrays are harmless." | Stale values and bugs. List everything used. |
| "Store the filtered list in state." | Calculate it, with `useMemo` if heavy. |

---

## 💬 Interview Corner

**Q1. When does a React component re-render?**
When its state changes, when its parent re-renders, or when a context it consumes changes.

**Q2. What does `React.memo` do?**
It skips re-rendering a component if its props are shallowly equal to the previous props.

**Q3. What is the difference between `useMemo` and `useCallback`?**
`useMemo` caches a **calculated value**. `useCallback` caches a **function**.

**Q4. Why can `memo` fail to help?**
Because props like objects, arrays, and functions are re-created on every parent render and fail the shallow comparison.

---

## 📝 Quick Summary

- 🔄 Re-render triggers: own state, parent render, context change.
- 🧊 `memo(Component)` skips renders when props are unchanged.
- 🔗 `useCallback` keeps function props stable.
- 🧮 `useMemo` caches expensive results (filtering, totals).
- 📏 Dependencies must list everything used.
- 📏 Measure with Profiler and `console.log` first.
- 📄 Pagination often beats micro-optimizations.
- ⚖️ Don't optimize small, fast components.

---

## 🎯 Class Activity

**🛠️ Activity: "Watch the renders"**

1. Create a page with 200 rows and a search input. Add `console.log("row", id)` inside the row component.
2. Type in the search box and watch the console. Count the logs.
3. Wrap the row in `memo` and filter with `useMemo`. Compare the logs.
4. Pass `onSelect={() => ...}` to the rows and see `memo` stop working. Fix it with `useCallback`.
5. Add a "dark mode" toggle and confirm that toggling doesn't re-run the filter (add a `console.log` inside `useMemo`).

---

# 📋 Assignments — Performance Basics

| Assignment |
|---|
| Add `console.log` inside a row component and count how many renders happen while typing in a search box (before optimization). |
| Wrap the row in `React.memo` and record the new render count. |
| Pass an inline function prop to the memoized row, show that renders increase again, then fix it with `useCallback`. |
| Create 5,000 fake transactions and filter them with `useMemo`. Time it with `console.time`. |
| Show that toggling an unrelated state (theme) does not rerun the `useMemo` calculation. |
| Pass a new object literal (`style={{ color: "red" }}`) to a memoized child and explain why it re-renders. |
| Open React DevTools Profiler, record typing in the search box, and screenshot the flame chart before and after optimization. |
| Add pagination (20 rows per page) and compare it with `memo` and `useMemo` in terms of speed. Write your conclusion in 5 lines. |

---
---

# 📚 Hospital App v2: Fetching, Routing, Context and Protected Pages

## 🎯 Learning Objectives

- 🧩 Combine **useEffect, React Router, Context, custom hooks, and protected routes** in one app
- 🐍 Connect a React app to a **FastAPI** hospital backend
- 🔐 Add login, logout, and guarded pages
- 🏗️ Organize a growing React project into folders

---

## 📖 Introduction

In the earlier project, the hospital app used mock data. Now the data comes from **FastAPI**, pages have their own **URLs**, and access needs a **login**. Every piece comes from the topics above.

---

## 🧠 Detailed Notes

### 🐍 1. Backend

**Setup:**

```bash
mkdir hospital-api && cd hospital-api
pip install fastapi "uvicorn[standard]"
```

**📁 `backend/main.py`**

```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="Hospital API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "nurse": {"password": "nurse123", "role": "staff"},
}

PATIENTS = [
    {"id": 1, "name": "Asha Verma", "age": 45, "department": "Cardiology"},
    {"id": 2, "name": "Ravi Kumar", "age": 62, "department": "Neurology"},
    {"id": 3, "name": "Meena Iyer", "age": 8, "department": "Pediatrics"},
    {"id": 4, "name": "Sanjay Gupta", "age": 51, "department": "Cardiology"},
]


class LoginIn(BaseModel):
    username: str
    password: str


class PatientIn(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0, le=120)
    department: str = Field(min_length=2)


@app.post("/login")
def login(body: LoginIn):
    user = USERS.get(body.username)
    if not user or user["password"] != body.password:
        raise HTTPException(status_code=401, detail="Wrong username or password")
    return {"user": {"username": body.username, "role": user["role"]}}


@app.get("/patients")
def list_patients():
    return PATIENTS


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for p in PATIENTS:
        if p["id"] == patient_id:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/patients", status_code=201)
def add_patient(body: PatientIn):
    new = {"id": max([p["id"] for p in PATIENTS], default=0) + 1, **body.model_dump()}
    PATIENTS.append(new)
    return new
```

Run it with `uvicorn main:app --reload` from the `backend` folder.

> ℹ️ **Note**
>
> This login is **simplified for teaching** (no tokens, no hashing, data in memory). Real apps use hashed passwords and JWT tokens, and FastAPI checks the token on every protected endpoint.

---

### 🚀 2. Frontend Setup

```bash
npm create vite@latest hospital-app-v2 -- --template react
cd hospital-app-v2
npm install
npm install react-router-dom
npm run dev
```

**Folder structure:**

```
src/
 ├── api.js
 ├── context/
 │     ├── AuthContext.js
 │     └── AuthProvider.jsx
 ├── hooks/
 │     ├── useAuth.js
 │     └── useFetch.js
 ├── components/
 │     ├── Navbar.jsx
 │     ├── PatientRow.jsx
 │     └── ProtectedRoute.jsx
 ├── pages/
 │     ├── LoginPage.jsx
 │     ├── PatientsPage.jsx
 │     └── PatientDetailsPage.jsx
 ├── App.jsx
 ├── App.css
 ├── index.css
 └── main.jsx
```

---

### 🧱 3. Shared Pieces

**📁 `src/api.js`**

```js
export const API = "http://127.0.0.1:8000"

export function errorText(data, fallback = "Something went wrong") {
  if (!data || !data.detail) return fallback
  if (Array.isArray(data.detail)) return data.detail.map((d) => d.msg).join(", ")
  return data.detail
}
```

**📁 `src/context/AuthContext.js`**

```js
import { createContext } from "react"

export const AuthContext = createContext(null)
```

**📁 `src/context/AuthProvider.jsx`**

```jsx
import { useState } from "react"
import { AuthContext } from "./AuthContext"
import { API, errorText } from "../api"

function loadUser() {
  try {
    return JSON.parse(localStorage.getItem("user"))
  } catch {
    return null
  }
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(loadUser)

  async function login(username, password) {
    const res = await fetch(`${API}/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    })
    const data = await res.json()
    if (!res.ok) throw new Error(errorText(data, "Login failed"))

    setUser(data.user)
    localStorage.setItem("user", JSON.stringify(data.user))
  }

  function logout() {
    setUser(null)
    localStorage.removeItem("user")
  }

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
```

**📁 `src/hooks/useAuth.js`**

```js
import { useContext } from "react"
import { AuthContext } from "../context/AuthContext"

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error("useAuth must be used inside <AuthProvider>")
  return ctx
}
```

**📁 `src/hooks/useFetch.js`**

```js
import { useState, useEffect, useCallback } from "react"

export function useFetch(url) {
  const [tick, setTick] = useState(0)
  const [result, setResult] = useState({ key: null, data: null, error: "" })

  const key = `${url}#${tick}`          // identifies THIS request

  useEffect(() => {
    const controller = new AbortController()

    fetch(url, { signal: controller.signal })
      .then((res) => {
        if (!res.ok) throw new Error(`Server error ${res.status}`)
        return res.json()
      })
      .then((data) => setResult({ key, data, error: "" }))
      .catch((err) => {
        if (err.name !== "AbortError") setResult({ key, data: null, error: err.message })
      })

    return () => controller.abort()
  }, [url, key])

  const reload = useCallback(() => setTick((t) => t + 1), [])

  const loading = result.key !== key    // the saved result is not for this request yet
  return { data: result.data, loading, error: loading ? "" : result.error, reload }
}
```

`reload()` changes `tick`, which changes `key`, which is in the dependency array, so the effect runs again.

> ℹ️ **Note**
>
> This is the same idea as the simple `useFetch` from the Context and Hooks topic. The only difference is that **loading is worked out** ("the saved result doesn't belong to the current request yet") instead of calling `setLoading(true)` at the start of the effect. It avoids an extra render and a lint warning in newer React setups.

---

### 🧭 4. Components

**📁 `src/components/ProtectedRoute.jsx`**

```jsx
import { Navigate, useLocation } from "react-router-dom"
import { useAuth } from "../hooks/useAuth"

function ProtectedRoute({ children, roles }) {
  const { user } = useAuth()
  const location = useLocation()

  if (!user) {
    return <Navigate to="/login" replace state={{ from: location }} />
  }

  if (roles && !roles.includes(user.role)) {
    return <p className="error">🚫 You are not allowed to view this page.</p>
  }

  return children
}

export default ProtectedRoute
```

**📁 `src/components/Navbar.jsx`**

```jsx
import { NavLink, useNavigate } from "react-router-dom"
import { useAuth } from "../hooks/useAuth"

function Navbar() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  function handleLogout() {
    logout()
    navigate("/login")
  }

  return (
    <nav className="navbar">
      <strong>🏥 Hospital App</strong>
      {user && <NavLink to="/patients">Patients</NavLink>}
      <span className="spacer" />
      {user ? (
        <>
          <span>👤 {user.username} ({user.role})</span>
          <button onClick={handleLogout}>Logout</button>
        </>
      ) : (
        <NavLink to="/login">Login</NavLink>
      )}
    </nav>
  )
}

export default Navbar
```

**📁 `src/components/PatientRow.jsx`**

```jsx
import { memo } from "react"
import { Link } from "react-router-dom"

function PatientRow({ patient }) {
  return (
    <tr>
      <td>{patient.id}</td>
      <td>{patient.name}</td>
      <td>{patient.age}</td>
      <td>{patient.department}</td>
      <td><Link to={`/patients/${patient.id}`}>View</Link></td>
    </tr>
  )
}

export default memo(PatientRow)
```

---

### 📄 5. Pages

**📁 `src/pages/LoginPage.jsx`**

```jsx
import { useState } from "react"
import { useLocation, useNavigate } from "react-router-dom"
import { useAuth } from "../hooks/useAuth"

function LoginPage() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const from = location.state?.from?.pathname || "/patients"

  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")

  async function handleSubmit(e) {
    e.preventDefault()
    setError("")
    try {
      await login(username.trim(), password)
      navigate(from, { replace: true })
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <section className="card narrow">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="field">
          <label htmlFor="username">Username</label>
          <input id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div className="field">
          <label htmlFor="password">Password</label>
          <input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button type="submit">Login</button>
        {error && <p className="error">{error}</p>}
      </form>
      <p className="hint">Try admin / admin123 or nurse / nurse123</p>
    </section>
  )
}

export default LoginPage
```

**📁 `src/pages/PatientsPage.jsx`**

```jsx
import { useMemo, useState } from "react"
import { API, errorText } from "../api"
import { useFetch } from "../hooks/useFetch"
import PatientRow from "../components/PatientRow"

const emptyForm = { name: "", age: "", department: "" }

function PatientsPage() {
  const { data: patients, loading, error, reload } = useFetch(`${API}/patients`)
  const [search, setSearch] = useState("")
  const [form, setForm] = useState(emptyForm)
  const [formError, setFormError] = useState("")

  const visible = useMemo(() => {
    const text = search.trim().toLowerCase()
    return (patients ?? []).filter(
      (p) =>
        p.name.toLowerCase().includes(text) ||
        p.department.toLowerCase().includes(text)
    )
  }, [patients, search])

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  async function handleAdd(e) {
    e.preventDefault()
    setFormError("")
    try {
      const res = await fetch(`${API}/patients`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: form.name.trim(),
          age: Number(form.age),
          department: form.department.trim(),
        }),
      })
      const body = await res.json()
      if (!res.ok) throw new Error(errorText(body))
      setForm(emptyForm)
      reload()
    } catch (err) {
      setFormError(err.message)
    }
  }

  return (
    <>
      <section className="card">
        <h2>Patients</h2>
        <input
          placeholder="Search by name or department..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />

        {loading && <p>⏳ Loading patients...</p>}
        {error && <p className="error">❌ {error}. Is the backend running?</p>}

        {!loading && !error && (
          visible.length === 0 ? (
            <p className="hint">No patients found.</p>
          ) : (
            <table>
              <thead>
                <tr><th>ID</th><th>Name</th><th>Age</th><th>Department</th><th></th></tr>
              </thead>
              <tbody>
                {visible.map((p) => <PatientRow key={p.id} patient={p} />)}
              </tbody>
            </table>
          )
        )}
      </section>

      <section className="card">
        <h2>Add Patient</h2>
        <form onSubmit={handleAdd} className="inline-form">
          <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
          <input name="age" type="number" placeholder="Age" value={form.age} onChange={handleChange} />
          <input name="department" placeholder="Department" value={form.department} onChange={handleChange} />
          <button type="submit">Add</button>
        </form>
        {formError && <p className="error">{formError}</p>}
      </section>
    </>
  )
}

export default PatientsPage
```

**📁 `src/pages/PatientDetailsPage.jsx`**

```jsx
import { Link, useNavigate, useParams } from "react-router-dom"
import { API } from "../api"
import { useFetch } from "../hooks/useFetch"

function PatientDetailsPage() {
  const { id } = useParams()
  const navigate = useNavigate()
  const { data: patient, loading, error } = useFetch(`${API}/patients/${id}`)

  if (loading) return <p>⏳ Loading...</p>
  if (error) {
    return (
      <section className="card">
        <p className="error">Patient not found or server error ({error}).</p>
        <Link to="/patients">← Back to patients</Link>
      </section>
    )
  }

  return (
    <section className="card">
      <h2>{patient.name}</h2>
      <p>🆔 ID: {patient.id}</p>
      <p>🎂 Age: {patient.age}</p>
      <p>🏥 Department: {patient.department}</p>
      <button onClick={() => navigate(-1)}>← Back</button>
    </section>
  )
}

export default PatientDetailsPage
```

---

### 🧭 6. Wiring: `App.jsx` and `main.jsx`

**📁 `src/App.jsx`**

```jsx
import { Navigate, Route, Routes } from "react-router-dom"
import Navbar from "./components/Navbar"
import ProtectedRoute from "./components/ProtectedRoute"
import LoginPage from "./pages/LoginPage"
import PatientsPage from "./pages/PatientsPage"
import PatientDetailsPage from "./pages/PatientDetailsPage"
import "./App.css"

function App() {
  return (
    <>
      <Navbar />
      <main className="app">
        <Routes>
          <Route path="/" element={<Navigate to="/patients" replace />} />
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/patients"
            element={<ProtectedRoute><PatientsPage /></ProtectedRoute>}
          />
          <Route
            path="/patients/:id"
            element={<ProtectedRoute><PatientDetailsPage /></ProtectedRoute>}
          />
          <Route path="*" element={<h2>404 - Page not found</h2>} />
        </Routes>
      </main>
    </>
  )
}

export default App
```

**📁 `src/main.jsx`**

```jsx
import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { BrowserRouter } from "react-router-dom"
import { AuthProvider } from "./context/AuthProvider"
import App from "./App"
import "./index.css"

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <App />
      </AuthProvider>
    </BrowserRouter>
  </StrictMode>
)
```

> ℹ️ **Note**
>
> The order matters: `BrowserRouter` is outside `AuthProvider` so the provider could use router hooks later, and both wrap `App`.

---

### 🎨 7. Styles

**📁 `src/index.css`**

```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  background: #f5f7fb;
  color: #1b2333;
}
```

**📁 `src/App.css`**

```css
.app { max-width: 900px; margin: 0 auto; padding: 16px; }
.navbar { display: flex; align-items: center; gap: 14px; padding: 10px 16px; background: #0b5ed7; color: #fff; }
.navbar a { color: #fff; text-decoration: none; }
.navbar a.active { text-decoration: underline; }
.spacer { flex: 1; }

.card { background: #fff; border-radius: 10px; padding: 16px; margin-bottom: 16px; box-shadow: 0 1px 6px rgba(0, 0, 0, 0.1); }
.narrow { max-width: 360px; margin: 24px auto; }

input, button { padding: 8px; font-size: 14px; border: 1px solid #bbb; border-radius: 6px; }
button { background: #0b5ed7; color: #fff; border: 0; cursor: pointer; }
.navbar button { background: #fff; color: #0b5ed7; }

.field { margin-bottom: 10px; }
.field label { display: block; font-weight: bold; margin-bottom: 4px; }
.field input { width: 100%; box-sizing: border-box; }
.inline-form { display: flex; flex-wrap: wrap; gap: 8px; }

table { width: 100%; border-collapse: collapse; margin-top: 10px; }
th, td { border-bottom: 1px solid #e3e3e3; padding: 8px; text-align: left; }
th { background: #f1f3f4; }

.error { color: #d93025; }
.hint { color: #666; font-style: italic; }
```

---

### ✅ 8. Testing Checklist

| Test | Expected result |
|---|---|
| Open `/patients` while logged out | Redirect to `/login` |
| Login with wrong password | "Wrong username or password" |
| Login `admin` / `admin123` | You land on `/patients` and the navbar shows the user |
| Open `/patients/2` while logged out, then login | You land on `/patients/2` |
| Search "cardio" | 2 patients |
| Click **View** | Details page with the correct patient |
| Open `/patients/999` | "Patient not found" message |
| Add a valid patient | Appears in the table without a page refresh |
| Add name "Al" | Error: String should have at least 3 characters |
| Stop the backend and reload | "Is the backend running?" error |
| Click Logout, then press Back | You are redirected to `/login` |
| Refresh while logged in | You stay logged in |
| Open `/xyz` | 404 page |

---

## 💡 Real-Life Analogy

🏥 **A hospital with a gate, signboards, and a records room.**

The **gate guard** is the protected route. The **signboards** are the routes and URLs. The **ID badge** is the auth context. The **records room clerk** is FastAPI, who hands over files only after checking again. Each ward fetches its own **files** with `useFetch`.

---

## 💻 Real-World Application

| Where | Same pattern |
|---|---|
| 🏥 Hospital and clinic systems | Staff login, patient list, patient details |
| 🏨 Hotel management (your earlier app) | Rooms and bookings with the same structure |
| 🛍️ E-commerce admin panels | Orders and product pages |
| 🏫 School ERP | Students, attendance, fee records |
| 🧑‍💼 HR portals | Employee list and profile page |

---

## 🔍 Industry Example

📘 **Scenario: A receptionist's morning**

1. 🔑 She opens `/patients`. `ProtectedRoute` redirects her to `/login`.
2. 📨 She logs in, `AuthProvider` calls `POST /login`, and the user object is stored in state and `localStorage`.
3. 📋 She lands on `/patients`. `useFetch` calls `GET /patients`, and the loading message becomes the table.
4. 🔍 She types "neuro". `useMemo` filters the in-memory list, with no new request.
5. ➕ She adds a new patient. `POST /patients` returns 201, `reload()` re-runs the effect, and the table refreshes.
6. 👁️ She clicks **View**. `useParams` gives the id, and `useFetch` loads `/patients/{id}`.
7. 🚪 At lunch she clicks Logout. The state is cleared and the app returns to the login page.

---

## 📊 Diagram

```
                    main.jsx
        BrowserRouter ─► AuthProvider ─► App
                                          │
                  ┌───────────────────────┼─────────────────────┐
               Navbar                  Routes                    │
            (useAuth)                    │                       │
              ┌────────────┬─────────────┼───────────────┐
           /login    /patients(🛡️)   /patients/:id(🛡️)    *
         LoginPage   PatientsPage   PatientDetailsPage   404
              │          │  │              │
          login()    useFetch  PatientRow   useParams + useFetch
              │          │     (memo)             │
              └──────────┴──────────┬─────────────┘
                                    ▼
                        FastAPI (127.0.0.1:8000)
                  /login  /patients  /patients/{id}
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "CORS error means my React code is wrong." | Add `CORSMiddleware` in FastAPI with the right origin. |
| "I started only the frontend." | Run both `uvicorn` and `npm run dev`. |
| "Forgetting the `AuthProvider`." | `useAuth` throws an error outside it. |
| "Imports fail with the wrong path." | Check folder names and `export default` versus named exports. |
| "`useParams` id is a number." | It's a string. The URL builds fine for the API. |
| "The login is secure." | It's a teaching version. Real apps need hashed passwords and tokens. |
| "The patients page shows an empty table while loading." | Handle `loading` and `error` before rendering rows. |

---

## 💬 Interview Corner

**Q1. How does your app know whether a user is logged in?**
`AuthProvider` holds `user` state (also saved in `localStorage`), and `ProtectedRoute` and `Navbar` read it with `useAuth()`.

**Q2. How does the details page know which patient to load?**
`useParams()` reads `:id` from the URL, and `useFetch` runs `GET /patients/${id}`. The URL change triggers a new fetch.

**Q3. How does the table update after adding a patient?**
After a successful POST, `reload()` changes a counter in the effect's dependency array, so `useFetch` fetches the list again.

**Q4. What would you add before using this in production?**
JWT tokens, hashed passwords, backend authorization on every endpoint, HTTPS, and better error handling.

---

## 📝 Quick Summary

- 🐍 FastAPI provides `/login`, `/patients`, and `/patients/{id}` with CORS enabled.
- 🌍 `AuthProvider` plus `useAuth` shares login state everywhere.
- 🌐 `useFetch` hides loading, error, and the effect, and offers `reload()`.
- 🧭 Routes: `/login`, `/patients`, `/patients/:id`, and a 404 page.
- 🛡️ `ProtectedRoute` redirects logged-out users and returns them after login.
- 🧮 `useMemo` filters the list and `memo` keeps rows from re-rendering needlessly.
- 🔒 Real security stays in the backend.

---

## 🎯 Class Activity

**🛠️ Activity: "Run the full stack"**

1. Start the backend and the frontend in two terminals.
2. Walk through the **testing checklist** and tick every row.
3. Open the Network tab and find the `login`, `patients`, and `patients/2` requests.
4. Add a `console.log` in `PatientRow` and see how many rows render while you type in search.
5. Stop the backend and observe the error message.

---

# 📋 Assignments — Hospital App v2

| Assignment |
|---|
| Build the full app from the notes, complete the testing checklist, and take screenshots of the login redirect, the patients list, and a details page. |
| Add a **Delete** button for patients. Create `DELETE /patients/{id}` in FastAPI and call it, then `reload()` the list. |
| Add a `/doctors` page with its own endpoint, `useFetch`, and a protected route. |
| Add a `/billing` page that only `admin` can open, and show "not allowed" for `nurse`. |
| Add a department dropdown filter on the patients page using `useSearchParams`, so the filter is in the URL. |
| Show a spinner or skeleton text while loading, and a "Retry" button on errors that calls `reload()`. |
| Replace the plain login with a response containing a fake token, store the token, and send it as an `Authorization` header from `useFetch`. |
| Write a short note (8 to 10 lines) listing what you must change in the backend to make the login and patient APIs production-ready. |
| Add pagination (10 patients per page) and compare the render counts with the unpaginated version. |
| Draw the component tree and data-flow diagram for this app and mark where each state lives. |