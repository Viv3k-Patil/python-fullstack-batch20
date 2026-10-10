# 📚 What is JavaScript? (and a Little History)

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🌐 Explain what JavaScript is in your own words
- 🕰️ Describe how and why JavaScript was created
- 🔀 Tell the difference between Java and JavaScript
- 🧩 Understand the role of HTML, CSS, and JavaScript in a web page
- 🖥️ Know where JavaScript runs (browser, server, mobile, desktop)
- ⌨️ Run your very first JavaScript code in the browser console

---

## 📖 Introduction

Open any website: Amazon, YouTube, Instagram, Gmail. Do you notice that things **move, change, and react** when you click or type? A menu slides open, a heart turns red when you click "Like", a search box suggests words while you type.

Who makes all of this happen? 👉 **JavaScript!**

Let's break it down. A web page is built from three technologies:

- **HTML** gives the page its *structure* (text, images, buttons)
- **CSS** gives the page its *style* (colors, fonts, layout)
- **JavaScript** gives the page its *behavior* (clicks, animations, logic)

**Why does JavaScript exist?** Early web pages were boring, static documents. You could read them, but nothing happened when you interacted with them. JavaScript was invented to bring pages to life.

**Why is it important?** JavaScript is the **only programming language that every web browser understands natively**. If you want to build modern websites, you must know it. It is also one of the most popular languages in the world.

**Where is it used?** Websites, web apps, mobile apps, desktop apps, servers, games, and even IoT devices.

---

## 🧠 Detailed Notes

### 🌟 1. What is JavaScript?

**JavaScript (JS)** is a **high-level, interpreted programming language** that lets you add logic and interactivity to web pages.

Let's decode those words:

| Term | Meaning in simple English |
|---|---|
| **High-level** | Written in human-friendly words, not machine code (0s and 1s) |
| **Interpreted** | Executed line by line by an engine, with no separate compile step needed from you |
| **Dynamic** | You don't have to declare the type of a variable up front |
| **Multi-paradigm** | You can write code in different styles (procedural, object-oriented, functional) |

> 💡 **Tip**
>
> You already know Python in this course. JavaScript is also interpreted and dynamic, so many ideas will feel familiar. Only the **syntax** (the way we write it) changes.

---

### 🕰️ 2. A Little History of JavaScript

Let's travel back in time ⏳

#### 📅 1993–1994: The browser era begins
- The first popular browser **Mosaic** appeared, followed by **Netscape Navigator**.
- Web pages were only static documents.

#### 📅 1995: JavaScript is born 🎂
- A company called **Netscape** wanted a simple scripting language for its browser.
- A programmer named **Brendan Eich** created the first version in just about **10 days** (May 1995).
- The first name was **Mocha**, then **LiveScript**, and finally **JavaScript**.

🤔 **Quick thinking question:** Why did they call it "JavaScript" if it has nothing to do with Java?

✅ **Answer:** It was a **marketing decision**. Java was the hottest language in 1995, so Netscape borrowed its popularity. The two languages are completely different!

#### 📅 1996: Microsoft enters
- Microsoft made its own version called **JScript** for Internet Explorer.
- Now there were different versions, and websites worked in one browser but broke in another. 😵

#### 📅 1997: Standardization
- Netscape gave JavaScript to **ECMA International**, a standards organization.
- The official standard was named **ECMAScript (ES)**.
- Today: **ECMAScript = the specification (rulebook)**, **JavaScript = the language that follows the rulebook**.

#### 📅 2005: AJAX changes everything
- A technique called **AJAX** allowed pages to fetch data **without reloading**.
- Google Maps and Gmail made it famous. Web pages started feeling like real apps.

#### 📅 2008: Google V8 engine 🚀
- Google released **Chrome** with the super-fast **V8 engine**.
- JavaScript became much faster.

#### 📅 2009: Node.js
- **Ryan Dahl** took the V8 engine out of the browser and created **Node.js**.
- Now JavaScript could run on **servers** too!

#### 📅 2015: ES6 (ES2015) 🎉
- The biggest upgrade ever. It introduced `let`, `const`, arrow functions, classes, promises, and more.
- Since then, a new version is released **every year** (ES2016, ES2017, and so on).

#### 📊 History at a glance

| Year | Event |
|---|---|
| 1995 | JavaScript created by Brendan Eich at Netscape |
| 1996 | Microsoft releases JScript |
| 1997 | ECMAScript standard (ES1) |
| 2005 | AJAX becomes popular |
| 2008 | Chrome and the V8 engine |
| 2009 | Node.js (JavaScript on servers) |
| 2015 | ES6, the modern JavaScript era begins |
| Every year | New ECMAScript updates |

---

### 🔀 3. Java vs JavaScript

This is the **most common confusion** among beginners.

| Feature | ☕ Java | 🟨 JavaScript |
|---|---|---|
| Created for | Large applications, Android, enterprise | Making web pages interactive |
| Type | Compiled | Interpreted (JIT-compiled by engines) |
| Typing | Strict (you must declare types) | Flexible (types decided at runtime) |
| Runs on | JVM (Java Virtual Machine) | Browser engine or Node.js |
| Relation | None except the name | None except the name |

> 💡 **Tip**
>
> **Java is to JavaScript as Car is to Carpet.** 🚗🧶 They share part of a name, nothing more.

---

### 🧩 4. HTML + CSS + JavaScript: The Three Musketeers

```
🏠 Think of a house:

   HTML  → Walls, doors, rooms      (Structure)
   CSS   → Paint, curtains, decor   (Style)
   JS    → Electricity, switches    (Behavior)
```

A tiny example showing all three together:

```html
<button id="btn" style="color: white; background: blue;">Click Me</button>

<script>
  document.getElementById("btn").onclick = function () {
    alert("Hello from JavaScript! 👋");
  };
</script>
```

- The `<button>` is **HTML** 🧱
- The `style` is **CSS** 🎨
- The `<script>` is **JavaScript** ⚡

---

### 🖥️ 5. Where Does JavaScript Run?

| Place | What it does | Example |
|---|---|---|
| 🌐 **Browser** (frontend) | Makes pages interactive | Click a button, form validation |
| 🗄️ **Server** (backend, via Node.js) | Handles data, APIs, databases | Login system |
| 📱 **Mobile apps** | Builds Android/iOS apps | React Native |
| 💻 **Desktop apps** | Builds installable programs | VS Code, Slack, Discord |
| 🎮 **Games and IoT** | Browser games, smart devices | Browser games |

> ℹ️ **Note**
>
> In our **Python Full Stack** course, Python will handle most backend work. JavaScript will be our **frontend language**, the part running in the user's browser.

---

### ⚙️ 6. How Does JavaScript Run in the Browser?

Every browser has a built-in **JavaScript Engine**:

| Browser | Engine |
|---|---|
| Chrome, Edge | **V8** |
| Firefox | **SpiderMonkey** |
| Safari | **JavaScriptCore** |

The engine reads your code and converts it into instructions your computer can run, very quickly.

---

### 🚀 7. What Can JavaScript Do?

- ✅ Show alerts and messages
- ✅ Change text, images, and colors on a page
- ✅ React to clicks, typing, and scrolling
- ✅ Validate forms ("Password too short!")
- ✅ Fetch live data (weather, news, prices)
- ✅ Build animations, games, and full apps

---

### ⌨️ 8. Your First JavaScript Code: the Browser Console

Every modern browser has a built-in place to try JavaScript instantly.

**Steps:**
1. Open **Google Chrome**.
2. Press **F12** (or right-click → **Inspect**).
3. Click the **Console** tab.
4. Type the code below and press **Enter**.

```javascript
console.log("Hello, World!");
```

You should see `Hello, World!` printed. 🎉

Try some more:

```javascript
console.log(10 + 5);          // 15
console.log("Java" + "Script"); // JavaScript
alert("I am learning JS!");   // shows a popup
```

- `console.log()` prints a message to the console. Developers use it all the time to check what the code is doing.
- `//` starts a **comment**. The engine ignores it.

🤔 **Quick thinking question:** What will `console.log(2 + 3)` print?

✅ **Answer:** `5`, because JavaScript does the math first and then prints the result.

---

## 💡 Real-Life Analogy

🎭 **A web page is like a stage play.**

- **HTML** is the stage, props, and actors (the structure).
- **CSS** is the costumes, lighting, and makeup (the look).
- **JavaScript** is the **director giving live instructions**: "Actor, walk in now! Lights, turn red!" (the behavior).

Without the director, the actors just stand still. Without JavaScript, the page just sits there.

---

## 💻 Real-World Application

| Company / Product | How JavaScript is used |
|---|---|
| 🔍 **Google** | Search suggestions as you type, Google Maps |
| 📺 **Netflix** | Interactive interface, video player controls |
| 🛒 **Amazon** | Cart updates, product image zoom |
| 💬 **WhatsApp Web** | Real-time message updates |
| 📝 **VS Code** | Built with JavaScript tech (Electron) |
| 🐦 **Instagram / Facebook** | Likes, comments, and feeds built with React |

---

## 🔍 Industry Example

📘 **Scenario: Typing in the Flipkart search box**

You open Flipkart and begin typing **"sho"** in the search bar.

1. 👆 JavaScript notices each **key you press** in the search box.
2. 📡 It sends a small request to the server: "What products start with *sho*?"
3. 📨 The server replies with suggestions (*shoes, shorts, shower curtain*).
4. 🖼️ JavaScript receives the list and **updates the dropdown** under the search box, without reloading the page.

All this happens in a **fraction of a second**. Without JavaScript, you would need to press Enter and wait for a whole new page.

---

## 📊 Diagram

```
        🌐 WEB PAGE IN YOUR BROWSER
 ┌──────────────────────────────────────────┐
 │                                          │
 │   📄 HTML  ──►  Structure (what's here)  │
 │                                          │
 │   🎨 CSS   ──►  Style (how it looks)     │
 │                                          │
 │   ⚡ JS    ──►  Behavior (what it does)  │
 │                                          │
 └──────────────────────────────────────────┘
                     │
                     ▼
        ┌──────────────────────────┐
        │  JavaScript Engine (V8)  │
        │  reads and runs your code│
        └──────────────────────────┘
                     │
                     ▼
        🖱️ User clicks → Page reacts!


     ⏳ JavaScript Timeline
 1995 ──► 1997 ──► 2005 ──► 2008 ──► 2009 ──► 2015
 Born    ECMA    AJAX     V8     Node.js    ES6
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "JavaScript is the same as Java." | They are two different languages. The shared name was a marketing choice. |
| "JavaScript only works in browsers." | With Node.js, it also runs on servers, desktops, and more. |
| "JavaScript is a toy language." | It powers almost every major website and many large applications. |
| "ECMAScript and JavaScript are totally different." | ECMAScript is the standard (rulebook). JavaScript is the implementation of it. |
| "I need to install a compiler to run JS." | No. Your browser already has an engine. Just open the console. |

---

## 💬 Interview Corner

**Q1. What is JavaScript?**
A high-level, interpreted programming language used to make web pages interactive. It also runs on servers through Node.js.

**Q2. Who created JavaScript, and when?**
Brendan Eich at Netscape, in 1995.

**Q3. What is the difference between Java and JavaScript?**
They are completely different languages. Java is compiled and used for large applications and Android. JavaScript is mainly used for web interactivity. They only share part of the name.

**Q4. What is ECMAScript?**
It is the official standard (specification) that JavaScript follows. New features are added to JavaScript through ECMAScript versions such as ES6.

---

## 📝 Quick Summary

- 🌐 JavaScript makes web pages **interactive and alive**.
- 🧱 HTML = structure, 🎨 CSS = style, ⚡ JS = behavior.
- 🎂 Created in **1995** by **Brendan Eich** at Netscape in about 10 days.
- 📜 **ECMAScript** is the standard. **ES6 (2015)** was a major modernization.
- 🚀 **V8 engine (2008)** and **Node.js (2009)** took JS beyond the browser.
- ☕ Java and JavaScript are **not** related.
- 🖥️ JS runs in browsers, servers, mobile apps, and desktop apps.
- ⌨️ `console.log()` is your best friend for testing code.

---

## 🎯 Class Activity

**🛠️ Activity: "Talk to your browser!"**

1. Open Chrome and visit any website (for example, a news site).
2. Press **F12** and open the **Console** tab.
3. Type each line below and press Enter after each:

```javascript
console.log("My name is <your name>");
console.log(5 * 8);
document.title = "I hacked this page! 😄";
```

4. Look at the browser tab title. It changed!
5. Refresh the page and notice that everything returns to normal. (Your change was only on your own screen.)

**Discuss:** How did JavaScript change the page without touching the server?

---

# 📋 Assignments — What is JavaScript? (and a Little History)

| Assignment |
|---|
| Open the browser console and print your name, age, and city using three separate `console.log()` statements. |
| Create a timeline of JavaScript history (at least 6 events) in a text file or on paper. |
| Write five differences between Java and JavaScript in your own words. |
| Open any three websites and, using Inspect, identify one thing on each page that you think JavaScript controls. Write your guesses. |
| In the console, use `console.log()` to print the result of 25 × 4, 100 / 8, and 17 + 33. |
| Use `alert("...")` in the console to show a popup with your favorite quote. |
| Find out which JavaScript engine your browser uses and write one line about it. |
| Visit a website and, in the console, change `document.title` to something funny. Take a screenshot as proof. |
| Research and list five famous websites or apps built with JavaScript. |
| Explain to a friend or family member (or write it down) what HTML, CSS, and JavaScript do, using your own analogy. |
| Find out what Node.js is and write three lines about why it was a big deal. |
| Look up the current latest ECMAScript version and write down one new feature it added. |

# 📚 Including JavaScript in HTML

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 📎 Add JavaScript to an HTML page in three different ways
- ✍️ Write inline, internal, and external JavaScript
- 📍 Decide where to place the `<script>` tag and why it matters
- ⏱️ Understand `defer` and `async` at a beginner level
- 🔍 Debug simple problems using the browser console
- 🏆 Choose the best method for real projects

---

## 📖 Introduction

In the last topic, we typed JavaScript into the browser console. That is great for practice, but real websites don't work that way. Visitors can't open the console and type your code! 😄

So how do we **attach our JavaScript to a web page** so it runs automatically when the page opens?

👉 We **include** it in the HTML file.

**Why is this important?** Without connecting JavaScript to HTML, your code never runs on the page. This is the first step of every frontend project you will ever build.

**Where is it used?** Every single website that has any interactivity.

---

## 🧠 Detailed Notes

### 🏷️ 1. The `<script>` Tag

HTML uses the `<script>` tag to tell the browser: "The following content is JavaScript. Please run it."

```html
<script>
  console.log("Hello from the script tag!");
