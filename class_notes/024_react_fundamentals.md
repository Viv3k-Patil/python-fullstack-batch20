# 📚 What is React and Why SPA?

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- ⚛️ Explain what React is and who uses it
- 📄 Describe the difference between a traditional multi-page website and a Single Page Application (SPA)
- 🧩 Understand the idea of **components**
- 🪞 Understand the **Virtual DOM** at a beginner level
- 🆚 Compare **imperative** (plain JavaScript) and **declarative** (React) code
- 🗺️ Know where React fits in the Python Full Stack architecture

---

## 📖 Introduction

In the last few topics, you built a hotel app using plain JavaScript. You selected elements, changed text, added event listeners, and re-rendered tables by hand. It worked, but notice how much **manual work** it took: every time the data changed, *you* had to remember to update the screen.

Now imagine an app with 50 screens and hundreds of buttons. Keeping everything in sync by hand becomes a nightmare. 😵

👉 This is the problem **React** solves.

**React** is a **JavaScript library for building user interfaces**. It was created by **Jordan Walke at Facebook (Meta)** and released as open source in **2013**.

**Why does this topic exist?** Modern websites are really *applications*. They need a better way to organize code than hundreds of `getElementById` calls.

**Why is it important?** React is one of the most in-demand frontend skills in the job market. Most companies hiring full stack developers expect React knowledge.

**Where is it used?** Facebook, Instagram, WhatsApp Web, Netflix, Airbnb, Uber, Discord, and thousands of startups.

---

## 🧠 Detailed Notes

### ⚛️ 1. What is React?

React is a **library** (not a full framework) with one main job: **build the user interface from small, reusable pieces called components**.

| Key idea | Meaning |
|---|---|
| **Component-based** | The UI is split into small reusable pieces (Navbar, RoomCard, BookingForm) |
| **Declarative** | You describe **what** the screen should look like. React figures out **how** to update it |
| **State-driven** | When your data changes, React updates the screen automatically |
| **Learn once, use anywhere** | Same ideas work for web (React), mobile (React Native), and more |

> ℹ️ **Note**
>
> **Library vs framework:** A library is a tool you call when you need it. A framework is a bigger structure that tells you how to organize everything. React focuses on the UI only. For routing, data fetching, and more, you add other tools.

---

### 📄 2. Traditional Websites (Multi-Page)

In a traditional website, **every click loads a brand-new HTML page** from the server.

```
 Click "Rooms"   ──►  Server sends rooms.html     ──► whole page reloads ⏳
 Click "Bookings" ──► Server sends bookings.html  ──► whole page reloads ⏳
```

- ✅ Simple and good for search engines
- ❌ Page flashes and reloads on every click
- ❌ Header and footer are downloaded again and again

---

### 🚀 3. Single Page Application (SPA)

In a **SPA**, the browser loads **one HTML page once**. After that, JavaScript **swaps the content** on the screen and fetches only the **data** it needs.

```
 First visit  ──► Server sends ONE html page + JavaScript bundle
 Click "Rooms" ──► JS swaps the screen instantly, no reload ⚡
 Need data?   ──► JS calls the API (fetch) and gets only JSON
```

| Feature | Multi-Page Website | Single Page Application |
|---|---|---|
| Page loads | Full reload on every click | One load, then instant updates |
| Feels like | A document | A desktop or mobile app |
| Data from server | Full HTML pages | Small JSON responses |
| First load | Fast | Slightly heavier (downloads JS first) |
| SEO | Easy | Needs extra care |
| Examples | Blogs, news sites | Gmail, Trello, Netflix, Google Maps |

> 💡 **Tip**
>
> The SEO weakness of SPAs is real, but tools built on top of React (like **Next.js**) solve it. For internal tools, dashboards, and logged-in apps, SEO barely matters.

🤔 **Quick thinking question:** When you switch tabs in Gmail (Inbox to Sent), does the browser tab show the loading spinner and reload the page?

✅ **Answer:** No. Gmail is a SPA. JavaScript fetches the new mail list and swaps the content on the same page.

---

### 🧩 4. Components: The Heart of React

A **component** is a **reusable piece of UI**. A full page is a **tree of components**.

```
 App
  ├── Navbar
  ├── RoomList
  │     ├── RoomCard  (Room 101)
  │     ├── RoomCard  (Room 102)
  │     └── RoomCard  (Room 201)
  ├── BookingForm
  └── Footer
```

You write `RoomCard` **once** and use it many times with different data. If the design must change, you fix it in **one place**.

---

### 🆚 5. Imperative vs Declarative

This is the biggest mindset shift.

**Plain JavaScript (imperative, you give step-by-step instructions):**

```html
<h2 id="count">0</h2>
<button id="btn">Add</button>

<script>
  let count = 0;
  document.getElementById("btn").addEventListener("click", () => {
    count++;
    document.getElementById("count").innerText = count;   // YOU update the screen
  });
</script>
```

**React (declarative, you describe the result):**

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
}
```

Notice there is **no** `getElementById` and **no** manual screen update. You say "show `count`", and React keeps the screen correct whenever `count` changes. Don't worry about the syntax yet. We will learn every part of it step by step.

---

### 🪞 6. The Virtual DOM (Beginner Level)

Updating the real DOM is slow if done carelessly. React uses a trick:

1. React keeps a **lightweight copy** of the page in memory: the **Virtual DOM**.
2. When data changes, React builds a **new** virtual copy.
3. It **compares** the old and new copies (this is called **diffing**).
4. It updates **only the parts that actually changed** in the real DOM.

```
  Data changes
      │
      ▼
 New Virtual DOM  ──compare──  Old Virtual DOM
      │
      ▼
 Only the DIFFERENCE is applied to the real DOM ⚡
```

> ℹ️ **Note**
>
> You never touch the Virtual DOM yourself. It is React's internal job. Just remember: *React updates only what changed.*

---

### ⭐ 7. Why Developers Choose React

- ♻️ **Reusable components** save time
- 🔄 **Automatic UI updates** when data changes
- 🌍 **Huge community**, libraries, and learning material
- 💼 **Many job openings**
- 📱 The same ideas carry over to **React Native** for mobile apps

---

### 🗺️ 8. React in the Full Stack Picture

```
   🌐 Browser (React SPA)  ◄── JSON over HTTP ──►  🐍 Python backend (FastAPI)  ◄──►  🗄️ Database
        shows the UI                                  business rules and APIs           stores data
```

React builds the **screens**. Your **FastAPI** backend provides the **data**. They talk using `fetch()` and JSON, exactly like the hotel app you already connected.

---

### 🆚 9. React vs Plain JavaScript vs Other Tools

| | Plain JavaScript | React | Vue / Angular |
|---|---|---|---|
| Type | Language | Library | Framework |
| Updates screen | Manually | Automatically | Automatically |
| Best for | Small pages | Small to very large apps | Small to very large apps |
| Learning curve | Low | Medium | Medium to high |

---

## 💡 Real-Life Analogy

🧱 **React is like building with LEGO blocks.**

- Each **component** is a LEGO piece (a wheel, a door, a window).
- You can **reuse the same piece** many times to build a car, a house, or a bus.
- If a wheel design improves, you replace the wheel piece and **every car** that uses it benefits.

And the **SPA** idea is like a **TV screen**: the screen stays on, and only the picture changes, instead of someone carrying in a new TV every time you change the channel. 📺

---

## 💻 Real-World Application

| Company / Product | How React is used |
|---|---|
| 📘 **Facebook / Instagram** | News feed, like buttons, comments, built from components |
| 🎬 **Netflix** | Interactive browsing interface |
| 🏠 **Airbnb** | Search filters, maps, listing pages |
| 🚗 **Uber** | Web booking dashboards |
| 💬 **Discord** | The chat interface |
| 🏢 **Company dashboards** | Admin panels with charts, tables, and forms |

---

## 🔍 Industry Example

📘 **Scenario: A booking dashboard at a hotel chain**

A hotel chain's staff use a web dashboard all day long. It shows room status, today's check-ins, and a booking form.

**What happens internally:**

1. 🌐 Staff open the dashboard URL. The browser downloads **one HTML file and the React JavaScript bundle**.
2. ⚛️ React builds the screen from components: `Navbar`, `RoomGrid`, `CheckInList`.
3. 📡 The components call the backend API: *"Give me today's rooms"*. The server replies with **JSON** only.
4. 🔄 A receptionist books a room. React updates **only that room's card** from green to red. The rest of the page stays untouched.
5. ⚡ No page reload happens all day, so the dashboard feels like a desktop app.

---

## 📊 Diagram

```
        TRADITIONAL (Multi-Page)                SPA (React)

   Click ──► Server ──► NEW full page      Click ──► JS runs in browser
   Click ──► Server ──► NEW full page            │
   Click ──► Server ──► NEW full page            ├─► swaps components instantly
                                                 └─► fetches only JSON if needed
   🔄 reload every time                      ⚡ no reloads


             HOW REACT UPDATES THE SCREEN

   State/data changes
          │
          ▼
   React re-runs your component  ──►  new Virtual DOM
          │
          ▼
   Diff: old vs new  ──►  smallest set of changes
          │
          ▼
   Real DOM updated (only what changed)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "React is a programming language." | React is a **JavaScript library**. You write JavaScript. |
| "React is a full framework like Angular." | React focuses on the UI. Routing and data fetching come from extra tools. |
| "React replaces JavaScript." | React is **built on** JavaScript. You still need strong JS basics. |
| "SPA means the website has only one URL." | SPAs can show many URLs using client-side routing. It only means **one HTML page** is loaded. |
| "The Virtual DOM is a second website." | It is just an in-memory JavaScript copy used to find differences quickly. |
| "React is always faster than plain JS." | React is about **organizing** big apps well. A tiny page may not need it. |

---

## 💬 Interview Corner

**Q1. What is React?**
A JavaScript library for building user interfaces using reusable components. It updates the screen automatically when data changes.

**Q2. What is a SPA?**
A web app that loads a single HTML page and then updates the content dynamically with JavaScript, without full page reloads.

**Q3. What is the Virtual DOM?**
A lightweight in-memory copy of the real DOM. React compares the old and new versions and updates only the parts of the real DOM that changed.

**Q4. Is React a library or a framework?**
A library. It handles the view layer only, and other tools are added for things like routing.

---

## 📝 Quick Summary

- ⚛️ **React** is a JavaScript library for building UIs, created at Facebook in 2013.
- 🧩 UIs are built from **reusable components**.
- 🚀 A **SPA** loads one page and updates content without reloading.
- 🔄 React is **declarative**: you describe the result, and React updates the screen.
- 🪞 The **Virtual DOM** helps React update only what changed.
- 🗺️ React is the **frontend**, and FastAPI (Python) is the **backend** data provider.
- 💼 React is a highly in-demand skill.
- 📚 Strong JavaScript basics make React much easier.

---

## 🎯 Class Activity

**🛠️ Activity: "Spot the components"**

1. Open any website you use daily (Flipkart, YouTube, Instagram).
2. Press **F12** and look at the page layout.
3. On paper, **draw boxes around the parts you think are components** (navbar, search bar, product card, footer).
4. Mark which components **repeat** (for example, product cards).
5. Draw the **component tree** like the one in this topic.
6. Install the **React Developer Tools** browser extension, visit a React-based site (such as `react.dev`), and open the **Components** tab to see a real component tree.

**Discuss:** Which component appears the most times on your chosen page?

---

# 📋 Assignments — What is React and Why SPA?

