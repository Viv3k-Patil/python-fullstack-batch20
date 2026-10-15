# 📚 DOM Tree Overview

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🌳 Explain what the DOM is and why browsers create it
- 🧱 Identify nodes, elements, text, and attributes in a page
- 👨‍👩‍👧 Describe parent, child, and sibling relationships
- 🔍 Inspect the DOM using browser DevTools
- 🧭 Understand the `document` object as the entry point to the page
- 🔁 Understand that JavaScript changes the DOM, not your HTML file

---

## 📖 Introduction

In earlier topics you wrote HTML and JavaScript separately. But how does JavaScript actually *reach into* a web page and change a heading or a button?

👉 Through the **DOM**.

**DOM** stands for **Document Object Model**. When a browser loads your HTML file, it does not keep it as plain text. It converts it into a **tree of objects** in memory. JavaScript can read and modify this tree, and the browser instantly updates what you see.

**Why does this topic exist?** HTML is just text. JavaScript cannot talk to text directly. The DOM turns every tag into an object that JavaScript can work with.

**Why is it important?** Everything interactive on the web (menus, form checks, likes, popups) works by changing the DOM.

**Where is it used?** Every interactive website you have ever used.

---

## 🧠 Detailed Notes

### 🌳 1. What is the DOM?

The DOM is a **live, tree-shaped representation** of your web page that the browser builds when the page loads.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>Welcome to <b>my</b> page</p>
  </body>
</html>
```

The browser turns this into a tree:

```
document
 └── html
      ├── head
      │    └── title
      │         └── "My Page"
      └── body
           ├── h1
           │    └── "Hello"
           └── p
                ├── "Welcome to "
                ├── b
                │    └── "my"
                └── " page"
```

> ℹ️ **Note**
>
> The DOM is **not** your HTML file. It is the browser's *living copy* built from your HTML. If JavaScript changes the DOM, your `.html` file on disk stays exactly the same.

---

### 🧱 2. Types of Nodes

Everything in the tree is a **node**. The most common types:

| Node type | What it is | Example |
|---|---|---|
| **Document node** | The very top of the tree | `document` |
| **Element node** | An HTML tag | `<h1>`, `<p>`, `<div>` |
| **Text node** | The text inside an element | `"Hello"` |
| **Attribute node** | Attributes of a tag | `id="title"`, `class="box"` |
| **Comment node** | HTML comments | `<!-- note -->` |

> 💡 **Tip**
>
> Even the **spaces and line breaks** between tags become text nodes. That is why some DOM properties give surprising results.

---

### 👨‍👩‍👧 3. Family Relationships in the Tree

The tree uses family words:

| Term | Meaning | Example in our page |
|---|---|---|
| **Parent** | The element directly above | `body` is the parent of `h1` |
| **Child** | An element directly inside | `h1` and `p` are children of `body` |
| **Sibling** | Elements at the same level with the same parent | `h1` and `p` are siblings |
| **Ancestor** | Any element above (parent, grandparent...) | `html` is an ancestor of `b` |
| **Descendant** | Any element below | `b` is a descendant of `body` |

JavaScript lets you move around the family:

```javascript
const heading = document.querySelector("h1");

console.log(heading.parentElement);          // <body>
console.log(heading.nextElementSibling);     // <p>
console.log(document.body.children);         // HTMLCollection of body's children
console.log(document.body.firstElementChild);// <h1>
```

🤔 **Quick thinking question:** In the tree above, what is the parent of the `<b>` element?

✅ **Answer:** The `<p>` element, because `<b>` sits directly inside it.

---

### 🚪 4. The `document` Object

`document` is the **front door** to the DOM. Every DOM task starts from it.

```javascript
console.log(document.title);        // "My Page"
console.log(document.URL);          // the page address
console.log(document.body);         // the <body> element
console.log(document.head);         // the <head> element
console.log(document.documentElement); // the <html> element
```

Changing the page title:

```javascript
document.title = "Changed by JavaScript! 🎉";
```

---

### 🔍 5. Inspecting the DOM with DevTools

1. Open any web page in Chrome.
2. Press **F12** (or right-click, then **Inspect**).
3. Open the **Elements** tab. You are looking at the **live DOM**.
4. Click any element in the tree. You will see its attributes and styles.
5. Double-click a piece of text and change it. The page updates instantly. (This is a change to the DOM only, not to the real website.)

> ⚠️ **Important**
>
> The **Elements** tab shows the **current DOM**, which may differ from "View Page Source". Page Source shows the original HTML text. Elements shows the tree after JavaScript has changed it.

---

### 🔗 6. How JavaScript and the DOM Work Together

```
  Your HTML file ──► Browser parses ──► DOM tree (objects)
                                             ▲   │
                                             │   ▼
                                   JavaScript reads / changes
                                             │
                                             ▼
                                  Browser repaints the screen
```

The DOM is a **bridge**: HTML on one side, JavaScript on the other.

---

### ⏱️ 7. When Is the DOM Ready?

JavaScript can only work with elements that **already exist** in the DOM. If your script runs before the browser has built them, selection fails.

Safe options (you learned these earlier):

```html
<script src="script.js" defer></script>
```

or place the script just before `</body>`. You can also wait explicitly:

```javascript
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM is fully built! ✅");
});
```

---

## 💡 Real-Life Analogy

🏛️ **The DOM is like a family tree on a wall.**

- Your HTML file is the **written list of family members** in a notebook.
- The DOM is the **big family tree chart** drawn from that list: grandparents at the top, children below, everyone connected by lines.
- JavaScript is a person with a **marker** who can add a new name, erase one, or change a name on the chart.
- The notebook (HTML file) stays the same. Only the **chart on the wall** (DOM) changes.

---

## 💻 Real-World Application

| Where | How the DOM is involved |
|---|---|
| 🔍 **Google search suggestions** | New suggestion items are added to the DOM as you type |
| 🛒 **Amazon cart** | Cart count in the header is updated in the DOM |
| 💬 **WhatsApp Web** | New messages are inserted as new DOM elements |
| 🧪 **Browser DevTools** | Directly display and edit the DOM |
| 🤖 **Automation tools (Selenium, Playwright)** | Find and click DOM elements for testing |
| ⚛️ **React / Vue** | Frameworks that manage the DOM for you efficiently |

---

## 🔍 Industry Example

📘 **Scenario: A QA engineer at an online bank debugs a missing button**

A customer complains: *"There is no 'Pay Now' button on my screen."* The developer says the HTML file contains the button.

The QA engineer opens **DevTools, Elements tab** and finds:

1. 🌳 The button element **exists in the HTML source** but is **missing from the live DOM**.
2. 🔎 She finds that a JavaScript function runs after the page loads and **removes** elements for users with a blocked account.
3. 🐞 The bug is in the JavaScript condition, not in the HTML.

Because she compared the **page source** (original text) with the **live DOM** (current tree), she found the cause in minutes. This is why understanding the DOM is a core professional skill.

---

## 📊 Diagram

```
                     document
                        │
                      <html>
                 ┌──────┴──────┐
              <head>         <body>
                │         ┌─────┼────────┐
            <title>     <h1>   <p>     <button>
                │         │     │  
            "My Page"  "Hello" "Welcome"


   Relationships (looking from <h1>)

        <body>  ◄── parent
          │
   ┌──────┼──────┐
 <h1>    <p>   <button>
  ▲       ▲
  │       └── next sibling
  └── current element


   JS ──► reads/changes DOM ──► Screen updates instantly
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "The DOM is my HTML file." | The DOM is the browser's **in-memory tree** built from the HTML. |
| "JavaScript changes my `.html` file." | It only changes the live DOM. Refresh and everything resets. |
| "The DOM and 'View Page Source' show the same thing." | Source is the original text. The DOM is the current state. |
| "DOM is part of JavaScript." | The DOM is a **browser API**. JavaScript is simply the language used to access it. |
| "Whitespace between tags doesn't matter in the DOM." | It creates text nodes, which can affect properties like `childNodes`. |
| "I can use the DOM before the page loads." | Elements must exist first. Use `defer` or `DOMContentLoaded`. |

---

## 💬 Interview Corner

**Q1. What is the DOM?**
The Document Object Model is a tree-like, in-memory representation of an HTML page that lets JavaScript read and change the page's content, structure, and style.

**Q2. Is the DOM the same as the HTML source?**
No. The HTML source is text. The DOM is a live object tree built from it, which JavaScript can modify.

**Q3. What are the main node types in the DOM?**
Document, element, text, attribute, and comment nodes.

**Q4. What is the `document` object?**
The root entry point of the DOM. Through it, we access elements, the title, the body, and more.

---

## 📝 Quick Summary

- 🌳 The **DOM** is a tree of objects the browser creates from your HTML.
- 🚪 `document` is the entry point to the whole tree.
- 🧱 Everything is a **node**: elements, text, attributes, comments.
- 👨‍👩‍👧 Elements have **parent, child, and sibling** relationships.
- 🔍 DevTools **Elements** tab shows the live DOM.
- 🔄 JavaScript changes the DOM, and the screen updates immediately.
- 💾 Your HTML file on disk is **not** changed.
- ⏱️ Scripts must run **after** the DOM elements exist (`defer` or `DOMContentLoaded`).

---

## 🎯 Class Activity

**🛠️ Activity: "Explore the tree"**

1. Create `index.html` with a heading, two paragraphs, and a list of three items.
2. Open it in Chrome and press **F12**, then the **Elements** tab.
3. Draw the DOM tree on paper for your page.
4. In the **Console**, run these and note the output:

