# 📚 SELECT with Filtering: WHERE, BETWEEN, IN, LIKE, IS NULL

## 🎯 Learning Objectives
* 🎯 Understand how to fetch specific data using SELECT and WHERE
* 🎯 Learn to filter ranges of data using BETWEEN
* 🎯 Learn to match multiple specific values using IN
* 🎯 Learn to search for patterns in text using LIKE
* 🎯 Learn to handle missing/empty values using IS NULL and IS NOT NULL

## 📖 Introduction
Imagine you have a table with 10,000 customer records, but you only want to see customers from "Mumbai" who are older than 25. Scrolling through all 10,000 rows manually would take forever! 😩

This is exactly why SQL gives us **filtering** — the ability to ask the database to show us **only the rows that match specific conditions**, instead of everything.

Why does this matter?
* Real-world tables often have thousands or millions of rows — you almost never want "everything."
* Filtering is the foundation of almost every useful SQL query you'll ever write.

Where is it used?
* Every search bar, every filter dropdown (price range, category, rating) on websites like Amazon or Flipkart is powered by SQL filtering behind the scenes.

> 💡 **Tip**
>
> `SELECT` is a DQL (Data Query Language) command — it *reads* data, it doesn't change it. It's the safest SQL command to experiment with!

## 🧠 Detailed Notes

### 1️⃣ Basic SELECT with WHERE
The `WHERE` clause filters rows based on a condition.

**Syntax:**
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

**Example:**
```sql
SELECT name, age, city
FROM students
WHERE city = 'Pune';
```

This returns only the students whose `city` is exactly `'Pune'`.

**Comparison operators used in WHERE:**

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `age = 20` |
| `!=` or `<>` | Not equal to | `city != 'Delhi'` |
| `>` | Greater than | `age > 18` |
| `<` | Less than | `price < 500` |
| `>=` | Greater than or equal to | `age >= 18` |
| `<=` | Less than or equal to | `price <= 1000` |

**Combining conditions with AND / OR:**
```sql
SELECT * FROM students
WHERE city = 'Pune' AND age > 20;

SELECT * FROM students
WHERE city = 'Pune' OR city = 'Mumbai';
```

🤔 **Quick Thinking Question:** What's the difference between `AND` and `OR` in a WHERE clause?
✅ **Answer:** `AND` requires ALL conditions to be true for a row to be included; `OR` requires AT LEAST ONE condition to be true.

### 2️⃣ BETWEEN — Filtering a Range
`BETWEEN` checks if a value falls within a specified range (inclusive of both ends).

```sql
SELECT * FROM employees
WHERE age BETWEEN 25 AND 35;
```

This is equivalent to writing `age >= 25 AND age <= 35`, but much cleaner to read.

It also works with dates:
```sql
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

> ⚠️ **Important**
>
> `BETWEEN` is **inclusive** — both the starting and ending values ARE included in the result.

### 3️⃣ IN — Matching Multiple Specific Values
`IN` lets you check if a value matches **any value in a list**, instead of writing multiple `OR` conditions.

**Without IN (messy):**
```sql
SELECT * FROM students
WHERE city = 'Pune' OR city = 'Mumbai' OR city = 'Delhi';
```

**With IN (clean):**
```sql
SELECT * FROM students
WHERE city IN ('Pune', 'Mumbai', 'Delhi');
```

Both queries return the exact same result, but `IN` is much easier to read and write.

🤔 **Quick Thinking Question:** How would you rewrite `status = 'Pending' OR status = 'Shipped'` using IN?
✅ **Answer:** `status IN ('Pending', 'Shipped')`

### 4️⃣ LIKE — Pattern Matching in Text
`LIKE` is used to search for a **pattern** within text data, using wildcard symbols.

| Wildcard | Meaning | Example | Matches |
|---|---|---|---|
| `%` | Any number of characters (including zero) | `'A%'` | 'Aman', 'Aditi', 'A' |
| `_` | Exactly one character | `'R_ya'` | 'Riya', 'Roya' |

**Examples:**
```sql
-- Names starting with 'A'
SELECT * FROM students WHERE name LIKE 'A%';

-- Names ending with 'a'
SELECT * FROM students WHERE name LIKE '%a';

-- Names containing 'an' anywhere
SELECT * FROM students WHERE name LIKE '%an%';

-- Emails from gmail.com
SELECT * FROM students WHERE email LIKE '%@gmail.com';
```

> 💡 **Tip**
>
> Think of `%` as "anything can go here (any length)" and `_` as "exactly one unknown character goes here."

### 5️⃣ IS NULL and IS NOT NULL — Handling Missing Data
`NULL` represents **missing or unknown data** — it is NOT the same as zero or an empty string. To check for NULL values, you **cannot** use `=`; you must use `IS NULL`.

```sql
-- ❌ This will NOT work correctly:
SELECT * FROM students WHERE email = NULL;

-- ✅ This is the correct way:
SELECT * FROM students WHERE email IS NULL;

-- Finding rows where email IS provided:
SELECT * FROM students WHERE email IS NOT NULL;
```

🤔 **Quick Thinking Question:** Why can't we use `WHERE email = NULL` to find rows with missing emails?
✅ **Answer:** Because NULL means "unknown," and comparing anything to "unknown" using `=` also results in "unknown" (not true) — so `IS NULL` is a special operator specifically designed to check for NULL values.

### 6️⃣ Combining Everything Together
```sql
SELECT name, age, city, email
FROM students
WHERE age BETWEEN 18 AND 25
  AND city IN ('Pune', 'Mumbai')
  AND name LIKE 'S%'
  AND email IS NOT NULL;
```

This single query filters students who are aged 18-25, live in Pune or Mumbai, have a name starting with 'S', and have provided an email — all at once!

## 💡 Real-Life Analogy
Filtering with WHERE is like using **search filters on a shopping website**:
* **WHERE** = Typing "red shoes" in the search bar — showing only matching products.
* **BETWEEN** = Using a price slider from ₹500 to ₹1500 — showing only products in that range.
* **IN** = Selecting multiple brands (Nike, Puma, Adidas) via checkboxes — showing products from ANY of these brands.
* **LIKE** = Typing "run" and seeing "Running Shoes," "Runner Jacket" — partial text matches.
* **IS NULL** = Filtering "products with no reviews yet" — where the reviews field is empty/unknown.

## 💻 Real-World Application

| Filtering Feature | Real-World Use Case |
|---|---|
| WHERE | Search bar on any e-commerce or app |
| BETWEEN | Price range slider, date range picker |
| IN | Multi-select category/brand filters |
| LIKE | Search-as-you-type / autocomplete suggestions |
| IS NULL | Finding incomplete user profiles, unassigned tasks |

## 🔍 Industry Example
When you use the **filter panel on Naukri.com** to search for jobs:
1. You select "Experience: 2-5 years" → backend runs `WHERE experience BETWEEN 2 AND 5`
2. You select "Location: Pune, Bangalore" (multi-select) → backend runs `WHERE location IN ('Pune', 'Bangalore')`
3. You type "Python" in the search box → backend runs `WHERE job_title LIKE '%Python%'`
4. The system also filters out incomplete job postings → `WHERE salary IS NOT NULL`
5. All these conditions get combined using `AND` into one big query, and the matching jobs are displayed to you in milliseconds.

## 📊 Diagram

```
        students table (100 rows)
   ┌─────────────────────────────────┐
   │  name  │ age │  city   │ email  │
   ├─────────────────────────────────┤
   │  ...   │ ... │   ...   │  ...   │   (100 rows total)
   └─────────────────────────────────┘
                  │
                  ▼  WHERE age BETWEEN 18 AND 25
                     AND city IN ('Pune','Mumbai')
                     AND name LIKE 'S%'
                  ▼
   ┌─────────────────────────────────┐
   │  Sneha │ 21  │  Pune   │ s@x.com│   (Only matching rows!)
   │  Sara  │ 19  │  Mumbai │ NULL   │
   └─────────────────────────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| `WHERE email = NULL` finds rows with missing email | You must use `WHERE email IS NULL`; `=` never works with NULL |
