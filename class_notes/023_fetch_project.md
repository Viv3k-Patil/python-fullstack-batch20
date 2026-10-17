# 📚 localStorage: Saving and Retrieving JSON

## 🎯 Learning Objectives
- 💾 Save data in the browser so it survives a page refresh
- 🔄 Convert objects and arrays to JSON and back
- 🧹 Read, update, and remove stored data

## 📖 Introduction
Variables in JavaScript disappear when you refresh the page. **localStorage** is a small storage space inside the browser that **keeps data even after the page or browser is closed**. It is used for things like themes, carts, and saved forms.

## 🧠 Detailed Notes

### 🗄️ The Basics
```javascript
localStorage.setItem("username", "Asha");        // save
console.log(localStorage.getItem("username"));   // "Asha"
localStorage.removeItem("username");             // delete one item
localStorage.clear();                            // delete everything
```

> ⚠️ **Important**
>
> localStorage stores **only strings**. Numbers, arrays, and objects must be converted first.

### 🔄 Saving JSON
- `JSON.stringify(value)` turns an object or array into a **string**.
- `JSON.parse(string)` turns that string back into an **object or array**.

```javascript
const booking = { name: "Asha", room: 101, nights: 2 };

localStorage.setItem("booking", JSON.stringify(booking));

const saved = JSON.parse(localStorage.getItem("booking"));
console.log(saved.name);   // Asha
```

### 🛡️ Safe Loading
`getItem` returns `null` if the key does not exist, so give it a default value:

```javascript
const bookings = JSON.parse(localStorage.getItem("bookings")) || [];
```

### 📊 Storage Options
| | localStorage | sessionStorage | Cookies |
|---|---|---|---|
| Lifetime | Until cleared | Until the tab closes | Set by expiry |
| Size | ~5 MB | ~5 MB | ~4 KB |
| Sent to server | ❌ No | ❌ No | ✅ Yes, every request |

🤔 **Quick thinking question:** What does `localStorage.setItem("age", 21)` actually store?

✅ **Answer:** The **string** `"21"`, not the number.

### 🔍 See It in DevTools
Press **F12**, open **Application**, then **Local Storage** to view, edit, and delete saved items.

## 💡 Real-Life Analogy
🎒 localStorage is your **school bag**. Things you put inside stay there until you take them out, even after you go home and come back the next morning.

## 💻 Real-World Application
- 🌗 Remembering dark mode
- 🛒 Keeping cart items for guests
- 📝 Saving a half-filled form draft

## 🔍 Industry Example
A news site remembers a reader's chosen **font size**. When the page loads, JavaScript reads `localStorage.getItem("fontSize")` and applies it before showing the article, with no login and no server needed.

## 📊 Diagram
```
 JS object ──stringify──► "JSON text" ──setItem──► 💾 localStorage
 JS object ◄──parse────── "JSON text" ◄──getItem── 💾 localStorage
```

## ⚠️ Common Mistakes
| ❌ Wrong | ✅ Correct |
|---|---|
| "I can store an object directly." | Use `JSON.stringify` first. |
| "`getItem` returns an object." | It returns a **string**. Use `JSON.parse`. |
| "localStorage is safe for passwords." | Never store secrets there. Any script on the page can read it. |

## 💬 Interview Corner
**Q1. What is localStorage?** Browser storage that keeps key-value string data with no expiry.

**Q2. Why do we use `JSON.stringify`?** Because localStorage only stores strings.

**Q3. localStorage vs sessionStorage?** localStorage persists after closing the browser. sessionStorage is cleared when the tab closes.

## 📝 Quick Summary
- 💾 `setItem`, `getItem`, `removeItem`, `clear`
- 🔤 Only strings are stored
- 🔄 `stringify` to save, `parse` to read
- 🛡️ Use `|| []` as a default
- 🔐 Never store passwords

## 🎯 Class Activity
Build a **theme toggle**: a button switches a `dark` class on `body` and saves `"dark"` or `"light"` in localStorage. On page load, read it and apply it.

