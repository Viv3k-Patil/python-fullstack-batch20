# 📚 Web & HTML Basics

## 🎯 Learning Objectives

By the end of this topic, students will be able to:

* 🎯 Explain the difference between "the Web" and a "Web Application," and what frontend vs backend each handle
* 🎯 Understand the required structure of every HTML document
* 🎯 Write headings, paragraphs, links, and images correctly
* 🎯 Build ordered and unordered lists
* 🎯 Build tables to display structured, real-world data
* 🎯 Use semantic HTML elements to structure a page meaningfully

---

## 📖 Introduction

Every single website you've ever visited — Google, Instagram, your bank's portal — is built on the same foundation: **HTML**. Until now, this course has focused entirely on the backend (Python, FastAPI, databases). Today we flip to the other half of "Full Stack": what the user actually **sees and clicks on** in their browser. 🌐

### 🤔 Why does this topic exist?

* 🖥️ Every backend API you've built (the Banking System, the Task Manager) eventually needs a face — something a real human can look at and interact with
* 🧱 HTML is the skeleton of every web page; CSS (styling) and JavaScript (behavior) are added ON TOP of it, later in this course
* 🔗 You've already built a working backend; today starts connecting it to something people can actually use in a browser, not just Postman or `/docs`

### 🤔 Where is it used?

* 🌍 Literally every website that exists — HTML is the one thing they all share
* 📱 Even mobile apps often use HTML internally (many apps are partly "web views")
* 📧 HTML emails, PDF generation tools, and documentation sites all rely on HTML structure

> 💡 **Tip**
>
> HTML is NOT a programming language — it has no `if`, no loops, no variables. It's a **markup language**: it describes the structure and content of a page, nothing more. Don't expect Python-style logic here.

---

## 🧠 Detailed Notes

### 1️⃣ Web vs Web Application, Role of Frontend vs Backend

**The Web** is the enormous network of documents and resources connected by links, accessed through browsers using the HTTP protocol you already know from FastAPI. A simple **website** is mostly static — think of a restaurant's "About Us" page, or a blog post. It shows information; it doesn't usually remember who you are or let you DO much.

A **Web Application** is a website that behaves more like software — it has logins, it stores your data, it reacts to your actions, and it changes based on who's using it. Gmail, Instagram, and the Task Manager API you built with a login system are all web applications, not just websites.

| | Website | Web Application |
|---|---|---|
| Example | A restaurant's menu page | Gmail, Instagram, your Task Manager project |
| Content | Mostly the same for everyone | Different for each logged-in user |
| Interaction | Mostly just reading | Creating, editing, deleting data |
| Typically needs | HTML + some CSS | HTML + CSS + JavaScript + a backend API |

**Frontend vs Backend — exactly where this course has been heading:**

```
                  THE FULL PICTURE
                  --------------------

   👤 User's Browser                    🖥️ Your Server
   ┌─────────────────────┐             ┌──────────────────────┐
   │  FRONTEND             │   HTTP      │  BACKEND                │
   │  HTML (structure)      │ requests/   │  FastAPI (your API)      │
   │  CSS (style)             │ responses  │  SQLAlchemy (database)    │
   │  JavaScript (behavior)    │ ◄────────► │  PostgreSQL (storage)       │
   └─────────────────────┘             └──────────────────────┘
        "what the user sees"                "what actually stores
         and clicks on"                       and processes data"
```

* **Frontend** = everything that runs in the user's browser: HTML, CSS, JavaScript
* **Backend** = everything that runs on your server: the FastAPI app, the database, the business logic

You've spent this whole course building the **backend** (the Task Manager's `/tasks/` endpoints, the auth system). The plain HTML pages you added at the very end (`index.html`, `tasks.html`) were your FIRST small step into the **frontend** — today, we properly learn the language those pages are written in.

> ⚠️ **Important**
>
> The frontend never talks to the database directly. It ALWAYS goes through the backend's API. This is exactly why your `tasks.html` page used `fetch()` to call `/tasks/` instead of trying to query PostgreSQL itself from the browser — the browser has no access to your database, and shouldn't.

🤔 **Quick thinking question:** Is a simple, single "Contact Us" page with no login a website or a web application?
✅ **Answer:** A website — it shows the same static information to everyone and doesn't store or react to individual user data.

---

### 2️⃣ HTML Document Structure