| `BETWEEN` excludes the boundary values | `BETWEEN` is inclusive — it includes both start and end values |
| `LIKE '%text%'` and `= 'text'` behave the same | `LIKE` does pattern/partial matching; `=` requires an exact full match |
| `IN` can only be used with numbers | `IN` works with text, numbers, and dates equally well |
| Text comparisons in WHERE are case-sensitive everywhere | Case-sensitivity depends on the database and its configuration — always test |

## 💬 Interview Corner
**Q1: What is the difference between WHERE and HAVING?**
✅ WHERE filters individual rows before any grouping happens; HAVING filters groups after aggregation (covered in the next topic).

**Q2: How do you find records with a NULL value in a column?**
✅ Using `IS NULL`, e.g., `WHERE column_name IS NULL` — never using `= NULL`.

**Q3: What does the `%` wildcard mean in a LIKE clause?**
✅ It matches any sequence of characters (including zero characters) in that position.

**Q4: Rewrite `age >= 18 AND age <= 30` using BETWEEN.**
✅ `age BETWEEN 18 AND 30`

## 📝 Quick Summary
* 📌 `WHERE` filters rows based on a condition
* 📌 `BETWEEN` filters an inclusive range of values (numbers or dates)
* 📌 `IN` matches against a list of specific values, replacing multiple ORs
* 📌 `LIKE` performs pattern matching using `%` (any characters) and `_` (one character)
* 📌 `NULL` means unknown/missing data — use `IS NULL` / `IS NOT NULL`, never `=`
* 📌 Multiple conditions can be combined using `AND` / `OR`
* 📌 Filtering is the foundation of nearly every real-world SQL query

## 🎯 Class Activity
Using your `students` table from earlier topics, write and run 5 different SELECT queries: one using WHERE, one using BETWEEN, one using IN, one using LIKE, and one using IS NULL. Compare your results with a classmate.

---

# 📋 Assignments — SELECT with Filtering (WHERE, BETWEEN, IN, LIKE, IS NULL)

| Assignment |
|---|
| Write a query to fetch all students older than 20 from your students table. |
| Write a query using BETWEEN to fetch students aged 18 to 22. |
| Write a query using IN to fetch students from 3 specific cities of your choice. |
| Write a query using LIKE to find all students whose name starts with a letter of your choice. |
| Write a query using LIKE to find all students whose email contains 'gmail'. |
| Write a query to find all students where the email column IS NULL. |
| Write a query combining WHERE, IN, and LIKE together in a single statement. |
| Insert 2 rows into your students table with a NULL email, then write a query to find only those rows. |
| Write a query using NOT IN to exclude students from 2 specific cities. |
| Write a query using LIKE with the `_` wildcard to match a 4-letter name pattern. |
| Explain in writing why `WHERE age = NULL` does not work, using your own words. |
| Write 3 different WHERE queries on an employees or products table of your choice, one each using AND, OR, and BETWEEN. |

---

# 📚 Aggregations: COUNT, SUM, AVG, MAX, MIN

## 🎯 Learning Objectives
* 🎯 Understand what aggregate functions are and why we need them
* 🎯 Learn to count rows using COUNT
* 🎯 Learn to calculate totals using SUM
* 🎯 Learn to calculate averages using AVG
* 🎯 Learn to find the highest and lowest values using MAX and MIN

## 📖 Introduction
Imagine your manager asks: "How many total orders did we get today?" or "What is the average salary of employees in the company?" You wouldn't scroll through thousands of rows and count manually — you'd want the database to **calculate it for you instantly**.

This is exactly what **aggregate functions** do — they take many rows of data and produce **one summarized result** (a total, an average, a count, etc.).

Why does this matter?
* Businesses run on numbers — total sales, average rating, highest bid, lowest stock. Aggregate functions are how we get these numbers directly from the database.
* Without them, we'd have to pull ALL the data into our application code and calculate manually — extremely slow and inefficient for large datasets.

Where is it used?
* Dashboards you see everywhere — "Total Revenue Today," "Average Order Value," "Total Users" — are all powered by SQL aggregate functions.

## 🧠 Detailed Notes

### 1️⃣ What is an Aggregate Function?
An aggregate function takes a **set of rows** and returns a **single summarized value**. The five most commonly used aggregate functions are:

| Function | Purpose | Example |
|---|---|---|
| `COUNT()` | Counts the number of rows | Total number of students |
| `SUM()` | Adds up numeric values | Total sales amount |
| `AVG()` | Calculates the average | Average employee salary |
| `MAX()` | Finds the highest value | Highest paid employee |
| `MIN()` | Finds the lowest value | Lowest priced product |

### 2️⃣ COUNT — Counting Rows
```sql
-- Count all rows in the table
SELECT COUNT(*) FROM students;

-- Count only rows where email is NOT NULL
SELECT COUNT(email) FROM students;

-- Count students from a specific city
SELECT COUNT(*) FROM students WHERE city = 'Pune';
```

> ⚠️ **Important**
>
> `COUNT(*)` counts ALL rows (including ones with NULL values in some columns), while `COUNT(column_name)` counts only rows where that specific column is NOT NULL.

🤔 **Quick Thinking Question:** If a `students` table has 50 rows total, but only 45 have a non-NULL email, what will `COUNT(*)` and `COUNT(email)` return respectively?
✅ **Answer:** `COUNT(*)` returns 50 (total rows); `COUNT(email)` returns 45 (only non-NULL emails).

### 3️⃣ SUM — Adding Up Values
```sql
-- Total salary paid across all employees
SELECT SUM(salary) FROM employees;

-- Total sales amount for a specific product
SELECT SUM(quantity * price) FROM orders WHERE product_id = 101;
```