---

# 📋 Assignments — localStorage: Saving and Retrieving JSON

| Assignment |
|---|
| Save your name in localStorage and show it on the page after a refresh. |
| Store an object with your profile (name, age, city) and read it back with `JSON.parse`. |
| Save an array of 3 favorite movies and print each one after reading it back. |
| Build a visit counter that increases by 1 on every page load. |
| Open DevTools, then Application, and manually edit a stored value. Refresh and observe. |
| Build a dark mode toggle that remembers the choice after refresh. |

---
---

# 📚 Persisting Bookings and Rooms in Browser Storage

## 🎯 Learning Objectives
- 📦 Store a list of records (bookings) in localStorage
- ➕ Add, ❌ delete, and 🔄 reload records
- 🧩 Follow the standard **load → change → save → render** pattern

## 📖 Introduction
Your hotel app will have a list of bookings. If it only lives in a variable, every refresh deletes all bookings. We keep the list in localStorage so it is **loaded when the page opens** and **saved after every change**.

## 🧠 Detailed Notes

### 🔁 The 4-Step Pattern
1. **Load** the array from localStorage when the page starts
2. **Change** the array (push or filter)
3. **Save** the whole array back
4. **Render** the page again

```javascript
let bookings = JSON.parse(localStorage.getItem("bookings")) || [];

function save() {
  localStorage.setItem("bookings", JSON.stringify(bookings));
}

// Add
bookings.push({ id: Date.now(), name: "Asha", roomNo: 101 });
save();

// Delete
bookings = bookings.filter((b) => b.id !== 12345);
save();
```

### 🆔 Why an `id`?
`Date.now()` gives a unique number, which makes it easy to delete the right booking later.

### 🏨 What About Rooms?
Rooms rarely change, so keep them as a plain array in your JS file. Work out each room's status from the bookings:

```javascript
const rooms = [
  { no: 101, type: "Standard", price: 3000 },
  { no: 201, type: "Deluxe", price: 4500 }
];

const isBooked = (roomNo) => bookings.some((b) => b.roomNo === roomNo);
```

> 💡 **Tip**
>
> Store only data that **changes** (bookings). Calculate everything else, such as room status, from it.

🤔 **Quick thinking question:** After deleting a booking from the array, why must we call `save()`?

✅ **Answer:** The array is only a copy in memory. Without saving, the booking returns after a refresh.

## 💡 Real-Life Analogy
📒 A **hotel register book**: the receptionist opens it in the morning (load), writes new guests (change), and keeps it at the desk (save), so it is still there tomorrow.

## 💻 Real-World Application
- 🛒 Guest shopping carts
- ✅ To-do apps
- 📋 Draft orders in billing screens

## 🔍 Industry Example
A small restaurant's tablet app keeps today's orders in localStorage. If the tablet restarts, the orders are loaded back and nothing is lost until the data is synced to a server.

## 📊 Diagram
```
 Page opens ─► LOAD array ─► RENDER
                  ▲             │
                  │          user adds/deletes
                SAVE ◄── CHANGE array
```

## ⚠️ Common Mistakes
| ❌ Wrong | ✅ Correct |
|---|---|
| Changing the array but forgetting `save()`. | Save after every change. |
| Saving only the new item. | Save the **whole array**. |
| Not giving a default for first-time users. | Use `|| []`. |

## 💬 Interview Corner
**Q1. How do you persist a list in the browser?** Stringify the array into localStorage and parse it on load.

**Q2. Why use `filter` to delete?** It creates a new array without the removed item.

**Q3. Is localStorage a database?** No. It is small, per-browser, and not secure. It suits simple client-side data.

## 📝 Quick Summary
- 📦 Keep a list as one JSON array under one key
- 🔁 Load, change, save, render
- 🆔 Give each record a unique id
- 🏨 Calculate room status from bookings

## 🎯 Class Activity
Build a tiny **notes app**: a text box and "Add" button save notes into an array in localStorage. Show them as a list, and reload them on page load.