```javascript
document.title
document.body.children
document.querySelector("h1").parentElement
document.querySelector("ul").children.length
```

5. In the Elements tab, double-click a paragraph and edit its text. Refresh and observe what happens.

---

# 📋 Assignments — DOM Tree Overview

| Assignment |
|---|
| Create an HTML page with at least 6 different tags and draw its DOM tree on paper. |
| Open any website, inspect it, and list five element nodes you can see in the Elements tab. |
| Use the console to print `document.title`, `document.URL`, and `document.body` for your own page. |
| Change `document.title` of any website from the console and take a screenshot. |
| For your own page, identify the parent, a child, and a sibling of a chosen element and print each in the console. |
| Print the number of children of `<body>` using `document.body.children.length`. |
| Compare "View Page Source" and the Elements tab for a website. Write down one difference you notice. |
| Edit text on a news website using DevTools, refresh, and explain in two lines why it reset. |
| Use `firstElementChild` and `lastElementChild` on a list (`<ul>`) and print both. |
| Add an HTML comment to your page and find it in the Elements tab. Write what type of node it is. |
| Write a short explanation (5 lines) of the DOM using your own analogy. |

---
---

# 📚 Selecting Elements: `getElementById` and `querySelector`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- 🎯 Select a single element using `getElementById` and `querySelector`
- 📦 Select multiple elements using `querySelectorAll`, `getElementsByClassName`, and `getElementsByTagName`
- 🧩 Write CSS selectors (id, class, tag, attribute, nested) for selection
- 🔁 Loop through a list of selected elements
- ⚖️ Choose the right selection method for the right job
- 🐞 Fix common `null` and "not a function" errors

---

## 📖 Introduction

Before JavaScript can change a button, a heading, or an input box, it must first **find** it in the DOM. This step is called **selecting elements**.

**Why does this topic exist?** A page can have hundreds of elements. You need a way to point at exactly the one (or the few) you want.

**Why is it important?** Every DOM task begins with selection. If you select the wrong thing, or nothing at all, nothing else works.

**Where is it used?** Reading form values, showing and hiding menus, updating counters, validating inputs: everything.

---

## 🧠 Detailed Notes

We will use this HTML throughout:

```html
<h1 id="title">Hotel Paradise 🏨</h1>
<p class="info">Free Wi-Fi</p>
<p class="info">Free Breakfast</p>
<ul id="rooms">
  <li class="room">Standard</li>
  <li class="room premium">Deluxe</li>
  <li class="room premium">Suite</li>
</ul>
<input type="text" name="guest" placeholder="Your name">
<button class="btn" id="book">Book Now</button>
```

### 🆔 1. `getElementById()`

Selects the **one** element with a matching `id`.

```javascript
const title = document.getElementById("title");
console.log(title);              // <h1 id="title">...</h1>
console.log(title.innerText);    // Hotel Paradise 🏨
```

- Pass the id **without** `#`.
- Returns the element, or **`null`** if not found.
- IDs should be **unique** on a page.

> 💡 **Tip**
>
> `getElementById` is very fast and very readable. Use it when you have a unique id.

---

### 🎯 2. `querySelector()`

Selects the **first** element that matches any **CSS selector**.

```javascript
document.querySelector("h1");            // by tag
document.querySelector("#title");        // by id (note the #)
document.querySelector(".info");         // by class (note the .), first match only
document.querySelector("ul li");         // nested: li inside ul, first match
document.querySelector("input[name='guest']"); // by attribute
document.querySelector(".room.premium"); // has BOTH classes
```

Returns the element, or **`null`** if nothing matches.

**Cheat sheet of selector syntax:**

| Selector | Meaning | Example |
|---|---|---|
| `tag` | By tag name | `"p"` |
| `#id` | By id | `"#title"` |
| `.class` | By class | `".info"` |
| `parent child` | Descendant | `"ul li"` |
| `parent > child` | Direct child only | `"ul > li"` |
| `[attr='value']` | By attribute | `"input[type='text']"` |
| `:first-child` / `:last-child` | By position | `"li:last-child"` |
| `a, b` | Either one | `"h1, h2"` |

---

### 📦 3. `querySelectorAll()`

Selects **all** matching elements and returns a **NodeList** (a list-like collection).

```javascript
const infos = document.querySelectorAll(".info");
console.log(infos.length);   // 2
console.log(infos[0]);       // first <p class="info">

// Loop with forEach
infos.forEach((p) => {
  console.log(p.innerText);
});

// Or for...of
for (const room of document.querySelectorAll(".room")) {
  console.log(room.innerText);
}
```

If nothing matches, you get an **empty NodeList** (not `null`).

---

### 🏷️ 4. Older Methods (Good to Know)

```javascript
const byClass = document.getElementsByClassName("room");   // HTMLCollection
const byTag   = document.getElementsByTagName("li");       // HTMLCollection
const byName  = document.getElementsByName("guest");       // NodeList
```

> ⚠️ **Important**
>
> `getElementsByClassName` and `getElementsByTagName` return an **HTMLCollection**, which has **no `forEach`**. Convert it first: `Array.from(byClass).forEach(...)` or `[...byClass]`. Or simply use `querySelectorAll`.

---

### ⚖️ 5. Which One Should I Use?

| Method | Returns | If not found | Best for |
|---|---|---|---|
| `getElementById("x")` | 1 element | `null` | Unique elements with an id |
| `querySelector("sel")` | 1 element (first match) | `null` | Flexible selection of one element |
| `querySelectorAll("sel")` | NodeList (all matches) | Empty list | Many elements, with `forEach` |
| `getElementsByClassName("x")` | HTMLCollection (live) | Empty collection | Legacy code |
| `getElementsByTagName("x")` | HTMLCollection (live) | Empty collection | Legacy code |

> 💡 **Tip**
>
> A common modern habit: use `getElementById` for ids and `querySelector` / `querySelectorAll` for everything else.

🤔 **Quick thinking question:** `document.querySelector(".info")` is used on a page with 5 elements having class `info`. How many elements come back?

✅ **Answer:** **One**, the first match. Use `querySelectorAll` to get all five.

---

### 🔎 6. Selecting Inside an Element

You can search **within** an element, not just the whole document.

```javascript
const list = document.getElementById("rooms");
const premiumRooms = list.querySelectorAll(".premium");
console.log(premiumRooms.length);   // 2
```

This keeps searches fast and avoids picking elements from other parts of the page.

---

### 🏗️ 7. Storing Elements in Variables

Selecting is a bit of work. Select **once**, store it in a `const`, and reuse it.

```javascript
const bookBtn = document.getElementById("book");
const guestInput = document.querySelector("input[name='guest']");

console.log(bookBtn.innerText);      // Book Now
console.log(guestInput.value);       // whatever is typed
```

---

### 🐞 8. Common Errors and What They Mean

| Error | Reason |
|---|---|
| `Cannot read properties of null (reading 'innerText')` | The element was **not found** (typo in id or script ran too early) |
| `x.forEach is not a function` | `x` is an HTMLCollection. Convert it or use `querySelectorAll` |
| `Uncaught SyntaxError: ... is not a valid selector` | Selector typo, such as a missing quote or bracket |
| Nothing happens, no error | Possibly selected the wrong element, or forgot the `#` or `.` in `querySelector` |

> ℹ️ **Note**
>
> Debug tip: `console.log(yourElement)`. If it prints `null`, selection failed. Check spelling, `#`/`.` usage, and script placement.

---

## 💡 Real-Life Analogy

🏢 **Finding people in a large office building:**

- **`getElementById`** is calling someone by their **employee ID**. It is unique, so you get exactly one person.
- **`querySelector`** is asking reception: *"Find me the **first** person in the Marketing department."*
- **`querySelectorAll`** is asking: *"Give me the **list of everyone** in Marketing."*
- Searching **inside an element** is like searching only **one floor** instead of the whole building.

If the ID doesn't exist, the receptionist replies "nobody found" (`null`), and trying to talk to nobody causes an error!

---

## 💻 Real-World Application

| Where | Selection used for |
|---|---|
| 📝 **Sign-up forms** | Select inputs to read what the user typed |
| 🍔 **Hamburger menus** | Select the menu element to show or hide it |
| 🛒 **Add-to-cart buttons** | `querySelectorAll(".add-btn")` to attach click actions to every button |
| 🌗 **Dark mode toggle** | Select `body` and switch a class |
| 🔔 **Notification badges** | Select a badge element to update the number |
| 🧪 **Automated testing** | Tools select elements with the same CSS selectors |

---

## 🔍 Industry Example

📘 **Scenario: "Add to Cart" buttons on a product listing page**

A product page shows 20 products, each with a button:

```html
<button class="add-btn" data-id="101">Add to Cart</button>
<button class="add-btn" data-id="102">Add to Cart</button>
<!-- ... 18 more ... -->
<span id="cart-count">0</span>
```

The developer writes:

```javascript
const cartCount = document.getElementById("cart-count");
const buttons = document.querySelectorAll(".add-btn");
let count = 0;

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    count++;
    cartCount.innerText = count;
    console.log("Added product", btn.dataset.id);
  });
});
```

**What happens internally:**

1. 🔍 `getElementById` finds the single cart counter.
2. 📦 `querySelectorAll(".add-btn")` returns all 20 buttons as a list.
3. 🔁 `forEach` visits each button and attaches a click action.
4. 🖱️ When a user clicks any button, the counter in the header goes up.

Selecting the right elements the right way lets **one small script** handle all 20 buttons.

---