Every HTML file, no matter how simple or complex, follows the same required skeleton.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my very first web page.</p>
</body>
</html>
```

Breaking down each piece:

| Tag | Purpose |
|---|---|
| `<!DOCTYPE html>` | Tells the browser "this is a modern HTML5 document" — always the very first line |
| `<html lang="en">` | The root element; everything else lives inside it. `lang="en"` tells browsers/screen readers the page is in English |
| `<head>` | Information ABOUT the page — not shown directly on screen (title, character encoding, linked CSS files, etc.) |
| `<meta charset="UTF-8">` | Ensures special characters (₹, emojis, accented letters) display correctly |
| `<title>` | Text shown in the browser tab |
| `<body>` | Everything the user actually SEES and interacts with goes here |

```
            HTML DOCUMENT HIERARCHY
            ---------------------------
   <html>
     │
     ├── <head>          (invisible metadata)
     │     ├── <meta>
     │     └── <title>
     │
     └── <body>           (visible content)
           ├── <h1>
           ├── <p>
           └── ... everything else
```

**HTML elements have a consistent pattern: an opening tag, content, and a closing tag.**

```html
<tagname attribute="value">Content goes here</tagname>
```

Some tags are **self-closing** — they have no content inside them, like `<meta>` and `<img>` (covered shortly).

> ⚠️ **Important**
>
> Tags must be properly **nested** — if you open `<body>` before `<head>`, or forget a closing tag, browsers will often still try to render SOMETHING, but the result becomes unpredictable. Always close what you open, in the right order.

🤔 **Quick thinking question:** Why does almost nothing inside `<head>` actually appear on the visible page?
✅ **Answer:** `<head>` holds METADATA — information describing the page itself (its title, character encoding, linked resources) — not the actual visible content, which all lives inside `<body>`.

---

### 3️⃣ Headings, Paragraphs, Links, and Images

**Headings** — six levels, `<h1>` (most important/largest) to `<h6>` (least important/smallest):

```html
<h1>Hospital Management System</h1>
<h2>Patient Records</h2>
<h3>Admission Details</h3>
```

> 💡 **Tip**
>
> Use headings for STRUCTURE, not just to make text big. A page should typically have exactly ONE `<h1>` (its main title), with `<h2>`, `<h3>` used for sections and sub-sections, in order — don't skip from `<h1>` straight to `<h4>` just because it "looks right."

**Paragraphs** — ordinary blocks of text:

```html
<p>This patient was admitted on 12th August for routine observation.</p>
<p>Each new paragraph tag starts on its own new line automatically.</p>
```

**Links** — the `<a>` (anchor) tag, using the `href` attribute for the destination:

```html
<a href="https://www.python.org">Visit Python's official site</a>

<!-- Opens in a new browser tab -->
<a href="https://fastapi.tiangolo.com" target="_blank">FastAPI Docs</a>

<!-- Links to ANOTHER page on your own site -->
<a href="tasks.html">Go to My Tasks</a>

<!-- Links to a specific section on the SAME page -->
<a href="#contact">Jump to Contact Section</a>
```

**Images** — the `<img>` tag, which is self-closing (no closing tag, no content inside it):

```html
<img src="hospital-logo.png" alt="Hospital logo" width="150">
```

| Attribute | Purpose |
|---|---|
| `src` | The image file's location (a local file or a full URL) |
| `alt` | Text shown if the image fails to load, AND read aloud by screen readers for accessibility |
| `width` / `height` | Controls the displayed size (in pixels, unless specified otherwise) |

> ⚠️ **Important**
>
> ALWAYS include a meaningful `alt` attribute on images. It's not optional "extra polish" — it's essential for accessibility (screen reader users) and for search engines to understand what the image shows.

🤔 **Quick thinking question:** Why does `<img>` have no closing tag, while `<a>` and `<p>` do?
✅ **Answer:** `<img>` doesn't wrap around any content — it's a single, self-contained element that just displays a file. `<a>` and `<p>` need an opening AND closing tag because they wrap around text or other content that goes between them.

---

### 4️⃣ Lists (Ordered, Unordered)

**Unordered lists** (`<ul>`) — bullet points, when ORDER doesn't matter:

```html
<ul>
    <li>Stethoscope</li>
    <li>Thermometer</li>
    <li>Blood pressure monitor</li>
</ul>
```

Renders as:
```
• Stethoscope
• Thermometer
• Blood pressure monitor
```

**Ordered lists** (`<ol>`) — numbered, when SEQUENCE matters:

```html
<ol>
    <li>Register the patient at the front desk</li>
    <li>Nurse records vital signs</li>
    <li>Doctor conducts examination</li>
    <li>Prescription issued</li>