| Assignment |
|---|
| Choose three websites. For each, decide whether it feels like a multi-page site or a SPA, and write your reasoning. |
| Draw a component tree on paper for the Instagram home page with at least 6 components. |
| Install the React Developer Tools extension and take a screenshot of the Components tab on any React-based website. |
| Write a comparison table of multi-page website vs SPA with at least five rows, in your own words. |
| Open Gmail or any web app, switch between sections, and watch the Network tab in DevTools. Note whether the full page is reloaded or only data is fetched. |
| Write the counter app in plain JavaScript (HTML, button, click handler) and list how many times you manually touch the DOM. |
| Break your hotel app from earlier into components on paper: list at least five components and the data each one needs. |
| Research and write three lines about each: Angular, Vue, and Svelte, and how they differ from React. |
| Find three companies hiring for a React developer role and note the skills they ask for along with React. |
| Explain the Virtual DOM to a friend or family member using your own analogy, and write what you said. |
| Draw a diagram showing how React (frontend), FastAPI (backend), and a database talk to each other for the hotel app. |

---
---

# 📚 Setting Up React with Vite

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🛠️ Install the tools needed for React development (Node.js, npm, VS Code)
- ⚡ Explain what **Vite** is and why we use it
- 🚀 Create a new React project using Vite
- 🗂️ Understand every important file and folder in the project
- ▶️ Run the development server and see live updates
- 🧹 Clean the starter template and build for production

---

## 📖 Introduction

Writing React is not like writing plain JavaScript where you just open an `.html` file in the browser. React code uses special syntax (**JSX**) and many small files. Browsers cannot understand that directly, so we need a **build tool** to convert it into normal HTML, CSS, and JavaScript.

👉 That tool is **Vite** (pronounced "veet", French for "fast").

**Why does this topic exist?** Before you can learn React, you need a working project on your computer.

**Why Vite?** It starts instantly and updates the browser in milliseconds when you save a file. It is now the standard way to start a React project. The older tool, **Create React App**, is no longer recommended.

**Where is it used?** Almost every modern React project, from student projects to startup products.

---

## 🧠 Detailed Notes

### 🧰 1. What You Need Installed

| Tool | Why we need it | How to check |
|---|---|---|
| **Node.js** (LTS version) | Runs JavaScript outside the browser and powers the build tools | `node -v` |
| **npm** | Comes with Node. Downloads packages (libraries) | `npm -v` |
| **VS Code** | Code editor | Open the app |
| **Chrome** | Browser with great DevTools | Open the app |

Download Node.js from **nodejs.org** and choose the **LTS** (Long Term Support) version. Then check:

```bash
node -v
npm -v
```

If both commands print a version number, you are ready. 🎉

> ⚠️ **Important**
>
> Use a **recent LTS** version of Node.js. Very old versions can make Vite fail to start. If you see strange errors, check your Node version first.

---

### ⚡ 2. What is Vite?

**Vite** is a **build tool and development server**.

| Job | What it means |
|---|---|
| 🖥️ **Dev server** | Runs your app locally at `http://localhost:5173` |
| 🔄 **Hot Module Replacement (HMR)** | When you save a file, only that part updates in the browser instantly, with no full refresh |
| 🔧 **Transforms code** | Converts JSX into plain JavaScript the browser understands |
| 📦 **Bundler** | Combines all your files into small optimized files for production |

---

### 🚀 3. Creating Your First React Project

Open a terminal (VS Code: **Terminal, then New Terminal**) in the folder where you keep your projects, and run:

```bash
npm create vite@latest hotel-ui -- --template react
```

- `hotel-ui` is the **project name** (you can choose any name).
- `--template react` chooses the **React with JavaScript** template.

If the tool asks questions (like extra options), choose the **JavaScript** variant. Then:

```bash
cd hotel-ui
npm install
npm run dev
```

| Command | What it does |
|---|---|
| `cd hotel-ui` | Move into the project folder |
| `npm install` | Downloads all libraries listed in `package.json` into `node_modules` |
| `npm run dev` | Starts the development server |

The terminal will show something like:

```
  VITE ready in 300 ms

  ➜  Local:   http://localhost:5173/
```

Open that link in your browser. You should see the **Vite + React** starter page. 🎉

> 💡 **Tip**
>
> Keep the terminal running while you work. Press **Ctrl + C** in the terminal to stop the server.

🤔 **Quick thinking question:** You created the project, but `npm run dev` says "missing script" or "cannot find package.json". What is the most likely mistake?

✅ **Answer:** You are in the **wrong folder**. Run `cd hotel-ui` first so the terminal is inside the project.

---

### 🗂️ 4. Project Structure Explained

```
hotel-ui/
 ├── node_modules/        ← downloaded libraries (never edit, never share)
 ├── public/              ← static files (images, icons) served as they are
 ├── src/                 ← ⭐ YOUR CODE LIVES HERE
 │    ├── assets/         ← images used inside components
 │    ├── App.jsx         ← the main (root) component
 │    ├── App.css         ← styles for App
 │    ├── index.css       ← global styles
 │    └── main.jsx        ← entry point: starts React
 ├── index.html           ← the ONE html page of the SPA
 ├── package.json         ← project info, libraries, and scripts
 ├── vite.config.js       ← Vite settings
 └── .oxlintrc.json       ← code-quality (linter) rules
```

> ℹ️ **Note**
>
> Templates change over time. Older Vite templates use **ESLint** (`eslint.config.js`) and newer ones use **Oxlint** (`.oxlintrc.json`). Both are linters that spot mistakes in your code. Your folder may also contain a few extra files such as `README.md` or `.gitignore`. That is normal.

| File / Folder | Purpose |
|---|---|
| `index.html` | The **single page** of the SPA. Contains an empty `<div id="root"></div>` |
| `src/main.jsx` | Finds the `root` div and tells React to draw `<App />` inside it |
| `src/App.jsx` | The top-level component. Everything else lives inside it |
| `package.json` | Lists **dependencies** (react, react-dom) and **scripts** (`dev`, `build`) |
| `node_modules/` | Hundreds of downloaded packages. Recreated any time with `npm install` |
| `public/` | Files that are copied as-is (favicon, images referenced by URL) |

> ⚠️ **Important**
>
> **Never upload `node_modules` to GitHub or send it to anyone.** It is huge. Share the project **without** it. The other person simply runs `npm install` to recreate it.

---

### 🔗 5. How the Files Connect

**`index.html`** (simplified):

```html
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.jsx"></script>
</body>
```

**`src/main.jsx`:**

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

**What this does, line by line:**

1. Imports React tools and your `App` component.
2. `document.getElementById('root')` finds the empty div in `index.html`.
3. `createRoot(...)` creates a React "root" inside that div.
4. `.render(<App />)` draws your `App` component there.

`<StrictMode>` is a **development helper**. It runs some checks twice to catch bugs early.

> ℹ️ **Note**
>
> Because of `StrictMode`, you may see a `console.log` print **twice** during development. This is normal and does not happen in the production build.

---

### 🧹 6. Cleaning the Starter Template

The starter page has a logo and a counter. Let's clean it up so we start with a blank slate.

**Replace `src/App.jsx` with:**

```jsx
function App() {
  return (
    <div>
      <h1>🏨 Hotel Paradise</h1>
      <p>React is working!</p>
    </div>
  )
}

export default App
```

**Then:**

- Delete everything inside `src/App.css` (or delete the file and its import).
- You can delete `src/assets/react.svg` if it is unused.

Save the file. The browser updates **instantly** without a refresh. That's Hot Module Replacement. ⚡

Now try changing the text inside `<p>`. Save. Watch the browser.

---

### 📜 7. npm Scripts

Open `package.json`. Find the `scripts` section:

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "lint": "oxlint",
  "preview": "vite preview"
}
```

(Older templates show `"lint": "eslint ."` instead. The idea is the same.)

| Command | Purpose |
|---|---|
| `npm run dev` | Start the **development** server (use this while coding) |
| `npm run build` | Create the **production** build in the `dist/` folder |
| `npm run preview` | Preview the production build locally |
| `npm run lint` | Check code for mistakes and bad practices (using the linter that came with your template) |

---

### 📦 8. Installing Extra Packages

Packages are installed with npm. For example:

```bash
npm install axios
```

This adds it to `package.json` and downloads it into `node_modules`. (We will use the built-in `fetch`, so you do not need axios right now.)

---

### 🏗️ 9. Building for Production

```bash
npm run build
```

Vite creates a **`dist/`** folder with small, optimized HTML, CSS, and JS files. This is what you upload to a hosting service. 🚀

---

### 🔌 10. Connecting to Your FastAPI Backend

Your React dev server runs at `http://localhost:5173` and your FastAPI server at `http://127.0.0.1:8000`. They are different **origins**, so the backend must allow CORS. The hotel backend you built already does this (`allow_origins=["*"]`).

In React you will later call it like this:

```jsx
fetch("http://127.0.0.1:8000/rooms")
  .then((res) => res.json())
  .then((data) => console.log(data))
```

> 💡 **Tip**
>
> Run **two terminals**: one for `uvicorn main:app --reload` (backend) and one for `npm run dev` (frontend).

---

### 🧯 11. Common Setup Problems

| Problem | Likely reason | Fix |
|---|---|---|
| `'node' is not recognized` | Node.js not installed or terminal not restarted | Install Node, then reopen the terminal |
| `Missing script: "dev"` | Wrong folder | `cd` into the project |
| `Cannot find module ...` | Forgot `npm install` | Run `npm install` |
| `Port 5173 is already in use` | Another dev server is running | Close it, or Vite will pick the next port automatically |
| Blank white page | Error in your code | Open **F12 Console** and read the red error |
| Styles not updating | File not saved | Press **Ctrl + S** |

---

## 💡 Real-Life Analogy

🍳 **Vite is like a modern kitchen setup.**

- Your **React code** is the raw ingredients and recipe.
- **Vite** is the kitchen that **prepares** the ingredients quickly, plates the dish (the dev server), and when a guest asks for a change in seasoning, it fixes that **one dish** instantly without remaking the whole meal (Hot Module Replacement).
- `npm run build` is **packing the meal into takeaway boxes** (`dist/`) for delivery.
- `node_modules` is the **big pantry** of ingredients. You don't carry the whole pantry when you share a recipe. You only share the list (`package.json`).

---

## 💻 Real-World Application

| Where | How Vite and React setup is used |
|---|---|
| 🏢 **Startups** | New React apps are commonly started with Vite |
| 🧪 **Prototypes and hackathons** | Instant setup means more time building |
| 📊 **Admin dashboards** | Built with React and Vite, then deployed as static files |
| 🌐 **Hosting platforms** | Vercel, Netlify, and similar services run `npm run build` automatically |
| 🔁 **CI/CD pipelines** | Teams run `npm install` and `npm run build` automatically before release |

---

## 🔍 Industry Example

📘 **Scenario: A new developer joins a team on Monday**

Rohit joins a company that builds a hotel booking dashboard. His lead says: *"Clone the repo and run it."*

**What happens internally:**

1. 📥 He clones the repository. There is **no `node_modules`** folder. It is intentionally excluded.
2. 📦 He runs `npm install`. npm reads `package.json` and downloads the **exact same libraries** the team uses.
3. ▶️ He runs `npm run dev`. Vite starts a local server in under a second.
4. 🔄 He edits a component and saves. The browser updates instantly through HMR.
5. 🚀 On Friday, the team runs `npm run build`. Vite bundles everything into `dist/`, which is deployed to the web.

In under 10 minutes, a new developer has a full working environment. This is why a standard project setup matters.

---

## 📊 Diagram