### 4️⃣ AVG — Calculating the Average
```sql
-- Average age of all students
SELECT AVG(age) FROM students;

-- Average order value
SELECT AVG(quantity * price) FROM orders;
```

> 💡 **Tip**
>
> `AVG()` automatically ignores NULL values when calculating the average — it does NOT treat them as zero.

### 5️⃣ MAX and MIN — Highest and Lowest Values
```sql
-- Highest salary in the company
SELECT MAX(salary) FROM employees;

-- Lowest priced product
SELECT MIN(price) FROM products;

-- Oldest and youngest student
SELECT MAX(age), MIN(age) FROM students;
```

MAX and MIN also work on text and dates! For example, `MAX(name)` returns the name that comes last alphabetically, and `MAX(order_date)` returns the most recent date.

### 6️⃣ Combining Aggregate Functions with WHERE
Aggregate functions can be combined with `WHERE` to summarize a **filtered subset** of data:

```sql
-- Average salary of employees in the 'IT' department
SELECT AVG(salary) FROM employees WHERE department = 'IT';

-- Total revenue from orders placed in January
SELECT SUM(quantity * price) FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

🤔 **Quick Thinking Question:** How would you find the total number of "Delivered" orders in an `orders` table?
✅ **Answer:** `SELECT COUNT(*) FROM orders WHERE status = 'Delivered';`

### 7️⃣ Giving Aggregates Readable Names with AS (Aliasing)
```sql
SELECT COUNT(*) AS total_students, AVG(age) AS average_age
FROM students;
```

Instead of a confusing column name like `COUNT(*)`, this gives you a clean, readable column name like `total_students` in your results.

## 💡 Real-Life Analogy
Think of aggregate functions like a **class teacher summarizing exam results**:
* **COUNT** = "How many students appeared for the exam?"
* **SUM** = "What is the total marks scored by the whole class combined?"
* **AVG** = "What is the class average?"
* **MAX** = "Who scored the highest marks?"
* **MIN** = "Who scored the lowest marks?"

The teacher doesn't need to re-read every single answer sheet again — she just uses the already-recorded marks to instantly calculate these summaries. That's exactly what aggregate functions do with table data.

## 💻 Real-World Application

| Aggregate Function | Real-World Dashboard Example |
|---|---|
| COUNT | "Total Users Registered: 45,231" |
| SUM | "Total Revenue This Month: ₹12,45,000" |
| AVG | "Average Order Value: ₹899" |
| MAX | "Highest Selling Product Price: ₹4,999" |
| MIN | "Lowest Stock Item: 2 units left" |

## 🔍 Industry Example
When a **Business Analyst at Swiggy** prepares a weekly performance report:
1. They run `SELECT COUNT(*) FROM orders WHERE order_date BETWEEN '2024-06-01' AND '2024-06-07';` to find total orders that week.
2. They run `SELECT SUM(total_amount) FROM orders WHERE order_date BETWEEN '2024-06-01' AND '2024-06-07';` to find total revenue.
3. They run `SELECT AVG(total_amount) FROM orders WHERE order_date BETWEEN '2024-06-01' AND '2024-06-07';` to find the average order value.
4. They run `SELECT MAX(total_amount) FROM orders;` to find the single largest order ever placed — useful for spotting outliers or celebrating big wins.
5. These numbers are then plugged into a company-wide dashboard that leadership reviews every Monday morning.

## 📊 Diagram

```
        orders table
 ┌─────────────────────────┐
 │ order_id │ amount │ ...  │
 ├─────────────────────────┤
 │   1      │  500   │      │
 │   2      │  800   │      │
 │   3      │  300   │      │
 │   4      │  1200  │      │
 └─────────────────────────┘
            │
            ▼   Aggregate Functions
   ┌─────────────────────────────┐
   │ COUNT(*) = 4                │
   │ SUM(amount) = 2800          │
   │ AVG(amount) = 700           │
   │ MAX(amount) = 1200          │
   │ MIN(amount) = 300           │
   └─────────────────────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| `COUNT(*)` and `COUNT(column)` always return the same result | `COUNT(column)` ignores NULL values in that column; `COUNT(*)` counts every row regardless |
| `AVG()` treats NULL as 0 in its calculation | `AVG()` completely ignores/skips NULL values; it does NOT count them as zero |
| Aggregate functions can be used directly with a normal SELECT of individual columns without GROUP BY | Mixing aggregate functions with regular columns (without GROUP BY) causes errors or unexpected results in most databases |
| MAX/MIN only work on numbers | MAX/MIN also work on text (alphabetical) and dates (chronological) |

## 💬 Interview Corner
**Q1: What is the difference between COUNT(*) and COUNT(column_name)?**
✅ COUNT(*) counts all rows regardless of NULL values; COUNT(column_name) counts only rows where that column has a non-NULL value.

**Q2: Does AVG() include NULL values in its calculation?**
✅ No, AVG() automatically ignores NULL values — it does not treat them as zero.

