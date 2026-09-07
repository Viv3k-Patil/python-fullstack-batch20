# 📚 What is SQL?

## 🎯 Learning Objectives
By the end of this topic, you will be able to:
* 🎯 Understand what SQL is and why it exists
* 🎯 Explain the difference between SQL and a database
* 🎯 Identify where SQL is used in real-world software
* 🎯 Understand the main categories of SQL commands (DDL, DML, DQL, DCL, TCL)
* 🎯 Run your very first SQL statement

## 📖 Introduction
Imagine you have a huge steel cupboard full of files — customer records, employee salaries, product lists. Now imagine you want to ask that cupboard a question like *"Give me all customers from Mumbai who bought something last month."* A cupboard can't answer that. But a **database** can — if you know how to "talk" to it.

**SQL (Structured Query Language)** is exactly that — the language we use to **talk to databases**. It is not a programming language like Python (no loops, no if-else in the traditional sense in basic SQL); it is a **special-purpose language** designed to **store, retrieve, update, and delete data** inside a database.

Why does SQL exist?
* Before SQL, programmers had to write custom code to search through files manually — slow and error-prone.
* SQL gives everyone a **common, simple, English-like language** to interact with data.
* It was developed by IBM in the 1970s and is now the **industry standard** for relational databases.

Where is SQL used?
* 🛒 E-commerce websites (Amazon, Flipkart) — storing products, orders, customers
* 🏦 Banking systems — storing accounts, transactions
* 📱 Every mobile app with a login system — storing usernames and passwords
* 📊 Data analytics — querying millions of rows to find trends

> 💡 **Tip**
>
> As a Full-Stack Developer, your Python backend will **talk to a database using SQL** to save and fetch data for your website or app.

## 🧠 Detailed Notes

### 1️⃣ What Exactly is SQL?
SQL stands for **Structured Query Language**. It is used to interact with **Relational Database Management Systems (RDBMS)** like MySQL, PostgreSQL, Oracle, and SQL Server.

Think of SQL as a set of **instructions** you give to the database:
* "Create a table for me"
* "Insert this new record"
* "Show me all records where age > 18"
* "Delete this old record"

### 2️⃣ Categories of SQL Commands
SQL commands are grouped into five categories:

| Category | Full Form | Purpose | Example Commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Defines structure of database | CREATE, ALTER, DROP |
| **DML** | Data Manipulation Language | Manipulates data inside tables | INSERT, UPDATE, DELETE |
| **DQL** | Data Query Language | Fetches/reads data | SELECT |
| **DCL** | Data Control Language | Controls access/permissions | GRANT, REVOKE |
| **TCL** | Transaction Control Language | Manages transactions | COMMIT, ROLLBACK |

🤔 **Quick Thinking Question:** If you wanted to create a new table for storing student data, which category of SQL command would you use?
✅ **Answer:** DDL (Data Definition Language) — specifically the `CREATE TABLE` command, because you are defining the *structure*, not adding data yet.

### 3️⃣ Your First SQL Statement
Let's write a very simple SQL query. Even though this course focuses on DDL/DML, let's peek at a SELECT statement to see SQL "in action":

```sql
SELECT * FROM students;
```

This simply means: "Show me everything (`*`) from the table called `students`."

### 4️⃣ SQL is Declarative, Not Procedural
In Python, you tell the computer **how** to do something, step by step:

```python
for student in students:
    if student.age > 18:
        print(student.name)
```

In SQL, you just tell it **what** you want, and the database figures out how:

```sql
SELECT name FROM students WHERE age > 18;
```

This is the biggest mindset shift beginners need to make — SQL is about describing the **result**, not the **process**.

> ⚠️ **Important**
>
> SQL keywords are **not case-sensitive** (`SELECT` = `select`), but it's an industry convention to write keywords in **UPPERCASE** and table/column names in **lowercase** for readability.

## 💡 Real-Life Analogy
Think of a **database** as a **library**, and **SQL** as the **language you use to talk to the librarian**.

* You don't go and search every shelf yourself (that's what old-style programming felt like).
* You simply tell the librarian: "I want all books written by J.K. Rowling published after 2005."
* The librarian (the database engine) understands your request (written in SQL) and fetches exactly what you asked for.

## 💻 Real-World Application

| Company/Product | How SQL is Used |
|---|---|
| 🛒 Amazon | Storing product catalog, orders, customer data |
| 🏦 HDFC Bank | Storing account balances and transaction history |
| 📸 Instagram | Storing user profiles, follower relationships |
| 🚕 Uber | Storing ride history, driver and rider details |
| 🎓 College ERP systems | Storing student records, attendance, marks |

## 🔍 Industry Example
When a **Backend Developer at Zomato** builds the "My Orders" page, here's what happens internally:
1. The user opens the app and taps "My Orders."
2. The Python backend (built with Django/Flask) receives this request.
3. The backend runs an SQL query like `SELECT * FROM orders WHERE user_id = 101;`
4. The database engine (MySQL/PostgreSQL) searches its `orders` table and returns matching rows.
5. The backend converts this data into JSON and sends it to the app.
6. The app displays the order history to the user.

All of this happens in **milliseconds**, and SQL is the language that made step 3 possible.

## 📊 Diagram