## 📊 Diagram

```
        Which selection method?

            How many elements do I need?
                    │
          ┌─────────┴──────────┐
        ONE                  MANY
          │                    │
   Has a unique id?      querySelectorAll(".class")
     │         │          returns NodeList
    YES        NO         (loop with forEach)
     │         │
getElementById  querySelector("css selector")
("title")       returns first match or null


   Selector syntax at a glance

   "h1"          → by TAG
   "#title"      → by ID
   ".info"       → by CLASS
   "ul li"       → NESTED
   "input[name='guest']" → ATTRIBUTE
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`getElementById('#title')` works." | No `#` with `getElementById`. Use `getElementById("title")`. |
| "`querySelector('title')` finds the id." | Without `#` it searches for a `<title>` **tag**. Use `"#title"`. |
| "`querySelector('.info')` returns all `.info` elements." | It returns only the **first**. Use `querySelectorAll`. |
| "HTMLCollection has `forEach`." | It doesn't. Convert it to an array or use `querySelectorAll`. |
| "A missing element gives an empty result." | `getElementById` and `querySelector` return **`null`**, which crashes if you use it. |
| "I can select before the element exists." | Scripts must run after the DOM is ready. |
| "Selecting repeatedly inside a loop is fine." | Select once, store in a `const`, and reuse. |

---

## 💬 Interview Corner

**Q1. What is the difference between `querySelector` and `querySelectorAll`?**
`querySelector` returns only the first matching element (or `null`). `querySelectorAll` returns a NodeList of all matching elements (empty if none).

**Q2. What does `getElementById` return if the id doesn't exist?**
`null`.

**Q3. What is the difference between NodeList and HTMLCollection?**
Both are list-like collections of nodes. A NodeList from `querySelectorAll` supports `forEach` and is static. An HTMLCollection from `getElementsByClassName` has no `forEach` and is live (it updates automatically when the DOM changes).

**Q4. How can you search for elements only inside a certain element?**
Call the method on that element instead of `document`, for example `list.querySelectorAll(".premium")`.

---

## 📝 Quick Summary

- 🎯 You must **select** an element before you can change it.
- 🆔 `getElementById("id")` returns one element and is written **without** `#`.
- 🎯 `querySelector("css")` returns the **first** match and uses CSS syntax (`#id`, `.class`, `tag`).
- 📦 `querySelectorAll("css")` returns **all** matches as a NodeList and supports `forEach`.
- 🏷️ `getElementsByClassName` and `getElementsByTagName` return HTMLCollections (no `forEach`).
- 🔎 You can search **inside** an element for faster, more targeted selection.
- ❓ Not found means `null` for single selectors and an empty list for multiple.
- 🏗️ Select once, store in a `const`, and reuse.

---

## 🎯 Class Activity

**🛠️ Activity: "Selector Treasure Hunt"**

Use the hotel HTML from this topic. In the console or a script file, write code to:

1. Print the text of the `<h1>`.
2. Print how many elements have the class `info`.
3. Print the text of every `.room` using `querySelectorAll` and `forEach`.
4. Select only the **premium** rooms and print their count.
5. Select the input by its `name` attribute and print its placeholder.
6. Try `document.getElementById("wrong")` and note what you get. Then try `.innerText` on it and note the error.

---

# 📋 Assignments — Selecting Elements

| Assignment |
|---|
| Create a page with a heading, three paragraphs (same class), and a button. Select each using `getElementById`, `querySelector`, and `querySelectorAll`. |
| Print the text of every paragraph with a given class using `querySelectorAll` and `forEach`. |
| Select the first and last `<li>` of a list using `querySelector` with `:first-child` and `:last-child`. |
| Use `getElementsByClassName` to select elements and convert the result to an array. Print its length. |
| Demonstrate `getElementById` returning `null` by using a wrong id. Explain the error you get when using it. |
| Select an input by its `name` attribute and print its `type` and `placeholder`. |
| Use `parent > child` and `parent child` selectors on a nested list and explain the difference. |
| Select all elements that have **two** classes at once (for example `.room.premium`). |
| Use `list.querySelectorAll("li")` to select only items inside a specific list when your page has two lists. |
| Select every `<a>` tag on a real website using the console and print the total number of links. |
| Select all `<img>` tags on a website and print each one's `alt` text (or empty if missing). |
| Write a short table in your notebook comparing five selection methods: return type and what happens if not found. |

---
---

# 📚 Manipulating Content: `innerText`, `innerHTML`, and `classList`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- ✏️ Change text on a page with `innerText` and `textContent`
- 🧱 Insert HTML with `innerHTML` and understand its risks
- 🎨 Add, remove, and toggle CSS classes using `classList`
- 🖌️ Change styles and attributes with JavaScript
- ➕ Create, add, and remove elements dynamically
- 🔐 Understand why untrusted user input must never go into `innerHTML`

---

## 📖 Introduction

You can now find elements. The next step is **changing** them: updating text, showing a message, turning a button red, or adding a new row to a table.

**Why does this topic exist?** Static pages cannot react. Changing content with JavaScript is what makes a page feel alive.

**Why is it important?** Error messages, success banners, live counters, toggled menus, dark mode: all of these are content and class changes.

**Where is it used?** In every interactive feature you see on websites, including the **hotel booking form** we will build in the last topic.

---

## 🧠 Detailed Notes

We will use this HTML:

```html
<h2 id="msg">Welcome</h2>
<div id="box" class="card">Hello Guest</div>
<ul id="list"></ul>
<img id="pic" src="room1.jpg" alt="Room">
```

### 📝 1. `innerText` and `textContent`

Read or change the **text** of an element.

```javascript
const msg = document.getElementById("msg");

console.log(msg.innerText);   // Welcome
msg.innerText = "Booking Confirmed ✅";
```

| Property | Behavior |
|---|---|
| `innerText` | Gives the **visible** text, respecting CSS (hidden text is ignored) |
| `textContent` | Gives **all** text, including hidden text, and is slightly faster |

Both treat what you assign as **plain text**. If you assign `"<b>Hi</b>"`, the user will literally see the tags, not bold text. This is **safe**.

```javascript
msg.innerText = "<b>Hi</b>";   // displays: <b>Hi</b>
```

---

### 🧱 2. `innerHTML`

Reads or sets the **HTML inside** an element. Tags you assign are **interpreted as real HTML**.

```javascript
const box = document.getElementById("box");

console.log(box.innerHTML);                 // Hello Guest
box.innerHTML = "<b>Hello</b> <i>Guest</i>"; // shows bold and italic text
```

Building a list quickly:

```javascript
const list = document.getElementById("list");
const rooms = ["Standard", "Deluxe", "Suite"];

list.innerHTML = "";   // clear first
rooms.forEach((r) => {
  list.innerHTML += `<li>${r}</li>`;
});
```

> ⚠️ **Important: security warning (XSS)**
>
> **Never put text typed by a user into `innerHTML`.** An attacker could type `<img src=x onerror="steal()">` and run harmful code on your page. For user text, always use **`innerText`** or **`textContent`**. Use `innerHTML` only for HTML **you wrote yourself**.

**Quick comparison:**

| Feature | `innerText` | `innerHTML` |
|---|---|---|
| Treats value as | Plain text | HTML code |
| Can insert tags | ❌ No | ✅ Yes |
| Safe for user input | ✅ Yes | ❌ No |
| Typical use | Messages, labels, errors | Inserting structured markup you control |

🤔 **Quick thinking question:** You want to display the guest's name (typed in a form) in a welcome message. Which should you use?

✅ **Answer:** `innerText` (or `textContent`), because user input must never be treated as HTML.

---

### 🎨 3. `classList`: The Right Way to Change Styles

Instead of writing styles in JavaScript, define styles in CSS **classes** and add or remove those classes.

**CSS:**

```css
.hidden   { display: none; }
.error    { color: red; border: 2px solid red; }
.success  { color: green; }
.dark     { background: #222; color: white; }
```

**JavaScript:**

```javascript
const box = document.getElementById("box");

box.classList.add("error");              // add a class
box.classList.remove("error");           // remove a class
box.classList.toggle("dark");            // add if missing, remove if present
console.log(box.classList.contains("card")); // true / false
box.classList.replace("card", "panel");  // swap one for another
```

| Method | What it does |
|---|---|
| `add("x")` | Adds class `x` (no duplicates) |
| `remove("x")` | Removes class `x` |
| `toggle("x")` | Switches class `x` on and off |
| `contains("x")` | Returns `true` or `false` |
| `replace("a", "b")` | Replaces class `a` with `b` |

> 💡 **Tip**
>
> Avoid `element.className = "..."`. It **overwrites all classes**. `classList` safely adds and removes **one at a time**.

**Example: show and hide with one class**

```javascript
const toggleBtn = document.getElementById("toggleBtn");
toggleBtn.addEventListener("click", () => {
  document.getElementById("box").classList.toggle("hidden");
});
```

---

### 🖌️ 4. Changing Styles Directly (`style`)

```javascript
box.style.color = "white";
box.style.backgroundColor = "teal";   // camelCase, not background-color
box.style.fontSize = "20px";
box.style.display = "none";
```

- CSS property names with hyphens become **camelCase**: `background-color` becomes `backgroundColor`.
- Use `style` for **quick one-off changes** and `classList` for **real projects**.

---

### 🏷️ 5. Attributes