```
        CREATING A REACT PROJECT

 npm create vite@latest  ──►  project folder created
          │
          ▼
        cd hotel-ui
          │
          ▼
       npm install  ──►  node_modules/ filled
          │
          ▼
      npm run dev   ──►  http://localhost:5173  🎉


        HOW THE FILES CONNECT

  index.html                main.jsx                 App.jsx
 ┌────────────────┐      ┌─────────────────┐     ┌────────────────┐
 │ <div id="root">│◄─────│ createRoot(root)│◄────│ function App() │
 │ </div>         │      │ .render(<App/>) │     │ returns JSX    │
 └────────────────┘      └─────────────────┘     └────────────────┘
        │
        ▼
   The browser shows your component tree inside #root


        DEV vs PRODUCTION

  npm run dev    ──►  fast, live updates, for coding
  npm run build  ──►  dist/ folder, small and optimized, for deployment
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can double-click `index.html` to run my React app." | Use `npm run dev`. The browser can't read JSX directly. |
| "I should edit files inside `node_modules`." | Never. It is auto-generated and will be overwritten. |
| "I should upload `node_modules` to GitHub." | Never. Share only the code. Others run `npm install`. |
| "My code is in the project root." | Your React code belongs in the **`src/`** folder. |
| "Closing the terminal doesn't matter." | The dev server stops, and the page will no longer load. |
| "`npm install` is needed every time I run." | Only once, or when `package.json` changes. |
| "The console message printing twice is a bug." | It is `StrictMode` in development. |

---

## 💬 Interview Corner

**Q1. What is Vite?**
A fast build tool and dev server for modern web projects. It provides instant startup, hot module replacement, and optimized production builds.

**Q2. What is the purpose of `package.json`?**
It stores project information, the list of dependencies, and scripts such as `dev` and `build`.

**Q3. What does `npm install` do?**
It reads `package.json` and downloads all required libraries into the `node_modules` folder.

**Q4. What is the difference between `npm run dev` and `npm run build`?**
`dev` starts a local development server with live updates. `build` creates optimized static files in `dist/` for deployment.

---

## 📝 Quick Summary

- 🛠️ You need **Node.js (LTS)**, **npm**, **VS Code**, and a browser.
- ⚡ **Vite** is the build tool and dev server used to run React projects.
- 🚀 Create a project with `npm create vite@latest <name> -- --template react`.
- 📦 Run `npm install` once, then `npm run dev` to start.
- 🗂️ Your code lives in **`src/`**, starting from `main.jsx` and `App.jsx`.
- 🔗 `index.html` has an empty `root` div that React fills.
- 🔄 **HMR** updates the browser instantly when you save.
- 🏗️ `npm run build` produces the `dist/` folder for deployment.
- 🙅 Never edit or share `node_modules`.

---

## 🎯 Class Activity

**🛠️ Activity: "Hello React, from my own machine"**

1. Check `node -v` and `npm -v`.
2. Create a project named `hotel-ui` using Vite's React template.
3. Run `npm install` and `npm run dev`. Open `http://localhost:5173`.
4. Replace `App.jsx` with the clean version from this topic.
5. Change the heading to **your own hotel name** and save. Watch the browser update without refreshing.
6. Open **F12, Console** and add `console.log("App loaded")` inside `App()` (before `return`). How many times does it print? Why?
7. Open the **Elements** tab and find the `<div id="root">`. Notice your content inside it.

---

# 📋 Assignments — Setting Up React with Vite

| Assignment |
|---|
| Install Node.js LTS and take a screenshot showing the output of `node -v` and `npm -v`. |
| Create a Vite React project named `my-first-react` and run it. Take a screenshot of the running starter page. |
| Clean the starter template so it shows only your name in an `<h1>` and a one-line `<p>`. |
| Draw the project folder structure on paper and write one line about the purpose of each file in `src/`. |
| Open `package.json` and list the dependencies and the four scripts with a one-line explanation each. |
| Add `console.log("rendered")` in `App()` and explain in two lines why it prints twice in development. |
| Deliberately delete `node_modules`, try `npm run dev`, note the error, and fix it using `npm install`. |
| Change the title in `index.html` (inside `<title>`) to your hotel's name and observe the browser tab. |
| Run `npm run build`, open the `dist/` folder, and list the files created. |
| Run `npm run preview` and compare it with `npm run dev`. Write two differences you notice. |
| Start the dev server on another terminal while the first is still running. Note what Vite does about the port. |
| Create a `.gitignore` check: confirm that `node_modules` is listed in it and explain why. |
| Start your FastAPI backend and, from `App.jsx`, call `fetch("http://127.0.0.1:8000/ping")` and print the result in the console. |

---
---

# 📚 JSX Syntax and Differences from HTML

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- ✍️ Explain what JSX is and why React uses it
- 🔄 Convert HTML into valid JSX
- 🎯 Embed JavaScript expressions inside JSX using `{ }`
- 🎨 Apply classes and inline styles correctly in JSX
- 🔀 Render content conditionally (ternary and `&&`)
- 📋 Render lists with `map()` and `key`
- 🧱 Use Fragments to return multiple elements

---

## 📖 Introduction

In the last topic, you saw something strange in `App.jsx`: **HTML inside JavaScript**.

```jsx
function App() {
  return <h1>Hello</h1>
}
```

That is not a string, and it is not exactly HTML either. It is **JSX**.

**JSX** stands for **JavaScript XML**. It is a syntax that lets you **write HTML-like markup directly inside JavaScript**. Vite converts it into regular JavaScript before the browser runs it.

**Why does this topic exist?** In React, the **structure** and the **logic** of a UI piece live together in one place, because they are tightly connected: the button's look and what it does belong to the same component.

**Why is it important?** Every React component you ever write will contain JSX. Small syntax mistakes here cause most beginner errors.

**Where is it used?** Inside every React component's `return`.

---

## 🧠 Detailed Notes

### ✍️ 1. What is JSX?

JSX looks like HTML, but it is **JavaScript underneath**.

```jsx
const element = <h1 className="title">Hello</h1>
```

Behind the scenes, this becomes a plain JavaScript function call that creates an object describing the element. You never write that by hand. JSX is simply a **friendlier way** to describe the UI.

> ℹ️ **Note**
>
> JSX is **optional** in theory, but nobody writes React without it. Browsers can't read JSX, so Vite converts it before the page loads.

---

### 🧱 2. Rule 1: Return ONE Root Element

A component can return only **one top-level element**.

```jsx
// ❌ Error: two siblings at the top level
function App() {
  return (
    <h1>Hotel</h1>
    <p>Welcome</p>
  )
}

// ✅ Wrap them in one parent
function App() {
  return (
    <div>
      <h1>Hotel</h1>
      <p>Welcome</p>
    </div>
  )
}
```

If you don't want an extra `<div>` in the page, use a **Fragment**: an empty wrapper that disappears in the final HTML.

```jsx
function App() {
  return (
    <>
      <h1>Hotel</h1>
      <p>Welcome</p>
    </>
  )
}
```

> 💡 **Tip**
>
> Wrap multi-line JSX in **parentheses** `( )` after `return`. Otherwise JavaScript may stop reading at the end of the first line.

---

### 🔒 3. Rule 2: Close Every Tag

HTML lets you leave some tags open. JSX does **not**.

```jsx
// HTML (allowed)           // JSX (required)
<img src="room.jpg">        <img src="room.jpg" />
<input type="text">         <input type="text" />
<br>                        <br />
```

Any element without children must be **self-closed** with `/>`.

---

### 🐫 4. Rule 3: camelCase Attributes

JSX attributes become JavaScript properties, so they use **camelCase**. Two names are different from HTML because they clash with JavaScript keywords.

| HTML | JSX | Why |
|---|---|---|
| `class` | **`className`** | `class` is a JavaScript keyword |
| `for` (on label) | **`htmlFor`** | `for` is a JavaScript keyword |
| `onclick` | **`onClick`** | camelCase for events |
| `onchange` | **`onChange`** | camelCase for events |
| `tabindex` | **`tabIndex`** | camelCase |
| `maxlength` | **`maxLength`** | camelCase |
| `readonly` | **`readOnly`** | camelCase |

```jsx
<label htmlFor="name">Name</label>
<input id="name" className="input-box" maxLength={30} />
```

> ℹ️ **Note**
>
> `data-*` and `aria-*` attributes (like `data-room-id`) keep their hyphens as they are.

---

### 🔢 5. Rule 4: JavaScript Inside `{ }`

Curly braces open a **window into JavaScript** inside your markup. Put any JavaScript **expression** inside.

```jsx
function Welcome() {
  const hotelName = "Hotel Paradise"
  const price = 3000
  const nights = 2

  return (
    <div>
      <h1>Welcome to {hotelName}</h1>
      <p>Total: ₹{price * nights}</p>
      <p>{hotelName.toUpperCase()}</p>
      <p>Booked on: {new Date().toDateString()}</p>
    </div>
  )
}
```

**What can go inside `{ }`?** Anything that produces a **value**: variables, math, function calls, ternary expressions.