</ol>
```

Renders as:
```
1. Register the patient at the front desk
2. Nurse records vital signs
3. Doctor conducts examination
4. Prescription issued
```

**Nested lists** — a list inside a list item, for sub-items:

```html
<ul>
    <li>Engineering Department
        <ul>
            <li>Priya Sharma</li>
            <li>Rahul Verma</li>
        </ul>
    </li>
    <li>HR Department
        <ul>
            <li>Ankit Singh</li>
        </ul>
    </li>
</ul>
```

| Tag | Use When |
|---|---|
| `<ul>` | Items with NO required order (ingredients, features, tags) |
| `<ol>` | Items where SEQUENCE matters (steps, rankings, instructions) |
| `<li>` | Each individual item, inside either `<ul>` or `<ol>` |

> 💡 **Tip**
>
> If you ever find yourself writing "Step 1," "Step 2" as plain text inside `<li>` tags within a `<ul>`, that's a strong sign you should be using `<ol>` instead — let the browser number it for you.

🤔 **Quick thinking question:** Why would a recipe's list of INGREDIENTS typically use `<ul>`, while the list of COOKING STEPS would use `<ol>`?
✅ **Answer:** The order you read ingredients usually doesn't matter — it's just a collection. Cooking steps, however, must happen in a specific sequence, which `<ol>`'s automatic numbering correctly represents.

---

### 5️⃣ Tables for Structured Data (Rooms, Patients, Accounts)

Tables display information organized into **rows and columns** — exactly like the database tables you've been building all course (`employees`, `departments`, `tasks`). This is the perfect connection point between backend data and frontend display.

```html
<table border="1">
    <thead>
        <tr>
            <th>Room No.</th>
            <th>Patient Name</th>
            <th>Admitted On</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>101</td>
            <td>Priya Sharma</td>
            <td>2026-08-12</td>
            <td>Admitted</td>
        </tr>
        <tr>
            <td>102</td>
            <td>Rahul Verma</td>
            <td>2026-08-14</td>
            <td>Discharged</td>
        </tr>
    </tbody>
</table>
```

Renders as:

| Room No. | Patient Name | Admitted On | Status |
|---|---|---|---|
| 101 | Priya Sharma | 2026-08-12 | Admitted |
| 102 | Rahul Verma | 2026-08-14 | Discharged |

**Anatomy of an HTML table:**

| Tag | Purpose |
|---|---|
| `<table>` | The whole table container |
| `<thead>` | The header section (column titles) |
| `<tbody>` | The body section (the actual data rows) |
| `<tr>` | One table row ("table row") |
| `<th>` | One header cell ("table header") — bold, used for column titles |
| `<td>` | One regular data cell ("table data") |

```
           TABLE STRUCTURE
           -------------------
   <table>
     ├── <thead>
     │     └── <tr>
     │           ├── <th>Room No.</th>
     │           ├── <th>Patient Name</th>
     │           └── ...
     └── <tbody>
           ├── <tr>   ← one row per record
           │     ├── <td>101</td>
           │     ├── <td>Priya Sharma</td>
           │     └── ...
           └── <tr>
                 └── ...
```

**A second example — bank accounts, connecting straight back to earlier projects:**

```html
<table border="1">
    <thead>
        <tr>
            <th>Account No.</th>
            <th>Holder Name</th>
            <th>Balance (₹)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ACC1001</td>
            <td>Priya Sharma</td>
            <td>50,000</td>
        </tr>
        <tr>
            <td>ACC1002</td>
            <td>Rahul Verma</td>
            <td>72,500</td>
        </tr>
    </tbody>