```javascript
const pic = document.getElementById("pic");

console.log(pic.getAttribute("src"));     // room1.jpg
pic.setAttribute("src", "room2.jpg");     // change the image
pic.alt = "Deluxe room";                  // many attributes are also properties
pic.removeAttribute("alt");
console.log(pic.hasAttribute("alt"));     // false

// Disabling a button
document.getElementById("book").disabled = true;
```

**Custom data attributes:**

```html
<button id="b" data-room-id="205">Book</button>
```

```javascript
console.log(document.getElementById("b").dataset.roomId); // "205"
```

---

### ➕ 6. Creating, Adding, and Removing Elements

```javascript
// 1. Create
const li = document.createElement("li");

// 2. Fill
li.innerText = "Presidential Suite";
li.classList.add("room");

// 3. Add to the page
document.getElementById("list").appendChild(li);   // add at the end
// document.getElementById("list").prepend(li);    // add at the start

// 4. Remove
li.remove();                                       // remove this element
```

| Method | What it does |
|---|---|
| `createElement("tag")` | Makes a new element in memory (not visible yet) |
| `appendChild(el)` / `append(el)` | Adds at the end of the parent |
| `prepend(el)` | Adds at the start |
| `remove()` | Removes the element from the page |

> ℹ️ **Note**
>
> Creating with `createElement` and `innerText` is **safer** than building with `innerHTML` strings, especially when the content includes user data.

---

### 🧪 7. Reading and Writing Form Values

Form fields use **`value`**, not `innerText`.

```html
<input type="text" id="guestName">
```

```javascript
const input = document.getElementById("guestName");
console.log(input.value);          // what the user typed
input.value = "Asha";              // fill the field
input.value = "";                  // clear it
```

---

### 🧩 8. Putting It Together

```html
<input type="text" id="nameInput" placeholder="Enter name">
<button id="greetBtn">Greet</button>
<p id="greeting"></p>
```

```javascript
const nameInput = document.getElementById("nameInput");
const greetBtn = document.getElementById("greetBtn");
const greeting = document.getElementById("greeting");

greetBtn.addEventListener("click", () => {
  const name = nameInput.value.trim();
  if (name === "") {
    greeting.innerText = "Please enter your name";
    greeting.classList.add("error");
    greeting.classList.remove("success");
  } else {
    greeting.innerText = `Welcome, ${name}! 🎉`;
    greeting.classList.add("success");
    greeting.classList.remove("error");
  }
});
```

---

## 💡 Real-Life Analogy

🪧 **A whiteboard in a classroom:**

- **`innerText`** is **writing plain words** on the whiteboard: whatever you write is shown exactly as written.
- **`innerHTML`** is **handing the board painter a design sheet** (with colors and shapes). The painter follows it, which is powerful, but if a stranger hands you the sheet, who knows what they'll paint? That is why we never accept unchecked sheets from users.
- **`classList`** is **sticking labeled stickers** on a box: a "Fragile" sticker, a "Priority" sticker. You can peel stickers off or add them without rebuilding the box.
- **`createElement`** is **cutting a brand-new paper card**, writing on it, and then **pinning** it (`appendChild`) to the board.

---

## 💻 Real-World Application

| Where | Content manipulation used for |
|---|---|
| 🌗 **Dark mode** | `document.body.classList.toggle("dark")` |
| ❌ **Form error messages** | `innerText` to show the message, `classList` to turn the field red |
| 🔔 **Notification badge** | Update `innerText` of the counter |
| 📝 **To-do apps** | `createElement` and `appendChild` for each new task, `remove()` for deletes |
| 🛒 **Cart updates** | Update the item quantity and total text |
| 🍔 **Dropdown menus** | `classList.toggle("open")` |

---

## 🔍 Industry Example

📘 **Scenario: Live search results on a travel site**

A user types "Goa" in a hotel search box, and the server returns a list of hotels.

```javascript
const results = document.getElementById("results");
const hotels = [
  { name: "Sea View Resort", price: 4500 },
  { name: "Palm Beach Inn", price: 3200 }
];

results.innerHTML = "";   // clear old results

hotels.forEach((h) => {
  const card = document.createElement("div");
  card.classList.add("hotel-card");

  const title = document.createElement("h3");
  title.innerText = h.name;

  const price = document.createElement("p");
  price.innerText = `₹${h.price} / night`;

  card.append(title, price);
  results.appendChild(card);
});
```

**What happens internally:**

1. 🧹 The old results are cleared so they don't pile up.
2. 🏗️ For each hotel, JavaScript **creates** a card, a title, and a price element in memory.
3. ✏️ `innerText` fills them with data. Because hotel names come from a server, using `innerText` keeps it **safe**.
4. 🎨 The `hotel-card` class applies all the styling from CSS.
5. 📌 `appendChild` puts each card on the page, and the user instantly sees fresh results with no reload.

---

## 📊 Diagram

```
         CHANGING THE DOM

   const el = document.getElementById("box")
                    │
     ┌──────────────┼───────────────┬──────────────┐
     ▼              ▼               ▼              ▼
  TEXT           HTML            CLASSES        ELEMENTS
 innerText     innerHTML        classList      createElement
 textContent                    .add()         appendChild
 (safe ✅)     (careful ⚠️)     .remove()      .remove()
                                .toggle()


      innerText vs innerHTML

   el.innerText = "<b>Hi</b>"   →   shows:  <b>Hi</b>
   el.innerHTML = "<b>Hi</b>"   →   shows:  **Hi** (bold)


      Class toggle in action

   [ box ]  ──toggle("dark")──►  [ box.dark ]  ──toggle("dark")──►  [ box ]
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`innerHTML` is the best way to show any text." | For plain text, use `innerText` or `textContent`. They are safer. |
| "It's fine to put user input in `innerHTML`." | It can cause **XSS attacks**. Never do this with untrusted input. |
| "Use `innerText` to read an input's content." | Inputs use **`.value`**. |
| "`className = 'error'` just adds a class." | It **replaces all** existing classes. Use `classList.add`. |
| "`style.background-color` works." | Use camelCase: `style.backgroundColor`. |
| "`createElement` makes the element appear." | It creates it in memory. You must `appendChild` it. |
| "`innerHTML +=` in a big loop is fine." | It re-parses the HTML every time, which is slow and can remove event listeners. Build elements instead. |
| "`classList.add('.error')` with a dot." | No dot. Use `classList.add("error")`. |

---

## 💬 Interview Corner

**Q1. What is the difference between `innerText` and `innerHTML`?**
`innerText` reads or writes plain text and shows tags literally. `innerHTML` reads or writes HTML and interprets tags as real elements. `innerHTML` is risky with untrusted input.

**Q2. Why should we use `classList` instead of changing `style` directly?**
It keeps styling in CSS, makes code cleaner and reusable, and lets you add, remove, or toggle individual classes safely.

**Q3. What is the difference between `innerText` and `textContent`?**
`innerText` considers CSS visibility and returns only visible text. `textContent` returns all text, including hidden, and is a bit faster.

**Q4. How do you add a new element to a page using JavaScript?**
Create it with `document.createElement()`, set its content and classes, then add it using `appendChild()` or `append()` on a parent element.

---

## 📝 Quick Summary

- ✏️ `innerText` / `textContent` change **plain text** and are safe.
- 🧱 `innerHTML` inserts **real HTML** but is **dangerous with user input**.
- 🎨 `classList.add / remove / toggle / contains` is the **best way** to change appearance.
- 🖌️ `style.camelCaseProperty` is okay for quick one-off changes.
- 🏷️ `getAttribute`, `setAttribute`, and properties like `disabled` and `src` control attributes.
- ➕ `createElement`, `appendChild`, and `remove()` add and delete elements.
- 🧪 Form fields use **`.value`**.
- 🔐 Prefer `innerText` or `createElement` when data comes from users or servers.

---

## 🎯 Class Activity

**🛠️ Activity: "Mini To-Do List"**

Build this in `todo.html` and `script.js`:

1. An input box, an "Add" button, and an empty `<ul id="tasks">`.
2. When "Add" is clicked, read the input's `.value`.
3. If it's empty, do nothing.
4. Otherwise, create an `<li>` with `createElement`, set its text with `innerText`, and add it to the list.
5. Clear the input after adding.
6. **Bonus:** Add a "Dark Mode" button that toggles a `dark` class on `document.body`.

---

# 📋 Assignments — Manipulating Content

| Assignment |
|---|
| Change the text of a heading using `innerText` when a button is clicked. |
| Show the difference between `innerText` and `innerHTML` by assigning `"<b>Hello</b>"` to each of two different paragraphs. Explain what you see. |
| Create CSS classes `.error` and `.success` and use `classList` to apply the correct one to a message. |
| Build a "Show / Hide" button that toggles a `hidden` class on a paragraph. |
| Build a dark mode toggle that switches a `dark` class on `document.body`. |
| Use `classList.contains()` to print whether an element has a certain class, before and after adding it. |
| Change the `src` of an image when a button is clicked using `setAttribute`. |
| Disable a button using JavaScript after it has been clicked once. |
| Read the value of an input box and display it in a paragraph using `innerText`. |
| Create a list of 5 items from an array using `createElement` and `appendChild`. |
| Add a "Remove" feature: when any list item is clicked, remove it using `remove()`. |
| Change the style of a box (color, background, font size) using the `style` property. Then redo it using classes and compare. |
| Demonstrate why `innerHTML` with user input is unsafe (use the text `<img src=x>` in a safe test page) and write how to fix it. |
| Build a simple counter: a number display with "+" and "−" buttons that update the number's text. |

---
---

# 📚 Handling Events: `click`, `submit`, and `input`

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- ⚡ Explain what an event is and how events drive web pages
- 🖱️ Handle `click` events using `addEventListener`
- 📨 Handle form `submit` events and stop the default page reload
- ⌨️ Handle `input` (and related) events for live feedback
- 📦 Use the `event` object and `event.target`
- 🧩 Understand the basics of event delegation and bubbling

---

## 📖 Introduction

So far, our JavaScript ran immediately when the page loaded. But real pages **wait for the user**: they react when someone **clicks, types, or submits**.

An **event** is *something that happens* on a page: a click, a key press, a form submission, a mouse move, a page load.

**Why does this topic exist?** Without events, JavaScript would run once and stop. Events let your code **respond to the user**.

**Why is it important?** Every button, form, menu, and game depends on event handling.

**Where is it used?** Anywhere a user interacts: Like buttons, search boxes, login forms, shopping carts.

---

## 🧠 Detailed Notes

### ⚡ 1. What is an Event?

An **event** is a signal the browser sends when something happens. Your job is to say *"when this event happens on this element, run this function."*

That function is called an **event handler** (or **listener**).

Common events:

| Event | When it fires |
|---|---|
| `click` | An element is clicked |
| `submit` | A form is submitted |
| `input` | The value of an input changes (every keystroke) |
| `change` | A value is changed and committed (leaving a field, picking a select option) |
| `focus` / `blur` | A field gains or loses focus |
| `keydown` / `keyup` | A key is pressed or released |
| `mouseover` / `mouseout` | The mouse enters or leaves |
| `DOMContentLoaded` | The DOM has finished building |

---

### 🔌 2. `addEventListener()`: The Standard Way

**Syntax:**

```javascript
element.addEventListener("eventName", handlerFunction);
```

```html
<button id="btn">Click Me</button>
<p id="out"></p>
```

```javascript
const btn = document.getElementById("btn");
const out = document.getElementById("out");