</script>
```

There are **three ways** to include JavaScript in HTML:

| Method | Where the code lives | Best for |
|---|---|---|
| 1️⃣ Inline | Inside an HTML tag's attribute | Tiny quick tests |
| 2️⃣ Internal | Inside `<script>` in the same HTML file | Small demos and learning |
| 3️⃣ External | In a separate `.js` file | **Real projects** ✅ |

---

### 1️⃣ 2. Inline JavaScript

You write JavaScript **directly inside an HTML element's event attribute**.

```html
<button onclick="alert('Button clicked!')">Click Me</button>
```

- `onclick` is an **event attribute**. It runs the code when the button is clicked.
- Works, but it mixes HTML and JS together, which becomes messy fast. 🍝

> ⚠️ **Important**
>
> Inline JavaScript is fine for quick experiments but is **not recommended** in professional projects. It makes code hard to read, reuse, and maintain.

---

### 2️⃣ 3. Internal JavaScript

You write JavaScript inside a `<script>` tag **within the same HTML file**.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Internal JS</title>
</head>
<body>
  <h1 id="title">Hello!</h1>
  <button onclick="changeText()">Change Text</button>

  <script>
    function changeText() {
      document.getElementById("title").innerText = "Text changed by JS! 🎉";
    }
  </script>
</body>
</html>
```

- Everything is in one file, so it is simple for beginners.
- Not reusable across pages. If you have 10 pages, you'd copy the same code 10 times.

---

### 3️⃣ 4. External JavaScript ⭐ (Best Practice)

You write JavaScript in a **separate file** with the `.js` extension and link it using the `src` attribute.

**📁 Project structure:**

```
my-project/
 ├── index.html
 └── script.js
```

**📄 index.html**

```html
<!DOCTYPE html>
<html>
<head>
  <title>External JS</title>
</head>
<body>
  <h1 id="title">Hello!</h1>
  <button id="btn">Change Text</button>

  <script src="script.js"></script>
</body>
</html>
```

**📄 script.js**

```javascript
document.getElementById("btn").onclick = function () {
  document.getElementById("title").innerText = "Changed from script.js! 🚀";
};
```

**Why external is the best:**

- ✅ Clean separation: HTML (structure) and JS (behavior) stay apart
- ✅ **Reusable**: one `.js` file can be used on many pages
- ✅ Browser **caches** the file, so pages load faster next time
- ✅ Easier teamwork and debugging

> 💡 **Tip**
>
> Do **not** put `<script>` tags inside your `.js` file. A `.js` file contains only JavaScript, nothing else.

---

### 📍 5. Where to Place the `<script>` Tag?

The browser reads HTML **from top to bottom**. If your script runs **before** the HTML elements exist, it can't find them and you get errors. ❌

**Option A: In the `<head>` (risky without `defer`)**

```html
<head>
  <script src="script.js"></script>  <!-- runs BEFORE body is ready -->
</head>
<body>
  <button id="btn">Click</button>
</body>
```

If `script.js` tries to find `#btn`, it will fail because the button isn't created yet.

**Option B: At the end of `<body>` ✅ (classic solution)**

```html
<body>
  <button id="btn">Click</button>

  <script src="script.js"></script>  <!-- runs AFTER elements exist -->
</body>
```

**Option C: In `<head>` with `defer` ✅ (modern solution)**

```html
<head>
  <script src="script.js" defer></script>
</head>
```

---

### ⏱️ 6. `defer` and `async` (Simple Introduction)

| Attribute | What it does | Runs when? |
|---|---|---|
| *(none)* | Stops HTML reading, downloads, runs script immediately | Right away (blocks the page) |
| `defer` | Downloads while HTML loads, **runs after HTML is fully ready** | After page is parsed, in order |
| `async` | Downloads while HTML loads, **runs as soon as it's downloaded** | Whenever ready (order not guaranteed) |

For now, remember this simple rule:

> 💡 **Tip**
>
> Use `<script src="..." defer></script>` in the `<head>`, or put a normal script at the **end of `<body>`**. Both are safe for beginners.

🤔 **Quick thinking question:** Your script is in the `<head>` without `defer`, and it tries to change an `<h1>` that is in the `<body>`. What happens?

✅ **Answer:** It fails with an error, because the `<h1>` does not exist yet when the script runs. Fix it by adding `defer` or moving the script to the end of the body.

---

### 🔍 7. Checking Your Work: the Console

If something doesn't work, open DevTools (**F12 → Console**). Common messages:

| Message | Likely reason |
|---|---|
| `Uncaught TypeError: Cannot set properties of null` | Script ran before the element existed, or the `id` is wrong |
| `Failed to load resource: 404` | The file path in `src` is wrong |
| `Uncaught ReferenceError: x is not defined` | You used a variable or function that doesn't exist |

---

### 🔀 8. Can I Use Multiple Scripts?

Yes! You can link as many as you like. They run in the **order written**.

```html
<script src="utils.js"></script>
<script src="main.js"></script>
```

---

## 💡 Real-Life Analogy

📺 **A TV and its remote control**

- The **HTML page** is the TV.
- **Inline JS** is like pressing buttons directly on the TV: quick but limited.
- **Internal JS** is like keeping the remote **taped to the TV**. It works, but it's not flexible.
- **External JS** is a **separate remote control** you can use with many TVs, replace, or upgrade anytime.

And the `<script>` placement? Imagine switching the TV on **before plugging it in**. Nothing happens! That's why script timing matters.

---

## 💻 Real-World Application

| Where | How script inclusion is used |
|---|---|
| 🛒 **E-commerce sites** | `cart.js`, `search.js`, and `payment.js` linked as separate files |
| 📊 **Google Analytics** | A small `<script>` snippet added to track visitors |
| 💬 **Live chat widgets** | A third-party script is included to show a chat bubble |
| 🏦 **Banking websites** | Different scripts for forms, validation, and security |
| 📰 **News portals** | Ad scripts and video player scripts loaded with `async` |

---

## 🔍 Industry Example

📘 **Scenario: A frontend developer at an online food delivery company**

Priya is building the **Order Page**. Her folder looks like this:

```
order-page/
 ├── index.html
 ├── styles.css
 └── js/
      ├── validation.js
      └── cart.js
```

In `index.html`, she writes:

```html
<script src="js/validation.js" defer></script>
<script src="js/cart.js" defer></script>
```

**What happens internally when a customer opens the page:**

1. 🌐 Browser starts reading `index.html` from the top.
2. 📥 It spots the two `defer` scripts and **starts downloading them in the background**.
3. 🧱 It continues building the page (buttons, menus, images).
4. ✅ Once the HTML is fully ready, it runs `validation.js` first, then `cart.js`.
5. 🖱️ The customer clicks "Add to Cart", and `cart.js` updates the order instantly.

Because the code is in separate files, her teammate can edit `validation.js` without touching `cart.js`.

---

## 📊 Diagram

```
        HOW TO INCLUDE JAVASCRIPT IN HTML
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 ┌─────────┐    ┌───────────┐    ┌────────────┐
 │ INLINE  │    │ INTERNAL  │    │ EXTERNAL ⭐│
 │ onclick │    │ <script>  │    │ <script    │
 │ =".."   │    │  code     │    │  src=".js">│
 │         │    │ </script> │    │            │
 └─────────┘    └───────────┘    └────────────┘
  Quick test     Small demo       Real projects


       BROWSER LOADING TIMELINE (with defer)

 HTML parsing:  ██████████████████████░░
 Script download:   ████████░░░░░░░░░░░░   (in background)
 Script runs:                         ██   (after HTML ready)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can write HTML inside a `.js` file and `<script>` tags too." | A `.js` file contains **only JavaScript**. |
| "If I put `<script>` in the head, it always works." | It may run before elements exist. Use `defer` or place at the end of body. |
| "The file path doesn't matter." | A wrong `src` path causes a 404 error and the script won't load. |
| "Inline JS is the best way." | Inline is quick but messy. External files are best for real projects. |
| "I should add `<script>` tags inside `script.js`." | Never. That causes a syntax error. |
| "Changing `script.js` doesn't need a refresh." | You must refresh the page to see the new behavior. |

---

## 💬 Interview Corner

**Q1. In how many ways can we include JavaScript in an HTML page?**
Three: inline, internal (inside a `<script>` tag), and external (a separate `.js` file linked with `src`).

**Q2. Which method is best and why?**
External JavaScript. It keeps code clean, reusable, cacheable, and easier to maintain.

**Q3. What is the difference between `defer` and `async`?**
`defer` runs the script after the HTML is fully parsed, in order. `async` runs it as soon as it is downloaded, with no guaranteed order.

**Q4. Why do we often place the script tag at the end of the body?**
So that all HTML elements are already created before the JavaScript tries to access them.

---

## 📝 Quick Summary

- 🏷️ JavaScript is attached to HTML using the `<script>` tag.
- 1️⃣ **Inline**: code inside an attribute like `onclick`. Quick but messy.
- 2️⃣ **Internal**: code inside `<script>` in the HTML file.
- 3️⃣ **External**: code in a `.js` file linked via `src`. ✅ Best practice.
- 📍 Place scripts at the **end of body**, or use **`defer`** in the head.
- ⏱️ `defer` waits for HTML, and `async` runs as soon as it downloads.
- 🔍 Use the **Console** (F12) to catch errors like 404 or null elements.
- 📂 Multiple scripts run in the order they are written.

---

## 🎯 Class Activity

**🛠️ Activity: "Three ways, one button"**

1. Create a folder called `js-include-practice`.
2. Inside it, create `index.html` and `script.js`.
3. In `index.html`, add three buttons and one `<h2 id="msg">Waiting...</h2>`:
   - Button 1 uses **inline** JS (`onclick="alert('Inline!')"`).
   - Button 2 uses **internal** JS (a function inside a `<script>` tag that changes the `h2` text).
   - Button 3 uses **external** JS (an event set up in `script.js` that changes the `h2` text).
4. Open the file in Chrome and test all three buttons.
5. Move your `<script src="script.js">` into the `<head>` **without** `defer`. Open the console. What error do you see?
6. Add `defer` and check that the error disappears.

---

# 📋 Assignments — Including JavaScript in HTML

| Assignment |
|---|
| Create an HTML page with a button that shows an alert using **inline** JavaScript. |
| Create an HTML page where clicking a button changes a heading's text using **internal** JavaScript. |
| Create a project folder with `index.html` and `script.js` and connect them using the **external** method. |
| Make a page that prints your name in the console when it loads, using an external script. |
| Deliberately put your external script in the `<head>` without `defer`, trigger the error, and take a screenshot of the console message. |
| Fix the error from the previous assignment using (a) `defer` and (b) moving the script to the end of the body. |
| Create two external files, `a.js` and `b.js`, each printing a different message. Link both and confirm the order they run in. |
| Swap the order of the two script tags and observe what changes in the console output. |
| Intentionally write a wrong file name in `src` and note the 404 error shown in the Console and Network tab. |
| Make a page with a "Change Color" button that changes the page's background color using external JS. |
| Write a short note (5 lines) explaining why external JavaScript is preferred in real projects. |
| Add an inline `onclick` button and an external-JS button on the same page. Compare how the code looks in each case and write your opinion. |

# 📚 Variables in JavaScript: `let`, `const`, and Avoiding `var`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 📦 Understand what a variable is and why we need it
- ✍️ Declare variables using `let` and `const`
- 🔒 Know when to use `const` and when to use `let`
- 🚫 Understand why modern developers avoid `var`
- 🔭 Understand scope (block scope vs function scope) at a beginner level
- 🧭 Follow naming rules and conventions for variables

---

## 📖 Introduction

Imagine you are building a shopping website. You need to remember the user's name, the items in the cart, and the total price. Where does JavaScript keep all this information while the page is open?

👉 In **variables**.

A **variable** is a **named container that stores a value** in the computer's memory.

**Why does this topic exist?** Every program needs to remember data. Variables are the foundation of everything you will write.

**Why avoid `var`?** JavaScript originally had only `var`. It had confusing behaviors that caused many bugs. In 2015 (ES6), `let` and `const` were introduced to fix those problems.

**Where is it used?** In literally every JavaScript program ever written.

---

## 🧠 Detailed Notes

### 📦 1. What is a Variable?

Think of a variable as a **labeled box** 📦. The label is the variable's name, and the content is the value.

```javascript
let userName = "Asha";
let age = 21;
console.log(userName); // Asha
console.log(age);      // 21
```

- `let` is the keyword that creates the variable.
- `userName` is the variable's **name**.
- `=` is the **assignment operator**. It stores the value on the right into the variable on the left.
- `"Asha"` is the **value**.

> ℹ️ **Note**
>
> In Python you just write `age = 21`. In JavaScript, you must use a keyword (`let`, `const`, or `var`) to **declare** the variable first.

---

### 🔄 2. `let`: for Values That Can Change

Use `let` when the value **may change later**.

```javascript
let score = 0;
console.log(score); // 0