</table>
```

> ⚠️ **Important**
>
> Tables are for DISPLAYING tabular data — not for laying out an entire page's visual design (positioning a header, sidebar, and footer). That was a common bad practice years ago; today, CSS (coming up later in the course) handles page layout instead.

🤔 **Quick thinking question:** If you're about to display a list of 50 employee records fetched from your FastAPI backend, why is an HTML `<table>` a better fit than a plain `<ul>` list?
✅ **Answer:** Each employee record has MULTIPLE related fields (name, department, salary) that need to line up clearly in columns for easy scanning and comparison — a `<table>` naturally organizes this, while a `<ul>` would just produce a flat, harder-to-compare list.

---

### 6️⃣ Semantic Elements: header, nav, main, section, footer

Older HTML relied heavily on generic `<div>` tags for everything, giving browsers (and developers reading the code later) no hint about what each section actually WAS. **Semantic elements** fix this — they describe the MEANING of a section, not just its box.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hospital Dashboard</title>
</head>
<body>

    <header>
        <h1>🏥 City Hospital</h1>
    </header>

    <nav>
        <a href="index.html">Home</a>
        <a href="patients.html">Patients</a>
        <a href="doctors.html">Doctors</a>
    </nav>

    <main>
        <section>
            <h2>Today's Admissions</h2>
            <p>3 new patients admitted today.</p>
        </section>

        <section>
            <h2>Available Rooms</h2>
            <p>12 rooms currently available.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 City Hospital. All rights reserved.</p>
    </footer>

</body>
</html>
```

| Tag | Meaning |
|---|---|
| `<header>` | Introductory content, typically the site/page title and top branding |
| `<nav>` | A block of navigation links |
| `<main>` | The PRIMARY content of the page — there should only be one per page |
| `<section>` | A distinct, self-contained grouping of related content within `<main>` |
| `<footer>` | Closing content — copyright notices, contact info, usually at the bottom |

```
          SEMANTIC PAGE LAYOUT
          ------------------------
   ┌─────────────────────────────┐
   │  <header>   🏥 City Hospital   │
   ├─────────────────────────────┤
   │  <nav>  Home | Patients | Doctors│
   ├─────────────────────────────┤
   │  <main>                         │
   │   ┌───────────────────────┐    │
   │   │ <section> Admissions    │    │
   │   └───────────────────────┘    │
   │   ┌───────────────────────┐    │
   │   │ <section> Available Rooms │  │
   │   └───────────────────────┘    │
   ├─────────────────────────────┤
   │  <footer>  © 2026 City Hospital  │
   └─────────────────────────────┘
```

**Why this matters, concretely:**

* ♿ **Accessibility** — screen readers can jump directly to "the navigation" or "the main content," improving the experience for visually impaired users
* 🔍 **SEO** — search engines understand your page structure better, which can affect how your site is indexed and ranked
* 🧹 **Readability** — another developer (or you, six months later) can scan the HTML and immediately understand the page's structure, instead of deciphering a wall of generic `<div>` tags

> 💡 **Tip**
>
> `<div>` still has its place — it's a generic, meaning-free container used when NONE of the semantic tags fit. But whenever a semantic tag DOES fit the purpose, prefer it over `<div>`.

🤔 **Quick thinking question:** Why is it recommended to have only ONE `<main>` element per page, but potentially several `<section>` elements?
✅ **Answer:** `<main>` represents the single, primary content area of the entire page — having more than one would be contradictory. `<section>` represents individual groupings of related content WITHIN that main area, and a page naturally has multiple distinct topics/sections worth separating.

---

## 💡 Real-Life Analogy

* 🏗️ **HTML Document Structure → A House's Basic Blueprint** — Every house needs a foundation, walls, and a roof in a specific arrangement, just like every HTML page needs `<!DOCTYPE>`, `<html>`, `<head>`, and `<body>` in the right order.
* 📰 **Headings → A Newspaper's Headline Hierarchy** — The front-page headline (`<h1>`) is bigger and more important than a section headline (`<h2>`), which is bigger than a sub-story headline (`<h3>`).
* 🔗 **Links → Doorways Between Rooms (or Buildings)** — Clicking a link is like walking through a doorway to another room (`#section` on the same page) or an entirely different building (another website).
* 🗄️ **Tables → A Filing Cabinet's Labeled Drawers and Folders** — Columns are like labeled drawers (Name, Date, Status), and each row is like one folder filed consistently across all the drawers.
* 🏢 **Semantic Elements → A Well-Signposted Office Building** — Instead of unmarked doors everywhere, clear signs say "Reception" (`<header>`), "Directory" (`<nav>`), "Main Office" (`<main>`), and "Exit" (`<footer>`) — anyone can navigate it immediately, even on their first visit.

---

## 💻 Real-World Application

| Concept | Real Company / Product Usage |
|---|---|
| Web application vs website | Wikipedia's article pages (mostly static) vs Wikipedia's login/edit features (a web application) |
| HTML document structure | Literally every site — view any page's source code (Ctrl+U in most browsers) and you'll see this same skeleton |
| Links | Navigation menus on every e-commerce site (Amazon, Flipkart) |
| Images with `alt` text | Accessibility compliance requirements for government and enterprise websites |
| Tables | Banking statements, hospital patient lists, admin dashboards showing database records |
| Semantic elements | Modern frameworks (React, Vue) still render down to these same semantic tags under the hood for accessibility and SEO |