---

# 📋 Assignments — Persisting Bookings and Rooms

| Assignment |
|---|
| Create a "guest list" app that saves guest names in localStorage and shows them after refresh. |
| Add a delete button next to each guest that removes it from storage too. |
| Give every guest a unique id using `Date.now()`. |
| Add a "Clear all" button using `localStorage.removeItem`. |
| Show a count like "Total guests: 5" that updates after every change. |
| Create a `rooms` array and show "Available" or "Booked" for each room based on a bookings array. |

---
---

# 📚 Intro to fetch() — GET and Simple POST

## 🎯 Learning Objectives
- 🌐 Understand what an API request is
- 📥 Get data using `fetch()` (GET)
- 📤 Send data using `fetch()` (POST)
- ❗ Handle errors simply

## 📖 Introduction
Websites often need data from a **server**: weather, products, bookings. `fetch()` is the built-in JavaScript function that **sends a request** to a URL and **receives the response**.

## 🧠 Detailed Notes

### 🌐 Key Terms
| Term | Meaning |
|---|---|
| **API / endpoint** | A URL that gives or accepts data |
| **GET** | Ask the server for data |
| **POST** | Send new data to the server |
| **JSON** | The text format used to exchange data |

### 📥 GET Request
We use a free dummy API: `https://jsonplaceholder.typicode.com`

```javascript
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((res) => res.json())     // turn the response into an object
  .then((data) => console.log(data.title))
  .catch((err) => console.log("Error:", err));
```

### ✨ Same Thing with `async / await` (easier to read)
```javascript
async function getPost() {
  try {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    if (!res.ok) throw new Error("HTTP " + res.status);
    const data = await res.json();
    console.log(data.title);
  } catch (err) {
    console.log("Error:", err.message);
  }
}
getPost();
```
- `async` marks a function that waits for things.
- `await` pauses until the result arrives.

### 📤 POST Request
```javascript
async function sendBooking() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: "Booking", body: "Asha, Room 101", userId: 1 })
  });
  const data = await res.json();
  console.log(data);   // includes a new id
}
sendBooking();
```
> ℹ️ **Note**
>
> The dummy API only **pretends** to save the data. It returns a fake `id` so you can practice.

### 🏓 Optional: Your Own `/ping` with FastAPI
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/ping")
def ping():
    return {"message": "pong"}
```
Run `uvicorn main:app --reload`, then in the browser console:
```javascript
fetch("http://127.0.0.1:8000/ping").then((r) => r.json()).then(console.log);
```

> ⚠️ **Important**
>
> `fetch` does **not** throw an error for a 404 or 500 response. Check `res.ok` yourself.

🤔 **Quick thinking question:** Why do we call `res.json()` after `fetch`?

✅ **Answer:** The response arrives as raw data. `res.json()` converts the body into a JavaScript object.

## 💡 Real-Life Analogy
🍽️ You are a **customer** (browser), the **waiter** is `fetch`, and the **kitchen** is the server. GET is *"bring me the menu"*. POST is *"here is my order"*.

## 💻 Real-World Application
- 🌦️ Weather widgets
- 🛍️ Loading products on Flipkart or Amazon
- 📝 Submitting a signup form without reloading the page

## 🔍 Industry Example
A booking website sends a **POST** with the guest details when you press "Confirm". The server saves it and replies with a booking number, which JavaScript then shows on screen.

## 📊 Diagram
```
 Browser ──fetch(GET/POST)──► Server
 Browser ◄───── JSON ──────── Server
         └─ res.json() ─► JS object ─► update page