**What cannot?** **Statements** such as `if`, `for`, and `while` (they don't produce a value). Use a ternary, `&&`, or `map()` instead.

**Using `{ }` in attributes:**

```jsx
const imageUrl = "room1.jpg"
<img src={imageUrl} alt="Deluxe room" />      // ✅ no quotes around {imageUrl}
<img src="{imageUrl}" />                       // ❌ treated as literal text
```

🤔 **Quick thinking question:** What will `<p>{2 + 3}</p>` show on the page?

✅ **Answer:** `5`. React evaluates the expression and displays the result.

---

### 🎨 6. Styling in JSX

**Option A: CSS classes (recommended)**

```jsx
<div className="card">Room 101</div>
```

```css
/* App.css */
.card { border: 1px solid #ccc; padding: 10px; border-radius: 8px; }
```

**Option B: Inline styles use an OBJECT, not a string**

```jsx
<p style={{ color: "red", fontSize: "20px", backgroundColor: "#eee" }}>
  Sold out
</p>
```

- The **outer** `{ }` means "JavaScript inside JSX".
- The **inner** `{ }` is the **JavaScript object** holding the styles.
- CSS names become **camelCase**: `font-size` becomes `fontSize`.

> 💡 **Tip**
>
> Prefer `className` with CSS files for most styling. Use inline `style` for small, dynamic values.

---

### 🔀 7. Conditional Rendering

Show different things depending on data. Since `if` can't go inside JSX, use these patterns.

**Ternary operator (either / or):**

```jsx
const isAvailable = true

<p>{isAvailable ? "✅ Available" : "❌ Booked"}</p>
```

**`&&` operator (show something or nothing):**

```jsx
const guests = 3

{guests > 2 && <p>Group discount applied! 🎉</p>}
```

**Plain `if` before the `return`:**

```jsx
function RoomStatus({ available }) {
  if (!available) {
    return <p>Sorry, sold out.</p>
  }
  return <p>Book now!</p>
}
```

> ⚠️ **Important: the `0` trap**
>
> `{count && <p>Items</p>}` shows a literal **`0`** on the screen when `count` is `0`. Write `{count > 0 && <p>Items</p>}` instead.

---

### 📋 8. Rendering Lists with `map()`

You already know `map()` from JavaScript. In React, it turns an **array of data** into an **array of elements**.

```jsx
function RoomList() {
  const rooms = [
    { id: 1, no: 101, type: "Standard", price: 3000 },
    { id: 2, no: 201, type: "Deluxe", price: 4500 },
    { id: 3, no: 301, type: "Suite", price: 7000 },
  ]

  return (
    <ul>
      {rooms.map((room) => (
        <li key={room.id}>
          Room {room.no} - {room.type} - ₹{room.price}
        </li>
      ))}
    </ul>
  )
}
```

**The `key` attribute:**

- Every item in a list needs a **unique `key`**.
- It helps React track which item is which when the list changes.
- Use a **stable unique id** from your data (`room.id`).
- Avoid using the array **index** as the key if items can be added, removed, or reordered.

---

### 💬 9. Comments in JSX

```jsx
return (
  <div>
    {/* This is a JSX comment */}
    <h1>Hotel</h1>
  </div>
)
```

A normal `// comment` outside the JSX (in the JavaScript part) works as usual.

---

### 🧾 10. HTML vs JSX at a Glance

| Feature | HTML | JSX |
|---|---|---|
| CSS class | `class="box"` | `className="box"` |
| Label link | `for="name"` | `htmlFor="name"` |
| Event | `onclick="go()"` | `onClick={go}` |
| Inline style | `style="color:red"` | `style={{ color: "red" }}` |
| Self-closing | `<br>`, `<img>` | `<br />`, `<img />` |
| Multiple roots | Allowed | One root (or Fragment) |
| Comments | `<!-- -->` | `{/* */}` |
| JavaScript values | Not possible | `{ expression }` |
| Boolean attribute | `disabled` | `disabled` or `disabled={true}` |

---

### 🔄 11. Converting HTML to JSX: Practice

**HTML:**

```html
<div class="card">
  <img src="room.jpg">
  <label for="guest">Guest</label>
  <input id="guest" maxlength="20">
  <button onclick="book()">Book</button>
</div>
```

**JSX:**

```jsx
<div className="card">
  <img src="room.jpg" alt="Room" />
  <label htmlFor="guest">Guest</label>
  <input id="guest" maxLength={20} />
  <button onClick={book}>Book</button>
</div>
```

Number of changes: `className`, self-closed `img`, `htmlFor`, self-closed `input`, `maxLength` as a number in `{}`, and `onClick={book}`.

---

## 💡 Real-Life Analogy

📝 **JSX is like a recipe card with fill-in-the-blanks.**

- The **HTML-like part** is the printed recipe layout (headings, steps).
- The **`{ }` curly braces** are the blanks where you write in today's values: *"Serves {number of guests}"*.
- **`map()`** is like a **photocopier**: one card design, copied once per dish on today's menu.
- **`key`** is the **unique number written on each copy**, so the chef never mixes them up if the menu changes.

---

## 💻 Real-World Application

| Where | How JSX features are used |
|---|---|
| 🛒 **Product pages** | `map()` renders hundreds of product cards from an array |
| 🔔 **Notification badge** | `{count > 0 && <span>{count}</span>}` hides the badge when empty |
| 🌗 **Dark mode** | `className={isDark ? "dark" : "light"}` |
| ❌ **Form errors** | `{error && <p className="error">{error}</p>}` |
| 🏷️ **Status labels** | A ternary shows "Available" or "Booked" |
| 📊 **Dashboards** | Table rows generated with `map()` from API data |

---

## 🔍 Industry Example

📘 **Scenario: Showing the room grid on a hotel dashboard**

The API returns an array of rooms. The developer writes:

```jsx
function RoomGrid({ rooms }) {
  return (
    <div className="grid">
      {rooms.length === 0 && <p>No rooms found.</p>}

      {rooms.map((room) => (
        <div
          key={room.no}
          className={room.booked_today ? "card booked" : "card free"}
        >
          <h3>Room {room.no}</h3>
          <p>{room.type} - ₹{room.price}</p>
          <p>{room.booked_today ? "❌ Booked today" : "✅ Available"}</p>
        </div>
      ))}
    </div>
  )
}
```

**What happens internally:**

1. 📦 The server sends the rooms as JSON, which becomes a JavaScript array.
2. 🔁 `map()` loops over the array and creates one `<div>` element **per room**.
3. 🏷️ `key={room.no}` gives each card a unique identity.
4. 🎨 `className` switches between `"card booked"` and `"card free"` using a **ternary**.
5. 🔄 When a room's status changes, React compares old and new, and updates **only that one card** on screen.

---

## 📊 Diagram

```
          WHAT JSX BECOMES

   You write:                          Browser runs:
  ┌──────────────────────┐            ┌─────────────────────────┐
  │ <h1 className="t">   │  Vite      │ plain JavaScript that   │
  │   Hello {name}       │ ───────►   │ builds the same element │
  │ </h1>                │ converts   │ in the DOM              │
  └──────────────────────┘            └─────────────────────────┘


          { } = WINDOW INTO JAVASCRIPT

   <p> Total: ₹{ price * nights } </p>
        ▲             ▲
        │             └── JavaScript expression (evaluated)
        └── plain text


          LIST RENDERING WITH map()

   [ room1 , room2 , room3 ]
        │       │       │
      map()   map()   map()
        ▼       ▼       ▼
   <Card/>  <Card/>  <Card/>     (each with a unique key)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can use `class` like in HTML." | Use **`className`**. |
| "I can return two sibling elements." | Wrap them in one parent or a Fragment `<>...</>`. |
| "`<img src='a.jpg'>` is fine." | JSX requires **self-closing**: `<img src="a.jpg" />`. |
| "`style="color: red"` works." | Style takes an **object**: `style={{ color: "red" }}`. |
| "I can write `if` inside `{ }`." | Use a ternary, `&&`, or move the `if` above the `return`. |
| "Keys are optional in lists." | Always give each item a unique `key`. |
| "Using the array index as key is always fine." | It can break when the list changes. Prefer a unique id. |
| "`{count && <p>..</p>}` is safe with numbers." | It shows `0` when count is 0. Use `count > 0 &&`. |
| "`<img src="{url}">` shows my image." | Remove the quotes: `src={url}`. |
| "Lowercase component names are fine." | Components must start with a **capital letter**. (More on this next.) |

---

## 💬 Interview Corner

**Q1. What is JSX?**
A syntax extension that lets you write HTML-like markup inside JavaScript. It is compiled into regular JavaScript calls before running in the browser.

**Q2. Why do we use `className` instead of `class` in JSX?**
Because `class` is a reserved keyword in JavaScript, and JSX attributes become JavaScript object properties.

**Q3. Why does each item in a list need a `key`?**
The key helps React identify which items changed, were added, or were removed, so it can update the DOM efficiently and correctly.

**Q4. What is a Fragment and when do we use it?**
A Fragment (`<>...</>`) lets a component return multiple elements without adding an extra wrapper node to the DOM.

---

## 📝 Quick Summary

- ✍️ **JSX** lets you write HTML-like code inside JavaScript.
- 🧱 Return **one root element**, or use a Fragment `<>...</>`.
- 🔒 **Close every tag**, using `<img />`, `<input />`, `<br />`.
- 🐫 Use **camelCase** attributes, with `className`, `htmlFor`, and `onClick`.
- 🔢 Use **`{ }`** to embed JavaScript expressions (not statements).
- 🎨 Inline `style` takes an **object**: `style={{ color: "red" }}`.
- 🔀 Conditional rendering uses **ternary** and **`&&`**.
- 📋 Render lists with **`map()`** and a unique **`key`**.
- 💬 JSX comments are `{/* ... */}`.

---

## 🎯 Class Activity

**🛠️ Activity: "Convert and render"**

In your `hotel-ui` project, edit `App.jsx`:

1. Show the hotel name in an `<h1>` using a **variable** and `{ }`.
2. Create an array of **5 room objects** (`id`, `no`, `type`, `price`, `available`).
3. Use `map()` to show each room as a `<div className="card">` with a `key`.
4. Show **"✅ Available"** or **"❌ Booked"** using a **ternary**.
5. Add a line using `&&` that shows **"Hurry! Only a few rooms left"** only when fewer than 3 rooms are available.
6. Give booked cards a red border using the `style` object and available cards a green border.
7. Take this HTML and convert it to JSX in a second file for practice:

```html
<form class="booking">
  <label for="n">Name</label>
  <input id="n" maxlength="30">
  <br>
  <button onclick="save()">Save</button>
</form>
```

---

# 📋 Assignments — JSX Syntax and Differences from HTML

| Assignment |
|---|
| Create `App.jsx` that shows your name, age, and city using JavaScript variables inside `{ }`. |
| Convert a small HTML page (heading, image, input, label, button) to valid JSX and list every change you made. |
| Deliberately return two sibling elements without a wrapper, read the error message, and fix it using both a `<div>` and a Fragment. |
| Show a price calculation in JSX, for example `{price * nights}` with a ₹ sign, and a formatted date using `new Date().toDateString()`. |
| Create an array of 5 rooms and display them as a list with `map()` and proper `key` values. |
| Remove the `key` from your list, open the console, and note the warning React prints. Then fix it. |
| Show "Available" or "Booked" with a ternary, and show a "Hot deal!" badge only for rooms under ₹3500 using `&&`. |
| Demonstrate the `0` trap: render `{count && <p>Items</p>}` with `count = 0`, observe the result, and fix it. |
| Style a card with a CSS class (`className`) and also style one element with the `style` object. Write which you prefer and why. |
| Build a `<select>` of room types by mapping over an array of strings, with the correct keys. |
| Write a JSX comment and a normal JavaScript comment in the same component and explain where each is valid. |
| Create an image gallery that maps over an array of image URLs, using `src={url}` and meaningful `alt` text. |
| Create a profile card for a staff member with a name, role, and skills list (array rendered with `map()`). |

---
---

# 📚 Functional Components and Props

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🧩 Explain what a component is and write a **functional component**
- 📁 Organize components into separate files using `export` and `import`
- 📨 Pass data into components using **props**
- 🎁 Use props destructuring, default values, and the special `children` prop
- 🔒 Understand why props are **read-only** and flow **one way**
- 🌳 Build a small component tree for the hotel app

---

## 📖 Introduction

Until now, we put everything inside `App.jsx`. That is like writing an entire book as one paragraph. 😅

Real apps are split into **components**: small, focused, reusable pieces. A `RoomCard` component knows how to display **one** room. You can then use it 50 times with different data.

But how does the `RoomCard` know *which* room to show? 👉 Through **props**.

**Props** (short for *properties*) are **inputs** that a parent component passes to a child component, just like arguments passed to a function.

**Why does this topic exist?** Reusable components with changing data are the entire idea of React.

**Why is it important?** Every React app is built from components and props. Mastering this topic is the foundation for everything that follows.

**Where is it used?** In every single React project.

---

## 🧠 Detailed Notes

### 🧩 1. What is a Functional Component?

A **functional component** is a **JavaScript function that returns JSX**.

```jsx
function Greeting() {
  return <h2>Welcome to Hotel Paradise!</h2>
}
```

**The rules:**

1. The name **must start with a capital letter** (`Greeting`, not `greeting`).
2. It must **return JSX** (or `null` if it shows nothing).
3. It returns **one root element** (or a Fragment).

**Using a component** looks like an HTML tag:

```jsx
function App() {
  return (
    <div>
      <Greeting />
      <Greeting />
    </div>
  )
}
```

`<Greeting />` renders the component. Using it twice shows the heading twice.

> ⚠️ **Important**
>
> **Capital letter = component, lowercase = HTML tag.** React treats `<greeting />` as an unknown HTML tag and `<Greeting />` as your component.

> ℹ️ **Note**
>
> Older React code used **class components**. Modern React uses **functional components** with hooks, so that's what you learn first.

---

### 📁 2. One Component Per File

Keep each component in its own file, and use `export` / `import`.

**📁 Suggested structure:**

```
src/
 ├── components/
 │     ├── RoomCard.jsx
 │     ├── RoomList.jsx
 │     └── Navbar.jsx
 ├── App.jsx
 └── main.jsx
```

**`src/components/Navbar.jsx`:**

```jsx
function Navbar() {
  return (
    <nav>
      <h1>🏨 Hotel Paradise</h1>
    </nav>
  )
}

export default Navbar
```

**`src/App.jsx`:**

```jsx
import Navbar from "./components/Navbar"

function App() {
  return (
    <div>
      <Navbar />
      <p>Rooms coming soon...</p>
    </div>
  )
}

export default App
```

- `export default` makes the component available.
- `import Navbar from "./components/Navbar"` brings it in. (The `.jsx` extension can be omitted.)

---

### 📨 3. Props: Passing Data to Components

Pass props like HTML attributes. Receive them as the function's **parameter**.

**Using the component (the parent):**

```jsx
<RoomCard no={101} type="Standard" price={3000} available={true} />
<RoomCard no={201} type="Deluxe" price={4500} available={false} />
```

**Defining the component (the child):**

```jsx
function RoomCard(props) {
  return (
    <div className="card">
      <h3>Room {props.no}</h3>
      <p>{props.type} - ₹{props.price}</p>
      <p>{props.available ? "✅ Available" : "❌ Booked"}</p>
    </div>
  )
}

export default RoomCard
```

**How values are written:**

| Value type | How to pass | Example |
|---|---|---|
| String | Quotes | `type="Deluxe"` |
| Number | Curly braces | `price={4500}` |
| Boolean | Curly braces | `available={true}` |
| Variable | Curly braces | `price={roomPrice}` |
| Array / Object | Curly braces | `tags={["wifi", "ac"]}` |
| Function | Curly braces | `onBook={handleBook}` |

> ⚠️ **Important**
>
> `price="3000"` passes a **string**. `price={3000}` passes a **number**. This matters for math!

---

### ✂️ 4. Destructuring Props (Cleaner Code)

Instead of writing `props.` every time, **destructure** in the parameter:

```jsx
function RoomCard({ no, type, price, available }) {
  return (
    <div className="card">
      <h3>Room {no}</h3>
      <p>{type} - ₹{price}</p>
      <p>{available ? "✅ Available" : "❌ Booked"}</p>
    </div>
  )
}
```

Note the **curly braces in the parameter**: `({ no, type, price, available })`. This is the same object destructuring you learned in JavaScript.

---

### 🪂 5. Default Props

Give a prop a **fallback value** when the parent doesn't send one:

```jsx
function RoomCard({ no, type = "Standard", price = 3000, available = true }) {
  // ...
}

<RoomCard no={102} />    // type = "Standard", price = 3000, available = true
```

---

### 🎁 6. The `children` Prop

Content placed **between** the opening and closing tags is automatically passed as **`children`**.

```jsx
function Card({ title, children }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      {children}
    </div>
  )
}