btn.addEventListener("click", function () {
  out.innerText = "Button was clicked! 🎉";
});

// Same thing with an arrow function:
btn.addEventListener("click", () => {
  out.innerText = "Button was clicked! 🎉";
});
```

- You can add **multiple** listeners to the same element and event.
- Pass the **function itself**, not its result. Write `handler`, **not** `handler()`.

```javascript
function sayHi() { console.log("Hi!"); }

btn.addEventListener("click", sayHi);     // ✅ correct
btn.addEventListener("click", sayHi());   // ❌ runs immediately, passes undefined
```

**Other ways (less preferred):**

```html
<button onclick="sayHi()">Inline (avoid)</button>
```

```javascript
btn.onclick = sayHi;   // works, but only ONE handler allowed
```

> 💡 **Tip**
>
> Prefer `addEventListener`. It keeps HTML clean and allows multiple handlers.

---

### 🖱️ 3. The `click` Event

```javascript
let likes = 0;
const likeBtn = document.getElementById("likeBtn");
const count = document.getElementById("count");

likeBtn.addEventListener("click", () => {
  likes++;
  count.innerText = likes;
});
```

Attaching `click` to **many** elements:

```javascript
document.querySelectorAll(".room").forEach((room) => {
  room.addEventListener("click", () => {
    room.classList.toggle("selected");
  });
});
```

---

### 📦 4. The Event Object

The browser passes an **event object** to your handler, full of useful information.

```javascript
btn.addEventListener("click", (event) => {
  console.log(event.type);     // "click"
  console.log(event.target);   // the exact element that was clicked
  console.log(event.clientX, event.clientY);  // mouse position
});
```

Most useful parts:

| Property / Method | Meaning |
|---|---|
| `event.target` | The element that triggered the event |
| `event.type` | The event name (`"click"`, `"input"`...) |
| `event.preventDefault()` | Stops the browser's default action |
| `event.key` | For keyboard events, the key pressed |
| `event.stopPropagation()` | Stops the event from bubbling up |

---

### 📨 5. The `submit` Event (Forms)

A form's default behavior on submit is to **send data and reload the page**. With JavaScript we usually want to **check the data first**.

```html
<form id="loginForm">
  <input type="text" id="username" placeholder="Username">
  <button type="submit">Login</button>
</form>
<p id="status"></p>
```

```javascript
const form = document.getElementById("loginForm");
const status = document.getElementById("status");

form.addEventListener("submit", (event) => {
  event.preventDefault();               // ⛔ stop the page reload

  const username = document.getElementById("username").value.trim();

  if (username === "") {
    status.innerText = "Username is required ❌";
  } else {
    status.innerText = `Welcome, ${username}! ✅`;
  }
});
```

> ⚠️ **Important**
>
> Listen for **`submit` on the `<form>`**, not `click` on the button. This way, the handler also runs when the user presses **Enter** inside a field.

> ⚠️ **Important**
>
> Forgetting `event.preventDefault()` makes the page reload, and your message disappears instantly.

🤔 **Quick thinking question:** Why do we attach `submit` to the form instead of `click` on the submit button?

✅ **Answer:** Because forms can be submitted in more than one way (button click, pressing Enter). The `submit` event covers **all** of them.

---

### ⌨️ 6. The `input` Event (Live Feedback)

`input` fires **every time the value changes**, with every letter typed, pasted, or deleted.

```html
<input type="text" id="bio" maxlength="50" placeholder="Short bio">
<p id="counter">0 / 50</p>
```

```javascript
const bio = document.getElementById("bio");
const counter = document.getElementById("counter");

bio.addEventListener("input", () => {
  counter.innerText = `${bio.value.length} / 50`;
});
```

**Other useful field events:**

| Event | Fires when | Good for |
|---|---|---|
| `input` | Every change | Live character counters, search-as-you-type |
| `change` | Value committed (blur, select pick, checkbox toggle) | Dropdowns, checkboxes, date pickers |
| `blur` | User leaves the field | Validating a field after the user is done |
| `focus` | User enters the field | Clearing hints, highlighting |

```javascript
const roomType = document.getElementById("roomType");   // a <select>
roomType.addEventListener("change", () => {
  console.log("Selected:", roomType.value);
});
```

---

### 🫧 7. Event Bubbling (Beginner Level)

When you click an element, the event **bubbles up**: the element handles it first, then its parent, then its grandparent, and so on up to `document`.

```html
<div id="outer">
  <button id="inner">Click</button>
</div>
```

```javascript
document.getElementById("outer").addEventListener("click", () => {
  console.log("Outer heard it");
});
document.getElementById("inner").addEventListener("click", () => {
  console.log("Inner heard it");
});
// Clicking the button prints: "Inner heard it", then "Outer heard it"
```

---

### 🎯 8. Event Delegation (One Listener, Many Elements)

Instead of adding a listener to **every** list item, add **one** to the parent and check `event.target`. This also works for items **added later**.

```html
<ul id="roomList">
  <li>Standard</li>
  <li>Deluxe</li>
  <li>Suite</li>
</ul>
```

```javascript
document.getElementById("roomList").addEventListener("click", (event) => {
  if (event.target.tagName === "LI") {
    event.target.classList.toggle("selected");
  }
});
```

New `<li>` items added later automatically work, with no extra code.

---

### 🧹 9. Removing a Listener

```javascript
function handler() { console.log("Clicked"); }

btn.addEventListener("click", handler);
btn.removeEventListener("click", handler);   // must pass the SAME function
```

> ℹ️ **Note**
>
> Anonymous arrow functions cannot be removed this way because you have no reference to them. Give the function a name if you plan to remove it.

---

### ⌨️ 10. Keyboard Events (Bonus)

```javascript
document.addEventListener("keydown", (event) => {
  console.log("You pressed:", event.key);
  if (event.key === "Escape") {
    document.getElementById("modal").classList.add("hidden");
  }
});
```

---

## 💡 Real-Life Analogy

🔔 **Events are like a doorbell at your house.**

- The **event** is someone **pressing the bell** (click).
- The **event listener** is **you, waiting at home** and ready to respond.
- The **handler function** is **what you do** when the bell rings: open the door.
- The **event object** is the **peephole view**: it tells you **who** pressed it and **when**.
- **`preventDefault()`** is deciding *"I won't follow the usual routine of the delivery guy walking in"*, and handling things your own way.
- **Bubbling** is like the doorbell ringing in the **flat, then the floor, then the whole building**, with each level able to respond.

---

## 💻 Real-World Application

| Where | Event used |
|---|---|
| ❤️ **Instagram Like button** | `click` toggles the heart color and updates the count |
| 🔎 **Google search suggestions** | `input` triggers suggestion fetching as you type |
| 📝 **Signup forms** | `submit` runs validation before sending |
| 🔐 **Password strength meters** | `input` updates the strength bar live |
| 🎮 **Browser games** | `keydown` controls the character |
| 📅 **Date pickers and dropdowns** | `change` updates dependent fields |
| ❎ **Modal popups** | `click` on the background and `keydown` for Escape close the popup |

---

## 🔍 Industry Example

📘 **Scenario: Password strength meter on a signup page**

A signup page shows a strength message as the user types.

```html
<input type="password" id="pwd" placeholder="Create password">
<p id="strength"></p>
```

```javascript
const pwd = document.getElementById("pwd");
const strength = document.getElementById("strength");