score = 10;         // updating the value
console.log(score); // 10

score = score + 5;
console.log(score); // 15
```

You can **declare** first and **assign** later:

```javascript
let city;           // declared, value is undefined
city = "Hyderabad"; // assigned later
console.log(city);
```

❌ You cannot declare the same name twice with `let` in the same scope:

```javascript
let x = 1;
let x = 2; // ❌ SyntaxError: 'x' has already been declared
```

---

### 🔒 3. `const`: for Values That Should NOT Change

Use `const` (constant) when the value **should never be reassigned**.

```javascript
const PI = 3.14159;
console.log(PI); // 3.14159

PI = 3.14;       // ❌ TypeError: Assignment to constant variable
```

Rules for `const`:

- ✅ Must be given a value **at the time of declaration**.
- ❌ Cannot be reassigned later.

```javascript
const country;        // ❌ SyntaxError: Missing initializer
const country = "India"; // ✅
```

> ⚠️ **Important: `const` with arrays and objects**
>
> `const` stops you from **reassigning** the variable, but it does **not freeze the contents** of arrays and objects. You can still change items inside them (you'll learn more in the Arrays & Objects topic).

```javascript
const colors = ["red", "green"];
colors.push("blue");   // ✅ allowed, we changed the contents
console.log(colors);   // ["red", "green", "blue"]

colors = ["black"];    // ❌ not allowed, we tried to reassign
```

🤔 **Quick thinking question:** Should you use `let` or `const` for the number of days in a week?

✅ **Answer:** `const`, because it never changes.

---

### 🚫 4. What is `var` and Why Avoid It?

`var` is the **old way** of declaring variables (before 2015). It still works, but it has problems.

#### Problem 1: `var` ignores block scope

A **block** is anything inside `{ }` curly braces, like an `if` or a loop.

```javascript
if (true) {
  var a = 10;
  let b = 20;
}
console.log(a); // 10 😮 var leaks out of the block!
console.log(b); // ❌ ReferenceError: b is not defined
```

`let` stays **inside** the block where it was created, which is safer and more predictable.

#### Problem 2: `var` allows accidental re-declaration

```javascript
var user = "Ravi";
var user = "Kiran"; // ✅ No error. This silently overwrites!
console.log(user);  // Kiran
```

In a big project, you could overwrite a variable by accident and never notice. 😱 With `let`, JavaScript warns you immediately.

#### Problem 3: `var` is "hoisted" with `undefined`

```javascript
console.log(name); // undefined (no error. Confusing!)
var name = "Meena";
```

With `let`, using it before declaration gives a clear error instead of a mysterious `undefined`:

```javascript
console.log(city); // ❌ ReferenceError: Cannot access 'city' before initialization
let city = "Pune";
```

> ⚠️ **Important**
>
> **Modern rule:** Use **`const` by default**. Use **`let`** only if the value must change. **Avoid `var`** in new code.

---

### 📊 5. `var` vs `let` vs `const` at a Glance

| Feature | `var` ❌ | `let` ✅ | `const` ✅ |
|---|---|---|---|
| Scope | Function | **Block** | **Block** |
| Re-assign value | ✅ Yes | ✅ Yes | ❌ No |
| Re-declare same name | ✅ Yes (risky) | ❌ No | ❌ No |
| Must initialize at declaration | No | No | **Yes** |
| Used before declaration | `undefined` | Error | Error |
| Recommended today | ❌ No | ✅ When value changes | ✅ **Default choice** |

---

### 🔭 6. Scope (Beginner Level)

**Scope** means *"where in the code a variable can be seen and used."*

```javascript
let globalMessage = "I am visible everywhere 🌍";

function greet() {
  let localMessage = "I live only inside this function 🏠";
  console.log(globalMessage); // ✅ works
  console.log(localMessage);  // ✅ works
}

greet();
console.log(globalMessage); // ✅ works
console.log(localMessage);  // ❌ ReferenceError
```

| Scope type | Meaning |
|---|---|
| 🌍 **Global scope** | Declared outside everything, visible everywhere |
| 🏠 **Function scope** | Declared inside a function, visible only there |
| 🧱 **Block scope** | Declared inside `{ }`, visible only inside that block (`let` and `const`) |

> 💡 **Tip**
>
> Keep variables in the **smallest scope** possible. It reduces bugs.

---

### 🏷️ 7. Naming Rules and Conventions

**Rules (must follow):**

- ✅ Can contain letters, digits, `_` and `$`
- ❌ Cannot start with a digit (`1name` is invalid)
- ❌ Cannot contain spaces or hyphens (`my-name` is invalid)
- ❌ Cannot be a reserved word (`let`, `if`, `class`, and so on)
- ⚠️ JavaScript is **case-sensitive**: `age` and `Age` are different

**Conventions (good habits):**

| Style | Used for | Example |
|---|---|---|
| `camelCase` | Normal variables and functions | `totalPrice`, `userName` |
| `UPPER_SNAKE_CASE` | True constants | `MAX_USERS`, `TAX_RATE` |
| Meaningful names | Always | `price` ✅, `x` ❌ |

> ℹ️ **Note**
>
> Python developers often use `snake_case` (`user_name`). JavaScript developers prefer `camelCase` (`userName`).

---

### 🧪 8. Declaring Multiple Variables

```javascript
let a = 1, b = 2, c = 3;  // works, but one per line is more readable

let firstName = "Asha";
let lastName = "Rao";
```

---

## 💡 Real-Life Analogy

🏫 **Think of a school classroom:**

- A **`const`** is like your **name on the school ID card**. It's fixed. You cannot change it casually.
- A **`let`** is like your **marks in the notebook**. They can be updated as you do better.
- A **`var`** is like a **loudspeaker announcement**: it can be heard in rooms where it shouldn't be (leaks out of blocks) and anyone can shout the same name again, confusing everyone. 📢

And **block scope** is like a **classroom door**: what is said inside the class stays inside the class. 🚪

---

## 💻 Real-World Application

| Where | Example usage |
|---|---|
| 🛒 **Shopping cart** | `let cartTotal` changes as items are added |
| 🏦 **Banking app** | `const INTEREST_RATE = 6.5` is a fixed value |
| 🎮 **Games** | `let lives = 3` decreases when a player loses |
| 🔐 **Login forms** | `const loginButton` stores a reference to the button |
| 🌦️ **Weather apps** | `let temperature` updates with fresh data |

Most **company coding standards** (Google, Airbnb style guides) say: *use `const` by default, `let` when needed, and never `var`.* Tools called **linters (ESLint)** will even warn you if you use `var`.

---

## 🔍 Industry Example

📘 **Scenario: A fuel-price tracker at an energy company**

A frontend developer writes:

```javascript
const COMPANY_NAME = "PetroFast";   // never changes
const TAX_PERCENT = 5;              // fixed rule

let fuelPrice = 100;                // changes daily
let litersBought = 0;               // changes with every purchase

litersBought = 10;
let total = fuelPrice * litersBought;
total = total + (total * TAX_PERCENT) / 100;

console.log(`Total bill: ₹${total}`);  // Total bill: ₹1050
```

**What happens internally:**

1. 📦 JavaScript reserves memory boxes named `COMPANY_NAME`, `TAX_PERCENT`, `fuelPrice`, `litersBought`.
2. 🔒 It marks `const` boxes as "do not reassign".
3. 🔄 When `litersBought` becomes 10, only that box's content is replaced.
4. 🧮 `total` is calculated using values from the boxes.
5. 🖨️ The final amount is printed.

If another developer accidentally writes `TAX_PERCENT = 18;`, JavaScript throws an error, **protecting the business logic** from accidental change.

---

## 📊 Diagram

```
        VARIABLES = LABELED BOXES IN MEMORY

   let score = 10;              const PI = 3.14;
 ┌──────────────┐             ┌──────────────┐
 │    score     │             │      PI      │
 │ ┌──────────┐ │             │ ┌──────────┐ │
 │ │    10    │ │             │ │   3.14   │ │
 │ └──────────┘ │             │ └──────────┘ │
 └──────────────┘             └──────────────┘
   score = 20; ✅                PI = 3; ❌ Error!


            WHICH KEYWORD SHOULD I USE?

               Will the value change?
                    /          \
                 YES            NO
                  │              │
                 let           const
                  
               (var → avoid ❌)


             BLOCK SCOPE EXAMPLE

   {                          
      let a = 5;    ← a lives only here 🧱
   }                          
   console.log(a);  ← ❌ not visible outside
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`const` means the object's contents can never change." | `const` prevents **reassignment** only. Array and object contents can still be modified. |
| "`var` and `let` are exactly the same." | `var` ignores block scope and allows re-declaration. `let` doesn't. |
| "I can declare `const` without a value." | `const` **must** be initialized when declared. |
| "Variable names like `my-name` are fine." | Hyphens are not allowed. Use `myName`. |
| "`Age` and `age` are the same." | JavaScript is case-sensitive, so they are different variables. |
| "I should use `let` for everything." | Prefer `const` by default. It tells readers the value won't change. |

---

## 💬 Interview Corner

**Q1. What is the difference between `var`, `let`, and `const`?**
`var` is function-scoped and allows re-declaration. `let` is block-scoped and can be reassigned. `const` is block-scoped and cannot be reassigned.

**Q2. Why should we avoid `var`?**
Because it ignores block scope, allows accidental re-declaration, and is hoisted as `undefined`, which leads to confusing bugs.

**Q3. Can we change the contents of a `const` array?**
Yes. `const` prevents reassigning the variable, but the array's elements can still be modified with methods like `push()`.

**Q4. What is scope?**
Scope defines where a variable can be accessed in the code: global, function, or block.

---

## 📝 Quick Summary

- 📦 A variable is a **named container** for storing data.
- 🔄 **`let`**: use when the value will change.
- 🔒 **`const`**: use when the value will not be reassigned. Make it your **default**.
- 🚫 **`var`**: the old way. Avoid it because of scope and re-declaration problems.
- 🧱 `let` and `const` are **block-scoped**. `var` is not.
- 🏷️ Use **camelCase** for names, and meaningful names always.
- ⚠️ `const` doesn't freeze array or object contents.
- 🔍 Variables must be declared before use with `let` and `const`.

---

## 🎯 Class Activity

**🛠️ Activity: "Break it to understand it"**

Create `variables.js` (or use the console) and try each experiment. Write down what you observe.

```javascript
// Experiment 1: let can change
let level = 1;
level = 2;
console.log(level);

// Experiment 2: const cannot change
const planet = "Earth";
// planet = "Mars";   // uncomment this line and see the error

// Experiment 3: var leaks out of blocks
if (true) {
  var leaky = "I escaped!";
  let safe = "I stay inside.";
}
console.log(leaky);
// console.log(safe);  // uncomment and see the error

// Experiment 4: const array
const fruits = ["apple", "banana"];
fruits.push("mango");
console.log(fruits);
```

**Discuss:** Which experiment surprised you the most, and why?

---

# 📋 Assignments — Variables: `let`, `const`, and Avoiding `var`