```
   ┌─────────────┐        SQL Query        ┌──────────────────┐
   │   Python    │ ───────────────────────▶ │    Database       │
   │  Backend    │                          │  (MySQL/Postgres) │
   │             │ ◀─────────────────────── │                   │
   └─────────────┘        Result Data       └──────────────────┘
        │
        ▼
   ┌─────────────┐
   │   Website   │
   │   / App UI  │
   └─────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| SQL is a full programming language like Python | SQL is a special-purpose language only for interacting with databases |
| SQL and a database are the same thing | SQL is the *language*; the database is the *software/storage system* |
| All databases use the exact same SQL | Most SQL is similar, but each RDBMS (MySQL, PostgreSQL, Oracle) has small syntax differences |
| You need SQL only for large companies | Even small apps (to-do lists, blogs) use SQL databases |

## 💬 Interview Corner
**Q1: What does SQL stand for?**
✅ Structured Query Language — used to communicate with relational databases.

**Q2: Is SQL case-sensitive?**
✅ Keywords are not case-sensitive, but some databases treat table/column names as case-sensitive depending on OS/configuration.

**Q3: Name the five categories of SQL commands.**
✅ DDL, DML, DQL, DCL, TCL.

**Q4: Is SQL a programming language?**
✅ It's a domain-specific/declarative language for data, not a general-purpose programming language like Python or Java.

## 📝 Quick Summary
* 📌 SQL = Structured Query Language, used to talk to databases
* 📌 It lets us Create, Read, Update, Delete data (CRUD)
* 📌 SQL commands are grouped into DDL, DML, DQL, DCL, TCL
* 📌 SQL is declarative — you describe *what* you want, not *how*
* 📌 Used across almost every industry: banking, e-commerce, social media
* 📌 As a full-stack developer, your backend code will send SQL queries to the database
* 📌 Different RDBMS (MySQL, PostgreSQL) have mostly similar SQL syntax

## 🎯 Class Activity
Install MySQL Workbench or use an online SQL playground (like sqliteonline.com). Type and run: `SELECT 'Hello SQL World';` and take a screenshot of the output. Discuss with your neighbor what you think happened internally.

---

# 📋 Assignments — What is SQL?

| Assignment |
|---|
| Write in your own words (3-4 lines) what SQL is, without copying the definition from notes. |
| List 5 apps/websites you use daily and guess what kind of data they might store in a database. |
| Install any one SQL tool (MySQL Workbench, DBeaver, or an online SQL editor) on your laptop. |
| Run the query `SELECT 'My name is <yourname>';` and take a screenshot. |
| Research and write down 2 differences between SQL and Python. |
| Find out which SQL category (DDL/DML/DQL/DCL/TCL) each of these belongs to: CREATE, SELECT, DELETE, GRANT. |
| Write down 3 real-world scenarios (other than the ones in class) where SQL might be used. |
| Search online for "Top 5 RDBMS in the industry" and list them with one line about each. |
| Explain in your own words why SQL is called a "declarative" language. |
| Try running an invalid SQL query (e.g., `SELET * FROM abc;`) and note down the error message shown. |
| Find out the name of the database engine used by any one app installed on your phone (research online). |
| Write one paragraph on "Why would a Full Stack Developer need to learn SQL?" |

---

# 📚 RDBMS & Schema Concepts

## 🎯 Learning Objectives
* 🎯 Understand what RDBMS means and how it differs from a plain file system
* 🎯 Learn the core building blocks: database, table, row, column
* 🎯 Understand what a "schema" is and why it matters
* 🎯 Understand relationships between tables (conceptually)
* 🎯 Identify popular RDBMS software used in the industry

## 📖 Introduction
Imagine storing all your college's student data in a single Excel-like sheet, but now imagine 10,000 students, 50 courses, and 200 teachers — all connected to each other. A random spreadsheet becomes messy and error-prone very quickly.

This is where an **RDBMS (Relational Database Management System)** comes in. It is **software** that stores data in a structured, organized way using **tables** that can be **related** to each other — hence the word "relational."

Why does RDBMS exist?
* Plain files (like .txt or .csv) don't enforce rules — you could accidentally save "abc" in an age field.
* RDBMS enforces structure, prevents duplicate/invalid data, and allows super-fast searching even with millions of records.
* It allows multiple tables to be **linked** together (e.g., a `students` table linked to a `courses` table).

Where is it used?
* Every serious backend system — banking, healthcare, e-commerce, education, government portals — all use an RDBMS to store their core data.

## 🧠 Detailed Notes

### 1️⃣ What is RDBMS?
RDBMS = **R**elational **D**atabase **M**anagement **S**ystem. It is software that manages databases where data is stored in the form of **tables** (rows and columns), and tables can be **related** to one another.

Popular RDBMS software:

| RDBMS | Owned By | Common Use |
|---|---|---|
| MySQL | Oracle (Open Source) | Web applications, startups |
| PostgreSQL | Open Source Community | Complex applications, analytics |
| Oracle DB | Oracle Corporation | Large enterprises, banks |
| SQL Server | Microsoft | Enterprise Windows-based systems |
| SQLite | Open Source | Mobile apps, small/embedded systems |

### 2️⃣ Building Blocks of RDBMS
Let's break down the hierarchy:

```
Database
   └── Table (e.g., students)
          ├── Column (e.g., name, age, city)
          └── Row (one actual student's record)
```

| Term | Meaning | Analogy |
|---|---|---|
| Database | Container holding all tables | An almirah/cupboard |
| Table | Structure to store similar data | A single drawer in the almirah |
| Column (Field) | A specific attribute of data | Labels on the drawer (Name, Age) |
| Row (Record) | One complete entry | One filled-in form inside the drawer |

Example table `students`:

| student_id | name | age | city |
|---|---|---|---|
| 1 | Riya | 20 | Pune |
| 2 | Aman | 22 | Delhi |

Here:
* `students` is the **table**
* `student_id, name, age, city` are **columns**
* Each horizontal line (Riya's data, Aman's data) is a **row**

🤔 **Quick Thinking Question:** If a table has 4 columns and 100 students, how many rows does it have?
✅ **Answer:** 100 rows — one row per student, regardless of the number of columns.

### 3️⃣ What is a Schema?
A **schema** is the **blueprint or structure** of a database — it defines what tables exist, what columns each table has, what data type each column holds, and how tables relate to each other. It does **not** include the actual data — just the design.

Think of schema as the **architectural plan of a house** — it shows where the rooms are, but doesn't include the furniture (that's the actual data).

Example schema description (conceptual, not code):
```
Database: college_db
 └── Table: students (student_id, name, age, city)
 └── Table: courses  (course_id, course_name, duration)
 └── Table: enrollments (enrollment_id, student_id, course_id)
```

### 4️⃣ Relationships Between Tables (Conceptual)
In RDBMS, tables are rarely alone — they are **connected**. For example, a `students` table can be connected to a `courses` table through an `enrollments` table.

Types of relationships (conceptual overview — we'll go deeper when we cover Foreign Keys):
* **One-to-One** — One student has one ID card
* **One-to-Many** — One teacher teaches many students
* **Many-to-Many** — Many students enroll in many courses

🤔 **Quick Thinking Question:** A single customer can place multiple orders on Amazon. What type of relationship is this?
✅ **Answer:** One-to-Many (one customer → many orders).

## 💡 Real-Life Analogy
An RDBMS is like a **well-organized steel cupboard with labeled drawers**:
* The **cupboard** = Database
* Each **drawer** = Table (e.g., one drawer for "Students," one for "Employees")
* The **label on the drawer** (Name, Age, City) = Columns
* Each **file inside the drawer** = a Row

And the **schema** is like the **instruction manual** that says "Drawer 1 must only contain Name (text), Age (number), and City (text) — nothing else."

## 💻 Real-World Application

| Domain | Example Tables in Schema |
|---|---|
| 🏫 School ERP | students, teachers, classes, attendance |
| 🏥 Hospital System | patients, doctors, appointments, bills |
| 🛒 E-commerce | products, customers, orders, payments |
| 🏦 Banking | accounts, transactions, branches, loans |

## 🔍 Industry Example
When a **Database Administrator (DBA) at Swiggy** is asked to design the system for a new "Group Order" feature, here's what happens:
1. The DBA first identifies the key entities: `users`, `restaurants`, `orders`, `group_orders`.
2. They design a **schema**: deciding what columns each table needs (e.g., `group_orders` needs `group_id`, `host_user_id`, `restaurant_id`).
3. They define relationships: one `group_order` connects to many `users` (many-to-many via a junction table).
4. This schema is reviewed by the backend team before any table is actually created in the RDBMS.
5. Only after the schema is finalized does the developer run `CREATE TABLE` statements (which we'll study next).

## 📊 Diagram

```
        college_db  (DATABASE)
        ┌─────────────────────────────────────┐
        │                                       │
        │   ┌─────────────┐    ┌─────────────┐ │
        │   │  students   │    │   courses    │ │
        │   ├─────────────┤    ├─────────────┤ │
        │   │ student_id  │    │ course_id    │ │
        │   │ name        │    │ course_name  │ │
        │   │ age         │    │ duration     │ │
        │   │ city        │    └─────────────┘ │
        │   └──────┬──────┘           ▲         │
        │          │                  │         │
        │          ▼                  │         │
        │   ┌───────────────────────┐ │         │
        │   │     enrollments       │─┘         │
        │   │ (student_id,course_id)│           │
        │   └───────────────────────┘           │
        └─────────────────────────────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| Database and Table mean the same thing | A database is a container that holds *many* tables |
| Schema means the actual data stored | Schema is the *structure/design*, not the data itself |
| All tables in a database must be related | Tables *can* exist independently, but relationships add power |
| RDBMS is just Excel with a fancy name | RDBMS enforces rules, relationships, and can handle millions of records reliably |

## 💬 Interview Corner
**Q1: What is RDBMS?**
✅ Software that manages data stored in related tables, following rules to keep data structured and consistent.

**Q2: What is a schema?**
✅ The blueprint/structure of a database — defining tables, columns, data types, and relationships, without the actual data.

**Q3: What is the difference between a row and a column?**
✅ A column is an attribute (like "age"), while a row is one complete record (like one student's full data).

**Q4: Give an example of a one-to-many relationship.**
✅ One teacher teaches many students — one row in `teachers` relates to many rows in `students`.

## 📝 Quick Summary
* 📌 RDBMS = software to manage data in related tables
* 📌 Database → Table → Column → Row is the hierarchy
* 📌 Schema is the blueprint/design of the database, not the actual data
* 📌 Tables can have relationships: One-to-One, One-to-Many, Many-to-Many
* 📌 Popular RDBMS: MySQL, PostgreSQL, Oracle, SQL Server, SQLite
* 📌 Good schema design is done *before* creating actual tables
* 📌 RDBMS prevents messy, duplicate, or invalid data compared to plain files

## 🎯 Class Activity
On paper or in a text file, design a simple schema (just table names and column names — no actual SQL yet) for a "Library Management System" with at least 3 tables (e.g., books, members, issued_books). Share it with a classmate and compare designs.

---

# 📋 Assignments — RDBMS & Schema Concepts

| Assignment |
|---|
| Draw the hierarchy Database → Table → Row → Column using your own example (not students/courses). |
| Design a schema (table names + column names only) for an "Online Food Delivery" app with at least 4 tables. |
| Identify whether these relationships are One-to-One, One-to-Many, or Many-to-Many: (a) Passport to Person (b) Author to Books (c) Students to Courses. |
| Research and note down 3 differences between MySQL and PostgreSQL. |
| List 5 columns you would expect in an "employees" table of a company. |
| Find out what "primary entity" and "junction table" mean (quick internet research) and write 2 lines on each. |
| Sketch (by hand or digitally) a diagram showing 3 related tables for a "Hospital Management System." |
| Explain in your own words why a spreadsheet is not the same as an RDBMS. |
| Visit an online SQL tool and explore its "schema" or "database structure" viewer if available; take a screenshot. |
| Write down the schema (tables + columns) for a "Movie Ticket Booking" system with at least 3 tables. |
| Identify what type of RDBMS (if any) is used by a college/company you know, by searching online or asking someone. |

---

# 📚 DDL: CREATE TABLE, ALTER TABLE, DROP TABLE

## 🎯 Learning Objectives
* 🎯 Understand what DDL (Data Definition Language) means
* 🎯 Learn how to create a new table using `CREATE TABLE`
* 🎯 Learn how to modify an existing table using `ALTER TABLE`
* 🎯 Learn how to remove a table using `DROP TABLE`
* 🎯 Understand the difference between DROP, DELETE, and TRUNCATE (conceptually)

## 📖 Introduction
So far, we've talked about databases and schemas as *concepts* — like an architect's drawing on paper. Now it's time to actually **build** the house. DDL (Data Definition Language) is the set of SQL commands used to **create, modify, and delete the structure** of database objects like tables.

Why does DDL exist?
* Before we can store any data, we need a "container" (table) with defined columns and data types.
* DDL commands let us design and later reshape that container as requirements change (e.g., adding a new column when the business needs more info).

Where is it used?
* Every time a developer sets up a new feature that needs to store data (e.g., adding a "Wishlist" feature to an e-commerce app), a DDL `CREATE TABLE` command is run first.

> ⚠️ **Important**
>
> DDL commands affect the **structure**, not the individual data rows. Think "structure first, data later."

## 🧠 Detailed Notes

### 1️⃣ CREATE TABLE — Building the Structure
The `CREATE TABLE` command is used to create a brand-new table.

**Syntax:**
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

**Example:**
```sql
CREATE TABLE students (
    student_id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);
```

Let's break this down:
* `CREATE TABLE students` → "I want to create a table named students."
* Inside the brackets, each line defines one **column name** and its **data type**.
* `INT` = whole number, `VARCHAR(50)` = text with a maximum of 50 characters.

🤔 **Quick Thinking Question:** What would happen if you tried to insert the text "Twenty" into the `age` column defined as `INT`?
✅ **Answer:** It would throw an error, because `INT` only accepts whole numbers, not text like "Twenty".

### 2️⃣ ALTER TABLE — Modifying an Existing Table
Once a table is created, requirements often change. Maybe you forgot a column, or a business decision requires a new field. `ALTER TABLE` lets us modify the table structure **without losing existing data**.

**Adding a new column:**
```sql
ALTER TABLE students ADD COLUMN email VARCHAR(100);
```

**Modifying a column's data type:**
```sql
ALTER TABLE students MODIFY COLUMN age SMALLINT;
```
*(Note: syntax for modifying varies slightly between MySQL `MODIFY` and PostgreSQL `ALTER COLUMN ... TYPE`.)*

**Renaming a column:**
```sql
ALTER TABLE students RENAME COLUMN city TO hometown;
```

**Dropping (removing) a column:**
```sql
ALTER TABLE students DROP COLUMN email;
```

> 💡 **Tip**
>
> `ALTER TABLE` is like renovating a house room by room — you're not demolishing it, just changing parts of it.

### 3️⃣ DROP TABLE — Deleting the Entire Table
`DROP TABLE` permanently removes a table **and all its data** from the database. This is different from just deleting rows.

**Syntax:**
```sql
DROP TABLE students;
```

⚠️ Once you run this, the table structure AND all the data inside it are **gone forever** (unless you have a backup).

### 4️⃣ DROP vs DELETE vs TRUNCATE (Important Distinction)

| Command | Type | What it Removes | Structure Remains? | Can Rollback? |
|---|---|---|---|---|
| `DROP TABLE` | DDL | Entire table + structure + data | ❌ No | ❌ Usually No |
| `TRUNCATE TABLE` | DDL | All rows (data only) | ✅ Yes | ❌ Usually No |
| `DELETE FROM table` | DML | Rows (all or selected via WHERE) | ✅ Yes | ✅ Yes (if inside transaction) |

🤔 **Quick Thinking Question:** If you want to remove only the *data* from a table but keep using the same table structure tomorrow, should you use `DROP TABLE` or `TRUNCATE TABLE`?
✅ **Answer:** `TRUNCATE TABLE` — it clears the data but keeps the table structure intact.

### 5️⃣ IF EXISTS / IF NOT EXISTS — Safety Nets
To avoid errors when a table may or may not already exist:

```sql
CREATE TABLE IF NOT EXISTS students (
    student_id INT,
    name VARCHAR(50)
);

DROP TABLE IF EXISTS old_students;
```

This prevents your script from crashing if the table already exists (or doesn't exist).

## 💡 Real-Life Analogy
* **CREATE TABLE** = Building a new cupboard with labeled drawers before storing anything in it.
* **ALTER TABLE** = Adding one more drawer to the same cupboard, or renaming a drawer's label — without throwing away what's already inside.
* **DROP TABLE** = Completely destroying the cupboard, including everything stored inside it.

## 💻 Real-World Application

| Scenario | DDL Command Used |
|---|---|
| Launching a new "Reviews" feature on an app | `CREATE TABLE reviews (...)` |
| Adding a "loyalty_points" field for existing customers | `ALTER TABLE customers ADD COLUMN loyalty_points INT` |
| Retiring an old, unused "legacy_orders" table | `DROP TABLE legacy_orders` |
| Renaming a poorly-named column found during a code review | `ALTER TABLE ... RENAME COLUMN ...` |

## 🔍 Industry Example
When the **Product Team at Myntra** decides to add a "Wishlist" feature:
1. A backend developer designs the schema: a new table called `wishlist` with columns `wishlist_id`, `user_id`, `product_id`, `added_date`.
2. The developer writes and runs:
   ```sql
   CREATE TABLE wishlist (
       wishlist_id INT,
       user_id INT,
       product_id INT,
       added_date DATE
   );
   ```
3. A few weeks later, the product team wants to track *why* a user added something to their wishlist (e.g., "price drop alert"). The developer runs:
   ```sql
   ALTER TABLE wishlist ADD COLUMN reason VARCHAR(100);
   ```
4. Six months later, the feature is deprecated in favor of a new "Favorites" system, and the old table is safely backed up, then removed:
   ```sql
   DROP TABLE wishlist;
   ```

## 📊 Diagram

```
   CREATE TABLE                ALTER TABLE                DROP TABLE
 ┌────────────────┐      ┌──────────────────────┐    ┌──────────────────┐
 │  Build a new    │      │  Modify structure     │    │  Destroy table    │
 │  empty table    │  ──▶ │  (add/remove/rename   │──▶ │  completely        │
 │  (structure only)│      │   columns)            │    │  (structure+data)  │
 └────────────────┘      └──────────────────────┘    └──────────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| `DROP TABLE` and `DELETE FROM table` do the same thing | `DROP TABLE` removes the entire table structure; `DELETE` only removes rows, keeping the structure |
| `ALTER TABLE` deletes all existing data when adding a column | Existing rows remain; new column just gets empty/default values for old rows |
| You can undo a `DROP TABLE` easily | In most databases, `DROP TABLE` is permanent unless you have a backup |
| Column data types can be changed with zero risk | Changing data types can cause data loss/errors if existing data doesn't fit the new type |

## 💬 Interview Corner
**Q1: What is the difference between DROP and TRUNCATE?**
✅ DROP removes the table structure and data entirely; TRUNCATE removes only the data but keeps the structure.

**Q2: How do you add a new column to an existing table?**
✅ Using `ALTER TABLE table_name ADD COLUMN column_name datatype;`

**Q3: Can you recover data after DROP TABLE?**
✅ Generally no, unless a backup exists — DROP TABLE is a permanent DDL operation.

**Q4: What does `CREATE TABLE IF NOT EXISTS` do?**
✅ It creates the table only if it doesn't already exist, preventing an error if it's run multiple times.

## 📝 Quick Summary
* 📌 DDL = commands that define/change database structure
* 📌 `CREATE TABLE` builds a new table with defined columns and data types
* 📌 `ALTER TABLE` modifies an existing table (add/remove/rename columns) without deleting data
* 📌 `DROP TABLE` permanently deletes the table structure AND its data
* 📌 `TRUNCATE` clears data but keeps structure; different from DROP
* 📌 Use `IF EXISTS` / `IF NOT EXISTS` to avoid errors in scripts
* 📌 DDL changes are usually immediate and hard to undo — be careful!

## 🎯 Class Activity
Using any SQL tool on your laptop, create a table called `my_practice` with columns `id (INT)`, `name (VARCHAR(30))`, and `joined_date (DATE)`. Then use `ALTER TABLE` to add a new column `phone (VARCHAR(15))`. Finally, view the table structure using `DESCRIBE my_practice;` (MySQL) or `\d my_practice` (PostgreSQL).

---

# 📋 Assignments — DDL: CREATE TABLE, ALTER TABLE, DROP TABLE

| Assignment |
|---|
| Create a table called `books` with columns: book_id, title, author, price. Take a screenshot after creation. |
| Add a new column `published_year` to the `books` table using ALTER TABLE. |
| Rename the column `author` to `writer_name` in the `books` table. |
| Drop the column `published_year` you added earlier. |
| Create a table `employees` with at least 5 relevant columns of your choice. |
| Use `CREATE TABLE IF NOT EXISTS` to try creating the same `employees` table twice and observe what happens. |
| Drop the `books` table completely and confirm it no longer exists using `SHOW TABLES;` or equivalent. |
| Research and write 3 lines explaining why DROP TABLE should be used carefully in production systems. |
| Create a table called `movies` and then use ALTER TABLE to change one column's data type. |
| Write and run a query to view the structure (columns + data types) of any table you created. |
| Create two tables of your choice for a "personal expense tracker" app idea. |
| Explain in writing the difference between DROP, DELETE, and TRUNCATE with one example each. |

---

# 📚 Data Types & Constraints: PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, DEFAULT, CHECK

## 🎯 Learning Objectives
* 🎯 Understand common SQL data types and when to use each
* 🎯 Understand what a "constraint" is and why databases need them
* 🎯 Learn PRIMARY KEY and how it uniquely identifies rows
* 🎯 Get a conceptual introduction to FOREIGN KEY and table relationships
* 🎯 Learn NOT NULL, UNIQUE, DEFAULT, and CHECK constraints with examples

## 📖 Introduction
Imagine a college admission form with no rules — students could leave the "Name" field blank, enter their age as "-5," or use the same roll number as another student. Chaos! 😱

**Constraints** are rules we apply to columns to make sure the data entered is **valid, consistent, and reliable**. Combined with proper **data types**, they act like a strict but helpful gatekeeper for your database.

Why do these exist?
* Without constraints, databases would accept garbage data — duplicate IDs, missing names, negative ages.
* Constraints protect **data integrity**, meaning the data always makes logical sense.

Where are they used?
* Every serious production database (banking, healthcare, e-commerce) relies heavily on constraints to avoid data corruption.

## 🧠 Detailed Notes

### 1️⃣ Common SQL Data Types
Before applying constraints, you must choose the correct **data type** for each column.

| Data Type | Meaning | Example |
|---|---|---|
| `INT` | Whole numbers | 25, -10, 1000 |
| `VARCHAR(n)` | Variable-length text, max n characters | 'Riya', 'Pune' |
| `CHAR(n)` | Fixed-length text | 'M' (for gender codes) |
| `DATE` | Date value | '2024-05-20' |
| `DECIMAL(p,s)` | Precise decimal numbers (for money) | 1999.50 |
| `BOOLEAN` | True/False value | TRUE, FALSE |
| `TEXT` | Large text (paragraphs, descriptions) | Product descriptions |

> 💡 **Tip**
>
> Always use `DECIMAL` (not `FLOAT`) for money-related columns like price or salary — it avoids rounding errors!

### 2️⃣ What is a Constraint?
A **constraint** is a rule enforced on a column (or table) to control what kind of data can be stored in it. If a rule is broken, the database **rejects** the operation with an error.

### 3️⃣ PRIMARY KEY
A **PRIMARY KEY** uniquely identifies each row in a table. No two rows can have the same primary key value, and it **cannot be NULL**.

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

Here, `student_id` must be unique for every student — like a roll number or Aadhaar number.

🤔 **Quick Thinking Question:** Can two students have the same `student_id` if it's marked as PRIMARY KEY?
✅ **Answer:** No! A PRIMARY KEY enforces uniqueness — duplicate values are automatically rejected by the database.

### 4️⃣ FOREIGN KEY (Conceptual Introduction)
A **FOREIGN KEY** is a column that creates a **link** between two tables. It refers to the PRIMARY KEY of another table, ensuring the connected data actually exists.

```sql
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

This means: "The `student_id` in `enrollments` MUST match an existing `student_id` in the `students` table." You cannot enroll a student who doesn't exist!

> ⚠️ **Important**
>
> We are introducing FOREIGN KEY conceptually here. We will go much deeper into relationships and JOINs in later topics.

### 5️⃣ NOT NULL
Ensures a column **cannot be left empty**.

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```

If someone tries to insert an employee without a name, the database will reject it.

### 6️⃣ UNIQUE
Ensures all values in a column are **different from each other**, but (unlike PRIMARY KEY) it CAN allow one NULL value, and a table can have multiple UNIQUE columns.

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

No two employees can have the same email address.

### 7️⃣ DEFAULT
Automatically assigns a **pre-set value** to a column if no value is provided during insertion.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

If you insert an order without specifying `status`, it automatically becomes `'Pending'`.

### 8️⃣ CHECK
Ensures values in a column satisfy a **specific condition**.

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    age INT CHECK (age >= 18)
);
```

This ensures no employee under 18 can be added to the table.

🤔 **Quick Thinking Question:** You want to make sure a `price` column in a `products` table never has a negative value. Which constraint would you use?
✅ **Answer:** `CHECK (price >= 0)` — this enforces the business rule directly at the database level.

### 9️⃣ Combining Multiple Constraints
Real tables usually combine several constraints together:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 18),
    membership_status VARCHAR(20) DEFAULT 'Basic'
);
```

## 💡 Real-Life Analogy
* **PRIMARY KEY** → Like an Aadhaar number — unique to each person, cannot be duplicated, cannot be blank.
* **FOREIGN KEY** → Like a "reference" section on a form — you can't mention a "Course ID" that doesn't actually exist in the course catalog.
* **NOT NULL** → Like a mandatory field on a form marked with a red asterisk (*) — you can't submit without filling it.
* **UNIQUE** → Like phone numbers — two people can't have the same number, but leaving it blank once might be acceptable.
* **DEFAULT** → Like a form that pre-fills "India" as the country if you don't select anything.
* **CHECK** → Like a form that rejects your entry if you type an age like "-5" or "500".

## 💻 Real-World Application

| Constraint | Real-World Use Case |
|---|---|
| PRIMARY KEY | Aadhaar Number, Employee ID, Order ID |
| FOREIGN KEY | Linking an Order to a Customer, a Comment to a Post |
| NOT NULL | Mandatory fields like Name, Email on signup forms |
| UNIQUE | Email addresses, usernames, phone numbers |
| DEFAULT | Default account status = "Active" on signup |
| CHECK | Minimum age = 18 for a banking account, price ≥ 0 |

## 🔍 Industry Example
When a **Backend Developer at Paytm** designs the `users` table for a new wallet feature:
1. They set `user_id` as `PRIMARY KEY` so every user has a guaranteed unique identifier.
2. They add `NOT NULL` on `phone_number` because a wallet account cannot exist without a phone number.
3. They add `UNIQUE` on `phone_number` too, because two different accounts cannot share one phone number.
4. They add a `CHECK (balance >= 0)` constraint so the wallet balance can never go negative due to a bug.
5. They set `DEFAULT 'Active'` on the `account_status` column so new users are automatically active without extra code.
6. They add a `FOREIGN KEY` linking a `transactions` table's `user_id` back to the `users` table, ensuring no transaction can reference a non-existent user.

## 📊 Diagram

```
   students table                     enrollments table
 ┌─────────────────────┐          ┌──────────────────────────┐
 │ student_id (PK)      │◀────────│ student_id (FK)            │
 │ name (NOT NULL)      │         │ course_id (FK)             │
 │ email (UNIQUE)       │         │ enrollment_date (DEFAULT)  │
 │ age (CHECK >= 5)     │         └──────────────────────────┘
 └─────────────────────┘
   PK = Primary Key   FK = Foreign Key (refers back to students)
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| A table can have multiple PRIMARY KEYS | A table can have only ONE primary key (though it can be made of multiple columns — a "composite key") |
| UNIQUE and PRIMARY KEY are exactly the same | PRIMARY KEY disallows NULL entirely; UNIQUE can allow one NULL value (behavior varies slightly by RDBMS) |
| FOREIGN KEY means "copy of data" | FOREIGN KEY is a *reference/link*, not a duplicate copy of the actual row |
| DEFAULT forces a value even if you provide your own | DEFAULT only applies when NO value is given during insert; your own value always overrides it |
| CHECK constraints slow down every query drastically | CHECK constraints have minimal overhead and are essential for maintaining valid data |

## 💬 Interview Corner
**Q1: What is the difference between PRIMARY KEY and UNIQUE constraint?**
✅ PRIMARY KEY uniquely identifies each row and cannot be NULL; UNIQUE also enforces uniqueness but can typically allow one NULL value, and a table can have multiple UNIQUE columns but only one PRIMARY KEY.

**Q2: What does a FOREIGN KEY do?**
✅ It creates a link between two tables by referencing the PRIMARY KEY of another table, ensuring referential integrity.

**Q3: What happens if you try to insert NULL into a NOT NULL column?**
✅ The database throws an error and rejects the insertion.

**Q4: Give a real example of a CHECK constraint.**
✅ `CHECK (age >= 18)` on an employees table ensures no employee below 18 years can be added.

## 📝 Quick Summary
* 📌 Data types (INT, VARCHAR, DATE, DECIMAL, etc.) define what kind of value a column can hold
* 📌 Constraints are rules that maintain data accuracy and consistency
* 📌 PRIMARY KEY = unique identifier for each row, cannot be NULL
* 📌 FOREIGN KEY = links one table's column to another table's PRIMARY KEY
* 📌 NOT NULL = column cannot be left empty
* 📌 UNIQUE = no duplicate values allowed in that column
* 📌 DEFAULT = auto-fills a value when none is provided
* 📌 CHECK = enforces a custom condition/rule on column values
* 📌 Combining constraints creates strong, reliable table structures

## 🎯 Class Activity
Create a table called `bank_accounts` with: `account_id` (PRIMARY KEY), `holder_name` (NOT NULL), `email` (UNIQUE), `balance` (CHECK >= 0, DEFAULT 0). Try inserting a row that violates one constraint and observe the error message.

---

# 📋 Assignments — Data Types & Constraints

| Assignment |
|---|
| Create a `students` table with student_id as PRIMARY KEY and name as NOT NULL. |
| Try inserting two rows with the same student_id and note the error you get. |
| Create an `employees` table with an email column marked UNIQUE. Try inserting two rows with the same email. |
| Create a `products` table with a price column that uses CHECK (price >= 0). Try inserting a negative price. |
| Create an `orders` table where `status` has DEFAULT value 'Pending'. Insert a row without specifying status and check the result. |
| Design a `courses` and `enrollments` table pair using a FOREIGN KEY relationship (conceptually explain even if you don't run it). |
| List 5 real-life fields you'd mark as NOT NULL on a college admission form. |
| Try creating a column with CHECK (age BETWEEN 18 AND 60) and test it with valid and invalid values. |
| Explain, with an example, why PRIMARY KEY cannot store NULL values. |
| Create a `library_books` table using at least 4 different data types (INT, VARCHAR, DATE, DECIMAL). |
| Write a short note (5-6 lines) on why constraints are important in real banking systems. |
| Design (on paper) a `hospital_patients` table with appropriate constraints for at least 5 columns. |

---

# 📚 DML: INSERT, UPDATE, DELETE

## 🎯 Learning Objectives
* 🎯 Understand what DML (Data Manipulation Language) means
* 🎯 Learn how to add data using `INSERT`
* 🎯 Learn how to modify existing data using `UPDATE`
* 🎯 Learn how to remove data using `DELETE`
* 🎯 Understand the danger of forgetting the `WHERE` clause

## 📖 Introduction
We've built our tables (DDL) and set rules for them using constraints. Now it's time to actually **fill them with real data, change it, and remove it when needed** — this is exactly what **DML (Data Manipulation Language)** is for.

Why does DML exist?
* A table with no data is like an empty cupboard — useless until you actually put things in it.
* DML gives us the power to insert new records, update existing ones (e.g., a customer changes their address), and delete outdated ones (e.g., a cancelled order).

Where is it used?
* Literally every single action a user takes on an app — signing up (INSERT), editing their profile (UPDATE), deleting their account (DELETE) — triggers DML commands behind the scenes.

> ⚠️ **Important**
>
> Unlike DDL (which changes structure), DML changes only the **data inside** the tables. The table structure stays the same.

## 🧠 Detailed Notes

### 1️⃣ INSERT — Adding New Data
The `INSERT INTO` statement adds a new row (record) into a table.

**Syntax (specifying columns — recommended):**
```sql
INSERT INTO students (student_id, name, age, city)
VALUES (1, 'Riya', 20, 'Pune');
```

**Inserting multiple rows at once:**
```sql
INSERT INTO students (student_id, name, age, city)
VALUES 
    (2, 'Aman', 22, 'Delhi'),
    (3, 'Sneha', 21, 'Mumbai');
```

**Inserting without specifying columns (not recommended — risky if table structure changes):**
```sql
INSERT INTO students VALUES (4, 'Karan', 23, 'Chennai');
```

🤔 **Quick Thinking Question:** Why is it safer to always specify column names in an INSERT statement?
✅ **Answer:** Because if the table structure changes later (e.g., a new column is added), specifying column names avoids errors or wrongly-placed values — the query stays reliable.

### 2️⃣ UPDATE — Modifying Existing Data
The `UPDATE` statement changes values in existing rows.

**Syntax:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

**Example:**
```sql
UPDATE students
SET city = 'Bangalore'
WHERE student_id = 1;
```

This changes Riya's city to 'Bangalore' — but ONLY for the row where `student_id = 1`.

> ⚠️ **Important**
>
> If you forget the `WHERE` clause in an UPDATE statement, **every single row** in the table gets updated! This is one of the most common (and dangerous) beginner mistakes.

```sql
-- ⚠️ DANGEROUS: This updates ALL students' cities to 'Bangalore'!
UPDATE students
SET city = 'Bangalore';
```

### 3️⃣ DELETE — Removing Data
The `DELETE` statement removes one or more rows from a table.

**Syntax:**
```sql
DELETE FROM table_name
WHERE condition;
```

**Example:**
```sql
DELETE FROM students
WHERE student_id = 3;
```

This removes only Sneha's row (student_id = 3) from the table.

```sql
-- ⚠️ DANGEROUS: This deletes ALL rows from the students table!
DELETE FROM students;
```

🤔 **Quick Thinking Question:** What is the difference between running `DELETE FROM students;` (no WHERE) and `DROP TABLE students;`?
✅ **Answer:** `DELETE FROM students;` (no WHERE) removes all rows but keeps the table structure intact; `DROP TABLE students;` removes the entire table structure along with the data.

### 4️⃣ The Golden Rule of DML: Always Use WHERE Carefully
Best practice before running UPDATE/DELETE in real projects:
1. First run a `SELECT` with the same `WHERE` condition to preview which rows will be affected.
   ```sql
   SELECT * FROM students WHERE student_id = 1;
   ```
2. Confirm the result looks correct.
3. THEN run the `UPDATE` or `DELETE` with the same condition.

> 💡 **Tip**
>
> In professional environments, many teams require a `SELECT` preview before any `UPDATE`/`DELETE` is run on production data. This habit saves you from disasters!

### 5️⃣ Comparing INSERT, UPDATE, DELETE

| Command | Purpose | Affects | Needs WHERE? |
|---|---|---|---|
| INSERT | Add new row(s) | New data | No (adds fresh rows) |
| UPDATE | Modify existing row(s) | Existing data | Yes (to target specific rows) |
| DELETE | Remove row(s) | Existing data | Yes (to avoid deleting everything) |

## 💡 Real-Life Analogy
Think of a table as a **filing cabinet drawer full of paper forms**:
* **INSERT** = Adding a brand-new filled form into the drawer.
* **UPDATE** = Taking out an existing form, crossing out old info, and writing new info (e.g., changing an address).
* **DELETE** = Physically removing a specific form from the drawer and shredding it.

If you're not careful and grab the wrong instruction ("update ALL forms" instead of "update THIS form"), you could accidentally change or destroy everything in the drawer!

## 💻 Real-World Application

| User Action on an App | DML Command Triggered Behind the Scenes |
|---|---|
| Signing up for a new account | `INSERT INTO users (...) VALUES (...)` |
| Editing your profile picture/bio | `UPDATE users SET bio = ... WHERE user_id = ...` |
| Deleting a comment on Instagram | `DELETE FROM comments WHERE comment_id = ...` |
| Adding an item to your cart | `INSERT INTO cart_items (...) VALUES (...)` |
| Cancelling an order on Amazon | `UPDATE orders SET status = 'Cancelled' WHERE order_id = ...` |

## 🔍 Industry Example
When you **update your delivery address on Flipkart** before checkout:
1. You edit the address field on the app and click "Save."
2. The frontend sends this new data to the backend server.
3. The backend (built in Python/Django, for example) runs something like:
   ```sql
   UPDATE addresses
   SET street = 'New Street', city = 'Pune'
   WHERE address_id = 4521 AND user_id = 9981;
   ```
4. Notice the backend adds `user_id = 9981` in the WHERE clause too — this ensures you can only update **your own** address, not someone else's! This is a critical security practice.
5. The database confirms the update, and the app shows "Address updated successfully."

## 📊 Diagram

```
        INSERT                  UPDATE                    DELETE
   ┌──────────────┐       ┌──────────────────┐      ┌──────────────────┐
   │  New row      │       │  Find row(s)       │      │  Find row(s)       │
   │  added to     │  ──▶  │  using WHERE,      │ ──▶  │  using WHERE,      │
   │  the table    │       │  then change values│      │  then remove them  │
   └──────────────┘       └──────────────────┘      └──────────────────┘
                                    │                          │
                                    ▼                          ▼
                          ⚠️ No WHERE = ALL rows      ⚠️ No WHERE = ALL rows
                             get updated!                get deleted!
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| Forgetting WHERE in UPDATE only affects "some" rows | Forgetting WHERE updates/deletes ALL rows in the table — a very costly mistake |
| INSERT and UPDATE do the same thing | INSERT creates a brand-new row; UPDATE modifies values in an already-existing row |
| DELETE removes the table too | DELETE only removes rows/data; the table structure remains (use DROP TABLE to remove structure) |
| You don't need to match column order in INSERT | If you don't specify column names, values must be in the exact same order as the table's columns |

## 💬 Interview Corner
**Q1: What is the difference between INSERT and UPDATE?**
✅ INSERT adds a completely new row to a table, while UPDATE modifies values in an already-existing row.

**Q2: What happens if you run UPDATE without a WHERE clause?**
✅ Every single row in the table gets updated with the new value(s), which is usually a costly mistake.

**Q3: How would you delete only the students from 'Mumbai' out of a table?**
✅ `DELETE FROM students WHERE city = 'Mumbai';`

**Q4: Is DELETE a DDL or DML command?**
✅ DELETE is a DML command because it manipulates data (rows), not the table structure.

## 📝 Quick Summary
* 📌 DML = commands that manipulate the actual data inside tables
* 📌 `INSERT INTO table (columns) VALUES (values);` adds new rows
* 📌 `UPDATE table SET column = value WHERE condition;` modifies existing rows
* 📌 `DELETE FROM table WHERE condition;` removes specific rows
* 📌 Forgetting `WHERE` in UPDATE/DELETE affects ALL rows — always double-check!
* 📌 Best practice: run a SELECT with the same WHERE first to preview affected rows
* 📌 DML changes data only; it does not change the table's structure

## 🎯 Class Activity
Using the `students` table you created earlier, insert 3 new students, then update one student's city, and finally delete one student using their `student_id`. Before each UPDATE/DELETE, run a SELECT with the same WHERE condition to preview the affected row.

---

# 📋 Assignments — DML: INSERT, UPDATE, DELETE

| Assignment |
|---|
| Insert 5 rows of sample data into your `students` table using a single INSERT statement (multi-row insert). |
| Update the age of one specific student using their student_id in the WHERE clause. |
| Delete one student record by student_id and verify using SELECT that it's gone. |
| Try running an UPDATE statement without a WHERE clause on a test/dummy table and observe what happens to all rows. |
| Insert a new employee record into an `employees` table without specifying column names, and note any issues you face. |
| Write an UPDATE query to change the status of all "Pending" orders to "Shipped" in an `orders` table. |
| Write a DELETE query to remove all records older than a certain date (conceptually explain the WHERE condition you'd use). |
| Create a `products` table, insert 5 products, then increase the price of one product by 10% using UPDATE. |
| Explain in your own words why running SELECT before UPDATE/DELETE is considered a best practice. |
| Insert a row that violates a NOT NULL or CHECK constraint and record the exact error message. |
| Write and execute a DELETE query using multiple conditions in WHERE (e.g., city = 'Pune' AND age > 25). |
| Create a mini "notes" table and add, update, and delete at least 3 entries to simulate a simple notes app. |

---

# 📚 Designing Simple Schemas (Students, Employees, Customers)

## 🎯 Learning Objectives
* 🎯 Understand the step-by-step process of designing a database schema
* 🎯 Practice identifying entities, attributes, and keys from a real-world scenario
* 🎯 Design complete schemas for Students, Employees, and Customers systems
* 🎯 Apply DDL, data types, and constraints learned so far into one combined design
* 🎯 Understand how to avoid common schema design mistakes

## 📖 Introduction
So far, we've learned individual building blocks: tables, data types, constraints, and how to insert/update/delete data. Now it's time to bring it ALL together and **design complete, real-world schemas** — this is one of the most important skills for any backend or full-stack developer.

Why does this matter?
* A poorly designed schema causes bugs, slow performance, and data corruption down the line.
* A well-designed schema makes your application easy to build, maintain, and scale.
* This is often tested directly in **job interviews** — "Design a database for X" is one of the most common interview questions for freshers.

Where is this skill used?
* Every time a new project starts, before writing a single line of backend code, developers sit down and design the schema first.

## 🧠 Detailed Notes

### 1️⃣ The Schema Design Process (Step-by-Step)
Follow these steps every time you design a schema:

1. **Identify Entities** — What are the "things" we need to store? (e.g., Student, Course, Employee)
2. **Identify Attributes** — What details do we need about each entity? (e.g., Student → name, age, email)
3. **Identify the Primary Key** — What uniquely identifies each record?
4. **Identify Relationships** — How do entities connect to each other?
5. **Choose Data Types** — What data type fits each attribute best?
6. **Apply Constraints** — Which columns need NOT NULL, UNIQUE, CHECK, DEFAULT, FOREIGN KEY?
7. **Write the CREATE TABLE statements**

🤔 **Quick Thinking Question:** Before writing any SQL code, what should be the very FIRST step in schema design?
✅ **Answer:** Identifying the entities — the real-world "things" you need to store data about (e.g., Students, Courses).

### 2️⃣ Designing a "Students" Schema
**Entities:** Student, Course, Enrollment (junction table for many-to-many relationship)

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    city VARCHAR(50) DEFAULT 'Not Specified'
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_weeks INT CHECK (duration_weeks > 0)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

Notice how `enrollments` acts as a **bridge table** connecting `students` and `courses` — this is how we represent a **many-to-many relationship** (many students can enroll in many courses).

### 3️⃣ Designing an "Employees" Schema
**Entities:** Employee, Department

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT CHECK (age >= 18),
    salary DECIMAL(10,2) CHECK (salary > 0),
    department_id INT,
    date_of_joining DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```

Here, each employee belongs to ONE department, but each department can have MANY employees — a classic **one-to-many relationship**, achieved simply by placing `department_id` (a FOREIGN KEY) inside the `employees` table.

🤔 **Quick Thinking Question:** Why is `department_id` placed in the `employees` table and not the other way around?
✅ **Answer:** Because the relationship is one-to-many (one department → many employees). The FOREIGN KEY always goes on the "many" side of the relationship.

### 4️⃣ Designing a "Customers" Schema (E-commerce Style)
**Entities:** Customer, Order, Product

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    membership_status VARCHAR(20) DEFAULT 'Basic'
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price >= 0),
    stock_quantity INT DEFAULT 0 CHECK (stock_quantity >= 0)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT CHECK (quantity > 0),
    order_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### 5️⃣ Checklist for a Good Schema Design
Use this checklist every time you design a schema:

| ✅ Checklist Item | Why It Matters |
|---|---|
| Every table has a PRIMARY KEY | Ensures each row is uniquely identifiable |
| Relationships use FOREIGN KEY | Prevents "orphan" data (e.g., an order with no real customer) |
| Mandatory fields use NOT NULL | Prevents missing critical information |
| Sensitive/unique fields use UNIQUE | Prevents duplicate emails, phone numbers, etc. |
| Sensible DEFAULT values are set | Reduces errors when optional data isn't provided |
| Business rules are enforced via CHECK | Keeps data logically valid (e.g., no negative prices) |
| Correct data types are chosen | Saves storage and prevents invalid data types |

## 💡 Real-Life Analogy
Designing a schema is like **planning a wedding seating chart** before the event:
* You first list out **who is coming** (entities: Family, Friends, Colleagues).
* You decide **what details you need** about each guest (attributes: name, meal preference, table number).
* You make sure **no two guests are assigned the exact same seat** (Primary Key = seat number).
* You link guests to their **respective tables** (Foreign Key = table_id).
* You set **default meal preference as "Veg"** if not mentioned (Default constraint).
* You made sure age is a **valid, sensible number** for children's menu decisions (Check constraint).

Only after this careful planning do you print the actual seating cards (the equivalent of running `CREATE TABLE`).

## 💻 Real-World Application

| System | Key Tables in the Schema |
|---|---|
| 🎓 College Management System | students, courses, enrollments, faculty |
| 🏢 HR/Payroll System | employees, departments, salaries, attendance |
| 🛍️ E-commerce Platform | customers, products, orders, payments, reviews |
| 🏥 Hospital Management | patients, doctors, appointments, prescriptions |
| 📚 Library System | books, members, issued_books |

## 🔍 Industry Example
When a **startup building a new "EdTech" platform** needs its very first database:
1. The founding engineering team sits down and lists entities: `students`, `courses`, `instructors`, `enrollments`, `payments`.
2. They identify that a student can enroll in MANY courses, and a course can have MANY students → many-to-many → they create an `enrollments` bridge table.
3. They identify that each course has exactly ONE instructor, but an instructor can teach MANY courses → one-to-many → they add `instructor_id` as a FOREIGN KEY inside the `courses` table.
4. They apply constraints: `email UNIQUE NOT NULL` on students (no duplicate accounts), `CHECK (price >= 0)` on courses, `DEFAULT 'Not Started'` on enrollment progress status.
5. Only after this full schema is reviewed and approved by the tech lead do developers begin writing `CREATE TABLE` statements and then the actual backend application code (in Python/Django, for example) that will use these tables.

## 📊 Diagram

```
   departments            employees                    
 ┌───────────────┐    ┌─────────────────────┐          
 │ department_id  │◀───│ department_id (FK)   │          
 │ department_name│    │ emp_id (PK)           │          
 └───────────────┘    │ full_name, salary...  │          
                       └─────────────────────┘          

   customers              orders                  products
 ┌───────────────┐    ┌─────────────────────┐  ┌───────────────┐
 │ customer_id(PK)│◀───│ customer_id (FK)      │  │ product_id(PK) │
 │ full_name      │    │ order_id (PK)         │─▶│ product_name   │
 │ email          │    │ product_id (FK)       │  │ price          │
 └───────────────┘    │ quantity, status      │  └───────────────┘
                       └─────────────────────┘

   students              enrollments               courses
 ┌───────────────┐    ┌─────────────────────┐  ┌───────────────┐
 │ student_id(PK) │◀───│ student_id (FK)       │  │ course_id(PK)  │
 │ full_name      │    │ course_id (FK)        │─▶│ course_name    │
 │ email          │    │ enrollment_date       │  │ duration_weeks │
 └───────────────┘    └─────────────────────┘  └───────────────┘
```

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| You can start writing CREATE TABLE without planning | Skipping the planning step leads to messy schemas that need painful rework later |
| Every relationship should be handled by copy-pasting data across tables | Relationships should use FOREIGN KEYS, not duplicated data, to avoid inconsistency |
| Many-to-many relationships can be done with just 2 tables | Many-to-many relationships require a third "bridge/junction" table (like enrollments) |
| Adding constraints is optional busywork | Constraints prevent real bugs and data corruption; skipping them is risky in production |
| One giant table is simpler than multiple related tables | Splitting data into well-related tables (normalization) avoids duplication and keeps data clean |

## 💬 Interview Corner
**Q1: How would you design a schema for a simple library management system?**
✅ Identify entities (books, members, issued_books), give each a primary key, connect issued_books to both books and members via foreign keys, and add constraints like NOT NULL on member name and CHECK on due dates.

**Q2: How do you represent a many-to-many relationship in a relational database?**
✅ By creating a third "junction" or "bridge" table that holds foreign keys referencing both related tables (e.g., `enrollments` links `students` and `courses`).

**Q3: Why is it important to plan a schema before writing any SQL?**
✅ Proper planning avoids costly restructuring later, ensures relationships are correctly modeled, and prevents data integrity issues.

**Q4: What's the difference between a one-to-many and many-to-many relationship, with examples?**
✅ One-to-many: one department has many employees (FOREIGN KEY placed on the "many" side). Many-to-many: many students enroll in many courses (needs a junction table like enrollments).

## 📝 Quick Summary
* 📌 Schema design follows a process: Entities → Attributes → Primary Keys → Relationships → Data Types → Constraints
* 📌 A "students" schema typically needs students, courses, and an enrollments junction table for many-to-many links
* 📌 An "employees" schema typically links employees to departments (one-to-many)
* 📌 A "customers" schema (e-commerce) typically links customers, products, and orders
* 📌 Junction/bridge tables are essential for many-to-many relationships
* 📌 Good schema design combines PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, DEFAULT, and CHECK thoughtfully
* 📌 This is a very common and important full-stack developer interview topic
* 📌 Planning before coding saves huge amounts of rework later

## 🎯 Class Activity
In groups of 2-3, design a complete schema (with CREATE TABLE statements including appropriate constraints) for a "Gym Membership Management System" with at least 3 related tables (e.g., members, trainers, membership_plans). Present your schema to the class and explain your relationship choices.

---

# 📋 Assignments — Designing Simple Schemas (Students, Employees, Customers)

| Assignment |
|---|
| Design and write CREATE TABLE statements (with constraints) for a complete "Students" schema including students, courses, and enrollments. |
| Design and write CREATE TABLE statements for an "Employees" schema including employees and departments with a proper FOREIGN KEY relationship. |
| Design and write CREATE TABLE statements for a "Customers" schema including customers, products, and orders. |
| Identify and write down whether each relationship in your 3 schemas above is one-to-one, one-to-many, or many-to-many. |
| Actually run all your CREATE TABLE statements in an SQL tool and insert at least 3 sample rows into each table. |
| Design a schema (tables + constraints) for a "Hotel Booking System" with at least 4 related tables. |
| Design a schema for a "Movie Ticket Booking" platform including a many-to-many relationship (e.g., movies and theatres). |
| Write 5 CHECK constraints you would add across your Students, Employees, and Customers schemas and explain each one. |
| Take any ONE of your designed schemas and insert data that intentionally violates a constraint; record the error. |
| Draw (by hand or using any tool) an ER-style diagram showing all tables and relationships for your "Customers" schema. |
| Write a one-page (in your own words) explanation of the full schema design process, step by step. |
| Redesign your "Employees" schema to also include a `salaries` table with a one-to-one relationship to employees, and explain your reasoning. |
| Peer-review a classmate's schema design and suggest at least 2 improvements. |