pwd.addEventListener("input", () => {
  const value = pwd.value;
  let score = 0;

  if (value.length >= 8) score++;
  if (/[A-Z]/.test(value)) score++;
  if (/[0-9]/.test(value)) score++;
  if (/[^A-Za-z0-9]/.test(value)) score++;

  const labels = ["Too weak", "Weak", "Okay", "Good", "Strong"];
  strength.innerText = value === "" ? "" : labels[score];
});
```

**What happens internally:**

1. ⌨️ The user types a character. The browser fires an **`input` event**.
2. 📞 The registered handler is **called automatically**.
3. 🔍 The handler reads `pwd.value` and checks length, uppercase letters, digits, and symbols.
4. 🧮 It computes a score from 0 to 4.
5. 🖨️ `innerText` updates the label right away, and the user gets **instant feedback** with every keystroke, with no page reload and no server call.

---

## 📊 Diagram

```
           THE EVENT FLOW

   User action          Browser              Your code
  ┌──────────┐      ┌──────────────┐      ┌──────────────────┐
  │ clicks   │ ───► │ creates an   │ ───► │ listener runs    │
  │ a button │      │ EVENT object │      │ handler(event)   │
  └──────────┘      └──────────────┘      └────────┬─────────┘
                                                   ▼
                                          DOM changes → screen updates


          addEventListener ANATOMY

   button.addEventListener( "click" , handlerFunction )
     │                         │             │
  WHO to watch           WHAT to hear    WHAT to do


           EVENT BUBBLING

   click on <button>
        │  1st
        ▼
    <button>   ──► handler runs
        │  2nd
        ▼
     <div>     ──► handler runs
        │  3rd
        ▼
     <body>    ──► handler runs
        │
        ▼
    document


      FORM SUBMIT WITH preventDefault

   Submit ──► preventDefault() ──► validate ──► show message
                │
                └─ without it: page reloads ❌
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`addEventListener('click', sayHi())` works." | The `()` calls it immediately. Pass the **function itself**: `sayHi`. |
| "I can listen for form submission with button `click`." | Use `submit` on the **form**. It also catches the Enter key. |
| "I don't need `preventDefault()` on forms." | Without it, the page reloads and your JavaScript result vanishes. |
| "`input` and `change` are the same." | `input` fires on **every keystroke**. `change` fires when the value is **committed**. |
| "Events only affect the element I clicked." | Events **bubble** to parent elements too. |
| "`onclick` and `addEventListener` are the same." | `onclick` allows only one handler. `addEventListener` allows many. |
| "Adding listeners to 100 list items is fine." | Use **event delegation** with one listener on the parent. |
| "`removeEventListener` works with arrow functions written inline." | You need the **same function reference**. Use a named function. |
| "`type="button"` isn't needed in forms." | A button inside a form submits by default. Use `type="button"` for non-submit buttons. |

---

## 💬 Interview Corner

**Q1. What is an event in JavaScript?**
An event is an action or occurrence in the browser, like a click, key press, or form submission, that JavaScript can respond to by running a function.

**Q2. What does `event.preventDefault()` do?**
It stops the browser's default behavior for the event. For a form `submit`, it stops the page from reloading so JavaScript can validate or handle the data.

**Q3. What is the difference between the `input` and `change` events?**
`input` fires immediately on every change to the value. `change` fires only when the value is committed, such as when a field loses focus or a select option is chosen.

**Q4. What is event bubbling?**
When an event happens on an element, it first runs handlers on that element and then travels up through its parent elements to the document.

---

## 📝 Quick Summary

- ⚡ An **event** is something that happens, and a **handler** is the function you run in response.
- 🔌 Use `element.addEventListener("event", handler)`.
- 🖱️ `click` is for buttons and clickable elements.
- 📨 `submit` belongs on the **form** and needs **`event.preventDefault()`** to prevent the reload.
- ⌨️ `input` fires on every keystroke, `change` fires when the value is committed.
- 📦 The **event object** gives `target`, `type`, `key`, and more.
- 🫧 Events **bubble** up from child to parent.
- 🎯 **Event delegation** uses one parent listener for many children.
- 🚫 Pass the function, don't call it: `handler`, **not** `handler()`.

---

## 🎯 Class Activity

**🛠️ Activity: "Live Registration Preview"**

Build a small form with a **name**, **email**, and **city** input plus a Submit button.

1. As the user types, **show a live preview** below: *"Hello, <name> from <city>!"* using the `input` event.
2. Add a **character counter** for the name field.
3. On `submit`, use `event.preventDefault()`, check that no field is empty, and show either a green success message or a red error using `classList`.
4. **Bonus:** Log every key pressed in the name field using `keydown`.

---

# 📋 Assignments — Handling Events