| Assignment |
|---|
| Declare variables for your name, age, and city using `let`, and print them with `console.log()`. |
| Declare a `const` named `PI` with value 3.14159 and calculate the area of a circle of radius 7. |
| Try to reassign a `const` variable and write down the exact error message you see. |
| Declare a `let` variable `counter = 0` and increase it three times, printing after each step. |
| Write a program with `if (true) { var x = 5; }` and print `x` outside. Then repeat with `let` and compare the results. |
| Declare the same variable twice using `var`, then twice using `let`. Observe and note the difference. |
| Try `console.log(a)` before declaring `var a = 5;`, then try it with `let a = 5;`. Write the difference. |
| Create a `const` array of 3 colors, add a fourth using `push()`, then try reassigning the array. Explain what worked and what failed. |
| Create a small bill calculator with `const TAX = 10`, `let price`, and `let total`, and print the final amount. |
| List five valid and five invalid variable names with reasons. |
| Rewrite this code replacing all `var` with the correct `let` or `const`: `var name = "Sam"; var age = 20; var PI = 3.14; age = 21;` |
| Create a scope experiment with one global variable and one function variable, and try to access the function variable outside. Record the error. |
| Write a short paragraph explaining in your own words why professional developers avoid `var`. |

# 📚 Data Types and Operators in JavaScript

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🧬 Identify the primitive and non-primitive data types in JavaScript
- 🔎 Use the `typeof` operator to check a value's type
- ➕ Use arithmetic, assignment, comparison, logical, and other operators
- ⚖️ Understand the difference between `==` and `===`
- 🔄 Understand type conversion (coercion) at a beginner level
- 🧮 Predict the output of simple expressions confidently

---

## 📖 Introduction

Every piece of information in a program has a **kind**: a name is text, an age is a number, "is the user logged in?" is a yes/no answer. This "kind" is called a **data type**.

**Operators** are the symbols that let us **do things with data**: add numbers, compare values, combine conditions.

**Why does this topic exist?** The computer must know what kind of data it's dealing with. You can add two numbers, but what does it mean to "multiply a name by a name"? 🤔

**Where is it used?** Every calculation, every form check, every decision your program makes.

---

## 🧠 Detailed Notes

### 🧬 1. Data Types in JavaScript

JavaScript has two big families:

| Family | Meaning | Examples |
|---|---|---|
| **Primitive** | Single, simple values | number, string, boolean, undefined, null, bigint, symbol |
| **Non-primitive** | Collections / complex structures | object, array, function |

In this topic, we focus on the main primitive types.

---

### 🔢 2. Number

Numbers cover both integers and decimals. JavaScript has just **one** number type.

```javascript
let age = 25;
let price = 99.99;
let temperature = -5;

console.log(typeof age); // "number"
```

Special number values:

```javascript
console.log(10 / 0);        // Infinity
console.log("abc" * 3);     // NaN (Not a Number)
console.log(typeof NaN);    // "number" (funny but true!)
```

> ℹ️ **Note**
>
> `NaN` means "this calculation didn't produce a valid number." Use `Number.isNaN(value)` to check it.

---

### 🔤 3. String

Text wrapped in quotes: single `' '`, double `" "`, or backticks `` ` ` ``.

```javascript
let firstName = "Asha";
let lastName = 'Rao';
let greeting = `Hello, ${firstName}!`;   // template literal ✨

console.log(greeting);          // Hello, Asha!
console.log(firstName.length);  // 4
console.log(firstName.toUpperCase()); // ASHA
console.log(firstName + " " + lastName); // Asha Rao
```

- **Backticks** let you embed variables with `${ }`. This is called a **template literal** and is very popular.

---

### ✅ 4. Boolean

Only two values: `true` or `false`.

```javascript
let isLoggedIn = true;
let hasPaid = false;
console.log(typeof isLoggedIn); // "boolean"
```

Booleans are the base of all decision making (`if/else`).

---

### 🕳️ 5. `undefined` and `null`

| Type | Meaning | Who sets it? |
|---|---|---|
| `undefined` | A variable was declared but **no value was given** | JavaScript automatically |
| `null` | An **intentional empty** value | The programmer, deliberately |

```javascript
let a;
console.log(a);          // undefined

let b = null;
console.log(b);          // null

console.log(typeof a);   // "undefined"
console.log(typeof b);   // "object" (a famous historical bug in JS 🐛)
```

> 💡 **Tip**
>
> Think of `undefined` as "I forgot to fill this in" and `null` as "I deliberately left this empty."

---

### 🧩 6. BigInt and Symbol (Just Awareness)

- **BigInt**: for very large integers: `12345678901234567890n`
- **Symbol**: a unique identifier, used in advanced cases.

You won't need these often as a beginner.

---

### 🔎 7. The `typeof` Operator

Use it to find the type of any value.

```javascript
console.log(typeof 42);          // "number"
console.log(typeof "hello");     // "string"
console.log(typeof true);        // "boolean"
console.log(typeof undefined);   // "undefined"
console.log(typeof null);        // "object" (quirk)
console.log(typeof [1, 2, 3]);   // "object"
console.log(typeof {name: "A"}); // "object"
```

🤔 **Quick thinking question:** What does `typeof "25"` return?

✅ **Answer:** `"string"`, because anything inside quotes is text, even if it looks like a number!

---

### ➕ 8. Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | 13 |
| `-` | Subtraction | `10 - 3` | 7 |
| `*` | Multiplication | `10 * 3` | 30 |
| `/` | Division | `10 / 3` | 3.333... |
| `%` | Remainder (modulus) | `10 % 3` | 1 |
| `**` | Power | `2 ** 3` | 8 |
| `++` | Increment by 1 | `x++` | x + 1 |
| `--` | Decrement by 1 | `x--` | x - 1 |

```javascript
let x = 10;
x++;
console.log(x);       // 11
console.log(10 % 2);  // 0 → even number!
console.log(7 % 2);   // 1 → odd number!
```

> 💡 **Tip**
>
> The `%` operator is great for checking **even/odd** numbers and for repeating patterns.

---

### 📝 9. Assignment Operators

| Operator | Same as | Example |
|---|---|---|
| `=` | assign | `x = 5` |
| `+=` | `x = x + 5` | `x += 5` |
| `-=` | `x = x - 5` | `x -= 5` |
| `*=` | `x = x * 5` | `x *= 5` |
| `/=` | `x = x / 5` | `x /= 5` |
| `%=` | `x = x % 5` | `x %= 5` |

```javascript
let balance = 1000;
balance += 500;   // 1500
balance -= 200;   // 1300
console.log(balance);
```

---

### ⚖️ 10. Comparison Operators

They compare two values and return **`true` or `false`**.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `>` | greater than | `5 > 3` | true |
| `<` | less than | `5 < 3` | false |
| `>=` | greater than or equal | `5 >= 5` | true |
| `<=` | less than or equal | `4 <= 3` | false |
| `==` | equal (loose) | `5 == "5"` | true 😮 |
| `===` | equal (strict) | `5 === "5"` | false ✅ |
| `!=` | not equal (loose) | `5 != "5"` | false |
| `!==` | not equal (strict) | `5 !== "5"` | true |

#### 🥊 `==` vs `===`: the most important rule here

- `==` compares **only the value** (it quietly converts types first).
- `===` compares **value AND type**.

```javascript
console.log(5 == "5");   // true  (types ignored)
console.log(5 === "5");  // false (number vs string)
console.log(0 == false); // true  (surprise!)
console.log(0 === false);// false
```

> ⚠️ **Important**
>
> **Always use `===` and `!==`** in your code. It avoids surprising bugs.

---

### 🧠 11. Logical Operators

Used to **combine conditions**.

| Operator | Name | Meaning |
|---|---|---|
| `&&` | AND | true only if **both** sides are true |
| `\|\|` | OR | true if **at least one** side is true |
| `!` | NOT | flips true ↔ false |

```javascript
let age = 20;
let hasTicket = true;

console.log(age >= 18 && hasTicket); // true  (both true)
console.log(age < 18 || hasTicket);  // true  (one is true)
console.log(!hasTicket);             // false
```

**Truth table for AND / OR:**

| A | B | A && B | A \|\| B |
|---|---|---|---|
| true | true | true | true |
| true | false | false | true |
| false | true | false | true |
| false | false | false | false |

---

### 🔗 12. String Operator: Concatenation

The `+` operator **joins strings**.

```javascript
console.log("Hello" + " " + "World");  // Hello World
console.log("Age: " + 25);              // Age: 25
```

---

### 🔄 13. Type Conversion (Beginner Level)

JavaScript sometimes converts types automatically (called **coercion**), and sometimes you convert manually.

**Automatic (can surprise you):**

```javascript
console.log("5" + 3);   // "53"  (number became text, then joined)
console.log("5" - 3);   // 2     (text became number, then subtracted)
console.log("5" * "2"); // 10
```

**Manual conversion (recommended):**

```javascript
console.log(Number("42"));      // 42
console.log(Number("abc"));     // NaN
console.log(parseInt("42px"));  // 42
console.log(parseFloat("3.14"));// 3.14
console.log(String(100));       // "100"
console.log(Boolean(0));        // false
console.log(Boolean("hello"));  // true
```

**Falsy values** (convert to `false`): `0`, `""`, `null`, `undefined`, `NaN`, `false`. Everything else is **truthy**.

---

### 🔀 14. Ternary Operator (Mini Preview)

A short way to write a simple if/else:

```javascript
let age = 17;
let message = age >= 18 ? "Adult" : "Minor";
console.log(message); // Minor
```

---

### 🥇 15. Operator Precedence (Which goes first?)

Just like math class (BODMAS), JavaScript follows an order.

```javascript
console.log(2 + 3 * 4);     // 14, not 20
console.log((2 + 3) * 4);   // 20 (brackets first)
```

> 💡 **Tip**
>
> When unsure, **use brackets**. They make code clearer for everyone.

---

## 💡 Real-Life Analogy

🍱 **Data types are like containers in a kitchen:**

- A **number** is like a measuring cup 📏: it holds quantities.
- A **string** is like a label 🏷️: it holds text.
- A **boolean** is like a light switch 💡: ON or OFF, nothing in between.
- **`undefined`** is an **empty jar nobody has filled yet**, and **`null`** is a jar you **deliberately emptied**.

**Operators are the kitchen tools**: the spoon mixes (`+`), the knife compares sizes (`>`), and the checklist `&&` says "only start cooking if I have rice AND water."

---

## 💻 Real-World Application

| Where | Types and operators used |
|---|---|
| 🛒 **Shopping cart** | Numbers (`price * quantity`), strings (product name) |
| 🔐 **Login check** | `username === "admin" && password === "1234"` |
| 🎟️ **Ticket booking** | Booleans (`isSeatAvailable`), comparison (`age >= 18`) |
| 💳 **Discount logic** | `total > 1000 ? 10 : 0` |
| 📅 **Leap-year check** | Modulus `%` with logical operators |
| 📝 **Form validation** | `typeof`, `length`, `===`, `!` |

---

## 🔍 Industry Example

📘 **Scenario: Applying a coupon on an online shopping site**

A developer writes this for the checkout page:

```javascript
const price = 1200;                 // number
const quantity = 2;                 // number
const couponCode = "SAVE10";        // string
let isMember = true;                // boolean

let total = price * quantity;       // 2400

if (couponCode === "SAVE10" && total > 2000) {
  total = total - (total * 10) / 100;   // apply 10% off
}

if (isMember) {
  total -= 50;                      // member bonus
}

console.log(`Final amount: ₹${total}`); // Final amount: ₹2110
```

**What happens internally:**

1. 🧮 JavaScript multiplies the two numbers: 2400.
2. 🔍 It checks `couponCode === "SAVE10"` (true) **and** `total > 2000` (true). `&&` gives true.
3. 💸 It calculates 10% of 2400 (240) and subtracts: 2160.
4. 🏅 Because `isMember` is true, it subtracts 50 more: 2110.
5. 🖨️ The template literal builds the final message.

If the developer had used `==` with user input that arrives as a string (like `"2400"`), subtle bugs could appear, which is why `===` is preferred.

---

## 📊 Diagram