```

## ⚠️ Common Mistakes
| ❌ Wrong | ✅ Correct |
|---|---|
| Using the response directly. | Call `await res.json()` first. |
| Sending an object as the body. | Use `JSON.stringify(...)`. |
| Forgetting the `Content-Type` header on POST. | Add `"Content-Type": "application/json"`. |
| Assuming a 404 triggers `catch`. | Check `res.ok`. |

## 💬 Interview Corner
**Q1. What is `fetch()`?** A built-in function that makes network requests and returns a Promise.

**Q2. GET vs POST?** GET reads data. POST sends data to be created.

**Q3. Does `fetch` reject on HTTP 404?** No. It only rejects on network failure. Check `res.ok`.

## 📝 Quick Summary
- 🌐 `fetch(url)` sends a request
- 📥 GET reads data, 📤 POST sends data
- 🔄 `res.json()` gives a usable object
- ✨ `async/await` keeps code clean
- ❗ Always check `res.ok` and use `try/catch`

## 🎯 Class Activity
Fetch `https://jsonplaceholder.typicode.com/users` and show the **names** of all users in a `<ul>` on the page.

---

# 📋 Assignments — Intro to fetch()

| Assignment |
|---|
| Fetch post number 5 and print its title in the console. |
| Fetch all `/users` and display their names in a list on the page. |
| Add a "Load" button that fetches a post only when clicked. |
| Send a POST request with your own booking details and print the response. |
| Fetch a wrong URL such as `/postsss/1`, then show a friendly error message on the page. |
| (Optional) Create the FastAPI `/ping` endpoint and call it from your page. |

---
---

# 📚 Project: Hotel Management App (Frontend Only)

## 🎯 Learning Objectives
- 🧩 Combine HTML, CSS, DOM, events, validation, and localStorage
- 🏨 Build a working app with rooms, a booking form, and a bookings table
- 🔍 Filter data live

## 📖 Introduction
You will turn a static hotel page into a small **interactive app**. No server is needed. Everything is saved in the browser.

## 🧠 Detailed Notes

### ✅ Features
| Feature | How it is built |
|---|---|
| Rooms dashboard | Rendered from a JS array, status calculated from bookings |
| Booking form | With validation, using `submit` and `preventDefault` |
| Bookings table | Built with `createElement` |
| Filters | By guest name and room type, using `input` and `change` events |
| Storage | Bookings saved in localStorage and loaded on page load |

### 📁 Folder
```
hotel-app/
 ├── index.html
 └── script.js
```