| Assignment |
|---|
| Create a button that shows an alert using `addEventListener("click", ...)`. |
| Build a click counter with a number display and "Increase", "Decrease", and "Reset" buttons. |
| Build a "Like" button that toggles between "🤍 Like" and "❤️ Liked" and updates a count. |
| Create three buttons (Red, Green, Blue) that change the page's background color on click. |
| Attach a `click` listener to every item in a list using `querySelectorAll` and `forEach`, and toggle a `selected` class. |
| Rewrite the previous assignment using **event delegation** with one listener on the parent `<ul>`. |
| Create a form with a name field and a submit button. Use `preventDefault()` and display "Hello, <name>" on submit. |
| Show what happens when you forget `preventDefault()` in a form submit and explain it in two lines. |
| Build a live character counter for a textarea using the `input` event (with a limit of 100 characters). |
| Create a search box that filters a list of fruit names as the user types (hide items that don't match). |
| Use the `change` event on a `<select>` to display the chosen option's value in a paragraph. |
| Use `keydown` to log the pressed key and hide a popup when the Escape key is pressed. |
| Use `event.target` to print the tag name and text of whichever element inside a `<div>` is clicked. |
| Demonstrate event bubbling using nested `div`s with listeners at each level and note the order of console messages. |
| Add a listener, then remove it with `removeEventListener` after the first click so the button works only once. |

---
---

# 📚 Form Validation with JavaScript: Hotel Booking Form

## 🎯 Learning Objectives

By the end of this topic, you will be able to:

- ✅ Explain why form validation is needed and the difference between client-side and server-side validation
- 🧪 Validate required fields, email, phone number, dates, and number ranges
- 🚫 Prevent form submission when data is invalid using `preventDefault()`
- 💬 Show clear, field-specific error messages and success feedback
- 🔄 Provide live validation using `input` and `blur` events
- 🏨 Build a complete hotel booking form with JavaScript validation

---

## 📖 Introduction

Imagine a hotel booking website where a guest enters check-out as **before** check-in, writes "abc" as a phone number, or leaves the name empty. If the form accepted everything, hotels would receive broken bookings. 😬

**Form validation** means **checking user input before it is accepted**, and telling the user clearly what to fix.

**Why does this topic exist?** People make typing mistakes, skip fields, and sometimes enter nonsense deliberately.

**Why is it important?** It gives users **instant helpful feedback**, saves server effort, and keeps bad data out of the system.

**Where is it used?** Login, signup, checkout, booking, payment, and contact forms across the web.

This topic **combines everything** you learned: selecting elements, changing content, and handling events.

---

## 🧠 Detailed Notes

### 🛡️ 1. Client-Side vs Server-Side Validation

| Type | Where it runs | Purpose |
|---|---|---|
| **Client-side** (JavaScript in the browser) | User's browser | **Fast feedback**, better user experience |
| **Server-side** (Python/Django/Flask later in the course) | Your server | **Real security**, final check |

> ⚠️ **Important**
>
> Client-side validation is for **user convenience**. Anyone can bypass it using DevTools. A real application must **always validate again on the server**. You will do this when we reach the Python backend.

---

### 🧰 2. Validation Building Blocks

**(a) Required fields: not empty**

```javascript
const name = nameInput.value.trim();   // trim() removes extra spaces
if (name === "") {
  // error: required
}
```

**(b) Minimum length**

```javascript
if (name.length < 3) {
  // error: too short
}
```

**(c) Email format using a regular expression (regex)**

```javascript
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
console.log(emailPattern.test("asha@gmail.com"));  // true
console.log(emailPattern.test("asha@gmail"));      // false
```

**(d) Phone number: exactly 10 digits**

```javascript
const phonePattern = /^[0-9]{10}$/;
console.log(phonePattern.test("9876543210"));   // true
console.log(phonePattern.test("98765"));        // false
```

**(e) Number range**

```javascript
const guests = Number(guestsInput.value);
if (guests < 1 || guests > 6) {
  // error: between 1 and 6
}
```

**(f) Dates**

```javascript
const checkIn = new Date(checkInInput.value);
const checkOut = new Date(checkOutInput.value);

if (checkOut <= checkIn) {
  // error: check-out must be after check-in
}
```

> ℹ️ **Note**
>
> A simple regex like the email one above checks the **shape**, not whether the email truly exists. That's perfectly fine for beginners and many real sites.

🤔 **Quick thinking question:** Why do we use `.trim()` before checking if a field is empty?

✅ **Answer:** Without it, a user typing only spaces would pass the "not empty" check. `trim()` removes leading and trailing spaces first.

---

### 🏨 3. The Hotel Booking Form: Planning

**Fields and rules:**

| Field | Rule |
|---|---|
| Full Name | Required, at least 3 characters |
| Email | Required, valid format |
| Phone | Required, exactly 10 digits |
| Check-in date | Required, **not in the past** |
| Check-out date | Required, **after** check-in |
| Number of guests | Required, between **1 and 6** |
| Room type | Must choose one |
| Terms and conditions | Must be ticked |

**Our approach:**

1. Build the HTML form with a small error message area under every field.
2. Write **one small function per field** that returns `true` (valid) or `false`, and shows or clears the error.
3. On `submit`: `preventDefault()`, run all validators, and only continue if **all** pass.
4. Add live feedback using `blur` and `input` events.
5. On success, show a **booking summary** with the number of nights.

---

### 🧱 4. HTML: The Form Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hotel Paradise: Book Your Stay</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6f9; }
    .container { max-width: 480px; margin: 30px auto; background: #fff;
                 padding: 24px; border-radius: 10px;
                 box-shadow: 0 2px 10px rgba(0,0,0,.1); }
    h2 { text-align: center; }
    .field { margin-bottom: 14px; }
    label { display: block; font-weight: bold; margin-bottom: 4px; }
    input, select { width: 100%; padding: 8px; box-sizing: border-box;
                    border: 1px solid #bbb; border-radius: 5px; }
    input.invalid, select.invalid { border-color: #d93025; }
    input.valid, select.valid { border-color: #1e8e3e; }
    .error { color: #d93025; font-size: 13px; min-height: 16px; }
    .checkbox-row { display: flex; align-items: center; gap: 8px; }
    .checkbox-row input { width: auto; }
    button { width: 100%; padding: 10px; background: #0b5ed7; color: #fff;
             border: 0; border-radius: 5px; font-size: 16px; cursor: pointer; }
    #summary { margin-top: 16px; padding: 12px; background: #e6f4ea;
               border-radius: 6px; color: #1e8e3e; }
    .hidden { display: none; }
  </style>
</head>
<body>
  <div class="container">
    <h2>🏨 Hotel Paradise Booking</h2>

    <form id="bookingForm" novalidate>
      <div class="field">
        <label for="fullName">Full Name</label>
        <input type="text" id="fullName" placeholder="Enter your name">
        <div class="error" id="nameError"></div>
      </div>

      <div class="field">
        <label for="email">Email</label>
        <input type="text" id="email" placeholder="you@example.com">
        <div class="error" id="emailError"></div>
      </div>

      <div class="field">
        <label for="phone">Phone (10 digits)</label>
        <input type="text" id="phone" placeholder="9876543210" maxlength="10">
        <div class="error" id="phoneError"></div>
      </div>

      <div class="field">
        <label for="checkIn">Check-in Date</label>
        <input type="date" id="checkIn">
        <div class="error" id="checkInError"></div>
      </div>

      <div class="field">
        <label for="checkOut">Check-out Date</label>
        <input type="date" id="checkOut">
        <div class="error" id="checkOutError"></div>
      </div>

      <div class="field">
        <label for="guests">Number of Guests (1 to 6)</label>
        <input type="number" id="guests" value="1">
        <div class="error" id="guestsError"></div>
      </div>

      <div class="field">
        <label for="roomType">Room Type</label>
        <select id="roomType">
          <option value="">-- Select a room --</option>
          <option value="standard">Standard</option>
          <option value="deluxe">Deluxe</option>
          <option value="suite">Suite</option>
        </select>
        <div class="error" id="roomError"></div>
      </div>

      <div class="field">
        <div class="checkbox-row">
          <input type="checkbox" id="terms">
          <label for="terms" style="margin:0; font-weight:normal;">
            I agree to the terms and conditions
          </label>
        </div>
        <div class="error" id="termsError"></div>
      </div>

      <button type="submit">Book Now</button>
    </form>

    <div id="summary" class="hidden"></div>
  </div>

  <script src="booking.js" defer></script>
</body>
</html>
```

> 💡 **Tip**
>
> `novalidate` on the `<form>` switches off the browser's built-in popups so our **own JavaScript messages** are shown instead.

---

### ⚙️ 5. JavaScript: `booking.js`

```javascript
// ---------- 1. Select elements ----------
const form = document.getElementById("bookingForm");
const summary = document.getElementById("summary");

const fullName = document.getElementById("fullName");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const checkIn = document.getElementById("checkIn");
const checkOut = document.getElementById("checkOut");
const guests = document.getElementById("guests");
const roomType = document.getElementById("roomType");
const terms = document.getElementById("terms");

// Set the earliest selectable check-in date to today
const today = new Date().toISOString().split("T")[0];   // "YYYY-MM-DD"
checkIn.min = today;
checkOut.min = today;

// ---------- 2. Helper functions ----------
function showError(input, errorId, message) {
  document.getElementById(errorId).innerText = message;
  input.classList.add("invalid");
  input.classList.remove("valid");
}

function showSuccess(input, errorId) {
  document.getElementById(errorId).innerText = "";
  input.classList.remove("invalid");
  input.classList.add("valid");
}

// ---------- 3. One validator per field ----------
function validateName() {
  const value = fullName.value.trim();
  if (value === "") {
    showError(fullName, "nameError", "Name is required.");
    return false;
  }
  if (value.length < 3) {
    showError(fullName, "nameError", "Name must be at least 3 characters.");
    return false;
  }
  showSuccess(fullName, "nameError");
  return true;
}

function validateEmail() {
  const value = email.value.trim();
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (value === "") {
    showError(email, "emailError", "Email is required.");
    return false;
  }
  if (!pattern.test(value)) {
    showError(email, "emailError", "Enter a valid email like name@example.com.");
    return false;
  }
  showSuccess(email, "emailError");
  return true;
}

function validatePhone() {
  const value = phone.value.trim();
  if (value === "") {
    showError(phone, "phoneError", "Phone number is required.");
    return false;
  }
  if (!/^[0-9]{10}$/.test(value)) {
    showError(phone, "phoneError", "Phone must be exactly 10 digits.");
    return false;
  }
  showSuccess(phone, "phoneError");
  return true;
}

function validateCheckIn() {
  if (checkIn.value === "") {
    showError(checkIn, "checkInError", "Please choose a check-in date.");
    return false;
  }
  // String comparison works for YYYY-MM-DD format
  if (checkIn.value < today) {
    showError(checkIn, "checkInError", "Check-in cannot be in the past.");
    return false;
  }
  showSuccess(checkIn, "checkInError");
  return true;
}

function validateCheckOut() {
  if (checkOut.value === "") {
    showError(checkOut, "checkOutError", "Please choose a check-out date.");
    return false;
  }
  if (checkIn.value !== "" && checkOut.value <= checkIn.value) {
    showError(checkOut, "checkOutError", "Check-out must be after check-in.");
    return false;
  }
  showSuccess(checkOut, "checkOutError");
  return true;
}

function validateGuests() {
  const value = guests.value.trim();
  const number = Number(value);
  if (value === "") {
    showError(guests, "guestsError", "Number of guests is required.");
    return false;
  }
  if (!Number.isInteger(number) || number < 1 || number > 6) {
    showError(guests, "guestsError", "Guests must be a whole number from 1 to 6.");
    return false;
  }
  showSuccess(guests, "guestsError");
  return true;
}

function validateRoom() {
  if (roomType.value === "") {
    showError(roomType, "roomError", "Please select a room type.");
    return false;
  }
  showSuccess(roomType, "roomError");
  return true;
}

function validateTerms() {
  if (!terms.checked) {
    document.getElementById("termsError").innerText =
      "You must accept the terms to continue.";
    return false;
  }
  document.getElementById("termsError").innerText = "";
  return true;
}

// ---------- 4. Live validation (feedback while filling) ----------
fullName.addEventListener("blur", validateName);
email.addEventListener("blur", validateEmail);
phone.addEventListener("input", () => {
  // Keep only digits as the user types
  phone.value = phone.value.replace(/[^0-9]/g, "");
});
phone.addEventListener("blur", validatePhone);
checkIn.addEventListener("change", () => {
  validateCheckIn();
  if (checkOut.value !== "") validateCheckOut();   // re-check dependent field
  checkOut.min = checkIn.value || today;
});
checkOut.addEventListener("change", validateCheckOut);
guests.addEventListener("input", validateGuests);
roomType.addEventListener("change", validateRoom);
terms.addEventListener("change", validateTerms);

// ---------- 5. Submit handler ----------
form.addEventListener("submit", (event) => {
  event.preventDefault();   // stop the page reload

  // Run ALL validators (don't stop at the first failure)
  const results = [
    validateName(),
    validateEmail(),
    validatePhone(),
    validateCheckIn(),
    validateCheckOut(),
    validateGuests(),
    validateRoom(),
    validateTerms()
  ];

  const isFormValid = results.every((r) => r === true);

  if (!isFormValid) {
    summary.classList.add("hidden");
    // Move focus to the first invalid field to help the user
    const firstInvalid = form.querySelector(".invalid");
    if (firstInvalid) firstInvalid.focus();
    return;
  }

  // ---------- 6. Success: build a booking summary ----------
  const msPerDay = 1000 * 60 * 60 * 24;
  const nights = Math.round(
    (new Date(checkOut.value) - new Date(checkIn.value)) / msPerDay
  );

  const prices = { standard: 3000, deluxe: 4500, suite: 7000 };
  const total = nights * prices[roomType.value];

  // innerText keeps user-typed text safe
  summary.innerText =
    `✅ Booking confirmed for ${fullName.value.trim()}! ` +
    `${nights} night(s) in a ${roomType.value} room ` +
    `for ${guests.value} guest(s). Total: ₹${total}.`;
  summary.classList.remove("hidden");

  console.log("Ready to send to server:", {
    name: fullName.value.trim(),
    email: email.value.trim(),
    phone: phone.value,
    checkIn: checkIn.value,
    checkOut: checkOut.value,
    guests: Number(guests.value),
    room: roomType.value
  });
});
```

---

### 🔬 6. How the Code Works, Step by Step

| Part | What it does |
|---|---|
| **Select elements** | Stores every input and the form in variables |
| **`checkIn.min = today`** | The date picker itself greys out past dates |
| **`showError` / `showSuccess`** | Reusable helpers that update the message and the red or green border |
| **Validators** | One function per field. Returns `true` or `false` |
| **`blur` / `input` / `change` listeners** | Instant feedback when the user leaves or edits a field |
| **`event.preventDefault()`** | Stops the reload on submit |
| **`results.every(...)`** | Form is valid only if **every** validator returned `true` |
| **Focus first invalid** | Helps keyboard and accessibility users |
| **`nights` calculation** | Date difference in milliseconds divided by milliseconds per day |

> 💡 **Tip**
>
> We call **all** validators on submit (using an array), instead of chaining with `&&`. With `&&`, JavaScript would stop at the first failure and the user would only see **one** error at a time.

---

### 🧪 7. Test Cases to Try

| Test input | Expected result |
|---|---|
| All fields empty, click Book Now | All errors appear, nothing is submitted |
| Name = `"  "` (spaces only) | "Name is required." |
| Email = `asha@gmail` | "Enter a valid email..." |
| Phone = `98765` | "Phone must be exactly 10 digits." |
| Check-out earlier than check-in | "Check-out must be after check-in." |
| Guests = `0` or `9` | "Guests must be a whole number from 1 to 6." |
| Terms unticked | "You must accept the terms..." |
| Everything valid | Green borders and the booking summary |

---

### 🔐 8. Good Practices to Remember

- ✅ Validate on the **client** for speed, and **again on the server** for security.
- ✅ Write **specific** messages ("Phone must be 10 digits") instead of "Invalid input".
- ✅ Show errors **next to the field** that has the problem.
- ✅ Don't scold the user before they even start typing. Validate on `blur`, or on `submit`.
- ✅ Use `innerText` for messages that include user-typed text.
- ✅ Keep one validator function per field. It makes the code easy to read and fix.

---

## 💡 Real-Life Analogy

🛂 **Form validation is like airport check-in:**

- The **check-in counter staff** (JavaScript) check your passport, ticket, and baggage **before you reach the gate**. If something is wrong, they tell you immediately: "Your passport has expired. Please fix it."
- It saves you the trouble of reaching the gate and being turned back. That's **client-side validation**: fast and friendly.
- But the **security gate and immigration** (server-side validation) check everything **again**, because the airline cannot assume the first check was honest or complete.
- And the staff don't just say "Problem!" They say **exactly what's wrong**, like a good error message.

---

## 💻 Real-World Application

| Where | Validation used |
|---|---|
| 🏨 **MakeMyTrip / Booking.com** | Date ranges, guest counts, required traveler details |
| 🏦 **Net banking** | Account number length, amount limits |
| 🛒 **Amazon / Flipkart checkout** | PIN code format, phone digits, address required |
| 🎟️ **BookMyShow** | Seat count limits, email and phone format |
| 🔐 **Signup pages** | Strong passwords, matching confirm password, valid email |
| 🏥 **Hospital portals** | Date of birth not in the future, valid mobile number |

---

## 🔍 Industry Example

📘 **Scenario: A travel company's booking page and abandoned bookings**

A travel startup noticed that **many customers abandoned their hotel booking** at the final step. Investigation showed customers submitted the form, waited for the server, and *then* got a single vague message: "Something went wrong."

The developers added JavaScript validation:

1. 🏷️ **Inline messages** under each field: "Check-out must be after check-in."
2. ⌨️ **Live feedback** with `blur` and `input` events, so errors appeared as soon as a field was done.
3. 🗓️ **Date picker limits** using `min` to prevent past dates.
4. 🎯 **Auto-focus** on the first invalid field on submit.
5. 🛡️ **Server-side checks** retained as the final safety net.

**Result:** Users fixed problems immediately, fewer invalid requests reached the server, and more users completed their bookings. This is a classic example of how **small JavaScript improvements** create real **business value**.

---

## 📊 Diagram

```
              FORM VALIDATION FLOW

   User fills form
         │
         ▼
  ┌─────────────────┐
  │  Live checks    │  blur / input / change
  │  (per field)    │  → red or green border + message
  └────────┬────────┘
           ▼
   User clicks "Book Now"
           │
           ▼
   submit event fires
           │
           ▼
   event.preventDefault()   ◄── stop page reload
           │
           ▼
 ┌───────────────────────────┐
 │ Run ALL validators        │
 │ name  email  phone        │
 │ dates guests  room  terms │
 └─────────────┬─────────────┘
               ▼
        Are ALL valid?
         /          \
       NO            YES
        │             │
 Show errors       Show booking summary
 Focus first       Send data to server
 invalid field     (server validates again 🛡️)


         ONE FIELD'S VALIDATOR

   read value ─► trim ─► empty? ──YES──► error "required" ─► return false
                            │NO
                            ▼
                      format wrong? ──YES──► error "format" ─► return false
                            │NO
                            ▼
                      showSuccess ─► return true
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "JavaScript validation is enough for security." | Users can bypass it. **Always validate on the server too.** |
| "I don't need `preventDefault()`." | Without it, invalid forms still submit and the page reloads. |
| "Checking `value === ''` is enough for required fields." | Use `trim()` too, or spaces-only will pass. |
| "`input.value` of a number field is a number." | It is always a **string**. Convert with `Number()`. |
| "Chain validators with `&&`." | It stops at the first failure. Run **all** and combine results. |
| "A regex email check proves the email exists." | It only checks the **format**. |
| "Compare dates as plain strings like `'5/10/2026'`." | Use `YYYY-MM-DD` strings (from date inputs) or `Date` objects. |
| "Showing all errors only after submit is best." | Use `blur` and `input` for friendlier, earlier feedback. |
| "Put `innerHTML = userName` in the success message." | Use `innerText`, because user input must never be treated as HTML. |
| "Forgetting `novalidate` is harmless." | The browser's own popups may appear **instead of** your custom messages. |

---

## 💬 Interview Corner

**Q1. What is the difference between client-side and server-side validation?**
Client-side validation runs in the browser (JavaScript) for fast feedback and better user experience. Server-side validation runs on the server and is essential for security, since client-side checks can be bypassed.

**Q2. Why do we use `event.preventDefault()` in form validation?**
To stop the form from submitting and reloading the page when the data is invalid, so we can show error messages and let the user correct them.

**Q3. How do you validate an email in JavaScript?**
Usually with a regular expression that checks the basic shape (`text@text.text`) using `pattern.test(value)`. Truly verifying the email requires sending a confirmation message from the server.

**Q4. Why is `input.value` often converted with `Number()` before validation?**
Because values from form inputs are always strings. Comparisons such as `guests > 6` should be done on numbers to avoid unexpected results.

---

## 📝 Quick Summary

- ✅ Validation checks user input **before accepting it** and tells the user how to fix problems.
- 🌐 **Client-side** gives fast feedback, and **server-side** gives real security. You need both.
- 🧪 Common checks: required (with `trim()`), length, regex (email and phone), number range, and date logic.
- 🚫 Use `submit` on the form with **`event.preventDefault()`** to control submission.
- 💬 Show **specific messages** next to each field, and use `classList` for red and green borders.
- 🔄 Use `blur`, `input`, and `change` for **live feedback**.
- 📋 Run **all** validators and combine results (`every`) to show all errors at once.
- 🎯 Focus the **first invalid field** for a better experience.
- 🔐 Use `innerText` for any message that includes user-typed data.

---

## 🎯 Class Activity

**🛠️ Activity: "Build and break the Hotel Booking form"**

1. Create `index.html` and `booking.js` from the code in this topic.
2. Open it in Chrome and run **every test case** from the test table. Tick them off.
3. **Break it deliberately:** remove `event.preventDefault()` and observe what happens. Put it back.
4. **Extend it:** add a new field **"Special Requests"** (optional textarea) with a **maximum of 200 characters** and a live character counter.
5. **Extend it:** add a **"Confirm Email"** field that must match the email.
6. Swap code with a classmate and try to find an input that **breaks** their validation.

---

# 📋 Assignments — Form Validation: Hotel Booking Form

| Assignment |
|---|
| Build the complete hotel booking form from the notes and test it with all the listed test cases. Take screenshots of at least three different error states. |
| Add a "Confirm Email" field and validate that it matches the email field exactly. |
| Add an optional "Special Requests" textarea with a live character counter and a 200-character limit that shows a warning at 180 characters. |
| Add a "Number of Children" field (0 to 4) and make sure total guests (adults plus children) never exceed 8. |
| Prevent the user from booking more than 30 nights and show a clear error message. |
| Add a "Payment Method" radio group (Card, UPI, Pay at Hotel) and make selecting one required. |
| Add a password-style "Booking PIN" field that must have exactly 4 digits and show a live strength or validity hint. |
| Make the phone field accept only digits by filtering other characters as the user types (using the `input` event). |
| Show the total price live, updating as the user changes room type and dates, before submission. |
| Add a "Reset" button that clears all fields, error messages, and the green or red borders. |
| Change the success message so it shows a formatted date such as "12 Oct 2026" instead of the raw `YYYY-MM-DD`. |
| Disable the "Book Now" button until all fields are valid, and enable it automatically afterwards. |
| Rewrite the email and phone validators as one reusable function `validateWithPattern(input, errorId, pattern, message)` and use it for both. |
| Create a second form of your own choice (for example movie ticket booking or library registration) with at least six fields and complete validation. |
| Write a short note (6 to 8 lines) explaining why server-side validation is still needed even though your JavaScript validation works well. |