```
                  JAVASCRIPT DATA TYPES
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
    PRIMITIVE 🧱                      NON-PRIMITIVE 🧰
 ┌──────────────────┐             ┌──────────────────┐
 │ number    42     │             │ object  {a: 1}   │
 │ string    "Hi"   │             │ array   [1,2,3]  │
 │ boolean   true   │             │ function ()=>{}  │
 │ undefined        │             └──────────────────┘
 │ null             │
 │ bigint / symbol  │
 └──────────────────┘


              OPERATOR FAMILIES
 ┌───────────┬────────────┬─────────────┬───────────┐
 │ Arithmetic│ Assignment │ Comparison  │  Logical  │
 │ + - * / % │ = += -= *= │ > < === !== │ && || !   │
 └───────────┴────────────┴─────────────┴───────────┘


        HOW  age >= 18 && hasTicket  IS EVALUATED

        age >= 18   ──►  true  ─┐
                                ├─► true && true ──► true ✅
        hasTicket   ──►  true  ─┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`=` checks if two values are equal." | `=` **assigns**. Use `===` to compare. |
| "`"5" + 3` gives 8." | It gives `"53"` because `+` joins when a string is present. |
| "`==` and `===` are the same." | `===` checks type too and is much safer. |
| "`null` and `undefined` are the same." | `undefined` is unassigned by default. `null` is intentionally empty. |
| "`typeof null` is `"null"`." | It returns `"object"`, a historic quirk. |
| "`NaN === NaN` is true." | It is **false**. Use `Number.isNaN()` to test. |
| "Numbers in quotes behave like numbers." | They are strings. Convert with `Number()` first. |

---

## 💬 Interview Corner

**Q1. What are the primitive data types in JavaScript?**
Number, string, boolean, undefined, null, bigint, and symbol.

**Q2. What is the difference between `==` and `===`?**
`==` compares values after converting types. `===` compares both value and type without conversion. Prefer `===`.

**Q3. What is the difference between `null` and `undefined`?**
`undefined` means a variable has been declared but not assigned. `null` is an intentional empty value assigned by the programmer.

**Q4. What does `typeof` do, and what does `typeof null` return?**
`typeof` returns the type of a value as a string. For `null` it returns `"object"`, which is a known bug kept for backward compatibility.

---

## 📝 Quick Summary

- 🧬 JavaScript has **primitive** types (number, string, boolean, undefined, null, bigint, symbol) and **non-primitive** types (object, array, function).
- 🔎 `typeof` tells you the type of a value.
- ➕ Arithmetic: `+ - * / % **`, plus `++` and `--`.
- 📝 Assignment: `=`, `+=`, `-=`, `*=`, `/=`.
- ⚖️ **Always use `===`** instead of `==`.
- 🧠 Logical: `&&` (AND), `||` (OR), `!` (NOT).
- 🔤 `+` joins strings, and a string plus a number gives a string.
- 🔄 Convert types manually with `Number()`, `String()`, `Boolean()`.
- 🥇 Use brackets when unsure about operator order.

---

## 🎯 Class Activity

**🛠️ Activity: "Predict, then run"**

For each line, first **write your prediction on paper**, then run it in the console and check.

```javascript
console.log(10 + "5");
console.log(10 - "5");
console.log(10 % 3);
console.log(5 == "5");
console.log(5 === "5");
console.log(typeof null);
console.log(typeof []);
console.log(true && false);
console.log(!true || true);
console.log(Boolean(""));
console.log(2 + 3 * 4);
console.log("5" * "2");
```

**Score yourself:** How many did you predict correctly? Discuss the surprises with your neighbor.

---

# 📋 Assignments — Data Types and Operators

| Assignment |
|---|
| Create one variable of each type (number, string, boolean, undefined, null) and print each with its `typeof`. |
| Write a program that stores two numbers and prints their sum, difference, product, quotient, and remainder. |
| Check whether a number is even or odd using the `%` operator, and print `true` or `false`. |
| Create variables `firstName` and `lastName` and print a full name using both `+` concatenation and a template literal. |
| Demonstrate the difference between `==` and `===` using at least four examples, and write your observation. |
| Predict and verify the output of `"10" + 5`, `"10" - 5`, `"10" * "2"`, and `true + 1`. |
| Convert the string `"123"` into a number three different ways and print the results with `typeof`. |
| Check whether a person is eligible to vote using `age >= 18` and print the result as a boolean. |
| Combine conditions: check if a number is between 10 and 50 using `&&`. |
| Write a program to find a discount: if `total > 1000`, discount is 10%, else 0. Use the ternary operator. |
| Use `+=` and `-=` to simulate a bank balance for five transactions and print the final balance. |
| Find out what `NaN` is. Write an example that produces it and another way to check it. |
| List all six falsy values in JavaScript and test each using `Boolean()`. |
| Calculate the area and perimeter of a rectangle using `const` and `let`, and print using template literals. |
| Evaluate `2 + 3 * 4 - 6 / 2` by hand, then run it. Add brackets to change the result and explain why it changed. |

# 📚 Control Flow: if/else, switch, and Loops (for, while)

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🚦 Understand what control flow means and why programs need it
- 🔀 Write decisions using `if`, `else if`, and `else`
- 🎛️ Use `switch` for multiple-choice situations
- 🔁 Repeat work using `for` and `while` loops (and `do...while`)
- ⏹️ Control loops using `break` and `continue`
- 🧩 Combine decisions and loops to solve small real-world problems

---

## 📖 Introduction

So far, our programs ran **line by line from top to bottom**, like reading a story. But real life isn't like that:

- "**If** it's raining, take an umbrella. **Otherwise**, wear sunglasses." 🌦️
- "Print the numbers from 1 to 100." (Would you really write 100 lines? 😅)

**Control flow** means **controlling which lines run, and how many times**. It gives programs the power to **decide** and **repeat**.

**Why is it important?** Without control flow, programs would be simple calculators. With it, you can build login systems, games, shopping carts, anything!

**Where is it used?** Everywhere: checking passwords, showing discounts, looping through products, running game rounds.

---

## 🧠 Detailed Notes

### 🚦 1. Decision Making: `if` Statement

Runs a block of code **only if a condition is true**.

```javascript
let age = 20;

if (age >= 18) {
  console.log("You can vote! 🗳️");
}
```

**Syntax:**

```javascript
if (condition) {
  // runs only when condition is true
}
```

The condition is anything that results in `true` or `false` (remember comparison and logical operators!).

---

### ↔️ 2. `if...else`

Gives you **two paths**: one for true, one for false.

```javascript
let marks = 35;

if (marks >= 40) {
  console.log("Pass ✅");
} else {
  console.log("Fail ❌");
}
```

---

### 🪜 3. `if...else if...else`

Use it when there are **more than two possibilities**. JavaScript checks conditions from top to bottom and runs the **first match**, then skips the rest.

```javascript
let score = 82;

if (score >= 90) {
  console.log("Grade A 🌟");
} else if (score >= 75) {
  console.log("Grade B 👍");
} else if (score >= 50) {
  console.log("Grade C 🙂");
} else {
  console.log("Grade D 📚 Keep trying!");
}
// Output: Grade B 👍
```

> ⚠️ **Important**
>
> **Order matters!** If you checked `score >= 50` first, an 82 would match immediately and print Grade C. Always put the **strictest condition first**.

🤔 **Quick thinking question:** If `score = 95`, how many of the conditions above are actually checked?

✅ **Answer:** Just **one**. `score >= 90` is true, so JavaScript runs it and skips everything else.

---

### 🪆 4. Nested `if`

An `if` inside another `if`.

```javascript
let age = 25;
let hasLicense = true;

if (age >= 18) {
  if (hasLicense) {
    console.log("You can drive 🚗");
  } else {
    console.log("Get a license first 📄");
  }
} else {
  console.log("You are too young ❌");
}
```

> 💡 **Tip**
>
> Often nested `if` can be replaced with `&&`: `if (age >= 18 && hasLicense)`. It's cleaner.

---

### 🎛️ 5. `switch` Statement

Great when you compare **one value against many fixed options**.

```javascript
let day = 3;
let dayName;

switch (day) {
  case 1:
    dayName = "Monday";
    break;
  case 2:
    dayName = "Tuesday";
    break;
  case 3:
    dayName = "Wednesday";
    break;
  default:
    dayName = "Unknown day";
}

console.log(dayName); // Wednesday
```

**Key parts:**

| Part | Meaning |
|---|---|
| `switch (value)` | The value we are checking |
| `case x:` | If value equals `x`, run this code |
| `break` | Stop here and leave the switch |
| `default` | Runs if **no case matches** (like `else`) |

> ⚠️ **Important**
>
> If you forget `break`, JavaScript keeps running the **next cases too**. This is called **fall-through**.

**Fall-through can be useful on purpose:**

```javascript
let fruit = "apple";

switch (fruit) {
  case "apple":
  case "mango":
  case "banana":
    console.log("It's a fruit 🍎");
    break;
  case "carrot":
    console.log("It's a vegetable 🥕");
    break;
  default:
    console.log("Not sure 🤷");
}
```

**`if/else` vs `switch`:**

| Use `if/else` when... | Use `switch` when... |
|---|---|
| Conditions are ranges (`age > 18`) | Comparing one value to fixed options |
| Conditions are complex (`&&`, `\|\|`) | Many exact matches (menu choices, days) |

---

### 🔁 6. Why Loops?

Imagine printing "Hello" 5 times:

```javascript
console.log("Hello");
console.log("Hello");
console.log("Hello");
console.log("Hello");
console.log("Hello");
```

Now imagine 1000 times! 😱 A **loop** repeats code for you.

---

### 🔢 7. The `for` Loop

Best when you **know how many times** to repeat.

```javascript
for (let i = 1; i <= 5; i++) {
  console.log("Count: " + i);
}
```

**Output:**

```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

**Anatomy of a `for` loop:**

```
for ( let i = 1 ;  i <= 5 ;  i++ ) { ... }
      └───┬────┘  └──┬───┘  └─┬─┘
       1) Start    2) Check  3) Update
```

**How it runs, step by step:**

1. ▶️ **Initialize**: `let i = 1` (happens once)
2. ❓ **Check condition**: is `i <= 5`? If yes, continue. If no, stop.
3. 🏃 **Run the body**
4. ➕ **Update**: `i++`
5. 🔄 Go back to step 2

**More examples:**

```javascript
// Print even numbers up to 10
for (let i = 2; i <= 10; i += 2) {
  console.log(i);
}

// Countdown
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
console.log("Liftoff! 🚀");

// Multiplication table of 7
for (let i = 1; i <= 10; i++) {
  console.log(`7 x ${i} = ${7 * i}`);
}
```

---

### 🔄 8. The `while` Loop

Best when you **don't know in advance** how many times, and you repeat **as long as a condition is true**.

```javascript
let count = 1;

while (count <= 5) {
  console.log("Count: " + count);
  count++;
}
```

```javascript
// Keep halving until number is less than 1
let n = 100;
while (n >= 1) {
  console.log(n);
  n = n / 2;
}
```

> ⚠️ **Important: the infinite loop!**
>
> If you forget `count++`, the condition stays true forever and your browser may **freeze**. 🥶 Always make sure something inside the loop eventually makes the condition **false**.

---

### 🔂 9. The `do...while` Loop

Runs the body **at least once**, then checks the condition.

```javascript
let number = 10;

do {
  console.log("This runs once even though the condition is false!");
} while (number < 5);
```

| Loop | Checks condition... | Runs at least once? |
|---|---|---|
| `while` | **Before** the body | No |
| `do...while` | **After** the body | **Yes** |

---

### ⏹️ 10. `break` and `continue`

| Keyword | What it does |
|---|---|
| `break` | **Stops** the loop completely |
| `continue` | **Skips** the current round and moves to the next |

```javascript
// break: stop when we find 5
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);   // prints 1 2 3 4
}

// continue: skip 5
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    continue;
  }
  console.log(i);   // prints 1 2 3 4 6 7 8 9 10
}
```

---

### 🪆 11. Nested Loops (Loop inside a Loop)

```javascript
for (let row = 1; row <= 3; row++) {
  let line = "";
  for (let col = 1; col <= 3; col++) {
    line += "* ";
  }
  console.log(line);
}
```

**Output:**

```
* * * 
* * * 
* * * 
```

For each **row**, the inner loop runs **completely**.

---

### 🧩 12. Putting It Together: FizzBuzz (a famous interview problem)

Print 1 to 15. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for multiples of both print "FizzBuzz".

```javascript
for (let i = 1; i <= 15; i++) {
  if (i % 3 === 0 && i % 5 === 0) {
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
```

> 💡 **Tip**
>
> Notice the **order**: we check "both" first. If we checked "multiple of 3" first, 15 would print "Fizz" and never reach "FizzBuzz".

---

## 💡 Real-Life Analogy

🚦 **Control flow is like a road trip:**

- **`if/else`** is a **traffic signal**: green means go, red means stop, and a different path is taken depending on the light.
- **`switch`** is a **lift (elevator) panel**: press 1, 2, or 3 and it goes to exactly that floor.
- **`for` loop** is like **running 5 laps on a track** 🏃. You know the number of laps in advance.
- **`while` loop** is like **"keep stirring until the sugar dissolves"** 🥄. You don't know how long it will take, only the condition.
- **`break`** is shouting "**Stop, I found it!**" and **`continue`** is saying "**Skip this one, next please!**"

---

## 💻 Real-World Application

| Where | Control flow used |
|---|---|
| 🔐 **Login systems** | `if (password === saved)` allow, else show an error |
| 🛒 **Product listing** | `for` loop displays every product on the page |
| 🎮 **Games** | `while (lives > 0)` keep the game running |
| 📊 **Reports** | Loops calculate totals of thousands of rows |
| 🏧 **ATM menu** | `switch` for Withdraw / Deposit / Balance options |
| 📧 **Email apps** | Loop checks every email, `if` marks spam |

---

## 🔍 Industry Example

📘 **Scenario: An ATM at a bank**

```javascript
let balance = 5000;
let choice = 2;   // user pressed 2 on the screen
let amount = 1500;

switch (choice) {
  case 1:
    console.log(`Your balance is ₹${balance}`);
    break;
  case 2:
    if (amount > balance) {
      console.log("Insufficient funds ❌");
    } else if (amount % 100 !== 0) {
      console.log("Enter amount in multiples of 100");
    } else {
      balance -= amount;
      console.log(`Please collect ₹${amount}. Balance: ₹${balance}`);
    }
    break;
  case 3:
    console.log("Thank you! Please take your card 💳");
    break;
  default:
    console.log("Invalid option");
}
```