---

## 🔍 Industry Example

**Scenario:** A **frontend developer at a hospital-tech startup** is building the dashboard for hospital staff to view patient and room information — connecting to a FastAPI backend similar to the one built in this course.

1. They structure the page using semantic elements: `<header>` for the hospital's branding, `<nav>` for links to "Patients," "Doctors," and "Rooms" sections, `<main>` holding the actual dashboard content, and `<footer>` for contact/compliance information.
2. Inside `<main>`, they use **`<section>`** elements to separate "Today's Admissions" from "Available Rooms" — each logically distinct.
3. Patient and room data fetched from the backend API is displayed using **`<table>`** elements — exactly matching the rows/columns structure of the underlying `patients` and `rooms` database tables.
4. Every patient photo includes a meaningful **`alt`** attribute (e.g., `alt="Photo of patient Priya Sharma"`) to meet accessibility requirements, which are often legally mandated for healthcare software.
5. **Links** in the `<nav>` let staff move between different dashboard pages (patient list, doctor roster) without reloading unrelated information unnecessarily.

This exact combination — semantic structure, tables for backend data, accessible images, clear navigation — is standard practice for any real dashboard-style web application, in healthcare or otherwise.

---

## 📊 Diagram

```
            FULL PICTURE: FRONTEND MEETS BACKEND
            ------------------------------------------

   Browser requests a page
            │
            ▼
   ┌─────────────────────────────┐
   │   index.html (FRONTEND)       │
   │   <header>, <nav>, <main>,      │
   │   <table> showing data            │
   └─────────────────────────────┘
            │
            │  JavaScript's fetch() calls your API
            ▼
   ┌─────────────────────────────┐
   │   FastAPI endpoints (BACKEND)   │
   │   /patients/, /rooms/, /accounts/ │
   └─────────────────────────────┘
            │
            ▼
   ┌─────────────────────────────┐
   │   PostgreSQL database            │
   │   patients table, rooms table,     │
   │   accounts table                    │
   └─────────────────────────────┘


         HTML DOCUMENT SKELETON
         --------------------------
   <!DOCTYPE html>
   <html>
     <head>  ──► metadata, title, not visible
     <body>  ──► header, nav, main, footer
                    └── section(s)
                          └── h1/h2, p, ul/ol, table, img, a
```

---

## ⚠️ Common Mistakes

* ❌ **Wrong belief:** "A website and a web application are basically the same thing."
  ✅ **Correct:** A website is mostly static, showing the same content to everyone. A web application reacts to user actions and typically stores/manages user-specific data.

* ❌ **Wrong belief:** "The frontend can directly read from or write to the database."
  ✅ **Correct:** The frontend NEVER talks to the database directly — it always goes through the backend's API, which is exactly why `fetch()` calls hit FastAPI endpoints, not PostgreSQL.

* ❌ **Wrong belief:** "You can skip heading levels (like going from `<h1>` straight to `<h4>`) if it visually looks right."
  ✅ **Correct:** Headings should follow a logical, sequential structure — skipping levels breaks the page's semantic outline, which matters for accessibility and SEO, even if it "looks fine" visually.

* ❌ **Wrong belief:** "The `alt` attribute on images is optional, just for extra polish."
  ✅ **Correct:** It's essential for accessibility (screen readers rely on it) and is considered a core requirement of properly written HTML, not a nice-to-have.

* ❌ **Wrong belief:** "Tables are a good way to control the overall visual layout of a page (header here, sidebar there)."
  ✅ **Correct:** Tables are for tabular DATA. Overall page layout is handled with CSS, not by misusing `<table>` as a page-layout tool.

* ❌ **Wrong belief:** "`<div>` and semantic tags like `<section>` are interchangeable, so it doesn't matter which you use."
  ✅ **Correct:** Whenever a semantic tag correctly describes a section's purpose, prefer it — `<div>` carries no meaning and should be reserved for cases where no semantic tag fits.

---

## 💬 Interview Corner

**Q1: What is the difference between a website and a web application?**
✅ A website is largely static and shows the same content to all visitors. A web application is interactive, typically requires login, and manages data that differs per user (e.g., Gmail, a task manager).