### 🧱 `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hotel Management</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 900px; margin: 20px auto; padding: 0 12px; }
    h2 { border-bottom: 2px solid #ddd; padding-bottom: 4px; }
    .rooms { display: flex; flex-wrap: wrap; gap: 10px; }
    .card { padding: 10px; border-radius: 8px; border: 2px solid; min-width: 150px; }
    .free { background: #e6f4ea; border-color: #1e8e3e; }
    .booked { background: #fce8e6; border-color: #d93025; }
    form input, form select, form button { padding: 7px; margin: 4px 4px 4px 0; }
    .error { color: #d93025; } .ok { color: #1e8e3e; }
    table { width: 100%; border-collapse: collapse; margin-top: 8px; }
    th, td { border: 1px solid #ccc; padding: 6px; text-align: left; }
    th { background: #f1f3f4; }
  </style>
</head>
<body>
  <h1>🏨 Hotel Paradise</h1>

  <h2>Rooms</h2>
  <div id="rooms" class="rooms"></div>

  <h2>Book a Room</h2>
  <form id="bookingForm" novalidate>
    <input type="text" id="guestName" placeholder="Guest name">
    <select id="roomSelect"></select>
    <input type="date" id="checkIn">
    <input type="date" id="checkOut">
    <button type="submit">Book</button>
  </form>
  <p id="msg"></p>

  <h2>Bookings</h2>
  <input type="text" id="filterName" placeholder="Filter by guest name">
  <select id="filterType">
    <option value="">All room types</option>
    <option>Standard</option>
    <option>Deluxe</option>
    <option>Suite</option>
  </select>
  <table>
    <thead>
      <tr><th>Guest</th><th>Room</th><th>Type</th><th>Check-in</th><th>Check-out</th><th>Nights</th><th>Total</th><th></th></tr>
    </thead>
    <tbody id="tbody"></tbody>
  </table>

  <script src="script.js" defer></script>
</body>
</html>
```

### ⚙️ `script.js`
```javascript
// ----- Data -----
const rooms = [
  { no: 101, type: "Standard", price: 3000 },
  { no: 102, type: "Standard", price: 3000 },
  { no: 201, type: "Deluxe", price: 4500 },
  { no: 202, type: "Deluxe", price: 4500 },
  { no: 301, type: "Suite", price: 7000 },
  { no: 302, type: "Suite", price: 7000 }
];

// Load saved bookings when the page opens
let bookings = JSON.parse(localStorage.getItem("bookings")) || [];

// ----- Elements -----
const roomsDiv = document.getElementById("rooms");
const form = document.getElementById("bookingForm");
const guestName = document.getElementById("guestName");
const roomSelect = document.getElementById("roomSelect");
const checkIn = document.getElementById("checkIn");
const checkOut = document.getElementById("checkOut");
const msg = document.getElementById("msg");
const filterName = document.getElementById("filterName");
const filterType = document.getElementById("filterType");
const tbody = document.getElementById("tbody");

// ----- Helpers -----
function save() {
  localStorage.setItem("bookings", JSON.stringify(bookings));
}

function isBooked(roomNo) {
  return bookings.some((b) => b.roomNo === roomNo);
}

// ----- Render: rooms dashboard -----
function renderRooms() {
  roomsDiv.innerHTML = "";
  rooms.forEach((r) => {
    const booked = isBooked(r.no);
    const card = document.createElement("div");
    card.className = "card " + (booked ? "booked" : "free");
    card.innerText = `Room ${r.no} | ${r.type} | ₹${r.price} | ${booked ? "Booked" : "Available"}`;
    roomsDiv.appendChild(card);
  });
}

// ----- Render: room dropdown (available rooms only) -----
function renderRoomSelect() {
  roomSelect.innerHTML = '<option value="">Select room</option>';
  rooms.filter((r) => !isBooked(r.no)).forEach((r) => {
    const opt = document.createElement("option");
    opt.value = r.no;
    opt.innerText = `${r.no} - ${r.type} (₹${r.price})`;
    roomSelect.appendChild(opt);
  });
}

// ----- Render: bookings table (with filters) -----
function renderBookings() {
  const nameText = filterName.value.trim().toLowerCase();
  const typeText = filterType.value;
  tbody.innerHTML = "";

  bookings
    .filter((b) => b.name.toLowerCase().includes(nameText))
    .filter((b) => typeText === "" || b.type === typeText)
    .forEach((b) => {
      const tr = document.createElement("tr");
      [b.name, b.roomNo, b.type, b.checkIn, b.checkOut, b.nights, "₹" + b.total].forEach((text) => {
        const td = document.createElement("td");
        td.innerText = text;
        tr.appendChild(td);
      });

      const td = document.createElement("td");
      const btn = document.createElement("button");
      btn.innerText = "Delete";
      btn.addEventListener("click", () => {
        bookings = bookings.filter((x) => x.id !== b.id);
        save();
        refresh();
      });
      td.appendChild(btn);
      tr.appendChild(td);
      tbody.appendChild(tr);
    });
}

function refresh() {
  renderRooms();
  renderRoomSelect();
  renderBookings();
}

// ----- Booking form -----
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = guestName.value.trim();
  const roomNo = Number(roomSelect.value);
  let error = "";

  if (name.length < 3) error = "Name must be at least 3 characters.";
  else if (!roomNo) error = "Please select a room.";
  else if (!checkIn.value || !checkOut.value) error = "Please choose both dates.";
  else if (checkOut.value <= checkIn.value) error = "Check-out must be after check-in.";

  if (error) {
    msg.innerText = error;
    msg.className = "error";
    return;
  }

  const room = rooms.find((r) => r.no === roomNo);
  const nights = Math.round((new Date(checkOut.value) - new Date(checkIn.value)) / 86400000);

  bookings.push({
    id: Date.now(),
    name,
    roomNo,
    type: room.type,
    checkIn: checkIn.value,
    checkOut: checkOut.value,
    nights,
    total: nights * room.price
  });

  save();
  form.reset();
  msg.innerText = "Booking saved ✅";
  msg.className = "ok";
  refresh();
});

// ----- Filters -----
filterName.addEventListener("input", renderBookings);
filterType.addEventListener("change", renderBookings);

// ----- Start: load and render on page load -----
refresh();
```

### 🔬 How It Works
1. 📥 On load, bookings come from localStorage and `refresh()` draws everything.
2. 📝 On submit, the form is validated. If valid, a booking is pushed, saved, and the page re-rendered.
3. 🏨 A room with a booking shows as **Booked** and disappears from the dropdown.
4. ❌ Deleting a booking frees the room again.
5. 🔍 The filters re-render the table as you type.

> ℹ️ **Note**
>
> This app is simplified: one booking blocks a room completely, with no date-overlap check. That is a good extension for later.

🤔 **Quick thinking question:** Why do we build table cells with `innerText` instead of `innerHTML`?

✅ **Answer:** Guest names come from the user. `innerText` treats them as plain text, so nobody can inject HTML or scripts.

## 💡 Real-Life Analogy
🛎️ This app is the **front desk of a small hotel**: a board showing which rooms are free (dashboard), a booking slip (form), the register book (table + localStorage), and a quick way to look up a guest (filters).

## 💻 Real-World Application
- 🏨 Booking tools for small guest houses
- 🩺 Clinic appointment lists
- 🍽️ Restaurant table reservations

## 🔍 Industry Example
Before building a full backend, a startup builds this exact kind of **frontend prototype** with fake or local data. It lets the team test the screens and validations quickly. Later the localStorage code is replaced by `fetch()` calls to a real API.

## 📊 Diagram
```
 Form ─validate─► bookings[] ─► save() ─► 💾 localStorage
                      │
                      ▼
      refresh() ─► Rooms dashboard
                ─► Room dropdown
                ─► Bookings table ◄── Filters (name / type)

 Page load: 💾 localStorage ─► bookings[] ─► refresh()
```

## ⚠️ Common Mistakes
| ❌ Wrong | ✅ Correct |
|---|---|
| Not calling `refresh()` after a change. | Re-render after every add or delete. |
| Forgetting `save()` after changing `bookings`. | Always save, or the data vanishes on refresh. |
| Script runs before the elements exist. | Use `defer`. |
| Comparing `roomNo` string with number. | Convert with `Number()`. |

## 💬 Interview Corner
**Q1. How does your app keep data after refresh?** Bookings are saved as JSON in localStorage and loaded on page load.

**Q2. How do the filters work?** Using `filter()` on the array, and re-rendering on `input` and `change` events.

**Q3. What would change if you add a backend?** Replace `localStorage` reads and writes with `fetch()` GET and POST calls.

## 📝 Quick Summary
- 🧩 One app that uses selection, events, validation, and storage
- 🔁 Pattern: change data, `save()`, `refresh()`
- 🏨 Room status is calculated from bookings
- 🔍 Filters use `filter()` and events
- 🔐 Use `innerText` for user-typed data

## 🎯 Class Activity
Build the app step by step: (1) rooms dashboard, (2) booking form with validation, (3) table, (4) localStorage, (5) filters. Book two rooms, refresh, and confirm that nothing is lost.

---

# 📋 Assignments — Project: Hotel Management App

| Assignment |
|---|
| Build the complete app from the notes and book at least three rooms. |
| Add a "Guest phone" field with validation (exactly 10 digits) and show it in the table. |
| Show a summary line above the table: total bookings and total revenue. |
| Add a "Clear all bookings" button that asks for confirmation using `confirm()`. |
| Prevent check-in dates in the past using the `min` attribute of the date input. |
| Add your own room type (for example "Family") and make sure the filter works for it. |