function App() {
  return (
    <Card title="Special Offer">
      <p>Book 3 nights and get 1 night free! 🎉</p>
      <button>Claim</button>
    </Card>
  )
}
```

`children` makes components flexible **wrappers** (cards, modals, layouts).

---

### 🔁 7. Rendering Many Components from Data

This is where components and `map()` come together.

```jsx
import RoomCard from "./RoomCard"

function RoomList() {
  const rooms = [
    { id: 1, no: 101, type: "Standard", price: 3000, available: true },
    { id: 2, no: 201, type: "Deluxe", price: 4500, available: false },
    { id: 3, no: 301, type: "Suite", price: 7000, available: true },
  ]

  return (
    <div className="room-list">
      {rooms.map((room) => (
        <RoomCard
          key={room.id}
          no={room.no}
          type={room.type}
          price={room.price}
          available={room.available}
        />
      ))}
    </div>
  )
}

export default RoomList
```

**Shortcut with the spread operator:**

```jsx
{rooms.map((room) => (
  <RoomCard key={room.id} {...room} />
))}
```

`{...room}` passes every property of the object as a prop. (`key` is not passed down as a prop. It is used only by React.)

🤔 **Quick thinking question:** You have 100 rooms in an array. How many `RoomCard` files do you need to write?

✅ **Answer:** **One.** You write the component once and render it 100 times with different props.

---

### 🔒 8. Props Are Read-Only

A component must **never change its own props**.

```jsx
function RoomCard({ price }) {
  price = price + 500        // ❌ Don't do this
  return <p>{price}</p>
}
```

If you need a changed value, create a **new variable**:

```jsx
function RoomCard({ price }) {
  const priceWithTax = price * 1.18     // ✅ new variable
  return <p>₹{priceWithTax}</p>
}
```

> 💡 **Tip**
>
> Think of props like **function arguments you only read**. If a value needs to change over time, it should be **state**, which is the next topic.

---

### ➡️ 9. One-Way Data Flow

Data flows **down** the tree, from parent to child. A child cannot reach up and change its parent's data directly.

```
        App  (owns the data)
         │  passes props ↓
      RoomList
         │  passes props ↓
      RoomCard (displays the data)
```

To let a child **tell** the parent something happened (like "Book button clicked"), the parent passes a **function as a prop**:

```jsx
function App() {
  function handleBook(roomNo) {
    console.log("Booking requested for room", roomNo)
  }

  return <RoomCard no={101} type="Standard" onBook={handleBook} />
}

function RoomCard({ no, type, onBook }) {
  return (
    <div className="card">
      <h3>Room {no} ({type})</h3>
      <button onClick={() => onBook(no)}>Book</button>
    </div>
  )
}
```

The child **calls** the function it was given. This pattern is used everywhere in React. We will build on it in the next topics.

---

### 🌳 10. Thinking in Components

How to decide what becomes a component:

| Ask yourself | If yes... |
|---|---|
| Does this piece **repeat**? | Make it a component (`RoomCard`) |
| Is this a **clear, separate** part of the screen? | Make it a component (`Navbar`, `Footer`) |
| Is this piece getting **too long**? | Split it into smaller components |
| Does this piece have **its own job**? | Give it its own component |

**Hotel app component tree:**

```
 App
  ├── Navbar
  ├── RoomList
  │     └── RoomCard  (× many)
  ├── BookingForm
  └── BookingTable
        └── BookingRow  (× many)