**Q2: What is the role of the `<head>` section in an HTML document?**
✅ It contains metadata ABOUT the page — such as the character encoding, the page title shown in the browser tab, and links to stylesheets/scripts — none of which is directly visible in the page's main content area.

**Q3: Why are semantic HTML elements (like `<header>`, `<nav>`, `<main>`) preferred over generic `<div>` tags?**
✅ They convey MEANING about each section's purpose, improving accessibility (screen readers can navigate by section), SEO (search engines understand page structure better), and code readability for other developers.

**Q4: Why should the frontend never query a database directly?**
✅ The browser has no secure way to connect to a database, and allowing it to do so would expose credentials and bypass all backend validation/security logic — all data access must go through the backend API instead.

---

## 📝 Quick Summary

* 🌐 A website is mostly static; a web application is interactive and manages user-specific data
* 🖥️ Frontend (HTML/CSS/JavaScript, runs in the browser) and backend (FastAPI/database, runs on the server) communicate over HTTP — the frontend never touches the database directly
* 🏗️ Every HTML document needs `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`, in that order
* 📰 Headings (`<h1>`–`<h6>`) should be used in logical order, not just for visual sizing
* 🔗 `<a href="...">` creates links; `<img src="..." alt="...">` displays images — always include meaningful `alt` text
* 📋 `<ul>` for unordered lists, `<ol>` for ordered/sequential lists, `<li>` for each item
* 🗄️ `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>` display structured, row-and-column data — exactly mirroring database tables
* 🏢 Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) describe a page's MEANING, improving accessibility, SEO, and readability over generic `<div>`s

---

## 🎯 Class Activity

**"Build a Mini Hospital Dashboard Page" 🏥**

1. Create a new `.html` file with the correct basic structure: `<!DOCTYPE html>`, `<html>`, `<head>` (with a `<title>`), and `<body>`.
2. Add a `<header>` with an `<h1>` showing a hospital name of your choice, and a `<nav>` with 3 links (even if they don't go anywhere real yet).
3. Inside a `<main>`, add two `<section>` elements: one listing today's admissions as an unordered list, and one showing a `<table>` of at least 3 patients (Room No., Name, Status).
4. Add at least one `<img>` with a meaningful `alt` attribute (any image, even a placeholder).
5. Add a `<footer>` with a copyright line.
6. Open the file directly in your browser and confirm everything displays correctly.


---

# 📋 Assignments — Web & HTML Basics

| Assignment |
|---|
| Write a short paragraph (3–4 sentences) in your own words explaining the difference between a website and a web application, using one example of each that you personally use. |
| Create a complete, valid HTML document from scratch (correct `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`) with a `<title>` of your choice, and open it in a browser to confirm the tab title shows correctly. |
| Add 3 headings of different levels (`<h1>`, `<h2>`, `<h3>`) to a page, each with different text, and explain in a comment why you chose that heading level for each. |
| Write 2 paragraphs about your favorite hobby, and add one link inside one of the paragraphs pointing to a real website about that hobby. |
| Add an image to your page with a properly descriptive `alt` attribute, then rename the image file so it can't be found, and observe what the `alt` text does in that case. |
| Create an unordered list of 5 ingredients for a recipe, and an ordered list of the 5 steps to prepare it. |
| Build a nested list showing 2 departments, each with at least 2 employee names listed underneath. |
| Create an HTML table showing at least 4 bank accounts, with columns for Account Number, Holder Name, and Balance. |
| Create a second HTML table showing at least 4 hospital rooms, with columns for Room Number, Patient Name, and Status (Admitted/Available). |
| Build a full page using ALL FIVE semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) for a topic of your choice (a school, a store, a gym). |
| Take an existing page you've built using `<div>` tags and rewrite it using the correct semantic elements instead, explaining in a comment which `<div>` became which semantic tag and why. |
| Create a navigation bar (`<nav>`) with 4 links, where one link jumps to a specific section further down the SAME page using `#` and an `id`. |
| Combine a table with semantic structure: build a `<main>` containing one `<section>` with a heading and a table of at least 5 rows of data on a topic of your choice. |
| View the HTML source code of any real website you use often (right-click → "View Page Source" or Ctrl+U), and find at least 3 semantic elements or table structures being used — write down what you found. |
| Write a short reflection (3–5 sentences) on how today's HTML topic connects to the FastAPI backend projects you've already built — specifically, where would data from your Task Manager or Banking System API actually appear on a page like the ones you built today? |