**What happens internally:**

1. 🎛️ `switch` looks at `choice` (2) and jumps to `case 2`.
2. 🔍 Nested `if/else if/else` checks: enough money? Valid multiple of 100?
3. ✅ Both pass, so the `else` block runs and subtracts the amount.
4. 🛑 `break` stops the switch so other cases don't run.
5. 🔁 In a real ATM, a `while` loop wraps this so the menu keeps appearing until the user chooses "Exit".

---

## 📊 Diagram

```
              if / else if / else FLOW

                 ┌───────────┐
                 │  START    │
                 └─────┬─────┘
                       ▼
               ┌───────────────┐
        YES    │ marks >= 90 ? │   NO
     ┌─────────┤               ├──────────┐
     ▼         └───────────────┘          ▼
 Print "A"                       ┌───────────────┐
                          YES    │ marks >= 75 ? │   NO
                       ┌─────────┤               ├──────┐
                       ▼         └───────────────┘      ▼
                   Print "B"                        Print "C"


                    for LOOP FLOW

           ┌──────────────────┐
           │  let i = 1       │  ← Initialize (once)
           └────────┬─────────┘
                    ▼
           ┌──────────────────┐   NO
     ┌────►│   i <= 5 ?       ├────────► EXIT LOOP
     │     └────────┬─────────┘
     │              │ YES
     │              ▼
     │     ┌──────────────────┐
     │     │  run loop body   │
     │     └────────┬─────────┘
     │              ▼
     │     ┌──────────────────┐
     └─────┤      i++         │
           └──────────────────┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I can write `if (x = 5)` to compare." | `=` assigns! Use `===` to compare. |
| "`switch` doesn't need `break`." | Without `break`, execution **falls through** to the next cases. |
| "A `while` loop will stop by itself." | Only if something inside makes the condition false. Otherwise it's an **infinite loop**. |
| "Loop counters start at 1 always." | Many programmers (and arrays) start at **0**. Choose based on need. |
| "`else if` order doesn't matter." | The first true condition wins, so put the **most specific** first. |
| "`continue` and `break` do the same thing." | `break` ends the loop. `continue` only skips one round. |
| "`for (let i = 0; i <= 5; i++)` runs 5 times." | It runs **6 times** (0,1,2,3,4,5). Watch `<` vs `<=`. |

---

## 💬 Interview Corner

**Q1. What is the difference between `while` and `do...while`?**
`while` checks the condition before running the body, so it may never run. `do...while` runs the body once first and then checks the condition.

**Q2. When would you use `switch` instead of `if/else`?**
When comparing one value against many fixed options, like menu choices or day names. It is cleaner than a long `else if` chain.

**Q3. What happens if you forget `break` in a `switch` case?**
Execution falls through into the next case and keeps running until it hits a `break` or the end.

**Q4. What is the difference between `break` and `continue`?**
`break` exits the loop completely, while `continue` skips the current iteration and goes on to the next one.

---

## 📝 Quick Summary

- 🚦 **Control flow** decides what runs and how many times.
- 🔀 `if`, `else if`, `else` handle decisions, and the first true condition wins.
- 🎛️ `switch` is best for one value compared against many fixed options. Don't forget `break`.
- 🔢 `for` loop is best when you know the number of repetitions.
- 🔄 `while` loop is best when you repeat until a condition changes.
- 🔂 `do...while` runs at least once.
- ⏹️ `break` stops a loop and `continue` skips one round.
- ♾️ Avoid infinite loops by always updating the loop condition.
- 🪆 Loops and `if` can be nested to solve bigger problems.

---

## 🎯 Class Activity

**🛠️ Activity: "Mini Game Master"**

Build these small programs one by one in a `.js` file or the console:

1. **Number checker:** For `let num = -5;` print whether it is *positive*, *negative*, or *zero*.
2. **Traffic light:** Use `switch` on `let light = "red";` and print "Stop", "Get Ready", or "Go".
3. **Times table:** Use a `for` loop to print the table of any number up to 10.
4. **Countdown:** Use a `while` loop to count down from 10 to 1, then print "Happy New Year! 🎆".
5. **FizzBuzz:** Print 1 to 30 with Fizz/Buzz rules.

Compare your solutions with a classmate and see whose version is shorter.

---

# 📋 Assignments — Control Flow: if/else, switch, and Loops

| Assignment |
|---|
| Write a program that checks whether a number is even or odd using `if/else` and prints the result. |
| Write a program that prints a grade (A/B/C/D/F) for a given mark using `if...else if...else`. |
| Check whether a given year is a leap year (divisible by 4, but century years must be divisible by 400). |
| Find the largest of three numbers using `if/else if` and logical operators. |
| Use `switch` to print the name of the day for numbers 1 to 7, with a `default` for invalid input. |
| Build a simple calculator using `switch` on an operator string (`"+"`, `"-"`, `"*"`, `"/"`) with two numbers. |
| Use a `for` loop to print numbers from 1 to 20. |
| Use a `for` loop to print all even numbers between 1 and 50. |
| Print the multiplication table of any number (say 9) up to 10 using a `for` loop. |
| Calculate the sum of numbers from 1 to 100 using a loop and print the answer. |
| Use a `while` loop to print numbers from 10 down to 1, then print "Done!". |
| Reverse a number (for example, 1234 becomes 4321) using a `while` loop and `%`. |
| Use `break` to stop a loop when the number 7 is found in a series from 1 to 20. |
| Use `continue` to print numbers from 1 to 15 but skip multiples of 3. |
| Use nested loops to print a right-angled triangle of stars with 5 rows. |

# 📚 Arrays and Objects Basics

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🗃️ Understand why we need arrays and objects
- 📋 Create arrays, access items, and modify them
- 🛠️ Use common array methods like `push`, `pop`, `shift`, `unshift`, `slice`, `splice`, `includes`, and `indexOf`
- 🔁 Loop through an array with `for` and `for...of`
- 🧳 Create objects with properties and access them using dot and bracket notation
- 🔗 Combine arrays and objects to represent real-world data

---

## 📖 Introduction

Until now, we stored **one value per variable**:

```javascript
let student1 = "Asha";
let student2 = "Ravi";
let student3 = "Meena";
```

What if there are **500 students**? Creating 500 variables would be a nightmare. 😵

And what if one student has a **name, age, course, and marks**? We would need many variables again.

JavaScript gives us two powerful tools:

- 📋 **Array**: an **ordered list** of values. (*"A list of students"*)
- 🧳 **Object**: a collection of **named properties** describing **one thing**. (*"Details of one student"*)

**Why important?** Almost all real data (products, users, orders, messages) is stored using arrays and objects, and this is how data travels between servers and web pages (JSON).

---

## 🧠 Detailed Notes

## 📋 PART A: ARRAYS

### 🏗️ 1. Creating an Array

```javascript
let fruits = ["apple", "banana", "mango"];
let numbers = [10, 20, 30, 40];
let mixed = ["Asha", 21, true, null];   // arrays can hold different types
let empty = [];

console.log(fruits);
console.log(typeof fruits); // "object" (arrays are special objects)
console.log(Array.isArray(fruits)); // true ✅ the correct way to check
```

---

### 🔢 2. Index: Position Starts at 0!

Every item has a position called an **index**, and the **first index is 0**, not 1.

```
 Index:     0         1         2
         ┌────────┬─────────┬────────┐
fruits = │ apple  │ banana  │ mango  │
         └────────┴─────────┴────────┘
```

```javascript
let fruits = ["apple", "banana", "mango"];

console.log(fruits[0]);              // apple
console.log(fruits[2]);              // mango
console.log(fruits[5]);              // undefined (doesn't exist)
console.log(fruits.length);          // 3
console.log(fruits[fruits.length - 1]); // mango (last item)
```

🤔 **Quick thinking question:** If an array has 10 items, what is the index of the last item?

✅ **Answer:** **9**, because counting starts at 0. In general the last index is `length - 1`.

---

### ✏️ 3. Changing Items

```javascript
let fruits = ["apple", "banana", "mango"];
fruits[1] = "grapes";
console.log(fruits); // ["apple", "grapes", "mango"]
```

> ℹ️ **Note**
>
> Even if the array is declared with `const`, you can still change its **items**. You just can't **reassign** the whole variable.

---

### ➕➖ 4. Adding and Removing Items

| Method | What it does | Where |
|---|---|---|
| `push(x)` | Adds item | at the **end** |
| `pop()` | Removes item | from the **end** |
| `unshift(x)` | Adds item | at the **start** |
| `shift()` | Removes item | from the **start** |

```javascript
let queue = ["A", "B", "C"];

queue.push("D");       // ["A","B","C","D"]
queue.pop();           // removes "D" → ["A","B","C"]
queue.unshift("Z");    // ["Z","A","B","C"]
queue.shift();         // removes "Z" → ["A","B","C"]

console.log(queue);
```

> 💡 **Tip**
>
> Remember: **push/pop** work at the **back** (like a stack of plates 🍽️). **unshift/shift** work at the **front**.

---

### 🔍 5. Searching Inside an Array

```javascript
let colors = ["red", "green", "blue"];

console.log(colors.includes("green"));  // true
console.log(colors.indexOf("blue"));    // 2
console.log(colors.indexOf("pink"));    // -1 (not found)
```

---

### ✂️ 6. `slice` and `splice`

These two names look alike but behave differently!

| Method | Changes original array? | Purpose |
|---|---|---|
| `slice(start, end)` | ❌ **No** | Copies a part of an array (end not included) |
| `splice(start, deleteCount, ...items)` | ✅ **Yes** | Removes and/or inserts items |

```javascript
let nums = [10, 20, 30, 40, 50];

// slice: just copies
let part = nums.slice(1, 4);
console.log(part);   // [20, 30, 40]
console.log(nums);   // [10, 20, 30, 40, 50] (unchanged)

// splice: changes the array
nums.splice(2, 1);          // remove 1 item at index 2
console.log(nums);          // [10, 20, 40, 50]

nums.splice(1, 0, 15);      // at index 1, delete 0, insert 15
console.log(nums);          // [10, 15, 20, 40, 50]
```

---

### 🔗 7. Other Handy Array Tools

```javascript
let a = [1, 2];
let b = [3, 4];

console.log(a.concat(b));            // [1, 2, 3, 4]
console.log([...a, ...b]);           // [1, 2, 3, 4] (spread operator)
console.log(["x", "y", "z"].join("-")); // "x-y-z"
console.log([3, 1, 2].sort());       // [1, 2, 3]
console.log([1, 2, 3].reverse());    // [3, 2, 1]
```

> ⚠️ **Important**
>
> `sort()` sorts **as text** by default, so `[10, 9, 1].sort()` gives `[1, 10, 9]`! For numbers, use `sort((a, b) => a - b)`.

---

### 🔁 8. Looping Through an Array

```javascript
let fruits = ["apple", "banana", "mango"];

// Classic for loop (when you need the index)
for (let i = 0; i < fruits.length; i++) {
  console.log(i, fruits[i]);
}

// for...of loop (cleanest when you only need values)
for (const fruit of fruits) {
  console.log(fruit);
}
```

---

### 🪆 9. Nested Arrays (Array of Arrays)

```javascript
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

console.log(matrix[1][2]); // 6  (row 1, column 2)
```

---

## 🧳 PART B: OBJECTS

### 🏗️ 10. Creating an Object

An object stores data as **key: value** pairs, called **properties**.

```javascript
let student = {
  name: "Asha",
  age: 21,
  course: "Python Full Stack",
  isPlaced: false
};

console.log(student);
console.log(typeof student); // "object"
```

---

### 🔑 11. Accessing Properties

**Dot notation** (most common):

```javascript
console.log(student.name);     // Asha
console.log(student.age);      // 21
```

**Bracket notation** (needed when the key is stored in a variable or has special characters):

```javascript
console.log(student["course"]);   // Python Full Stack

let key = "age";
console.log(student[key]);        // 21
```

---

### ✏️ 12. Add, Update, and Delete Properties

```javascript
let student = { name: "Asha", age: 21 };

student.age = 22;               // update
student.city = "Hyderabad";     // add new
delete student.city;            // remove

console.log(student);           // { name: "Asha", age: 22 }
```

---

### ⚙️ 13. Methods: Functions Inside Objects

```javascript
let car = {
  brand: "Toyota",
  speed: 0,
  start: function () {
    console.log(this.brand + " is starting 🚗");
  },
  // shorter modern syntax
  stop() {
    console.log(this.brand + " has stopped 🛑");
  }
};

car.start(); // Toyota is starting 🚗
car.stop();  // Toyota has stopped 🛑
```

- `this` refers to **the object itself** (here, `car`).

---

### 🔍 14. Useful Object Tools

```javascript
let user = { name: "Ravi", age: 25, city: "Pune" };

console.log(Object.keys(user));     // ["name", "age", "city"]
console.log(Object.values(user));   // ["Ravi", 25, "Pune"]
console.log(Object.entries(user));  // [["name","Ravi"], ["age",25], ["city","Pune"]]
console.log("age" in user);         // true
console.log(user.hasOwnProperty("email")); // false