**Q3: How would you find the total revenue from an orders table?**
✅ `SELECT SUM(amount) FROM orders;` (or `SUM(quantity * price)` if amount isn't precomputed).

**Q4: Can MAX() and MIN() be used on text columns?**
✅ Yes — MAX() returns the alphabetically last value, and MIN() returns the alphabetically first value.

## 📝 Quick Summary
* 📌 Aggregate functions summarize many rows into a single value
* 📌 `COUNT()` counts rows (with subtle NULL-handling differences between `*` and column name)
* 📌 `SUM()` adds up numeric values
* 📌 `AVG()` calculates the average, automatically skipping NULLs
* 📌 `MAX()` / `MIN()` find the highest/lowest values — works on numbers, text, and dates
* 📌 Aggregate functions can be combined with WHERE to summarize filtered data
* 📌 Use `AS` to give your aggregate result a clean, readable column name

## 🎯 Class Activity
Using your `orders` or `employees` table, write 5 queries: total row count, sum of a numeric column, average of that column, and its maximum and minimum values. Use `AS` to name each result clearly.

---

# 📋 Assignments — Aggregations: COUNT, SUM, AVG, MAX, MIN

| Assignment |
|---|
| Write a query to count the total number of students in your students table. |
| Write a query to find the sum of all employee salaries in your employees table. |
| Write a query to find the average price of all products in your products table. |
| Write a query to find the maximum and minimum age among your students. |
| Write a query to count how many orders have status = 'Delivered'. |
| Compare COUNT(*) vs COUNT(email) on your students table and explain any difference you observe. |
| Write a query using SUM with WHERE to find total sales for a specific product. |
| Write a query giving readable aliases (using AS) to at least 3 aggregate results. |
| Find the employee with the highest salary using MAX (just the value, not the full row). |
| Write a query to calculate the average order value in your orders table. |
| Insert a row with a NULL value in a numeric column and check how it affects AVG() and SUM(). |
| Write a short paragraph explaining a real dashboard (from any app you use) and which aggregate functions might power it. |

---

# 📚 GROUP BY and HAVING

## 🎯 Learning Objectives
* 🎯 Understand what GROUP BY does and why it's needed
* 🎯 Learn to combine GROUP BY with aggregate functions
* 🎯 Understand the purpose of the HAVING clause
* 🎯 Learn the key difference between WHERE and HAVING
* 🎯 Practice writing grouped summary queries on real-world-style data

## 📖 Introduction
In the last topic, we learned to calculate totals like "total salary of ALL employees." But what if your manager asks: "What is the total salary **department-wise**?" Now you need separate totals for IT, HR, Sales, etc. — not just one grand total.

This is exactly what `GROUP BY` does — it **splits your data into groups** (based on a column) and then applies aggregate functions to **each group separately**.

Why does this matter?
* Almost every real business report is grouped: sales by region, orders by month, students by course, revenue by product category.
* Without GROUP BY, you'd have to write a separate query for every single group manually — extremely inefficient.

Where is it used?
* Every "breakdown" chart you see in analytics dashboards (sales by category, users by country) is powered by GROUP BY.

## 🧠 Detailed Notes

### 1️⃣ What Does GROUP BY Do?
`GROUP BY` groups rows that have the same value in a specified column, so aggregate functions operate on each group separately instead of the whole table.

**Syntax:**
```sql
SELECT column_name, AGGREGATE_FUNCTION(another_column)
FROM table_name
GROUP BY column_name;
```

**Example:**
```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;
```

**Sample Result:**

| department | total_salary |
|---|---|
| IT | 450000 |
| HR | 180000 |
| Sales | 320000 |

Instead of one big total, we now get a **separate total for each department**.

🤔 **Quick Thinking Question:** If you want to find the number of students enrolled in EACH course (not just the total across all courses), which clause would you use?
✅ **Answer:** `GROUP BY course_id` (or `course_name`) combined with `COUNT(*)`.

### 2️⃣ GROUP BY with Multiple Columns
You can also group by more than one column at once:

```sql
SELECT department, city, COUNT(*) AS emp_count
FROM employees
GROUP BY department, city;
```

This creates a separate group for every unique **combination** of department AND city.

### 3️⃣ The Golden Rule of GROUP BY
Every column in your `SELECT` list must either:
1. Be part of the `GROUP BY` clause, OR
2. Be wrapped inside an aggregate function (COUNT, SUM, AVG, MAX, MIN)

```sql
-- ✅ CORRECT
SELECT department, AVG(salary) FROM employees GROUP BY department;

-- ❌ INCORRECT (name is neither grouped nor aggregated)
SELECT department, name, AVG(salary) FROM employees GROUP BY department;
```

> ⚠️ **Important**
>
> Most databases will throw an error (or unpredictable results in older MySQL versions) if you break this rule. Always double-check your SELECT list against your GROUP BY list!

### 4️⃣ HAVING — Filtering Groups
We already know `WHERE` filters individual rows. But what if we want to filter **groups** — for example, "show only departments where total salary exceeds ₹3,00,000"? For this, we need `HAVING`, because `WHERE` cannot be used with aggregate functions.

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 300000;
```

This first groups employees by department, calculates the total salary per group, and THEN keeps only the groups where that total exceeds ₹3,00,000.

### 5️⃣ WHERE vs HAVING — The Most Important Distinction

| Aspect | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups (after GROUP BY) |
| Runs | Before grouping/aggregation | After grouping/aggregation |
| Can use aggregate functions? | ❌ No | ✅ Yes |
| Example | `WHERE age > 18` | `HAVING COUNT(*) > 5` |

**Using both together:**
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE age > 25
GROUP BY department
HAVING AVG(salary) > 50000;
```

Here's the order of execution:
1. `WHERE age > 25` → filters individual employee rows first
2. `GROUP BY department` → groups the remaining rows by department
3. `AVG(salary)` → calculates average salary per department
4. `HAVING AVG(salary) > 50000` → keeps only departments whose average exceeds ₹50,000

🤔 **Quick Thinking Question:** Why can't we write `WHERE AVG(salary) > 50000` instead of using HAVING?
✅ **Answer:** Because `WHERE` filters rows BEFORE any aggregation happens, and at that point, an average hasn't been calculated yet — aggregate functions can only be filtered using `HAVING`, which runs AFTER grouping.

### 6️⃣ Combining GROUP BY, HAVING, and ORDER BY
```sql
SELECT department, COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 2
ORDER BY emp_count DESC;
```

This finds departments with more than 2 employees, then sorts the result from the largest department to the smallest.

## 💡 Real-Life Analogy
Think of a **class teacher sorting exam mark sheets into piles by Section** (Section A, Section B, Section C):
* **GROUP BY Section** = Physically sorting all mark sheets into 3 piles based on section.
* **Aggregate function (AVG)** = Calculating the average marks for each pile separately.
* **HAVING AVG(marks) > 70** = Only keeping the piles (sections) whose average is above 70, and setting aside the rest.

Notice the teacher couldn't calculate "average above 70" until AFTER she calculated each section's average — that's exactly why HAVING runs after grouping.

## 💻 Real-World Application

| Business Question | SQL Concept Used |
|---|---|
| "Total sales by product category" | GROUP BY category, SUM(sales) |
| "Number of orders per customer" | GROUP BY customer_id, COUNT(*) |
| "Departments with more than 10 employees" | GROUP BY department, HAVING COUNT(*) > 10 |
| "Average rating per restaurant" | GROUP BY restaurant_id, AVG(rating) |
| "Cities with total revenue above ₹1 lakh" | GROUP BY city, HAVING SUM(revenue) > 100000 |

## 🔍 Industry Example
When a **Data Analyst at Zomato** is asked "Which restaurants have received more than 100 orders this month?":
1. They start with the `orders` table containing every single order with a `restaurant_id`.
2. They run:
   ```sql
   SELECT restaurant_id, COUNT(*) AS order_count
   FROM orders
   WHERE order_date BETWEEN '2024-06-01' AND '2024-06-30'
   GROUP BY restaurant_id
   HAVING COUNT(*) > 100
   ORDER BY order_count DESC;
   ```
3. `WHERE` first filters only June's orders.
4. `GROUP BY restaurant_id` groups all remaining orders by restaurant.
5. `COUNT(*)` calculates how many orders each restaurant received.
6. `HAVING COUNT(*) > 100` keeps only the high-performing restaurants.
7. `ORDER BY order_count DESC` shows the busiest restaurant first — ready to be shared with the business team.

## 📊 Diagram

```
   employees table                GROUP BY department
 ┌───────────────────┐          ┌─────────────────────┐
 │ name │ dept │ sal  │          │  IT:  [Ravi, Amit]   │
 ├───────────────────┤   ────▶  │  HR:  [Priya]         │
 │Ravi  │ IT   │30000 │          │  Sales:[Neha, Raj]    │
 │Amit  │ IT   │40000 │          └─────────────────────┘
 │Priya │ HR   │25000 │                    │
 │Neha  │Sales │28000 │                    ▼  SUM(salary)
 │Raj   │Sales │32000 │          ┌─────────────────────┐
 └───────────────────┘          │ IT: 70000             │
                                 │ HR: 25000             │
                                 │ Sales: 60000          │
                                 └─────────────────────┘
                                          │
                                          ▼  HAVING SUM(salary) > 50000
                                 ┌─────────────────────┐
                                 │ IT: 70000             │
                                 │ Sales: 60000          │
                                 └─────────────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| WHERE and HAVING can be used interchangeably | WHERE filters rows before grouping; HAVING filters groups after aggregation — they serve different purposes |
| You can SELECT any column alongside an aggregate without GROUP BY issues | Non-aggregated columns in SELECT must appear in GROUP BY, or the query becomes invalid/unpredictable |
| GROUP BY sorts your results | GROUP BY only groups data; use `ORDER BY` separately to sort the final result |
| HAVING can only be used with GROUP BY | While HAVING is almost always used with GROUP BY, technically it can also filter a single aggregate result over the whole table |

## 💬 Interview Corner
**Q1: What is the main difference between WHERE and HAVING?**
✅ WHERE filters individual rows before grouping/aggregation; HAVING filters groups after aggregation and can use aggregate functions.

**Q2: Can you use an aggregate function inside a WHERE clause?**
✅ No, aggregate functions cannot be used in WHERE — you must use HAVING for that.

**Q3: Write a query to find departments having more than 5 employees.**
✅ `SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 5;`

**Q4: What is the correct order of execution: WHERE, GROUP BY, HAVING, ORDER BY?**
✅ WHERE → GROUP BY → HAVING → ORDER BY (rows filtered first, then grouped, then groups filtered, then sorted).

## 📝 Quick Summary
* 📌 `GROUP BY` splits data into groups based on column values
* 📌 Aggregate functions (COUNT, SUM, AVG, etc.) then operate on each group separately
* 📌 Every non-aggregated column in SELECT must appear in GROUP BY
* 📌 `HAVING` filters groups AFTER aggregation — unlike WHERE which filters rows BEFORE
* 📌 WHERE cannot use aggregate functions; HAVING can
* 📌 Execution order: WHERE → GROUP BY → HAVING → ORDER BY
* 📌 GROUP BY + HAVING powers almost every "breakdown" report in real businesses

## 🎯 Class Activity
Using your `employees` table (with a department column), write a query to find the total salary per department, then extend it using HAVING to show only departments where total salary exceeds a value of your choice. Finally, add ORDER BY to sort the result.

---

# 📋 Assignments — GROUP BY and HAVING

| Assignment |
|---|
| Write a query to find the number of students in each city using GROUP BY. |
| Write a query to find the total salary paid per department. |
| Write a query to find the average price of products grouped by category. |
| Write a query using HAVING to find cities with more than 3 students. |
| Write a query using HAVING to find departments where average salary is above a value of your choice. |
| Combine WHERE, GROUP BY, and HAVING in a single query on your orders/employees table. |
| Explain, in your own words with an example, why `WHERE COUNT(*) > 5` is invalid but `HAVING COUNT(*) > 5` is valid. |
| Write a query to find total order amount per customer, sorted from highest to lowest using ORDER BY. |
| Group your products table by category and find MAX and MIN price in each category. |
| Try writing a GROUP BY query that intentionally selects a non-grouped, non-aggregated column and note the error. |
| Write a query to count the number of orders placed per month (using a date column) if applicable. |
| Design and run a full query combining WHERE, GROUP BY, HAVING, and ORDER BY together on any table of your choice. |

---

# 📚 JOINS: INNER JOIN, LEFT JOIN (and the idea of RIGHT JOIN)

## 🎯 Learning Objectives
* 🎯 Understand why JOINs are needed in a relational database
* 🎯 Learn how INNER JOIN combines matching data from two tables
* 🎯 Learn how LEFT JOIN includes all rows from one table, even without a match
* 🎯 Get a conceptual understanding of RIGHT JOIN
* 🎯 Practice writing JOIN queries using realistic related tables

## 📖 Introduction
So far, we've worked with single tables. But real databases almost always have **multiple related tables** — remember our `students` and `courses` tables connected via `enrollments`? If we want to see a student's name **alongside** their enrolled course name, we need a way to **combine data from multiple tables into one result** — this is exactly what a **JOIN** does.

Why does this matter?
* Relational databases are designed to avoid duplicating data across tables (this is called "normalization").
* But when we need to actually SEE combined information (e.g., "student name + course name"), we must JOIN the related tables back together.

Where is it used?
* Virtually every meaningful report or app screen that shows related information ("Order #123 by Customer Riya for Product XYZ") is built using JOINs behind the scenes.

## 🧠 Detailed Notes

### 1️⃣ Why Do We Need JOINs?
Let's say we have:

`employees` table:

| emp_id | name | department_id |
|---|---|---|
| 1 | Ravi | 10 |
| 2 | Priya | 20 |
| 3 | Aman | NULL |

`departments` table:

| department_id | department_name |
|---|---|
| 10 | IT |
| 20 | HR |
| 30 | Sales |

If we want a report showing "employee name + department name," neither table alone has both pieces of information. We need to **JOIN** them using the shared column `department_id`.

### 2️⃣ INNER JOIN — Only Matching Rows
`INNER JOIN` returns rows **only when there is a match in both tables**. If a row in one table has no matching row in the other, it is **excluded** from the result.

**Syntax:**
```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

**Result:**

| name | department_name |
|---|---|
| Ravi | IT |
| Priya | HR |

Notice: **Aman is missing!** Because his `department_id` is `NULL`, there's no match in the `departments` table, so INNER JOIN excludes him. Also notice "Sales" (department_id 30) doesn't appear either, because no employee belongs to it.

🤔 **Quick Thinking Question:** If an employee has a `department_id` that doesn't exist in the `departments` table at all, will INNER JOIN include that employee in the result?
✅ **Answer:** No — INNER JOIN only includes rows where a match is found in BOTH tables, so an unmatched employee is excluded entirely.

### 3️⃣ LEFT JOIN — All Rows from the Left Table
`LEFT JOIN` (also called `LEFT OUTER JOIN`) returns **ALL rows from the left (first) table**, and matching rows from the right table. If there's no match, the right table's columns simply show `NULL`.

```sql
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

**Result:**

| name | department_name |
|---|---|
| Ravi | IT |
| Priya | HR |
| Aman | NULL |

Now **Aman appears**, but since he has no matching department, `department_name` shows `NULL` for him.

> 💡 **Tip**
>
> "LEFT" refers to the table mentioned FIRST in the FROM clause (before the word JOIN). LEFT JOIN always keeps every row from that first/left table, no matter what.

### 4️⃣ RIGHT JOIN (Conceptual Introduction)
`RIGHT JOIN` (or `RIGHT OUTER JOIN`) is the exact mirror of LEFT JOIN — it returns **ALL rows from the right (second) table**, and matching rows from the left table.

```sql
SELECT employees.name, departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.department_id = departments.department_id;
```

**Result:**

| name | department_name |
|---|---|
| Ravi | IT |
| Priya | HR |
| NULL | Sales |

Now "Sales" appears (because it's guaranteed from the right table), even though no employee belongs to it — so `name` shows `NULL`.

> 💡 **Tip**
>
> In practice, most developers prefer using LEFT JOIN and simply swapping the table order, instead of using RIGHT JOIN — but it's important to understand both conceptually, especially for interviews.

### 5️⃣ Visual Comparison of JOIN Types

| JOIN Type | Keeps All Rows From | Non-Matching Side Shows |
|---|---|---|
| INNER JOIN | Only matched rows from both | Excluded entirely |
| LEFT JOIN | Left (first) table | NULL for right table's columns |
| RIGHT JOIN | Right (second) table | NULL for left table's columns |

### 6️⃣ JOINs with WHERE, GROUP BY (Bringing It All Together)
JOINs can be combined with everything we've learned so far!

```sql
SELECT departments.department_name, COUNT(employees.emp_id) AS emp_count
FROM departments
LEFT JOIN employees
ON departments.department_id = employees.department_id
GROUP BY departments.department_name;
```

This shows the employee count for EVERY department — including departments with ZERO employees (thanks to LEFT JOIN), which an INNER JOIN would have hidden.

🤔 **Quick Thinking Question:** Why might a business specifically want to use LEFT JOIN instead of INNER JOIN when generating a "department headcount" report?
✅ **Answer:** Because with LEFT JOIN, departments with zero employees still show up in the report (with a count of 0), which is important information — INNER JOIN would silently hide empty departments.

### 7️⃣ Using Table Aliases for Cleaner JOINs
```sql
SELECT e.name, d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id;
```

Using short aliases (`e`, `d`) makes JOIN queries shorter and easier to read, especially as queries get more complex.

## 💡 Real-Life Analogy
Think of two separate registers in a school office:
* **Register A (Students)**: Roll Number, Name
* **Register B (Fee Records)**: Roll Number, Fee Paid Status

If the office clerk wants a combined list of "Student Name + Fee Status," she has to **match rows using Roll Number** — flipping between both registers and lining up matching entries. That's exactly what a JOIN does electronically.
* **INNER JOIN** = Only show students who exist in BOTH registers (ignore students missing from either register).
* **LEFT JOIN** = Show ALL students from Register A, even if their fee record is missing in Register B (shown as "Not Found").
* **RIGHT JOIN** = Show ALL fee records from Register B, even if that roll number doesn't exist in Register A anymore.

## 💻 Real-World Application

| Scenario | JOIN Type Used |
|---|---|
| Show only customers who have placed at least one order | INNER JOIN (customers + orders) |
| Show ALL customers, including those who never ordered anything | LEFT JOIN (customers + orders) |
| Show ALL products, including ones with zero sales | LEFT JOIN (products + order_items) |
| Combine employee details with their department name | INNER JOIN (employees + departments) |
| Show every department, even ones with no employees assigned yet | LEFT JOIN (departments + employees) |

## 🔍 Industry Example
When a **Marketing Analyst at Myntra** wants to identify "customers who have NEVER placed an order" (to send them a discount coupon):
1. They start with the `customers` table (containing ALL registered customers) and the `orders` table (containing only customers who've actually ordered).
2. They run:
   ```sql
   SELECT c.customer_id, c.name
   FROM customers c
   LEFT JOIN orders o
   ON c.customer_id = o.customer_id
   WHERE o.order_id IS NULL;
   ```
3. `LEFT JOIN` keeps ALL customers, and for customers with no orders, `o.order_id` naturally becomes `NULL`.
4. The `WHERE o.order_id IS NULL` line then filters down to ONLY those customers who never ordered anything.
5. This exact list is then used to trigger a "We miss you! Here's 20% off" email campaign — a very common real-world use of LEFT JOIN.

## 📊 Diagram

```
   employees                    departments
 ┌───────────────┐          ┌───────────────────┐
 │ emp_id │dept_id│         │dept_id│ dept_name   │
 ├───────────────┤          ├───────────────────┤
 │  1     │  10   │────────▶│  10   │  IT          │
 │  2     │  20   │────────▶│  20   │  HR          │
 │  3     │ NULL  │    ✗    │  30   │  Sales       │
 └───────────────┘          └───────────────────┘

  INNER JOIN  →  [Ravi-IT, Priya-HR]                (Aman & Sales excluded)
  LEFT JOIN   →  [Ravi-IT, Priya-HR, Aman-NULL]       (all employees kept)
  RIGHT JOIN  →  [Ravi-IT, Priya-HR, NULL-Sales]      (all departments kept)
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| JOIN combines tables side-by-side randomly | JOIN combines rows based on a matching condition specified in `ON`, not randomly |
| INNER JOIN and LEFT JOIN always give the same result | They differ whenever there are unmatched rows — INNER JOIN excludes them, LEFT JOIN keeps them (with NULLs) |
| LEFT JOIN keeps all rows from BOTH tables | LEFT JOIN keeps all rows only from the LEFT (first-mentioned) table |
| You can only JOIN two tables at a time | You can JOIN as many tables as needed by chaining multiple JOIN clauses |
| Forgetting the `ON` condition is harmless | Forgetting `ON` (or using a wrong join type like CROSS JOIN accidentally) can produce a huge, incorrect result combining every row with every other row |

## 💬 Interview Corner
**Q1: What is the difference between INNER JOIN and LEFT JOIN?**
✅ INNER JOIN returns only rows with matches in both tables; LEFT JOIN returns all rows from the left table, with NULLs where there's no match in the right table.

**Q2: How would you find customers who have never placed an order?**
✅ Use a LEFT JOIN from customers to orders, then filter with `WHERE orders.order_id IS NULL`.

**Q3: What does RIGHT JOIN do?**
✅ It returns all rows from the right (second) table, along with matching rows from the left table, showing NULL where there's no match.

**Q4: Can INNER JOIN return more rows than either original table?**
✅ Yes, if there are multiple matches on both sides (e.g., one department matching multiple employees), the result can have more rows than either single table.

## 📝 Quick Summary
* 📌 JOINs combine related data from two or more tables using a shared column
* 📌 `INNER JOIN` returns only rows that match in both tables
* 📌 `LEFT JOIN` returns all rows from the left table, with NULLs for unmatched right-table columns
* 📌 `RIGHT JOIN` is the mirror of LEFT JOIN, keeping all rows from the right table
* 📌 LEFT JOIN + `IS NULL` is a powerful pattern to find "missing" or "unmatched" relationships
* 📌 Table aliases (e.g., `e`, `d`) make JOIN queries cleaner and easier to read
* 📌 JOINs work seamlessly with WHERE, GROUP BY, and HAVING for advanced reports

## 🎯 Class Activity
Using your `employees` and `departments` tables (or `students`, `courses`, `enrollments`), write one INNER JOIN query and one LEFT JOIN query that produce different results. Discuss with a classmate why the row counts differ.

---

# 📋 Assignments — JOINS: INNER JOIN, LEFT JOIN, RIGHT JOIN

| Assignment |
|---|
| Write an INNER JOIN query combining your employees and departments tables to show employee name with department name. |
| Write a LEFT JOIN query on the same tables and compare the row count/result with the INNER JOIN version. |
| Insert an employee with a department_id that doesn't exist in the departments table, then re-run both JOIN queries and observe the difference. |
| Write a LEFT JOIN query to find all customers who have never placed an order (using customers and orders tables). |
| Write an INNER JOIN query combining students, enrollments, and courses to show student name with their enrolled course name. |
| Write a query using RIGHT JOIN (or explain conceptually if your database doesn't support it) between departments and employees. |
| Use table aliases in at least 2 of your JOIN queries above to make them shorter. |
| Combine a LEFT JOIN with GROUP BY to count the number of employees per department, including departments with zero employees. |
| Write a JOIN query and add a WHERE clause to filter results further (e.g., only employees earning above a certain salary). |
| Explain, with a real example from an app you use, a scenario where LEFT JOIN would be more useful than INNER JOIN. |
| Draw a diagram (by hand or digitally) showing how INNER JOIN and LEFT JOIN would differ for your students/courses tables. |
| Chain three tables together in one JOIN query (e.g., students + enrollments + courses) and display 4 relevant columns from across all three. |

---

# 📚 Practical Exercises with Related Tables (Employee-Department, Customer-Orders)

## 🎯 Learning Objectives
* 🎯 Apply filtering, aggregation, GROUP BY/HAVING, and JOINs together in realistic scenarios
* 🎯 Practice writing complete queries against an Employee-Department schema
* 🎯 Practice writing complete queries against a Customer-Orders schema
* 🎯 Build confidence solving "business questions" using SQL, just like in real jobs
* 🎯 Understand how to break down a complex business question into a step-by-step query

## 📖 Introduction
Over the last few topics, we've learned individual SQL tools: filtering (WHERE, BETWEEN, IN, LIKE), summarizing (COUNT, SUM, AVG, MAX, MIN), grouping (GROUP BY, HAVING), and connecting tables (JOINs). But in the real world, you rarely use just ONE of these at a time — **real business questions require combining several of these tools together**.

Why does this matter?
* Interview questions and real job tasks almost always sound like: "Find the department with the highest average salary among employees older than 30" — this needs WHERE + JOIN + GROUP BY + AVG + ORDER BY, all in one query!
* Practicing on realistic schemas (Employee-Department, Customer-Orders) builds the exact muscle memory you'll need on the job.

Where is it used?
* This is EXACTLY what Data Analysts, Backend Developers, and Business Intelligence professionals do every single day — translating a business question into a working SQL query.

## 🧠 Detailed Notes

### 1️⃣ Setting Up Our Practice Schemas
For this practical topic, let's assume these two schemas already exist (as designed in our earlier "Designing Simple Schemas" topic):

**Employee-Department Schema:**
```sql
departments(department_id, department_name)
employees(emp_id, full_name, age, salary, department_id)
```

**Customer-Orders Schema:**
```sql
customers(customer_id, full_name, city)
products(product_id, product_name, price)
orders(order_id, customer_id, product_id, quantity, order_date, status)
```

### 2️⃣ Employee-Department: Step-by-Step Practical Queries

**Question A: "List all employees along with their department name."**
```sql
SELECT e.full_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```

**Question B: "Find the average salary per department."**
```sql
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```

**Question C: "Find departments where the average salary is above ₹50,000."**
```sql
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 50000;
```

**Question D: "List all departments, including those with zero employees, along with headcount."**
```sql
SELECT d.department_name, COUNT(e.emp_id) AS headcount
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
```

🤔 **Quick Thinking Question:** In Question D, why did we start the FROM clause with `departments` instead of `employees`?
✅ **Answer:** Because we want ALL departments (even empty ones) to appear, and LEFT JOIN always keeps every row from the table mentioned first (the "left" table) — so `departments` must come first.

**Question E: "Find employees aged between 25 and 40 working in the 'IT' or 'Sales' department."**
```sql
SELECT e.full_name, e.age, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.age BETWEEN 25 AND 40
  AND d.department_name IN ('IT', 'Sales');
```

### 3️⃣ Customer-Orders: Step-by-Step Practical Queries

**Question F: "List all orders along with the customer's name and the product name."**
```sql
SELECT o.order_id, c.full_name, p.product_name, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id;
```

**Question G: "Find the total amount spent by each customer."**
```sql
SELECT c.full_name, SUM(o.quantity * p.price) AS total_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY c.full_name;
```

**Question H: "Find customers who have spent more than ₹5,000 in total."**
```sql
SELECT c.full_name, SUM(o.quantity * p.price) AS total_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY c.full_name
HAVING SUM(o.quantity * p.price) > 5000;
```

**Question I: "Find customers who have NEVER placed an order."**
```sql
SELECT c.full_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

**Question J: "Find the best-selling product (highest total quantity sold)."**
```sql
SELECT p.product_name, SUM(o.quantity) AS total_sold
FROM orders o
INNER JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
```

*(We'll learn `LIMIT`/`TOP` to get just the #1 result in later topics — for now, `ORDER BY DESC` puts the top seller at the very top of the list.)*

🤔 **Quick Thinking Question:** In Question J, why did we use `SUM(o.quantity)` instead of `COUNT(*)`?
✅ **Answer:** Because a single order row might have a quantity greater than 1 (e.g., ordering 3 units of the same product), so `SUM(quantity)` gives the true total units sold, while `COUNT(*)` would only count the number of order rows, not actual units.

### 4️⃣ A Framework for Solving Any Business Question
When faced with any business question, follow this thinking process:

1. **Identify which tables** contain the information needed.
2. **Decide the JOIN type** — INNER (only matches) or LEFT (keep all from one side, even unmatched).
3. **Apply WHERE** if you need to filter individual rows (e.g., a specific date range or age).
4. **Apply GROUP BY** if the question mentions "per," "each," or "by" (e.g., "sales per city").
5. **Apply HAVING** if the question filters on a summarized value (e.g., "more than," "average above").
6. **Apply ORDER BY** if the question asks for "highest," "lowest," "top," or "ranked."

> 💡 **Tip**
>
> Keywords like "total," "average," "how many," "per," "each," and "more than X" are strong hints about which SQL clauses you'll need!

## 💡 Real-Life Analogy
Solving a real business SQL question is like being a **detective solving a case using multiple pieces of evidence**:
* Each **table** is a separate file of clues (Employee records, Department records).
* **JOIN** is connecting clues from different files that relate to the same case.
* **WHERE** is ignoring irrelevant clues (e.g., ignoring witnesses outside the relevant time window).
* **GROUP BY** is organizing clues into related categories (e.g., grouping suspects by location).
* **HAVING** is narrowing down groups based on a pattern (e.g., "only groups with more than 3 suspects").
* **ORDER BY** is ranking your final list of suspects by likelihood.

Just like a detective doesn't use just ONE clue-gathering method, a good SQL query often combines several of these techniques together.

## 💻 Real-World Application

| Business Question | SQL Concepts Combined |
|---|---|
| "Top 5 customers by total spend this year" | JOIN + WHERE + GROUP BY + SUM + ORDER BY |
| "Departments with average salary above company average" | JOIN + GROUP BY + HAVING |
| "Products that have never been ordered" | LEFT JOIN + WHERE IS NULL |
| "Monthly revenue trend for the last 6 months" | WHERE (date range) + GROUP BY (month) + SUM |
| "Employees who joined in 2023 and earn above ₹40,000" | WHERE (date + salary conditions combined with AND) |

## 🔍 Industry Example
When an **HR Analyst at TCS** is asked: *"Show me every department along with its headcount and average salary, but only for departments with more than 20 employees, sorted by average salary from highest to lowest"*:

1. They break the question down using our framework:
   * Tables needed: `employees`, `departments` → needs a JOIN
   * "along with its headcount" → needs COUNT + GROUP BY
   * "average salary" → needs AVG
   * "only for departments with more than 20 employees" → needs HAVING (since it filters on COUNT, an aggregate)
   * "sorted by average salary...highest to lowest" → needs ORDER BY ... DESC

2. They write the final query:
   ```sql
   SELECT d.department_name, 
          COUNT(e.emp_id) AS headcount, 
          AVG(e.salary) AS avg_salary
   FROM departments d
   LEFT JOIN employees e ON d.department_id = e.department_id
   GROUP BY d.department_name
   HAVING COUNT(e.emp_id) > 20
   ORDER BY avg_salary DESC;
   ```
3. This single, well-structured query answers a complex business question instantly — something that would take hours to calculate manually in a spreadsheet with thousands of employee records.

## 📊 Diagram

```
   Business Question
          │
          ▼
 ┌─────────────────────────────────────────────┐
 │ 1. Which tables? ──────▶ JOIN                 │
 │ 2. Filter rows? ───────▶ WHERE                │
 │ 3. "per/each/by"? ─────▶ GROUP BY             │
 │ 4. Filter on totals? ──▶ HAVING               │
 │ 5. "top/highest/rank"?─▶ ORDER BY             │
 └─────────────────────────────────────────────┘
          │
          ▼
      Final SQL Query
          │
          ▼
      Business Answer 📊
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| You need to memorize a fixed query for every possible business question | Learn the framework (JOIN→WHERE→GROUP BY→HAVING→ORDER BY) and adapt it to any question |
| JOIN order (INNER vs LEFT) doesn't really matter | It changes whether unmatched rows (e.g., customers with zero orders) appear in your results — always matters! |
| Combining WHERE and HAVING in the same query is not allowed | It's very common and correct — WHERE filters rows first, HAVING filters the resulting groups afterward |
| Complex business questions need special new SQL commands | Most complex questions are solved by combining the SAME basic clauses (JOIN, WHERE, GROUP BY, HAVING, ORDER BY) thoughtfully |

## 💬 Interview Corner
**Q1: How would you find the total number of orders placed by each customer, including customers with zero orders?**
✅ Use a LEFT JOIN from customers to orders, then GROUP BY customer, using COUNT(orders.order_id) so customers with no orders show 0.

**Q2: How do you find the department with the highest average employee salary?**
✅ JOIN employees and departments, GROUP BY department, calculate AVG(salary), then use ORDER BY avg_salary DESC (and LIMIT 1 if supported) to get the top result.

**Q3: A business question says "total spend by customer, but only show customers who spent more than ₹10,000." What clause do you need in addition to GROUP BY?**
✅ HAVING — because "more than ₹10,000" is a condition on the aggregated SUM, which requires HAVING rather than WHERE.

**Q4: What is the general order of clauses in a complete SQL query using JOIN, WHERE, GROUP BY, HAVING, and ORDER BY?**
✅ `SELECT ... FROM ... JOIN ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...` — matching that same logical execution flow.

## 📝 Quick Summary
* 📌 Real business questions almost always combine multiple SQL concepts together
* 📌 Use JOINs to bring related tables together (INNER for matches only, LEFT to keep all from one side)
* 📌 Use WHERE to filter individual rows before any grouping happens
* 📌 Use GROUP BY whenever a question asks for results "per," "each," or "by" some category
* 📌 Use HAVING to filter on aggregated/summarized values (totals, averages, counts)
* 📌 Use ORDER BY to rank or sort final results (highest to lowest, or vice versa)
* 📌 A simple 5-step framework (tables → JOIN type → WHERE → GROUP BY → HAVING → ORDER BY) can solve almost any business SQL question
* 📌 This exact skill — translating business questions into SQL — is used daily by real Data Analysts and Backend Developers

## 🎯 Class Activity
Using your Employee-Department and Customer-Orders tables, solve these 3 questions completely on your own: (1) Find the department with the most employees. (2) Find the total revenue generated by each product. (3) Find customers from a specific city who have spent more than a chosen amount. Compare your final queries with a classmate's approach.

---

# 📋 Assignments — Practical Exercises with Related Tables

| Assignment |
|---|
| Write a query to list all employees with their department names using INNER JOIN. |
| Write a query to find the average salary per department, sorted from highest to lowest. |
| Write a query to find departments with more than 3 employees using HAVING. |
| Write a query to list all departments (including empty ones) with their employee headcount using LEFT JOIN. |
| Write a query to find employees aged 25-40 working in 2 specific departments of your choice. |
| Write a query listing all orders with customer name and product name using multiple INNER JOINs. |
| Write a query to find total amount spent by each customer, sorted highest to lowest. |
| Write a query to find customers who spent more than a chosen amount, using HAVING. |
| Write a query to find customers who have never placed an order, using LEFT JOIN and IS NULL. |
| Write a query to find the best-selling product by total quantity sold. |
| Pick any 2 realistic business questions of your own (e.g., about a college or gym) and write full SQL queries combining JOIN, WHERE, GROUP BY, HAVING, and ORDER BY to answer them. |
| Create a one-page cheat sheet (in your own words) summarizing when to use WHERE vs HAVING vs GROUP BY vs JOIN, with one example each. |
| Take any single complex business question from your workplace/college idea and manually break it down step-by-step using the 5-step framework before writing the SQL. |