```

---

## 💡 Real-Life Analogy

🍕 **A component is a pizza recipe, and props are the toppings order.**

- The **recipe** (component) is written **once**: dough, sauce, bake.
- Each **order** (props) says: *"Margherita, large, extra cheese"* or *"Veg, small, no onions"*.
- The same recipe produces **different pizzas** depending on the order.
- The kitchen **never changes the customer's order slip** (props are read-only). It just reads it.
- And `children` is like **"anything extra on top"**: whatever the customer places inside the box.

---

## 💻 Real-World Application

| Where | Components and props in action |
|---|---|
| 🛒 **Amazon** | One `ProductCard` component reused for thousands of products |
| 🎵 **Spotify** | `SongRow` component receives title, artist, and duration as props |
| 📱 **Instagram** | `Post` component receives image, likes, and caption |
| 🧭 **Any website** | `Navbar` and `Footer` shared across all pages |
| 🪟 **Popups** | A `Modal` component with `children` for flexible content |
| 📊 **Dashboards** | `StatCard` receives a title, a number, and a color |

---

## 🔍 Industry Example

📘 **Scenario: A design-system team at an e-commerce company**

A company wants **every button, card, and badge** across 20 internal tools to look identical.

**What happens internally:**

1. 🎨 A small team builds a shared **component library**: `Button`, `Card`, `Badge`.
2. 📨 Each component takes **props** such as `variant="primary"`, `size="large"`, `disabled`.
3. 🧩 Product teams import `Button` and write `<Button variant="danger">Delete</Button>`.
4. ✏️ The design team later changes the danger color. They edit **one file**.
5. 🚀 All 20 tools update on their next release, with no manual changes needed.

That is the power of reusable components: **fix once, update everywhere**.

---

## 📊 Diagram

```
          COMPONENT + PROPS

   Parent passes props          Child receives props
  ┌──────────────────────┐    ┌──────────────────────────┐
  │ <RoomCard            │    │ function RoomCard({      │
  │    no={101}          │───►│   no, type, price        │
  │    type="Standard"   │    │ }) {                     │
  │    price={3000} />   │    │   return <div>...</div>  │
  └──────────────────────┘    └──────────────────────────┘


          ONE-WAY DATA FLOW

          App ── data ──► RoomList ── data ──► RoomCard
                                                 │
          App ◄── function call (onBook) ◄───────┘
              (child tells parent through a function prop)


          children PROP

   <Card title="Offer">            function Card({title, children}) {
      <p>Hello</p>        ──►         <h3>{title}</h3>
   </Card>                            {children}  ← <p>Hello</p> appears here
                                   }
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can name a component `roomCard`." | Component names **must start with a capital letter**. |
| "I should call it like `RoomCard()`." | Use it as a tag: `<RoomCard />`. |
| "Props are the same as state." | Props come **from the parent** and are read-only. State is owned by the component (next topic). |
| "I can modify props inside the child." | Props are **read-only**. Create a new variable instead. |
| "`price="3000"` is a number." | It is a **string**. Use `price={3000}`. |
| "I forgot the curly braces in the parameter." | Use `({ no, type })` to destructure. Without braces, the whole object arrives as one value. |
| "I should define components inside other components." | Define components at the **top level** of the file. |
| "A component can return two siblings." | Return one root element or a Fragment. |
| "I forgot `export default`." | Without it, `import` fails or gives `undefined`. |
| "A child can change the parent's variable directly." | Data flows down. Use a **function prop** for upward communication. |

---

## 💬 Interview Corner

**Q1. What is a functional component?**
A JavaScript function that accepts props and returns JSX describing a piece of UI.

**Q2. What are props?**
Inputs passed from a parent to a child component, like function arguments. They are read-only.

**Q3. Why must component names start with a capital letter?**
React uses the capital letter to tell components apart from regular HTML tags.

**Q4. What is the `children` prop?**
A special prop containing whatever is placed between a component's opening and closing tags. It makes wrapper components flexible.

---

## 📝 Quick Summary

- 🧩 A **functional component** is a function that returns JSX.
- 🔠 Names start with a **capital letter**.
- 📁 One component per file, using `export default` and `import`.
- 📨 **Props** pass data from parent to child: `<RoomCard no={101} />`.
- ✂️ Destructure props in the parameter: `function RoomCard({ no, type })`.
- 🪂 Use default values like `type = "Standard"`.
- 🎁 **`children`** holds whatever is nested inside a component's tags.
- 🔒 Props are **read-only** and flow **one way**, from parent to child.
- 🔁 Combine `map()` with components to render lists of data.

---

## 🎯 Class Activity

**🛠️ Activity: "Build the Room Dashboard"**

In `hotel-ui`:

1. Create `src/components/RoomCard.jsx`. It receives `no`, `type`, `price`, and `available` as props, with default `type = "Standard"`.
2. Create `src/components/RoomList.jsx` with an array of **6 rooms** and render them using `map()` with `key`.
3. Create `src/components/Navbar.jsx` showing the hotel name.
4. Create a reusable `src/components/Card.jsx` that accepts `title` and `children`. Use it to show a **"Today's Offer"** box in `App.jsx`.
5. In `App.jsx`, compose `Navbar`, the offer card, and `RoomList`.
6. Add an `onBook` function prop: `RoomCard` shows a **Book** button (only when available) that calls `onBook(no)`. In `App`, make `onBook` print a message to the console.
7. Style available cards green and booked cards red using `className`.

**Discuss:** Which components could you reuse in a completely different project?

---

# 📋 Assignments — Functional Components and Props

| Assignment |
|---|
| Create a `Footer` component showing "© 2026 Hotel Paradise" and use it in `App.jsx`. |
| Create a `Navbar` component with the hotel name and three links (Home, Rooms, Bookings). Put it in its own file and import it. |
| Create a `RoomCard` component that takes `no`, `type`, `price`, and `available` as props and displays them. |
| Render 6 `RoomCard` components from an array using `map()` and keys. Take a screenshot. |
| Add default values to `RoomCard` for `type` and `price`, then render `<RoomCard no={999} />` and describe what you see. |
| Pass a number as `price="3000"` (string) and `price={3000}` (number) and show with `typeof` in `console.log` that they differ. |
| Create a `Card` wrapper component with a `title` prop and `children`, and use it three times with different content. |
| Create a `StaffCard` component (name, role, and skills array) and render five staff members. |
| Try to modify a prop inside a child component. Observe the result and rewrite the code properly using a new variable. |
| Create a `Badge` component with a `color` and `text` prop that you use for "New", "Sale", and "Sold out" labels. |
| Pass a function prop `onBook` from `App` to `RoomCard`. Make the button call it with the room number and print a message in the console. |
| Use the spread syntax `{...room}` to pass all properties of a room object and list one advantage and one risk of that style. |
| Draw the component tree for the full hotel app on paper and mark which components receive props and what those props are. |
| Create a `Stats` row showing three `StatCard` components: total rooms, available rooms, and booked rooms, computed from the array in `App`. |

---
---

# 📚 The `useState` Hook for Local State

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🧠 Explain what **state** is and why normal variables are not enough
- 🪝 Use the `useState` hook in a functional component
- 🔄 Understand how updating state causes a **re-render**
- ➕ Use the **functional update** form when new state depends on old state
- 📋 Update **arrays and objects** in state correctly (without mutation)
- 📏 Follow the **rules of hooks**

---

## 📖 Introduction

Props let a parent send data **down** to a child. But what about data that **changes over time** inside a component?

- A **counter** that goes up when you click
- Whether a **menu is open or closed**
- What the user has **typed so far**
- The **list of bookings** that grows when a booking is made

This changing data is called **state**.

👉 In React, you manage state with a **hook** called **`useState`**.

**Why does this topic exist?** Plain variables inside a component don't make React update the screen. State does.

**Why is it important?** State is what turns a static page into an interactive app. It is the single most important concept in React.

**Where is it used?** Every interactive piece of every React app.

---

## 🧠 Detailed Notes

### 🚫 1. Why Normal Variables Don't Work

Try this component:

```jsx
function Counter() {
  let count = 0

  function handleClick() {
    count = count + 1
    console.log(count)
  }

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={handleClick}>Add</button>
    </div>
  )
}
```

Click the button. The **console** shows `1, 2, 3...`, but the **screen stays at `0`**. 😮

**Two reasons:**

1. React doesn't know the variable changed, so it **doesn't re-draw** the screen.
2. Even if it did re-draw, the function would run again from the top, and `let count = 0` would **reset** the value.

We need a way to (a) **remember** a value between renders and (b) **tell React** to update the screen. That is exactly what `useState` does.

---

### 🪝 2. What is a Hook?

A **hook** is a special React function whose name starts with **`use`**. Hooks let functional components "hook into" React features like state.

`useState` is the first and most important hook. (You will meet others like `useEffect` later.)

---

### ✨ 3. The `useState` Syntax

```jsx
import { useState } from "react"

function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  )
}
```

Now the screen updates on every click. 🎉

**Breaking down this line:**

```jsx
const [count, setCount] = useState(0)
```

| Part | Meaning |
|---|---|
| `useState(0)` | Creates a state value. `0` is the **initial value** |
| `count` | The **current value** of the state |
| `setCount` | The **function** you call to change it |
| `[ , ]` | **Array destructuring**. `useState` returns a pair `[value, setter]` |

**Naming convention:** `[thing, setThing]`, such as `[name, setName]`, `[isOpen, setIsOpen]`, `[bookings, setBookings]`.

> ⚠️ **Important**
>
> **Never change state directly.** Writing `count = count + 1` does nothing useful. **Always use the setter**: `setCount(count + 1)`.

🤔 **Quick thinking question:** What happens when you call `setCount(5)`?

✅ **Answer:** React stores `5` as the new value and **re-renders** the component. The next time the function runs, `count` is `5`.

---

### 🔄 4. How State Updates Work

```
   1. First render      count = 0   →  screen shows 0
   2. User clicks       setCount(1) called
   3. React re-renders  runs Counter() again
   4. useState returns  count = 1   →  screen shows 1
```

Key facts:

- 🔁 Calling a setter **schedules a re-render** of that component (and its children).
- 💾 React **remembers** the state between renders, so `useState(0)` only uses `0` the **first** time.
- 🧍 **Each component instance has its own state.** Two `<Counter />` components keep separate counts.
- 📸 State is a **snapshot** for each render. Inside one render, `count` doesn't change, even after calling `setCount`.

---

### 📸 5. State is a Snapshot (Important Gotcha)

```jsx
function handleClick() {
  setCount(count + 1)
  setCount(count + 1)
  setCount(count + 1)
}
```

You might expect `+3`, but the result is **+1**. In this render, `count` is a fixed snapshot (say `0`), so all three calls say `setCount(0 + 1)`.

**Fix: the functional update form.** Pass a function that receives the **latest** value:

```jsx
function handleClick() {
  setCount((prev) => prev + 1)
  setCount((prev) => prev + 1)
  setCount((prev) => prev + 1)
}
```

Now the result is **+3**. ✅

> 💡 **Tip**
>
> Use the **functional form** `setX(prev => ...)` whenever the new state **depends on the old state**. It is always safe.

---

### 🧪 6. State Can Hold Any Type

```jsx
const [name, setName] = useState("")                    // string
const [nights, setNights] = useState(1)                 // number
const [isOpen, setIsOpen] = useState(false)             // boolean
const [rooms, setRooms] = useState([])                  // array
const [form, setForm] = useState({ name: "", nights: 1 })  // object
```

**Toggle a boolean:**

```jsx
function Details() {
  const [show, setShow] = useState(false)

  return (
    <div>
      <button onClick={() => setShow(!show)}>
        {show ? "Hide" : "Show"} details
      </button>
      {show && <p>Free Wi-Fi, breakfast, and parking.</p>}
    </div>
  )
}
```

---

### 📋 7. Updating Arrays and Objects (Never Mutate!)

React decides whether to re-render by checking if the state **value changed**. If you **mutate** an array or object in place, React may not notice. Always create a **new** array or object.

**Arrays:**

| Task | ❌ Mutating (don't) | ✅ New array (do) |
|---|---|---|
| Add | `bookings.push(b)` | `setBookings([...bookings, b])` |
| Remove | `bookings.splice(i, 1)` | `setBookings(bookings.filter(x => x.id !== id))` |
| Update one | `bookings[0].name = "X"` | `setBookings(bookings.map(x => x.id === id ? { ...x, name: "X" } : x))` |

```jsx
function BookingList() {
  const [bookings, setBookings] = useState([])

  function addBooking() {
    const newBooking = { id: Date.now(), name: "Asha", room: 101 }
    setBookings([...bookings, newBooking])           // add
  }

  function removeBooking(id) {
    setBookings(bookings.filter((b) => b.id !== id)) // remove
  }

  return (
    <div>
      <button onClick={addBooking}>Add booking</button>
      <ul>
        {bookings.map((b) => (
          <li key={b.id}>
            {b.name} - Room {b.room}
            <button onClick={() => removeBooking(b.id)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

**Objects:**

```jsx
const [guest, setGuest] = useState({ name: "Asha", nights: 2 })

// ❌ guest.nights = 3
// ✅ copy the old object, then override one field:
setGuest({ ...guest, nights: 3 })
```

The **spread operator `...`** copies everything, and the field after it overrides the one you want to change.

---

### 🧮 8. Derived Values (Don't Store What You Can Calculate)

If a value can be **calculated** from existing state, **don't** create separate state for it.

```jsx
const [nights, setNights] = useState(2)
const pricePerNight = 3000

const total = nights * pricePerNight    // ✅ just calculate it each render
```

Storing `total` in its own state creates two values that can go out of sync.

---

### 🏗️ 9. Putting Props and State Together

```jsx
function RoomCard({ no, type, price }) {
  const [nights, setNights] = useState(1)

  return (
    <div className="card">
      <h3>Room {no} ({type})</h3>
      <p>Price: ₹{price} per night</p>

      <button onClick={() => setNights((n) => Math.max(1, n - 1))}>-</button>
      <span> {nights} night(s) </span>
      <button onClick={() => setNights((n) => n + 1)}>+</button>

      <p><b>Total: ₹{price * nights}</b></p>
    </div>
  )
}
```

- `no`, `type`, `price` are **props** (given by the parent, read-only).
- `nights` is **state** (owned by the card and changes with clicks).
- Each `RoomCard` has its **own** `nights`.

| | Props | State |
|---|---|---|
| Who owns it? | Parent | The component itself |
| Can the component change it? | ❌ No (read-only) | ✅ Yes (via setter) |
| Triggers re-render when changed? | Yes (when the parent re-renders with new props) | Yes |
| Used for | Configuring a component | Remembering changing data |

---

### 🏗️ 10. Sharing State: Lifting It Up (Preview)

If two sibling components need the **same** state, move the state up to their **common parent** and pass it down as props (plus setter functions).

```
        App  (owns bookings state)
        ├── BookingForm   (gets onBook function)
        └── BookingList   (gets bookings array)
```

You will practice this in the booking form topic and the project.

---

### 📏 11. Rules of Hooks

1. ✅ Call hooks **only at the top level** of a component (not inside `if`, loops, or nested functions).
2. ✅ Call hooks **only inside functional components** (or your own custom hooks).
3. ✅ Hook names start with **`use`**.

```jsx
function Bad({ show }) {
  if (show) {
    const [x, setX] = useState(0)   // ❌ inside a condition
  }
}
```

React relies on hooks being called in the **same order** every render. Conditions or loops would break that order.

---

### 💾 12. Initial State from localStorage (Preview)

Remember the localStorage pattern from the hotel app? You can set the **initial** state from storage using a function:

```jsx
const [bookings, setBookings] = useState(() => {
  return JSON.parse(localStorage.getItem("bookings")) || []
})
```

The function runs **only on the first render**. (To **save** changes automatically, you will use another hook, `useEffect`, in a later topic.)

---

## 💡 Real-Life Analogy

📝 **State is a whiteboard in a classroom. Props are a printed handout.**

- The **handout** (props) is given by the teacher. You can read it but not rewrite it.
- The **whiteboard** (state) belongs to the class. You can **erase and rewrite** it, and everyone looking at the board sees the new content.
- Calling the **setter** is like picking up the marker: *"I'm updating the board."* Once you write on it, **everyone's view refreshes**.
- A normal variable is a **scribble on a sticky note in your pocket**: you change it, but nobody (including React) ever sees it.

---

## 💻 Real-World Application

| Where | State is used for |
|---|---|
| ❤️ **Instagram Like button** | `liked` (true or false) and `likeCount` |
| 🛒 **Shopping cart** | Array of cart items, quantity per item |
| 🔍 **Search box** | The text typed so far |
| 🍔 **Dropdown or hamburger menu** | `isOpen` toggle |
| 🪟 **Modal popup** | `showModal` boolean |
| 📑 **Tabs** | The currently selected tab index |
| 📝 **Multi-step forms** | The current step and form data |

---

## 🔍 Industry Example

📘 **Scenario: The "Add to Cart" quantity control on a shopping site**

A product card has `−  2  +` buttons and a price that updates live.

```jsx
function ProductCard({ name, price }) {
  const [qty, setQty] = useState(1)

  return (
    <div className="product">
      <h3>{name}</h3>
      <button onClick={() => setQty((q) => Math.max(1, q - 1))}>-</button>
      <span>{qty}</span>
      <button onClick={() => setQty((q) => q + 1)}>+</button>
      <p>Total: ₹{price * qty}</p>
    </div>
  )
}
```

**What happens internally:**

1. 🧠 On the first render, React creates a state slot for `qty` with value `1`.
2. 🖱️ The user clicks **+**. The handler calls `setQty(q => q + 1)`.
3. 📨 React schedules a re-render of **this one** `ProductCard`.
4. 🔁 The function runs again. `useState` now returns `qty = 2`, and the JSX shows `2` and the new total.
5. 🪞 React compares old and new output and updates **only** the quantity and total text in the DOM.
6. 🧍 Other product cards on the page are **unaffected**. Each has its own `qty`.

---

## 📊 Diagram

```
             THE useState CYCLE

   ┌──────────────────────────────────────────┐
   │  Render:  count = 0                      │
   │  Screen shows 0                          │
   └───────────────┬──────────────────────────┘
                   │ user clicks
                   ▼
   ┌──────────────────────────────────────────┐
   │  Event handler: setCount(count + 1)      │
   └───────────────┬──────────────────────────┘
                   │ React schedules re-render
                   ▼
   ┌──────────────────────────────────────────┐
   │  Render again:  count = 1                │
   │  Screen shows 1                          │
   └──────────────────────────────────────────┘


        const [count, setCount] = useState(0)
               │       │                │
               │       │                └── initial value (first render only)
               │       └── function to UPDATE the value
               └── current value


          PROPS vs STATE

   Parent ──props (read-only)──► Child
                                  │
                                  └── own state (changeable)  ◄── setter
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can change state with `count = count + 1`." | Always use the setter: `setCount(count + 1)`. |
| "`count++` works on state." | It mutates the local variable only. Use `setCount(c => c + 1)`. |
| "After `setCount(5)`, `count` is immediately 5 in the same function." | State is a **snapshot**. The new value appears on the **next render**. |
| "`push()` is fine for an array in state." | Create a new array: `setList([...list, item])`. |
| "Calling `setCount` three times adds 3." | Not with plain values. Use the functional form `setCount(c => c + 1)`. |
| "Hooks can go inside `if` statements." | Hooks must be at the top level of the component. |
| "I'll store `total` in state as well." | Calculate derived values directly instead. |
| "Two `<Counter />` components share a count." | Each instance has its **own** state. |
| "State is the same as props." | Props come from the parent and are read-only. State belongs to the component. |
| "I forgot to import `useState`." | Add `import { useState } from "react"`. |

---

## 💬 Interview Corner

**Q1. What is state in React?**
Data that belongs to a component and can change over time. When state changes, React re-renders the component to show the new data.

**Q2. What does `useState` return?**
An array with two items: the current state value and a function to update it. We usually destructure it: `const [value, setValue] = useState(initial)`.

**Q3. Why can't we update state directly?**
React only knows to re-render when the setter function is called. Changing the variable directly doesn't trigger a re-render, and for arrays and objects, mutating in place can cause stale or missing updates.

**Q4. What is the difference between props and state?**
Props are passed from a parent and are read-only. State is managed inside the component and can be changed using its setter function.

---

## 📝 Quick Summary

- 🧠 **State** is data that changes over time and drives what the screen shows.
- 🪝 `useState(initial)` returns `[value, setValue]`.
- 🔄 Calling the setter triggers a **re-render** with the new value.
- 🚫 Never modify state directly. **Always use the setter**.
- ➕ Use `setX(prev => ...)` when the new value depends on the old one.
- 📋 For arrays and objects, create **new copies** (`spread`, `map`, `filter`), and don't mutate.
- 🧮 Don't store values you can **calculate** from other state.
- 🧍 Each component instance has **its own** state.
- 📏 Call hooks only at the **top level** of a component.

---

## 🎯 Class Activity

**🛠️ Activity: "Make the hotel app interactive"**

Create the following in your `hotel-ui` project:

1. **Counter:** A `Counter` component with **+**, **−**, and **Reset** buttons. The count should never go below 0.
2. **Toggle:** A `RoomDetails` component with a **Show / Hide details** button (boolean state).
3. **Nights selector:** In `RoomCard`, add a `nights` state with **+/−** buttons (minimum 1) and show **total price** as a calculated value.
4. **Booking list:** An `App`-level `bookings` array state. Add a button **"Book Room 101"** that adds an object `{ id: Date.now(), room: 101 }`. Show the list with a **Cancel** button per item using `filter`.
5. **Experiment:** Write a button that calls `setCount(count + 1)` three times, then another that uses the functional form three times. Compare the results.
6. **Experiment:** Try `bookings.push(...)` and observe what happens. Then fix it with spread.

**Discuss:** Why does each `RoomCard` keep its own `nights`?

---

# 📋 Assignments — The `useState` Hook for Local State

| Assignment |
|---|
| Build a counter with Increase, Decrease, and Reset buttons. Make sure it never goes below zero. |
| Show the plain-variable version of the counter (using `let`) and explain in two lines why the screen doesn't update. |
| Build a "Show / Hide" toggle for a paragraph using boolean state. |
| Build a Like button that toggles between "🤍 Like" and "❤️ Liked" and shows a like count that goes up and down accordingly. |
| Create a `RoomCard` with a nights selector (min 1, max 10) and a live total price calculated from `price * nights`. |
| Demonstrate the snapshot problem: call `setCount(count + 1)` three times in one click, observe the result, then fix it using the functional form. |
| Create a list of bookings in state. Add a booking with spread, remove one with `filter`, and show the number of bookings. |
| Add an "Edit name" feature that updates one booking's name using `map` and object spread, without mutating. |
| Store an object in state `{ name, room, nights }` and write buttons that update **one field at a time** with spread. |
| Build a tab bar (Standard, Deluxe, Suite) using a `selectedType` state that shows only the rooms of that type. |
| Create two `Counter` components on the page and prove that their states are independent. Explain why. |
| Break the rules of hooks on purpose by putting `useState` inside an `if`. Read the error or warning and write what it says. |
| Initialize a `bookings` state from localStorage using a function: `useState(() => ...)`, and confirm it loads existing data after refresh. |
| Show a summary bar above the booking list that displays total bookings and total revenue, calculated (not stored in state). |
| Write a short note (6 to 8 lines) explaining the difference between props and state using your own analogy. |

---
---

# 📚 Event Handling in React: `onClick` and `onChange`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🖱️ Attach event handlers in JSX using camelCase props like `onClick`
- 📌 Pass the **function itself**, not its result
- 🎯 Pass arguments to handlers using arrow functions
- 📦 Use the **event object** (`e.target`, `e.preventDefault()`)
- ⌨️ Build **controlled inputs** using `value` and `onChange`
- 📨 Handle form `onSubmit` with simple validation
- 🏨 Build a small booking form that adds records to state

---

## 📖 Introduction

You already know events from plain JavaScript: you used `addEventListener("click", ...)`. In React, handling events is **simpler and cleaner**. You attach the handler **directly in JSX**.

```jsx
<button onClick={handleClick}>Book</button>
```

**Why does this topic exist?** State changes only matter if something triggers them. Events (clicks, typing, submitting) are the **triggers** that call your state setters.

**Why is it important?** Every interactive feature, from buttons to forms to search boxes, is built with event handlers plus state.

**Where is it used?** Every login form, search bar, shopping cart, filter, and button on every React site.

---

## 🧠 Detailed Notes

### 🆚 1. Plain JavaScript vs React

| | Plain JavaScript | React |
|---|---|---|
| Find the element | `document.getElementById("btn")` | Not needed |
| Attach handler | `btn.addEventListener("click", fn)` | `<button onClick={fn}>` |
| Update screen | `element.innerText = ...` | Change **state**, and React updates the screen |
| Event names | lowercase: `click`, `input` | camelCase props: `onClick`, `onChange` |

---

### 🖱️ 2. `onClick`: Handling Clicks

```jsx
function BookButton() {
  function handleClick() {
    alert("Room booked! 🎉")
  }

  return <button onClick={handleClick}>Book Now</button>
}
```

**Three ways to write a handler:**

```jsx
// 1. A named function (best for longer logic)
<button onClick={handleClick}>Book</button>

// 2. An inline arrow function (good for short logic)
<button onClick={() => alert("Booked!")}>Book</button>

// 3. An inline arrow that calls a function with arguments
<button onClick={() => bookRoom(101)}>Book Room 101</button>
```

> 💡 **Tip**
>
> **Naming convention:** handler functions start with **`handle`** (`handleClick`, `handleSubmit`), and props that receive handlers start with **`on`** (`onClick`, `onBook`).

---

### ⚠️ 3. The #1 Beginner Bug: Calling Instead of Passing

```jsx
<button onClick={handleClick()}>Book</button>   // ❌ runs immediately while rendering!
<button onClick={handleClick}>Book</button>     // ✅ passes the function; React calls it on click
```

- `handleClick` means **"here is the function, call it when clicked"**.
- `handleClick()` means **"call it right now"** and passes the **result** to `onClick`.

**With arguments, wrap it in an arrow function:**

```jsx
<button onClick={bookRoom(101)}>Book</button>         // ❌ runs immediately
<button onClick={() => bookRoom(101)}>Book</button>   // ✅ runs on click
```

🤔 **Quick thinking question:** Why does `onClick={setCount(count + 1)}` cause an infinite loop?

✅ **Answer:** It **calls** `setCount` during rendering. That triggers a re-render, which calls it again, and so on. Fix: `onClick={() => setCount(count + 1)}`.

---

### 🔗 4. Click Handlers + State

```jsx
import { useState } from "react"

function Wishlist() {
  const [saved, setSaved] = useState(false)

  function handleToggle() {
    setSaved(!saved)
  }

  return (
    <button onClick={handleToggle}>
      {saved ? "💖 Saved" : "🤍 Save room"}
    </button>
  )
}
```

The pattern is always: **event → handler → state setter → re-render → new screen**.

---

### 📦 5. The Event Object

React passes an **event object** to your handler automatically.

```jsx
function handleClick(e) {
  console.log(e.type)       // "click"
  console.log(e.target)     // the element that was clicked
}

<button onClick={handleClick}>Test</button>
```

| Property / method | Purpose |
|---|---|
| `e.target` | The element that triggered the event |
| `e.target.value` | The current value of an input |
| `e.target.checked` | Whether a checkbox is ticked |
| `e.target.name` | The `name` attribute of the element |
| `e.preventDefault()` | Stop the browser's default action (for example form submit reload) |
| `e.stopPropagation()` | Stop the event from bubbling up to parents |

> ℹ️ **Note**
>
> React wraps the browser's event in its own "synthetic event". It behaves like the normal event, so everything you learned still applies.

---

### ⌨️ 6. `onChange` and Controlled Inputs

For form fields, we use **`onChange`**, which fires **on every change** (every keystroke in a text box). This is similar to the `input` event in plain JavaScript.

**The controlled input pattern:**

1. Keep the field's value in **state**.
2. Set the input's `value` to that state.
3. Update the state in `onChange`.

```jsx
function GuestName() {
  const [name, setName] = useState("")

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Guest name"
      />
      <p>Hello, {name || "guest"}! 👋</p>
    </div>
  )
}
```

**Why "controlled"?** React state is the **single source of truth**. The input always shows exactly what's in state. You can easily validate it, clear it, or use it elsewhere.

> ⚠️ **Important**
>
> If you set `value={name}` **without** an `onChange`, the input becomes **read-only** (you can't type) and React prints a warning.

**Other input types:**

```jsx
// Select (dropdown)
const [roomType, setRoomType] = useState("")
<select value={roomType} onChange={(e) => setRoomType(e.target.value)}>
  <option value="">Select</option>
  <option value="Standard">Standard</option>
  <option value="Deluxe">Deluxe</option>
</select>

// Checkbox uses `checked` and `e.target.checked`
const [agree, setAgree] = useState(false)
<input type="checkbox" checked={agree} onChange={(e) => setAgree(e.target.checked)} />

// Number input: the value is still a STRING, so convert it
const [nights, setNights] = useState(1)
<input type="number" value={nights} onChange={(e) => setNights(Number(e.target.value))} />
```

---

### 📨 7. `onSubmit` for Forms

Attach `onSubmit` to the **form** (not `onClick` on the button). That way it also works when the user presses **Enter**.

```jsx
function handleSubmit(e) {
  e.preventDefault()          // stop the page from reloading
  // validate and save...
}

<form onSubmit={handleSubmit}>
  ...
  <button type="submit">Book</button>
</form>
```

> ⚠️ **Important**
>
> Forgetting `e.preventDefault()` makes the browser **reload the page**, and your state is lost.

---

### 🧺 8. Many Fields, One State Object

For a form with many fields, use **one state object** and **one handler**. Give each input a `name` that matches the object key.

```jsx
const [form, setForm] = useState({ name: "", roomType: "", nights: 1, agree: false })

function handleChange(e) {
  const { name, value, type, checked } = e.target
  setForm({
    ...form,
    [name]: type === "checkbox" ? checked : value,
  })
}
```

- `[name]: ...` is a **computed property**. It uses the `name` attribute as the key.
- `...form` copies the old values, and the computed key overrides one field.

---

### 🏨 9. Full Example: Hotel Booking Form

**📁 `src/components/BookingForm.jsx`**

```jsx
import { useState } from "react"

const emptyForm = { name: "", roomType: "", nights: 1, agree: false }

function BookingForm({ onBook }) {
  const [form, setForm] = useState(emptyForm)
  const [error, setError] = useState("")

  function handleChange(e) {
    const { name, value, type, checked } = e.target
    setForm({ ...form, [name]: type === "checkbox" ? checked : value })
  }

  function handleSubmit(e) {
    e.preventDefault()

    let message = ""
    if (form.name.trim().length < 3) message = "Name must be at least 3 characters."
    else if (!form.roomType) message = "Please choose a room type."
    else if (Number(form.nights) < 1) message = "Nights must be at least 1."
    else if (!form.agree) message = "Please accept the terms."

    if (message) {
      setError(message)
      return
    }

    setError("")
    onBook({
      id: Date.now(),
      name: form.name.trim(),
      roomType: form.roomType,
      nights: Number(form.nights),
    })
    setForm(emptyForm)        // clear the form
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Guest name"
      />

      <select name="roomType" value={form.roomType} onChange={handleChange}>
        <option value="">Select room type</option>
        <option value="Standard">Standard</option>
        <option value="Deluxe">Deluxe</option>
        <option value="Suite">Suite</option>
      </select>

      <input
        type="number"
        name="nights"
        min="1"
        value={form.nights}
        onChange={handleChange}
      />

      <label>
        <input
          type="checkbox"
          name="agree"
          checked={form.agree}
          onChange={handleChange}
        />
        I accept the terms
      </label>

      <button type="submit">Book</button>

      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  )
}

export default BookingForm
```

**📁 `src/App.jsx`**

```jsx
import { useState } from "react"
import BookingForm from "./components/BookingForm"

function App() {
  const [bookings, setBookings] = useState([])

  function addBooking(booking) {
    setBookings([...bookings, booking])
  }

  function removeBooking(id) {
    setBookings(bookings.filter((b) => b.id !== id))
  }

  return (
    <div>
      <h1>🏨 Hotel Paradise</h1>
      <BookingForm onBook={addBooking} />

      <h2>Bookings ({bookings.length})</h2>
      <ul>
        {bookings.map((b) => (
          <li key={b.id}>
            {b.name} - {b.roomType}, {b.nights} night(s)
            <button onClick={() => removeBooking(b.id)}>Cancel</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
```

**What is happening here:**

1. 🧺 `BookingForm` owns the **form state** (what is being typed).
2. 📨 `App` owns the **bookings list** and passes `addBooking` down as the **`onBook` prop**.
3. ⌨️ Each keystroke calls `handleChange`, which updates `form` state, and the input re-renders with the new value.
4. 🚦 On submit, the form validates. If something is wrong, it shows an error. Otherwise, it calls `onBook(...)`.
5. 🔁 `App` adds the booking to its state, and React re-renders the list.
6. 🧹 The form clears itself by resetting its state.

---

### 🫧 10. Event Bubbling in React

Events **bubble up** from a child to its parents, just like plain JavaScript.

```jsx
<div onClick={() => console.log("card clicked")}>
  <button onClick={(e) => {
    e.stopPropagation()               // don't let the card's handler run
    console.log("button clicked")
  }}>
    Book
  </button>
</div>
```

Use `e.stopPropagation()` when a child's click should **not** trigger the parent's handler.

---

### 🎯 11. Other Common Events

| Prop | Fires when |
|---|---|
| `onClick` | Element is clicked |
| `onChange` | Input value changes (every keystroke for text) |
| `onSubmit` | Form is submitted |
| `onFocus` / `onBlur` | Field gains or loses focus |
| `onKeyDown` | A key is pressed (`e.key`) |
| `onMouseEnter` / `onMouseLeave` | Mouse enters or leaves |

```jsx
<input onKeyDown={(e) => { if (e.key === "Enter") handleSearch() }} />
```

---

## 💡 Real-Life Analogy

🔔 **Event handling is like a doorbell connected to a smart home.**

- The **button** (`onClick`) is the doorbell.
- The **handler function** is the instruction you programmed: *"When the bell rings, turn on the porch light."*
- **State** is the status board inside the house showing *"Porch light: ON"*.
- Writing `onClick={handler()}` is like **ringing the bell yourself the moment you install it**, instead of waiting for a visitor. 😅

And a **controlled input** is like a **mirror**: whatever you write on the paper (typing) is instantly copied to the board (state), and the board always shows exactly what is on the paper.

---

## 💻 Real-World Application

| Where | Events used |
|---|---|
| 🔍 **Flipkart/Amazon search bar** | `onChange` updates the query as you type |
| ❤️ **Like buttons** | `onClick` toggles the liked state |
| 🛒 **Add to cart** | `onClick` adds an item to the cart array |
| 📝 **Login and signup** | `onChange` for fields and `onSubmit` for validation |
| 🎚️ **Filters and sorting** | `onChange` on dropdowns and checkboxes |
| ⌨️ **Chat apps** | `onKeyDown` to send a message when you press Enter |
| 🗑️ **To-do apps** | `onClick` on delete, `onChange` on checkboxes |

---

## 🔍 Industry Example

📘 **Scenario: A live-filter search on a hotel booking site**

A user types in the search box, and the room list narrows instantly.

```jsx
function RoomSearch({ rooms }) {
  const [query, setQuery] = useState("")

  const filtered = rooms.filter((r) =>
    r.type.toLowerCase().includes(query.toLowerCase())
  )

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search by room type..."
      />
      <p>{filtered.length} room(s) found</p>
      <ul>
        {filtered.map((r) => (
          <li key={r.id}>Room {r.no} - {r.type}</li>
        ))}
      </ul>
    </div>
  )
}
```

**What happens internally:**

1. ⌨️ The user types **"del"**. Each keystroke fires `onChange`.
2. 📦 The handler reads `e.target.value` and calls `setQuery`.
3. 🔁 React re-renders `RoomSearch` with the new `query`.
4. 🧮 The component **calculates** `filtered` from `rooms` and `query` on every render (no extra state needed).
5. 🖼️ The list shows only matching rooms, and the count text updates too.
6. ⚡ It all happens on every keystroke without reloading the page or touching `getElementById` once.

---

## 📊 Diagram

```
         EVENT → STATE → SCREEN LOOP

   User action          Handler               React
  ┌───────────┐     ┌────────────────┐    ┌─────────────────────┐
  │ types /   │────►│ onChange /     │───►│ setState(newValue)  │
  │ clicks    │     │ onClick runs   │    │ re-render component │
  └───────────┘     └────────────────┘    └──────────┬──────────┘
        ▲                                            │
        └────────────── new screen shown ◄───────────┘


        CONTROLLED INPUT

   state: name = "As"
        │
        ▼
   <input value={name} onChange={e => setName(e.target.value)} />
        ▲                                        │
        └──────────── user types "h" ────────────┘
                  state becomes "Ash"


        PASS vs CALL

   onClick={handle}       ✅  "call handle when clicked"
   onClick={handle()}     ❌  "call handle NOW, pass its result"
   onClick={() => handle(5)}  ✅  "when clicked, call handle(5)"
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`onClick={handleClick()}` is correct." | It runs immediately. Use `onClick={handleClick}`. |
| "`onclick` (lowercase) works in JSX." | Use camelCase: `onClick`, `onChange`, `onSubmit`. |
| "I can pass arguments like `onClick={fn(5)}`." | Wrap it: `onClick={() => fn(5)}`. |
| "Set `value` but skip `onChange`." | The input becomes read-only. Add `onChange` with a state setter. |
| "`e.target.value` of a number input is a number." | It is always a **string**. Convert with `Number()`. |
| "Checkboxes use `value`." | Use **`checked`** and `e.target.checked`. |
| "I don't need `preventDefault()` in forms." | Without it, the page reloads and state is lost. |
| "I should use `getElementById` to read inputs in React." | Use **state** with controlled inputs instead. |
| "Handlers can mutate state directly." | Always use setters and create new arrays and objects. |
| "`onClick` on the button is the best place to validate a form." | Use **`onSubmit` on the form**. It also handles the Enter key. |
| "`setForm({ [name]: value })` is enough." | That **drops** other fields. Spread the old state first: `{ ...form, [name]: value }`. |

---

## 💬 Interview Corner

**Q1. How do you handle events in React?**
By passing a function to a camelCase event prop in JSX, like `<button onClick={handleClick}>`. The function runs when the event happens.

**Q2. What is a controlled component?**
A form element whose value is controlled by React state. The `value` prop comes from state, and `onChange` updates that state, so state is the single source of truth.

**Q3. Why do we call `e.preventDefault()` in a form's `onSubmit`?**
To stop the browser's default behavior of reloading the page, so React can validate and handle the data itself.

**Q4. What is the difference between `onClick={fn}` and `onClick={fn()}`?**
`onClick={fn}` passes the function to be called when the click happens. `onClick={fn()}` calls the function immediately during rendering and passes its return value, which is usually a bug.

---

## 📝 Quick Summary

- 🖱️ React events are **camelCase props**: `onClick`, `onChange`, `onSubmit`.
- 📌 **Pass the function**, don't call it: `onClick={handle}`.
- 🎯 For arguments, use an arrow: `onClick={() => handle(id)}`.
- 📦 The handler receives an **event object**: `e.target.value`, `e.preventDefault()`.
- ⌨️ **Controlled inputs** use `value={state}` and `onChange={...setState}`.
- ☑️ Checkboxes use **`checked`**, and number inputs still give **strings**.
- 📨 Use **`onSubmit`** on the form with `e.preventDefault()`.
- 🧺 One state **object** plus `[name]: value` handles many fields.
- 🔁 The core loop is: **event → handler → setState → re-render**.

---

## 🎯 Class Activity

**🛠️ Activity: "Complete the interactive hotel app"**

Using everything from this module:

1. Create `BookingForm.jsx` and `App.jsx` from the example. Run the app and book three guests.
2. Test every **validation message** (short name, no room type, nights below 1, terms unticked).
3. Add a **phone** field that must have **exactly 10 digits**, with validation and an error message.
4. Add a **search box** above the bookings list that filters bookings by guest name as you type (use a `query` state and the `filter()` method, with no extra state for the filtered list).
5. Add a **room type filter** dropdown (All, Standard, Deluxe, Suite) that filters the list.
6. Show a **summary line**: total bookings and total nights.
7. **Bonus:** Make your `RoomCard`'s **Book** button fill the `roomType` field of the form (hint: lift state up to `App`).

**Discuss:** What was the difference between building this in plain JavaScript and in React? Which parts felt easier?

---

# 📋 Assignments — Event Handling in React: `onClick` and `onChange`

| Assignment |
|---|
| Create a button that shows an `alert` using a named handler function, then rewrite it with an inline arrow function. |
| Deliberately write `onClick={handleClick()}` and observe what happens. Write one line explaining why, then fix it. |
| Create a list of three rooms, each with a "Book" button that calls `bookRoom(roomNo)` using the correct arrow-function syntax, and prints the room number in the console. |
| Build a controlled text input that shows "Hello, <name>!" below it as the user types. |
| Add a character counter (for example "12 / 50") to a text input, with a `maxLength`. |
| Create a controlled dropdown for room types and display the selected value below it. |
| Create a checkbox "Breakfast included" that adds ₹300 to a displayed total only when checked. |
| Build a number input for nights using `Number(e.target.value)` and show the total price `nights * price`. Test what happens if you forget `Number()` in a calculation like `nights + 1`. |
| Build a login form (email and password) with `onSubmit`, `e.preventDefault()`, and validation messages for empty fields and a short password. |
| Remove `e.preventDefault()` from your form on purpose, submit it, and write what you observed. |
| Build the full `BookingForm` from the notes and extend it with a "check-in date" and "check-out date" with the rule that check-out must be after check-in. |
| Build a live search box that filters an array of at least 8 rooms by type as you type. Show "No rooms found" when the result is empty. |
| Make a to-do list: add tasks with an input and button, mark them done with a checkbox, and delete them with a button. |
| Use `onKeyDown` so that pressing **Enter** in a search box triggers a search action, and **Escape** clears the box. |
| Create a card with a click handler and a button inside it with its own handler. Use `e.stopPropagation()` so that clicking the button doesn't trigger the card's handler, and demonstrate both cases. |
| Convert one feature of your plain-JavaScript hotel app (for example the booking form) to React and write a short comparison of what code you were able to delete. |