// Looping through an object
for (const key in user) {
  console.log(key + ": " + user[key]);
}
```

---

### 🪆 15. Nested Objects

```javascript
let employee = {
  name: "Kiran",
  address: {
    city: "Bengaluru",
    pin: 560001
  },
  skills: ["HTML", "CSS", "JavaScript"]
};

console.log(employee.address.city);  // Bengaluru
console.log(employee.skills[2]);     // JavaScript
```

---

### 🔗 16. The Power Combo: Array of Objects ⭐

This is the **most common data shape** in real projects.

```javascript
let students = [
  { name: "Asha", marks: 85 },
  { name: "Ravi", marks: 62 },
  { name: "Meena", marks: 91 }
];

console.log(students[0].name);      // Asha
console.log(students[2].marks);     // 91

for (const s of students) {
  console.log(`${s.name} scored ${s.marks}`);
}
```

> ℹ️ **Note**
>
> This looks just like **JSON**, the format APIs use to send data. Learn this shape well and API data will feel natural. 🌐

---

### ⚖️ 17. Array vs Object

| Feature | 📋 Array | 🧳 Object |
|---|---|---|
| Stores | Ordered **list** of values | Named **properties** (key-value) |
| Access by | Index (`arr[0]`) | Key (`obj.name`) |
| Best for | Many similar items | Describing one thing |
| Example | `["a", "b", "c"]` | `{name: "A", age: 20}` |

---

## 💡 Real-Life Analogy

🏫 **Think of a school:**

- An **array** is like a **row of lockers** 🔢. Each locker has a number (index) starting from 0, and you open one by its number.
- An **object** is like a **student ID card** 🪪. Each field has a label (name, age, class), and you read information by the label.
- An **array of objects** is a **stack of ID cards** 🗂️, one for each student in the class.

---

## 💻 Real-World Application

| Where | How arrays/objects are used |
|---|---|
| 🛒 **Amazon cart** | Array of product objects: `[{name, price, qty}, ...]` |
| 🎵 **Spotify playlist** | Array of song objects with title, artist, duration |
| 📱 **Instagram feed** | Array of post objects with image, likes, comments |
| 👤 **User profile** | Object with name, email, address, preferences |
| 🌐 **API responses** | Data arrives as JSON: arrays and objects |
| 📅 **Calendar apps** | Array of event objects |

---

## 🔍 Industry Example

📘 **Scenario: A food delivery app showing your cart**

```javascript
const cart = [
  { item: "Margherita Pizza", price: 299, qty: 1 },
  { item: "Garlic Bread",     price: 129, qty: 2 },
  { item: "Cold Drink",       price: 60,  qty: 3 }
];

let total = 0;
for (const product of cart) {
  total += product.price * product.qty;
}

console.log(`Cart items: ${cart.length}`);
console.log(`Total: ₹${total}`);   // 299 + 258 + 180 = ₹737
```

**What happens internally:**

1. 📦 The server sends the cart as **JSON**, which JavaScript turns into an **array of objects**.
2. 🔁 The `for...of` loop picks each object one at a time.
3. 🔑 `product.price` and `product.qty` read the properties using dot notation.
4. 🧮 The total is built up step by step.
5. 🖼️ The page then shows each item as a row and displays the total at the bottom.

When you press **"+"** on an item, JavaScript simply updates `qty` for that object and recalculates, with no page reload.

---

## 📊 Diagram

```
                ARRAY (ordered list)

   index →   0        1        2        3
          ┌───────┬────────┬────────┬────────┐
 names =  │ "Asha"│ "Ravi" │"Meena" │ "Kiran"│
          └───────┴────────┴────────┴────────┘
   names[2]  →  "Meena"


                OBJECT (key → value)

        student = {
          ┌──────────┬───────────────────┐
          │  KEY     │   VALUE           │
          ├──────────┼───────────────────┤
          │  name    │  "Asha"           │
          │  age     │  21               │
          │  course  │  "Full Stack"     │
          └──────────┴───────────────────┘
        }
   student.name  →  "Asha"


          ARRAY OF OBJECTS (real-world shape)

   users = [
       { name: "Asha",  marks: 85 },   ← users[0]
       { name: "Ravi",  marks: 62 },   ← users[1]
       { name: "Meena", marks: 91 }    ← users[2]
   ]
   users[1].name  →  "Ravi"
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "The first item is at index 1." | Arrays start at **index 0**. |
| "The last index equals `length`." | The last index is **`length - 1`**. |
| "`slice` and `splice` do the same thing." | `slice` copies without changing. `splice` modifies the original. |
| "`const` arrays can't be changed." | Their **contents** can change. Only reassignment is blocked. |
| "`typeof []` returns `"array"`." | It returns `"object"`. Use `Array.isArray()`. |
| "Use `obj.key` for a key stored in a variable." | Use **bracket notation**: `obj[key]`. |
| "`[10, 9, 1].sort()` sorts numbers correctly." | It sorts as **text**. Use `sort((a, b) => a - b)`. |
| "Objects keep a numbered order like arrays." | Objects are accessed by **key**, not by position. |

---

## 💬 Interview Corner

**Q1. What is the difference between an array and an object?**
An array is an ordered list accessed by numeric index. An object is a collection of key-value pairs accessed by key names.

**Q2. What is the difference between `push()` and `unshift()`?**
`push()` adds an item to the end of an array, and `unshift()` adds it to the beginning.

**Q3. What is the difference between `slice()` and `splice()`?**
`slice()` returns a copy of part of an array without changing the original. `splice()` changes the original array by removing or inserting items.

**Q4. What are the two ways to access an object property?**
Dot notation (`obj.name`) and bracket notation (`obj["name"]`). Bracket notation is needed when the key is dynamic or has special characters.

---

## 📝 Quick Summary

- 📋 **Arrays** store ordered lists and use index positions starting at **0**.
- 🧳 **Objects** store data as **key: value** pairs and describe one entity.
- ➕ `push/pop` work at the end, and `unshift/shift` work at the start of an array.
- ✂️ `slice` copies, `splice` modifies the original.
- 🔍 `includes()` and `indexOf()` help search an array.
- 🔁 Use `for` or `for...of` to loop through arrays, and `for...in` for objects.
- 🔑 Access object properties with **dot** or **bracket** notation.
- 🔗 **Array of objects** is the most common real-world data structure.
- 🧱 `const` allows changing contents but not reassigning the variable.

---

## 🎯 Class Activity

**🛠️ Activity: "Build your class database"**

1. Create an array called `classmates` containing **5 objects**, each with `name`, `age`, and `favoriteLanguage`.
2. Print the name of the **third** classmate.
3. Use a `for...of` loop to print `"<name> loves <favoriteLanguage>"` for everyone.
4. Add a new classmate using `push()`.
5. Remove the first classmate using `shift()`.
6. Calculate and print the **average age** of the class.

**Bonus:** Print only the names of classmates older than 20.

---

# 📋 Assignments — Arrays and Objects Basics

| Assignment |
|---|
| Create an array of your 5 favorite movies and print the first, last, and total count. |
| Add two new items to the end of the array using `push()` and one item to the start using `unshift()`. Print the array after each step. |
| Remove the last and first items using `pop()` and `shift()` and print what was removed each time. |
| Check whether a given item exists in your array using `includes()`, and find its position using `indexOf()`. |
| Given `[10, 20, 30, 40, 50]`, use `slice()` to get `[20, 30, 40]` and confirm the original is unchanged. |
| Using `splice()`, remove the number 30 from `[10, 20, 30, 40, 50]` and insert 25 and 35 in its place. |
| Loop through an array of numbers and print the sum and the largest number. |
| Reverse an array of names and join them into a single string separated by commas. |
| Sort `[25, 100, 1, 8]` correctly in ascending and descending order. Also show what happens with the default `sort()`. |
| Create an object `myProfile` with at least 5 properties (name, age, city, hobbies array, address object) and print each using dot notation. |
| Add a new property, update an existing property, and delete a property from your object. Print the object after each change. |
| Use bracket notation with a variable to print a property whose name is stored in a variable. |
| Use `Object.keys()`, `Object.values()`, and `Object.entries()` on your object and print the results. |
| Create an object `calculator` with methods `add(a, b)` and `subtract(a, b)` and call both. |
| Create an array of 5 product objects (name, price, stock). Print products that cost more than 500 and the total price of all products. |

# 📚 Intro to Array Methods: `map`, `filter`, and `reduce`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🧩 Understand what a callback function is (in simple terms)
- ➡️ Read and write simple arrow functions
- 🔄 Use `map()` to **transform** every item in an array
- 🔍 Use `filter()` to **select** items that meet a condition
- ➕ Use `reduce()` to **combine** all items into a single value
- 🔗 Chain `map`, `filter`, and `reduce` together for real-world tasks
- 🆚 Choose between a `for` loop and these array methods

---

## 📖 Introduction

In the last topic, you learned to loop through arrays using `for` and `for...of`. That works well, but notice how often we write the same patterns:

- "Make a **new list** where every item is changed" (like adding tax to every price) 💰
- "Pick only the items that **match a rule**" (like products under ₹500) 🛍️
- "Add up everything and give me **one answer**" (like the cart total) 🧮

These three patterns are so common that JavaScript gives us **built-in tools** for them:

| Pattern | Tool |
|---|---|
| Transform every item | `map()` |
| Select some items | `filter()` |
| Combine into one value | `reduce()` |

**Why important?** Modern JavaScript code (React, Node.js, API handling) uses these methods **everywhere**. They make code shorter, cleaner, and easier to read, and they are favorites in **interviews**.

---

## 🧠 Detailed Notes

### 🧩 1. Prerequisite: Functions and Arrow Functions (Quick Recap)

A **function** is a reusable block of code.

```javascript
function double(n) {
  return n * 2;
}
console.log(double(5)); // 10
```

An **arrow function** is a shorter way to write the same thing:

```javascript
const double = (n) => {
  return n * 2;
};

// even shorter (one-line, return is implied)
const double2 = (n) => n * 2;

console.log(double2(5)); // 10
```

| Style | Code |
|---|---|
| Normal function | `function double(n) { return n * 2; }` |
| Arrow function | `(n) => { return n * 2; }` |
| Short arrow function | `n => n * 2` |

---

### 📞 2. What is a Callback Function?

A **callback** is a function that you **give to another function** so it can **call it later**.

`map`, `filter`, and `reduce` all **take a function as input**. They run it for each item in the array.

```javascript
const numbers = [1, 2, 3];

numbers.forEach((n) => {
  console.log(n * 10);
});
// 10, 20, 30
```

Here `(n) => console.log(n * 10)` is the **callback**. `forEach` calls it once per item.

> 💡 **Tip**
>
> Think of a callback as **instructions you hand over**: "For each item, do *this*."

---

### 🔄 3. `map()`: Transform Every Item

**Purpose:** Creates a **new array** by applying a function to **every** item. The new array has the **same length** as the original.

**Syntax:**

```javascript
const newArray = oldArray.map((item, index) => {
  return /* new value */;
});
```

**Example 1: double every number**

```javascript
const numbers = [1, 2, 3, 4];
const doubled = numbers.map((n) => n * 2);

console.log(doubled); // [2, 4, 6, 8]
console.log(numbers); // [1, 2, 3, 4] (original is unchanged ✅)
```

**Example 2: convert names to uppercase**

```javascript
const names = ["asha", "ravi", "meena"];
const upper = names.map((name) => name.toUpperCase());
console.log(upper); // ["ASHA", "RAVI", "MEENA"]
```

**Example 3: pick one property from objects**

```javascript
const students = [
  { name: "Asha", marks: 85 },
  { name: "Ravi", marks: 62 },
  { name: "Meena", marks: 91 }
];

const onlyNames = students.map((s) => s.name);
console.log(onlyNames); // ["Asha", "Ravi", "Meena"]
```

**Example 4: create new objects**

```javascript
const prices = [100, 200, 300];
const withTax = prices.map((p) => ({ price: p, total: p * 1.18 }));
console.log(withTax);
```

> ℹ️ **Note**
>
> When returning an **object** from a short arrow function, wrap it in **parentheses** `({ ... })`. Otherwise JavaScript thinks the `{ }` is a function body.

🤔 **Quick thinking question:** If you `map` over an array of 5 items, how many items will the new array have?

✅ **Answer:** **5**. `map` always returns an array of the **same length**.

---

### 🔍 4. `filter()`: Keep Only What Matches

**Purpose:** Creates a **new array** containing only the items for which the function returns **`true`**. The new array can be **shorter** (or even empty).

**Syntax:**

```javascript
const result = array.filter((item) => /* condition that gives true/false */);
```

**Example 1: keep even numbers**

```javascript
const numbers = [1, 2, 3, 4, 5, 6];
const evens = numbers.filter((n) => n % 2 === 0);
console.log(evens); // [2, 4, 6]
```

**Example 2: students who passed**

```javascript
const students = [
  { name: "Asha", marks: 85 },
  { name: "Ravi", marks: 32 },
  { name: "Meena", marks: 91 }
];

const passed = students.filter((s) => s.marks >= 40);
console.log(passed);
// [{ name: "Asha", marks: 85 }, { name: "Meena", marks: 91 }]
```

**Example 3: search by text**

```javascript
const fruits = ["apple", "banana", "avocado", "mango"];
const startsWithA = fruits.filter((f) => f.startsWith("a"));
console.log(startsWithA); // ["apple", "avocado"]
```

> 💡 **Tip**
>
> The callback of `filter` must return **true or false**. True means keep, false means drop.

---

### ➕ 5. `reduce()`: Combine Everything into One Value

**Purpose:** Goes through the array and **reduces it to a single value**: a number, a string, an object, anything.

**Syntax:**

```javascript
const result = array.reduce((accumulator, currentItem) => {
  return /* updated accumulator */;
}, initialValue);
```

| Part | Meaning |
|---|---|
| `accumulator` (acc) | The running result, like a snowball ⛄ that grows |
| `currentItem` | The item being looked at right now |
| `initialValue` | The starting value of the accumulator |

**Example 1: sum of numbers**

```javascript
const numbers = [10, 20, 30, 40];
const sum = numbers.reduce((acc, n) => acc + n, 0);
console.log(sum); // 100
```

**Let's trace it step by step:**

| Step | `acc` (before) | `n` (current) | Returns (`acc + n`) |
|---|---|---|---|
| 1 | 0 (initial) | 10 | 10 |
| 2 | 10 | 20 | 30 |
| 3 | 30 | 30 | 60 |
| 4 | 60 | 40 | **100** ✅ |

**Example 2: find the maximum**

```javascript
const scores = [45, 90, 67, 82];
const highest = scores.reduce((max, s) => (s > max ? s : max), scores[0]);
console.log(highest); // 90
```

**Example 3: total price of a cart**

```javascript
const cart = [
  { item: "Pizza", price: 299, qty: 1 },
  { item: "Bread", price: 129, qty: 2 },
  { item: "Drink", price: 60,  qty: 3 }
];

const total = cart.reduce((acc, p) => acc + p.price * p.qty, 0);
console.log(total); // 737
```

**Example 4: count occurrences**

```javascript
const votes = ["A", "B", "A", "C", "A", "B"];
const count = votes.reduce((acc, v) => {
  acc[v] = (acc[v] || 0) + 1;
  return acc;
}, {});
console.log(count); // { A: 3, B: 2, C: 1 }
```

> ⚠️ **Important**
>
> **Always provide the `initialValue`** (like `0`). Without it, `reduce` uses the first array item as the start, and on an **empty array** it throws an error.

---

### 🔗 6. Chaining: Using Them Together

Since `map` and `filter` return arrays, you can **chain** methods one after another. This is where the real power shows up. ⚡

**Problem:** From a list of students, find the **total marks of those who passed**.

```javascript
const students = [
  { name: "Asha", marks: 85 },
  { name: "Ravi", marks: 32 },
  { name: "Meena", marks: 91 },
  { name: "Kiran", marks: 38 }
];

const totalOfPassed = students
  .filter((s) => s.marks >= 40)       // keep only passed students
  .map((s) => s.marks)                // pick just the marks → [85, 91]
  .reduce((acc, m) => acc + m, 0);    // add them up

console.log(totalOfPassed); // 176
```

**Flow of data:**

```
 students (4 objects)
      │  filter (marks >= 40)
      ▼
 [Asha, Meena]              (2 objects)
      │  map (get marks)
      ▼
 [85, 91]                   (2 numbers)
      │  reduce (sum)
      ▼
 176                        (1 number)
```

---

### 🆚 7. `for` Loop vs `map/filter/reduce`

Same task, two styles: **double the even numbers**.

```javascript
const nums = [1, 2, 3, 4, 5, 6];

// Using a for loop
const result1 = [];
for (let i = 0; i < nums.length; i++) {
  if (nums[i] % 2 === 0) {
    result1.push(nums[i] * 2);
  }
}

// Using filter + map
const result2 = nums.filter((n) => n % 2 === 0).map((n) => n * 2);

console.log(result1); // [4, 8, 12]
console.log(result2); // [4, 8, 12]
```

| Aspect | `for` loop | `map/filter/reduce` |
|---|---|---|
| Code length | Longer | Shorter |
| Readability | Describes **how** | Describes **what** you want |
| Changes original array? | Depends on you | **No**, returns a new value |
| Can use `break`? | ✅ Yes | ❌ No |

---

### 🧰 8. Quick Cheat Sheet

| Method | Input array of N items | Returns | Use when you want to... |
|---|---|---|---|
| `map` | N items | **Array of N items** | Transform each item |
| `filter` | N items | **Array of 0 to N items** | Keep only matching items |
| `reduce` | N items | **One single value** | Combine into a total, max, count, etc. |
| `forEach` | N items | Nothing (`undefined`) | Just do something for each item (like printing) |

> 💡 **Tip**
>
> Don't use `map` just to print things. Use `forEach` for that. `map` is for **creating a new array**.

---

## 💡 Real-Life Analogy

🏭 **Think of a juice factory:**

- **`map`** is the **machine that peels and cuts every fruit**. 100 fruits go in, and 100 cut fruits come out. Each one is transformed.
- **`filter`** is the **quality checker** 🔍 standing at the conveyor belt who **removes rotten fruits**. 100 go in, maybe 90 come out.
- **`reduce`** is the **juicer** 🧃 that **squeezes all fruits into one glass of juice**. Many go in, one comes out.

And **chaining** is the whole factory line: check quality, cut the fruit, then squeeze the juice.

---

## 💻 Real-World Application

| Where | Which method | How |
|---|---|---|
| 🛒 **Amazon price filter** | `filter` | Show only products between ₹500 and ₹1000 |
| 🛍️ **Currency conversion** | `map` | Convert all prices from USD to INR |
| 🧾 **Cart total** | `reduce` | Add price x quantity of all items |
| 🎵 **Spotify "Liked songs"** | `filter` | Songs where `liked === true` |
| 📱 **Instagram feed** | `map` | Turn each post object into a visible card on the page |
| 📊 **Dashboards** | `reduce` | Total sales, average rating, count per category |
| ⚛️ **React apps** | `map` | Render lists of components (extremely common!) |

---

## 🔍 Industry Example

📘 **Scenario: An e-commerce analyst preparing a sales report**

The server sends today's orders as an array of objects:

```javascript
const orders = [
  { id: 1, customer: "Asha",  amount: 1200, status: "delivered" },
  { id: 2, customer: "Ravi",  amount: 450,  status: "cancelled" },
  { id: 3, customer: "Meena", amount: 2300, status: "delivered" },
  { id: 4, customer: "Kiran", amount: 800,  status: "delivered" },
  { id: 5, customer: "Sana",  amount: 150,  status: "cancelled" }
];

// 1) Revenue from delivered orders only
const revenue = orders
  .filter((o) => o.status === "delivered")
  .reduce((sum, o) => sum + o.amount, 0);

// 2) Names of customers with big orders (> ₹1000)
const bigSpenders = orders
  .filter((o) => o.amount > 1000)
  .map((o) => o.customer);

// 3) Amount after 18% GST for each order
const withGST = orders.map((o) => ({ ...o, amount: o.amount * 1.18 }));

console.log(revenue);      // 4300
console.log(bigSpenders);  // ["Asha", "Meena"]
```

**What happens internally:**

1. 📥 The data arrives from the server as JSON and becomes an array of objects.
2. 🔍 `filter` creates a **new array** with only delivered orders (3 items).
3. ➕ `reduce` walks through those 3 orders, adding their amounts: 1200 + 2300 + 800 = **4300**.
4. 🔄 `map` creates a **new array** where every order has the GST-added amount. The original `orders` array stays untouched.
5. 📊 These results feed charts and numbers on the company's dashboard.

---

## 📊 Diagram

```
                    map()  🔄
        transforms EACH item → same length

   [ 1 ,  2 ,  3 ,  4 ]
      │    │    │    │
    (x2) (x2) (x2) (x2)
      ▼    ▼    ▼    ▼
   [ 2 ,  4 ,  6 ,  8 ]


                  filter()  🔍
        keeps items where condition is TRUE

   [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ]
      ✖    ✔    ✖    ✔    ✖    ✔     (is it even?)
   [      2 ,       4 ,       6 ]


                 reduce()  ➕
        combines everything into ONE value

   [ 10 , 20 , 30 , 40 ]
      │
   acc=0 ──(+10)──► 10 ──(+20)──► 30 ──(+30)──► 60 ──(+40)──► 100
                                                              ▲
                                                       final result


             🏭 CHAINING THE PIPELINE

   data ──► filter ──► map ──► reduce ──► answer
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`map` changes the original array." | `map` returns a **new** array. The original stays unchanged. |
| "I forgot `return` and my `map` gives `[undefined, ...]`." | With curly braces `{ }` you **must** write `return`. Without braces, the arrow function returns automatically. |
| "`filter` can transform items." | `filter` only **selects**. Use `map` to change items. |
| "`reduce` always returns an array." | It returns **any single value**: number, string, object, array. |
| "I can skip the initial value in `reduce`." | It's risky. On an empty array it throws an error. Always give it. |
| "Use `map` to just print items." | Use `forEach` for side effects like printing. |
| "`filter` returns one item." | It always returns an **array**, even if it has one item or none. Use `find()` for a single item. |
| "I forgot to return `acc` inside `reduce`." | The callback **must return the accumulator** every time, or the next step gets `undefined`. |

---

## 💬 Interview Corner

**Q1. What is the difference between `map()` and `forEach()`?**
`map()` returns a **new array** with transformed items. `forEach()` just runs a function for each item and returns nothing (`undefined`).

**Q2. What does `filter()` return if no items match?**
An **empty array** `[]`, not `undefined` or an error.

**Q3. Explain how `reduce()` works.**
It runs a callback on each item with an accumulator that holds the running result. After the last item, the accumulator becomes the final single value. We pass an initial value to start it.

**Q4. Do `map`, `filter`, and `reduce` modify the original array?**
No. They return new values and leave the original array unchanged, which makes code safer and more predictable.

---

## 📝 Quick Summary

- 🔄 **`map`**: transforms every item and returns a new array of the **same length**.
- 🔍 **`filter`**: keeps only the items that pass a true/false test and returns a **shorter (or equal) array**.
- ➕ **`reduce`**: combines all items into **one value** using an accumulator and an initial value.
- 📞 All three take a **callback function** as input.
- ➡️ **Arrow functions** (`n => n * 2`) make callbacks short and neat.
- 🔗 You can **chain** them: `filter().map().reduce()`.
- 🛡️ They **do not change** the original array.
- 🆚 Use `forEach` to just do something and `map` to produce a new array.
- 🧠 Always remember `return` inside callbacks with `{ }` braces.

---

## 🎯 Class Activity

**🛠️ Activity: "Shop Analyzer"**

Use this data in your console or a `.js` file:

```javascript
const products = [
  { name: "Laptop",   price: 55000, category: "electronics" },
  { name: "Shirt",    price: 899,   category: "clothing" },
  { name: "Phone",    price: 20000, category: "electronics" },
  { name: "Jeans",    price: 1499,  category: "clothing" },
  { name: "Earbuds",  price: 1999,  category: "electronics" }
];
```

Solve each task using `map`, `filter`, or `reduce`:

1. Get an array of **only the product names**.
2. Get only the **electronics** products.
3. Find the **total price** of all products.
4. Create a new array where every price has a **10% discount**.
5. **Challenge:** Find the total price of **only the clothing** items using chaining.

Compare your answers with your neighbor and explain **why** you chose each method.

---

# 📋 Assignments — Intro to Array Methods: `map`, `filter`, `reduce`

| Assignment |
|---|
| Given `[1, 2, 3, 4, 5]`, use `map()` to create a new array with the square of each number. |
| Given an array of names in lowercase, use `map()` to produce an array with each name capitalized (first letter uppercase). |
| Given an array of temperatures in Celsius, use `map()` to convert all of them to Fahrenheit (`C * 9/5 + 32`). |
| Given an array of student objects, use `map()` to create an array containing only their names. |
| Use `filter()` to get all numbers greater than 10 from `[5, 12, 8, 130, 44]`. |
| Use `filter()` to get all words with more than 4 letters from an array of words. |
| Given an array of product objects, use `filter()` to find products priced below ₹1000. |
| Use `filter()` to remove all falsy values (`0`, `""`, `null`, `undefined`, `false`) from a mixed array. |
| Use `reduce()` to find the sum of all numbers in an array. |
| Use `reduce()` to find the largest number in an array. |
| Use `reduce()` to calculate the total cost of a cart where each item has `price` and `qty`. |
| Use `reduce()` to count how many times each word appears in an array of words. |
| Use chaining to get the sum of squares of only the even numbers in `[1, 2, 3, 4, 5, 6]`. |
| Given an array of student objects with marks, use chaining to find the **average marks of students who passed** (marks ≥ 40). |
| Solve the same problem (doubling even numbers) with a `for` loop and with `filter` + `map`, and write two lines on which you find easier to read. |