# 📚 What Is Git? Version Control and Setup

## 🎯 Learning Objectives

- 🧠 Understand what **version control** is and why every developer uses it
- 🆚 Know the difference between **Git** (the tool) and **GitHub** (a website, coming in the next session)
- 🗂️ Understand how Git thinks: **working directory, staging area, repository**
- 💻 Use the **terminal basics** you need for Git (`pwd`, `ls`, `cd`, `mkdir`)
- ⚙️ Install Git and **configure your name and email**

---

## 📖 Introduction

Have you ever saved files like `project_final.py`, `project_final_v2.py`, `project_final_REAL.py`? 😅 That is a manual (and messy) version control system.

**Git** is a tool that **remembers every version of your project**, tells you **what changed and when**, and lets you **go back** if something breaks.

**Why is it important?** Every software company uses Git. It is the first tool you will use in any developer job.

**Where is it used?** Every project in this course (your hotel app, hospital app, FastAPI backend) should live in Git.

> 💡 **Tip**
>
> Today is a **hands-on** session. Everything happens **on your own laptop**, with **Git only**. No internet account is needed. Type every command yourself. Don't copy-paste, because typing builds muscle memory! ⌨️

---

## 🧠 Detailed Notes

### 🧭 1. What Is Version Control?

A **Version Control System (VCS)** records changes to files over time.

| Without version control | With Git |
|---|---|
| Copy folders named `final_v3` | One folder, full history inside |
| "Who broke the code?" | `git log` shows what changed and when |
| Fear of trying new ideas | Try it on a **branch**, delete it if it fails |
| One wrong edit ruins everything | Go back to any saved version |

Git is **distributed**: the full history lives **on your computer**, so it works without internet.

---

### 🆚 2. Git vs GitHub

| | **Git** | **GitHub** |
|---|---|---|
| What is it? | A **tool** installed on your laptop | A **website** that stores Git projects online |
| Needs internet? | ❌ No | ✅ Yes |
| Today's session | ✅ **Yes** | ❌ Next session |

> ℹ️ **Note**
>
> Today we use **only Git**. Once you are comfortable, the next session moves your project to GitHub.

---

### 🗂️ 3. How Git Thinks: Three Areas

```
 Working Directory  ──git add──►  Staging Area  ──git commit──►  Repository
   (your files)                  (ready to save)                 (saved history)
```

| Area | Meaning | Analogy |
|---|---|---|
| **Working directory** | The files you edit | Your desk |
| **Staging area** | Changes you picked for the next save | Putting items in a box |
| **Repository** | Permanent snapshots called **commits** | Sealed, labeled boxes in a warehouse |

A **commit** is a snapshot of your project with a message ("what I changed"), your name, and a time.

🤔 **Quick thinking question:** Why does Git have a staging area? Why not save everything automatically?

✅ **Answer:** So you can choose **exactly what goes into each snapshot**. For example, fix a bug in one file and add a feature in another, and save them as two separate, clearly labeled commits.

---

### 💻 4. Terminal Survival Kit

Git is used from the **terminal**. On Windows we use **Git Bash**, a terminal that is installed together with Git.

**How to open it:** press the **Windows key**, type `Git Bash`, press Enter. Or open any folder in File Explorer, right-click an empty space, and choose **Open Git Bash here** (Windows 11: click *Show more options* first).

> ⚠️ **Important**
>
> Use **Git Bash** for the whole course, not CMD or PowerShell. Commands like `ls -a`, `cat`, and `echo >>` behave differently there, and the outputs in these notes won't match.

| Command | Meaning |
|---|---|
| `pwd` | Where am I? (print working directory) |
| `ls` | List files in this folder |
| `cd folder` | Go **into** a folder |
| `cd ..` | Go **up** one folder |
| `mkdir name` | Make a new folder |
| `clear` | Clean the screen |

Try it:

```bash
pwd
cd ~
mkdir git-class
cd git-class
pwd
```

`~` means your user folder (`C:\Users\YourName`). Git Bash shows it as `/c/Users/YourName`. We use it instead of **Documents**, because OneDrive often moves the Documents folder and confuses paths.

> 💡 **Tip**
>
> Press the **Tab** key to auto-complete folder names, and the **Up arrow** to repeat the previous command. In Git Bash, paste with **right-click** or **Shift + Insert** (Ctrl + V may not work).

---

### ⚙️ 5. Installing and Configuring Git (Lab 0)

**Step 1. Install Git for Windows.** Download it from **git-scm.com** and run the installer. Click **Next** on most screens, but change these two:

| Installer screen | Choose |
|---|---|
| *Choosing the default editor used by Git* | **Visual Studio Code** (if installed). This avoids the confusing Vim editor. |
| *Adjusting the name of the initial branch* | **Override the default branch name** and type `main` |

Everything else can stay at the default.

**Step 2. Check it works:**

```bash
git --version
```

Expected: something like `git version 2.43.0` (your number may differ).

**Step 3. Tell Git who you are** (once per laptop). Every commit you make will carry this name:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

**Step 4. Check it:**

```bash
git config --list
```

You should see your `user.name` and `user.email` in the list.

**Step 5. Check Python** (we run Python code in the labs):

```bash
python --version
```

Expected: `Python 3.x.x`. If Windows opens the **Microsoft Store**, or says *"python is not recognized"*, install Python from **python.org** and tick **"Add python.exe to PATH"** on the first screen. Then close and reopen Git Bash.

✅ **Checkpoint:** `git --version` and `python --version` both work, and `git config --list` shows your name and email. Raise your hand if not. Don't move on yet!

> ℹ️ **Note**
>
> If you skip Step 3, Git will refuse your first commit with the message *"Please tell me who you are."* Just run the two `git config` commands and try again.

---

## 💡 Real-Life Analogy

🎮 **Saving points in a video game.**

Each **commit** is a **save point**. You keep playing (coding), and if you make a big mistake you **load an earlier save**. The **staging area** is choosing what progress goes into the next save.

---

## 💻 Real-World Application

| Where | Git usage |
|---|---|
| 🐧 Linux kernel | Git was created for it (by Linus Torvalds, 2005) |
| 🏢 Google, Microsoft, Amazon | Teams track code in Git |
| 🏥 Hospital software teams | Every change is traceable for audits |
| 🎓 Students | Portfolio projects shown to recruiters |
| ⚙️ DevOps | Server configs and deployments are versioned |

---

## 🔍 Industry Example

📘 **Scenario: A bug appears after Friday's release**

1. 🐞 On Monday, the billing page shows wrong totals.
2. 🔍 A developer runs `git log` and sees a commit from Friday: "Change tax calculation".
3. 🔬 She looks at exactly what that commit changed and finds a `*` that should have been `+`.
4. 🩹 She fixes it and commits: "Fix tax calculation operator".
5. 📜 The history now shows **what broke, who changed it, when, and how it was fixed**. Without Git, this could take hours of guessing.

---

## 📊 Diagram

```
         YOUR LAPTOP (everything today happens here)
 ┌─────────────────────────────────────────────────────┐
 │  Working Directory     Staging Area     Repository   │
 │  (edit files)          (git add)        (git commit) │
 │  ┌────────────┐       ┌───────────┐    ┌──────────┐ │
 │  │ app.py     │──────►│ app.py    │───►│ commit 1 │ │
 │  │ patients.py│       │           │    │ commit 2 │ │
 │  └────────────┘       └───────────┘    │ commit 3 │ │
 │                                        └──────────┘ │
 └─────────────────────────────────────────────────────┘
            (GitHub, the online copy, comes later)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Git and GitHub are the same." | Git is the tool on your laptop. GitHub is a website that hosts Git projects. |
| "I need internet to use Git." | Git works fully offline. |
| "I can skip `git config`." | Without your name and email, commits fail. |
| "Git saves my files automatically." | Git only saves when **you** commit. |
| "I must memorize all commands today." | Learn the basic 8. Look up the rest. |
| "Typing commands in the wrong folder is fine." | Always check with `pwd` where you are. |
| "CMD, PowerShell, and Git Bash are the same." | Use **Git Bash** so commands match these notes. |

---

## 💬 Interview Corner

**Q1. What is Git?**
A distributed version control system that tracks changes in files and lets you return to earlier versions.

**Q2. What is the difference between Git and GitHub?**
Git is the tool installed on your computer. GitHub is an online service that hosts Git repositories.

**Q3. What are the three areas in Git?**
Working directory (your files), staging area (changes chosen for the next commit), and repository (saved commits).

**Q4. What is a commit?**
A saved snapshot of the project with a message, author, and timestamp.

---

## 📝 Quick Summary

- 🧠 Git remembers **every version** of your project.
- 🆚 Git = tool on your laptop, GitHub = website (later).
- 🗂️ Working directory → staging area → repository.
- 📸 A **commit** is a snapshot with a message.
- 💻 Basic terminal commands: `pwd`, `ls`, `cd`, `mkdir`.
- ⚙️ Set `user.name` and `user.email` once.
- 🌐 Git works **offline**.

---

## 🎯 Class Activity

**🛠️ Activity: "Get ready" (about 10 minutes)**

1. Open the terminal (Git Bash on Windows).
2. Run `pwd`, `ls`, `cd`, and `mkdir git-class` to get comfortable.
3. Install Git (if not installed) and run `git --version`.
4. Configure your name, email, and default branch.
5. Run `git config --list` and find your details.
6. Show your screen to a neighbour, and help them if they are stuck.

---

# 📋 Assignments — What Is Git? Version Control and Setup

| Assignment |
|---|
| Take a screenshot of `git --version` and `git config --list` showing your name and email. |
| In the terminal, create the folder structure `git-class/practice/notes` using only `mkdir` and `cd`, and show the result with `pwd`. |
| Use `ls -a` inside any Git project later and find the hidden `.git` folder. Write one line about what you think it stores. |
| Write 5 real-life things (not software) that have "version history" or "save points". |
| Explain in your own words, in 4 lines, why the staging area exists. |
| Write the difference between Git and GitHub in a table with at least 3 rows. |
| Find where your laptop stores the global Git config (hint: `git config --global --list --show-origin`) and note the path. |
| List 3 problems you faced in the past that Git would have solved (like overwritten files or lost versions). |

---
---

# 📚 Hands-On: Your First Local Repository

## 🎯 Learning Objectives

- 📦 Create a repository with `git init`
- 🔍 Read `git status` and understand its messages
- ➕ Stage files with `git add` and save them with `git commit`
- 📜 View history with `git log`
- 🔬 See your changes with `git diff`
- 🙈 Ignore unwanted files using `.gitignore`

---

## 📖 Introduction

Time to build! In this lab you create a tiny **hospital app in Python** and save it in Git step by step, exactly like a real developer.

You will repeat one rhythm again and again, and it will become automatic:

```
 edit  ──►  status  ──►  add  ──►  commit
```

**Why is it important?** These four moves are about 90% of daily Git use.

> 💡 **Tip**
>
> Use **VS Code** to create and edit files (`code .` opens the current folder), and type Git commands in **Git Bash**. We run Python with `python` (Mac/Linux users type `python3`).

> 🔎 **Note**
>
> Your **commit codes** (like `0e62652`) will be different from the ones in these notes. That is normal.

---

## 🧠 Detailed Notes

### 🪜 Step 1. Create the Project Folder and Start Git

```bash
cd ~/git-class                 # the folder from the setup topic
mkdir hospital-app
cd hospital-app
git init
```

Expected:

```
Initialized empty Git repository in .../hospital-app/.git/
```

Git created a hidden `.git` folder. **That folder is the entire history.**

> ⚠️ **Important**
>
> Never delete `.git`, and never run `git init` inside another Git project.

---

### 🪜 Step 2. Check the Status

```bash
git status
```

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

📖 *"On branch main"* means you are on the main line. *"No commits yet"* means the history is empty.

**`git status` is your best friend.** Run it **all the time**.

---

### 🪜 Step 3. Create Your First File

In VS Code, create **`app.py`**:

```python
print("Welcome to City Hospital")
```

Run it:

```bash
python app.py
```

```
Welcome to City Hospital
```

Now ask Git:

```bash
git status
```

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	app.py

nothing added to commit but untracked files present (use "git add" to track)
```

📖 **Untracked** means: *"Git sees this file but isn't watching it yet."*

---

### 🪜 Step 4. Stage the File (`git add`)

```bash
git add app.py
git status
```

```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   app.py
```

📖 The file is now in the **staging area**, ready to be saved.

---

### 🪜 Step 5. Make Your First Commit

```bash
git commit -m "Add welcome message"
```

```
[main (root-commit) 0e62652] Add welcome message
 1 file changed, 1 insertion(+)
 create mode 100644 app.py
```

🎉 **Congratulations, you made your first save point!**

- `-m` lets you type the **message** right there.
- `root-commit` just means "the very first commit".

> ⚠️ **Important**
>
> If you forget `-m`, an editor opens so you can type the message. Don't panic!
> - **VS Code opened:** type your message on the first line, save (**Ctrl + S**), and close the tab. (To cancel, close the tab with an empty message.)
> - **Vim opened (a black screen with `~` lines):** press **Esc**, type `:q!` and press **Enter** to escape. Then run the commit again with `-m`.

**Writing good commit messages:**

| ❌ Bad | ✅ Good |
|---|---|
| `update` | `Add patient list to app` |
| `fixed stuff` | `Fix crash when name is empty` |
| `asdf` | `Add .gitignore` |

Start with a verb and say **what** you changed.

---

### 🪜 Step 6. See the History

```bash
git log --oneline
```

```
0e62652 Add welcome message
```

Also try the long version:

```bash
git log
```

```
commit 0e62652...  (long code)
Author: Your Name <you@example.com>
Date:   ...

    Add welcome message
```

✅ **Checkpoint 1:** You have **1 commit** in `git log`, and `git status` says **"nothing to commit, working tree clean"**.

---

### 🪜 Step 7. Make Your Second Change

Create a new file **`patients.py`**:

```python
patients = ["Asha", "Ravi"]
```

Change **`app.py`** to:

```python
from patients import patients

print("Welcome to City Hospital")
for name in patients:
    print("Patient:", name)
```

Run it:

```bash
python app.py
```

```
Welcome to City Hospital
Patient: Asha
Patient: Ravi
```

Now check Git:

```bash
git status
```

```
Changes not staged for commit:
	modified:   app.py

Untracked files:
	__pycache__/
	patients.py
```

📖 Two kinds of changes: **`app.py` is modified** (Git knows it), and **`patients.py` is untracked** (new). And look: Python created a **`__pycache__/`** folder by itself.

🤔 **Quick thinking question:** Should `__pycache__/` be saved in Git?

✅ **Answer:** **No.** It is auto-generated junk that can be re-created anytime. We tell Git to ignore it. Let's do that next.

---

### 🪜 Step 8. Create `.gitignore`

Create a file named **`.gitignore`** (with the dot at the start):

```
__pycache__/
venv/
.env
```

> ⚠️ **Important (Windows)**
>
> Create this file **in VS Code** (*New File*, then type `.gitignore`). If you use Notepad, Windows may save it as `.gitignore.txt`, and Git will ignore **nothing**. Check with `ls -a` in Git Bash: you must see `.gitignore`, not `.gitignore.txt`.

```bash
git status
```

```
Untracked files:
	.gitignore
	patients.py
```

🎉 `__pycache__/` has **disappeared** from the list. Git now ignores it.

> ⚠️ **Important**
>
> Always add `.gitignore` **before** your first `git add .`. If you commit a file once (like `.env` with passwords), adding it to `.gitignore` later **won't remove it from history**.

---

### 🪜 Step 9. See What Changed (`git diff`)

```bash
git diff
```

```
--- a/app.py
+++ b/app.py
@@ -1 +1,5 @@
+from patients import patients
+
 print("Welcome to City Hospital")
+for name in patients:
+    print("Patient:", name)
```

📖 Lines starting with **`+`** were **added**. Lines starting with **`-`** were **removed**. `git diff` shows changes **before** you stage them. (It only compares files Git already tracks.)

---

### 🪜 Step 10. Stage Everything and Commit

```bash
git add .
git status
```

```
Changes to be committed:
	new file:   .gitignore
	modified:   app.py
	new file:   patients.py
```

The `.` means "everything in this folder". Always **read the list** before committing!

```bash
git commit -m "Show patient list and add .gitignore"
```

```
[main cf39de2] Show patient list and add .gitignore
 3 files changed, 8 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 patients.py
```

---

### 🪜 Step 11. Look at Your History

```bash
git log --oneline
```

```
cf39de2 Show patient list and add .gitignore
35ab63e Add welcome message
```

To see what a commit changed:

```bash
git show --stat
```

```
commit cf39de2...
Author: Your Name <you@example.com>

    Show patient list and add .gitignore

 .gitignore  | 3 +++
 app.py      | 4 ++++
 patients.py | 1 +
 3 files changed, 8 insertions(+)
```

✅ **Checkpoint 2:** You have **2 commits**, a clean status, and **no** `__pycache__` in Git.

---

### 🔁 The Rhythm to Remember

```
 1. edit files
 2. git status        ← what changed?
 3. git diff          ← what exactly?
 4. git add .         ← pick it
 5. git commit -m ""  ← save it
 6. git log --oneline ← confirm
```

> 💡 **Tip**
>
> A shortcut: `git commit -am "message"` stages **and** commits all **already-tracked** files in one go. It does **not** include brand-new (untracked) files.

---

### 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| `fatal: not a git repository` | You are in the wrong folder. Use `pwd` and `cd` into `hospital-app`. |
| `Please tell me who you are` | Run the two `git config --global` commands from the setup. |
| An editor opened after `git commit` | VS Code: write a message, save, close the tab. Vim: press Esc, type `:q!`, Enter. Next time use `-m`. |
| `python` is not recognized, or the Microsoft Store opens | Install Python from python.org with **"Add python.exe to PATH"**, then reopen Git Bash. |
| `.gitignore` has no effect | Check `ls -a`. The file may be named `.gitignore.txt`. Rename it. |
| `nothing to commit` | You didn't change or stage anything. Edit a file and try again. |
| `warning: ... LF will be replaced by CRLF` | Harmless Windows line-ending message. Ignore it. |
| Typed a wrong commit message | Tell the instructor. We'll fix it in the last topic. |

---

## 💡 Real-Life Analogy

📦 **Packing a box to send.**

You collect items on your table (**working directory**), choose which ones go in the box (**`git add`**), seal it and write a label (**`git commit -m`**). `git log` is the **shipping register** of all boxes sent. `.gitignore` is the list of things you **never** pack, like garbage and your personal diary.

---

## 💻 Real-World Application

| Where | Same workflow |
|---|---|
| 💼 Every developer, every day | edit → status → add → commit |
| 🏥 Hospital software | Each change has a message for audits |
| 🧪 Data science | Version notebooks and scripts |
| 📚 Writers and designers | Even documents can live in Git |
| ⚙️ Config management | Server settings tracked like code |

---

## 🔍 Industry Example

📘 **Scenario: A developer's morning**

1. ☕ She opens the project and runs `git status` to see where she left off.
2. ✍️ She edits the patient search function and tests it.
3. 🔬 `git diff` shows exactly 12 changed lines, so she reviews her own work.
4. ➕ `git add patients.py`, because she wants to leave out a half-finished experiment in another file.
5. 📸 `git commit -m "Add search by department"`.
6. 🔁 She repeats this 5 to 10 times a day. Each commit is a **safe point** she can return to.

---

## 📊 Diagram

```
   git init                                git commit
      │                                        │
      ▼                                        ▼
  ┌────────┐   edit    ┌───────────┐  add  ┌────────┐ commit ┌────────────┐
  │ empty  │ ────────► │ modified  │ ────► │ staged │ ─────► │ committed  │
  │  repo  │           │ untracked │       │        │        │ (history)  │
  └────────┘           └───────────┘       └────────┘        └────────────┘
                              ▲                                     │
                              └─────────── edit again ◄─────────────┘

  git status  tells you which box each file is in
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`git add` saves my work." | It only **stages**. `git commit` saves. |
| "Commit message: `update`." | Write what changed so future-you understands. |
| "`git add .` without looking." | Run `git status` first. Don't commit junk. |
| "`.gitignore` can come later." | Create it **before** the first `git add .`. |
| "`git diff` shows my new files." | It only shows changes in **tracked** files. |
| "`git commit -am` adds new files." | It only includes files Git already tracks. |
| "I ran `git init` twice, no problem." | Don't `git init` inside another repo. |

---

## 💬 Interview Corner

**Q1. What does `git init` do?**
It creates a hidden `.git` folder and turns the current folder into a Git repository.

**Q2. What is the difference between `git add` and `git commit`?**
`git add` places changes in the staging area. `git commit` saves the staged changes permanently as a snapshot in history.

**Q3. What does `git status` show?**
The current branch and which files are untracked, modified, or staged.

**Q4. What is `.gitignore`?**
A file listing files and folders that Git should not track, like `venv/`, `__pycache__/`, and `.env`.

---

## 📝 Quick Summary

- 📦 `git init` starts a repository.
- 🔍 `git status` shows what is going on. Use it constantly.
- ➕ `git add` stages, 📸 `git commit -m` saves.
- 📜 `git log --oneline` shows history.
- 🔬 `git diff` shows exact changes (`+` added, `-` removed).
- 🙈 `.gitignore` hides junk like `__pycache__/`, `venv/`, `.env`.
- 🔁 Rhythm: edit → status → add → commit.
- ✍️ Write clear commit messages.

---

## 🎯 Class Activity

**🛠️ Activity: "Build the hospital app history" (about 20 minutes)**

Follow Steps 1 to 11 on your own laptop. Raise your hand at each ✅ Checkpoint. Then, **on your own**:

1. Add a third patient `"Meena"` to `patients.py`.
2. Run `git status` and `git diff` and read them.
3. Stage and commit it with a clear message.
4. Create `doctors.py` with a list of two doctor names, and print them from `app.py`.
5. Commit that as a separate commit.
6. Show `git log --oneline`. You should have **4 commits**.

---

# 📋 Assignments — Hands-On: Your First Local Repository

| Assignment |
|---|
| Create a new repository called `hotel-app` with a Python file that prints a welcome message, and make 5 commits with clear messages. Submit a screenshot of `git log --oneline`. |
| Create a `.gitignore` before your first commit that ignores `__pycache__/`, `venv/`, and `.env`. Create a fake `.env` file and prove with `git status` that it is ignored. |
| Edit a file, run `git diff`, and explain each `+` and `-` line in your own words. |
| Edit two files but stage and commit only one of them. Show `git status` before and after. |
| Run `git show --stat` on three of your commits and write what each one changed. |
| Make a commit **without** `-m` on purpose, get out of the editor that opens (Vim: `Esc`, `:q!`, Enter. VS Code: close the tab), and write the steps you followed. |
| Create an empty folder, run `git status` there, and write the error message and why it appears. Then run `git init` and check again. |
| Use `ls -a` to find `.git`. Look inside it (`ls .git`) and list 3 names you see. Do **not** change anything. |
| Write 6 bad commit messages and rewrite each as a good one. |
| Put your earlier React or JavaScript project in Git by running `git init` in its folder, adding a proper `.gitignore` (including `node_modules/`), and making the first commit. |

---
---

# 📚 Hands-On: Branching and Merging

## 🎯 Learning Objectives

- 🌿 Explain what a **branch** is and why we use it
- 🔀 Create, switch between, and list branches
- 🤝 **Merge** a branch back into `main`
- 💥 Recognize and **resolve a merge conflict**
- 🧭 Read the commit graph with `git log --graph`

---

## 📖 Introduction

Imagine you want to try a new feature, but you're afraid of breaking the working app. 😰

A **branch** is a **safe, separate copy of your timeline**. You experiment on the branch. If it works, you **merge** it into `main`. If it doesn't, you simply delete the branch and `main` was never touched.

**Why is it important?** Every professional team works on branches. **Nobody** builds features directly on `main`.

> 🔎 **Note**
>
> You will continue in the **same `hospital-app`** folder from the last lab. Before starting, run `git status` and make sure it says **"nothing to commit, working tree clean"**.

---

## 🧠 Detailed Notes

### 🌿 1. What Is a Branch?

A branch is just a **movable label** pointing to a commit. Creating one is instant.

- `main` is the default branch (the official, working version).
- You are always **on exactly one branch**. `git status` tells you which.

```
 main:   A ── B ── C
                    \
 feature-add-patient: D
```

---

### 🪜 Lab 1. Create a Branch and Work on It

**Step 1. See your branches:**

```bash
git branch
```

```
* main
```

The `*` marks the branch you are on.

**Step 2. Create and switch to a new branch:**

```bash
git switch -c feature-add-patient
```

```
Switched to a new branch 'feature-add-patient'
```

(`-c` means *create*. It is the same as `git branch name` + `git switch name`.)

**Step 3. Make a change.** Edit **`patients.py`** to:

```python
patients = ["Asha", "Ravi", "Meena"]
```

**Step 4. Check, stage, commit:**

```bash
git status
git add patients.py
git commit -m "Add patient Meena"
```

```
[feature-add-patient 11d0ece] Add patient Meena
 1 file changed, 1 insertion(+), 1 deletion(-)
```

**Step 5. Now the magic. Go back to `main`:**

```bash
git switch main
cat patients.py
```

```
patients = ["Asha", "Ravi"]
```

✨ **Meena is gone!** Your file went back to the `main` version, because the new commit lives **only on the other branch**. (Open `patients.py` in VS Code, and you'll see the change live as you switch.)

```bash
git switch feature-add-patient
```

Meena is **back**. Same folder, different timeline. 🤯

✅ **Checkpoint 3:** You can switch between the two branches and see `patients.py` change.

🤔 **Quick thinking question:** You're on `feature-add-patient` with an **uncommitted** edit and you try `git switch main`. What might happen?

✅ **Answer:** Git may refuse (or carry the change along) to protect your work. The clean habit: **commit before you switch branches**.

---

### 🤝 2. Lab 2. Merge the Branch into `main`

**Rule:** to bring branch **X** into **main**, first **go to main**, then run `git merge X`.

```bash
git switch main
git merge feature-add-patient
```

```
Updating cf39de2..11d0ece
Fast-forward
 patients.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

📖 **Fast-forward** means `main` had no new commits of its own, so Git simply **moved the `main` label forward**. No new commit was needed.

Check:

```bash
cat patients.py
git branch
```

Meena is now in `main` ✅. Clean up the finished branch:

```bash
git branch -d feature-add-patient
```

```
Deleted branch feature-add-patient (was 11d0ece).
```

✅ **Checkpoint 4:** `git branch` shows only `main`, and `main` contains Meena.

---

### 💥 3. Lab 3. A Merge Conflict (On Purpose!)

A **conflict** happens when **two branches change the same line**. Git can't decide which one you want, so it asks **you**. It is **normal**, not an error you caused.

**Step 1. Make a branch that changes the hospital name:**

```bash
git switch -c feature-rename
```

Edit line 3 of `app.py`: change `City Hospital` to `Sunrise Hospital`.

```bash
git commit -am "Rename hospital to Sunrise"
```

**Step 2. Go back to `main` and change the SAME line differently:**

```bash
git switch main
```

Edit line 3 of `app.py`: change `City Hospital` to `Green Valley Hospital`.

```bash
git commit -am "Rename hospital to Green Valley"
```

**Step 3. Merge, and watch it fail:**

```bash
git merge feature-rename
```

```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

😮 Don't panic. Run `git status`:

```
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
	both modified:   app.py
```

**Step 4. Open `app.py`.** Git has written both versions into the file:

```
from patients import patients

<<<<<<< HEAD
print("Welcome to Green Valley Hospital")
=======
print("Welcome to Sunrise Hospital")
>>>>>>> feature-rename
for name in patients:
    print("Patient:", name)
```

| Marker | Meaning |
|---|---|
| `<<<<<<< HEAD` | **Your current branch's** version starts here (`main`) |
| `=======` | Divider |
| `>>>>>>> feature-rename` | The **incoming** version ends here |

**Step 5. Decide and edit.** Delete the three marker lines and keep the line you want. Say we keep Green Valley:

```python
from patients import patients

print("Welcome to Green Valley Hospital")
for name in patients:
    print("Patient:", name)
```

(In VS Code you can also click **Accept Current Change**, **Accept Incoming Change**, or **Accept Both Changes**.)

**Step 6. Tell Git it's resolved and finish:**

```bash
git add app.py
git commit -m "Resolve rename conflict"
```

```
[main f30a138] Resolve rename conflict
```

**Step 7. Admire the graph:**

```bash
git log --oneline --graph --all
```

```
*   f30a138 Resolve rename conflict
|\
| * eb8b2fb Rename hospital to Sunrise
* | 10be3f4 Rename hospital to Green Valley
|/
* 11d0ece Add patient Meena
* cf39de2 Show patient list and add .gitignore
* 35ab63e Add welcome message
```

The two lines split and came back together. That's your merge. 🎉

✅ **Checkpoint 5:** The app runs (`python app.py`), there are **no** `<<<<<<<` lines left in any file, and the graph shows a merge.

> 💡 **Tip**
>
> If you get scared in the middle of a conflict, run **`git merge --abort`**. It puts everything back to how it was before the merge. You can try again calmly.

---

### 🧭 4. Good Branch Habits

| Habit | Example |
|---|---|
| One branch per task | `feature-login`, `fix-age-bug` |
| Clear names (lowercase, hyphens) | `feature-add-patient` |
| Keep branches short-lived | Merge in days, not months |
| Keep `main` always working | Never commit half-done code to it |
| Delete branches after merging | `git branch -d name` |

---

## 💡 Real-Life Analogy

📝 **Writing an essay with a friend.**

`main` is the **final copy**. You make a **photocopy** (branch) to try rewriting the introduction. If you like it, you **replace** the intro in the final copy (merge). If you don't, you **throw the photocopy away**. A **conflict** is when you and your friend both rewrote the **same sentence** in different ways, and you sit together to pick the final sentence.

---

## 💻 Real-World Application

| Where | Branching |
|---|---|
| 🏢 Every company | One branch per feature or bug |
| 🧪 Experiments | Try risky ideas safely, delete if they fail |
| 🚀 Releases | A `release` branch to stabilize a version |
| 🆘 Hotfix | A quick branch to fix a live bug |
| 👥 Teams | Many developers work in parallel without stepping on each other |

---

## 🔍 Industry Example

📘 **Scenario: Two developers, one app**

1. 👩‍💻 Riya creates `feature-search` to add a search box.
2. 👨‍💻 Arjun creates `fix-table-style` to repair table CSS.
3. ✅ Arjun finishes first and merges into `main`.
4. 🔄 Riya finishes later. Both touched `App.css`, so her merge shows a **conflict**.
5. 🧩 She opens the file, keeps both sets of CSS, runs `git add App.css`, and commits.
6. 🎉 `main` now has the search box **and** the fixed table. Neither person lost any work.

---

## 📊 Diagram

```
                 git switch -c feature-add-patient
  main     ●──────●──────●────────────────────●   ← git merge (fast-forward)
                           \                  /
  feature                   ●────────────────      (commit "Add patient Meena")


  CONFLICT FLOW
  ─────────────
  git merge ─► CONFLICT ─► open file ─► edit (remove markers) ─► git add
                  │                                                │
                  └──► git merge --abort (undo)             git commit ✅
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "A branch is a full copy of my project." | It's a lightweight label. Creating one is instant. |
| "I run `git merge` on the feature branch to update main." | Switch to the **target** (`main`) first, then merge. |
| "A conflict means I broke Git." | It's normal when two branches edit the same line. |
| "Leave the `<<<<<<<` lines in the file." | Delete all markers. The code must run. |
| "Switch branches with uncommitted work." | Commit first, to avoid confusion. |
| "I'm on `main`, working on my feature." | Check `git status` or `git branch` before you start. |
| "Skip `git add` after fixing the conflict." | You must `git add` the file, then `git commit`. |

---

## 💬 Interview Corner

**Q1. What is a branch in Git?**
A lightweight, movable pointer to a commit that allows independent lines of development.

**Q2. What is a merge conflict, and how do you resolve it?**
It occurs when two branches change the same lines. You edit the file to the version you want, `git add` it, and `git commit`.

**Q3. What is a fast-forward merge?**
When the target branch has no new commits, Git just moves its pointer ahead. No merge commit is needed.

**Q4. How do you create and switch to a new branch in one command?**
`git switch -c branch-name`.

---

## 📝 Quick Summary

- 🌿 A branch is a safe, separate line of work.
- 🆕 `git switch -c name` creates and switches.
- 🔁 `git switch name` moves between branches. Files change with it!
- 🤝 `git merge X` brings X **into the branch you're on**.
- ⏩ Fast-forward = pointer move. Conflict = same line edited twice.
- 💥 Fix conflict: edit → `git add` → `git commit`.
- 🛑 `git merge --abort` cancels a merge.
- 🧹 Delete merged branches with `git branch -d`.

---

## 🎯 Class Activity

**🛠️ Activity: "Branch, merge, conflict" (about 20 minutes)**

Follow Labs 1, 2, and 3 above in your `hospital-app`. Then **on your own**:

1. Create a branch `feature-doctors` and add a `doctors.py` file (or edit it if you made one). Commit.
2. Switch to `main` and confirm `doctors.py` is **gone** from the folder (or unchanged).
3. Merge `feature-doctors` into `main` and delete the branch.
4. Create a **second conflict** with a classmate's help: each of you changes the same line in a different way on different branches, then merge and resolve.
5. Run `git log --oneline --graph --all` and explain the picture to a neighbour.

---

# 📋 Assignments — Hands-On: Branching and Merging

| Assignment |
|---|
| In your `hotel-app` repository, create branches `feature-a` and `feature-b`, make one commit on each, and show `git branch` output. |
| Do a fast-forward merge and prove it with `git log --oneline --graph`. Write why it was a fast-forward. |
| Create a merge conflict on purpose, resolve it in VS Code, and write the exact steps you followed. |
| Start a merge conflict and cancel it with `git merge --abort`. Show `git status` before and after. |
| Switch between two branches 5 times while keeping `patients.py` open in VS Code, and describe what you saw happen to the file. |
| Create a branch, make a commit, then delete it with `git branch -d`. Try deleting a branch that has **not** been merged and write what Git says. |
| Draw (or write in text) the commit graph of your project after 3 branches have been merged. |
| Rename a branch using `git branch -m old-name new-name` and show the result. |
| Add a new feature (for example a `search` function) on a branch to your hospital app, test it, and merge it to `main`. |
| Write a 6-line "branch rules" guide for a team of 3 friends working on one project. |

---
---

# 📚 A First Look at Advanced Git

## 🎯 Learning Objectives

- ↩️ Know the **names** and purposes of the common "undo" tools: `restore`, `revert`, `reset`
- 🧳 Try `stash` to pause unfinished work
- 🏷️ Try `tag` to label a version
- 🕰️ Know that `reflog` is a safety net
- 🗺️ See what's coming next: **GitHub, push, pull, pull requests**

> 🔎 **Note**
>
> This topic is an **introduction only**. Today you learn *what these tools are for*. We will practice them in detail in later sessions.

---

## 📖 Introduction

You now know the core of Git: **init, status, add, commit, log, diff, branch, switch, merge**. That is enough to use Git every day. 🎉

Mistakes will happen, though: wrong edit, wrong file, unfinished work. This topic gives you a **map** of the extra tools, so when you need them, you know they exist.

---

## 🧠 Detailed Notes

### 🗺️ 1. The "Undo" Map

| Situation | Tool | Danger level |
|---|---|---|
| I edited a file and want the **old version back** | `git restore file` | ⚠️ Deletes my unsaved edits |
| I staged a file by mistake | `git restore --staged file` | ✅ Safe |
| I committed something wrong and want to **cancel it safely** | `git revert <commit>` | ✅ Safe |
| I want to erase recent commits completely | `git reset` | 🔴 Dangerous (just know it exists) |

---

### 🪜 Mini-Lab A. `git restore` (Discard an Edit)

Make sure your status is clean. Then add a junk line to `app.py` (run these in **Git Bash**, where `echo ... >> file` adds a line to the end of a file):

```bash
echo 'print("oops")' >> app.py
git status --short
```

```
 M app.py
```

Undo it:

```bash
git restore app.py
git status
```

```
nothing to commit, working tree clean
```

The "oops" line is **gone for good** (Git can't bring back edits that were never committed).

> ⚠️ **Important**
>
> `git restore file` is **permanent**. Run `git diff` first to be sure you really want to throw the changes away.

---

### 🪜 Mini-Lab B. `git revert` (Safely Cancel a Commit)

Make a commit by mistake:

```bash
echo "secret" > bad.txt
git add bad.txt
git commit -m "Add bad file"
```

Cancel it **without rewriting history**:

```bash
git revert --no-edit HEAD
```

```
[main 56d33cf] Revert "Add bad file"
 1 file changed, 1 deletion(-)
 delete mode 100644 bad.txt
```

`bad.txt` is gone, and `git log --oneline` now shows **both** the mistake and the revert. Nothing was erased, so it is **safe** even in a team.

🤔 **Quick thinking question:** Why does Git add a new "revert" commit instead of just deleting the bad one?

✅ **Answer:** Because history is a **record**. Teammates may already have the bad commit. Adding a new "undo" commit keeps everyone's history consistent. (Deleting commits, as `reset` does, is risky on shared work.)

---

### 🧳 2. `git stash`: Pause Unfinished Work

Imagine you're halfway through an edit and must switch branches urgently. Use the stash drawer:

```bash
echo "work in progress" >> patients.py
git stash
```

```
Saved working directory and index state WIP on main: f30a138 Resolve rename conflict
```

Your folder is clean again. Do your urgent work, then bring the edit back:

```bash
git stash pop
```

```
Changes not staged for commit:
	modified:   patients.py
```

Clean up the practice edit afterwards:

```bash
git restore patients.py
```

---

### 🏷️ 3. `git tag`: Label a Version

A **tag** is a permanent name for a commit, usually a version number.

```bash
git tag v1.0
git tag
```

```
v1.0
```

Companies tag every release (`v1.0`, `v1.1`, `v2.0`) so they can always find exactly what was shipped.

---

### 🕰️ 4. Just Know These Names (Introduction Only)

| Tool | One-line meaning | When you'll meet it |
|---|---|---|
| `git reset` | Move the branch backward, erasing commits | Later, with care |
| `git reflog` | A diary of where Git's pointers have been. Can rescue "lost" commits | When you panic |
| `git commit --amend` | Fix the **last** commit's message or contents | Before sharing |
| `git rebase` | Replay your commits on top of another branch (a cleaner alternative to merge) | Advanced |
| `git cherry-pick` | Copy one specific commit to another branch | Advanced |
| `git blame` | Who last changed each line of a file | Debugging |

> 💡 **Tip**
>
> You don't need these today. Just remember: **committed work is very hard to lose**. If you ever think you've lost something, ask before trying clever commands.

---

### 🌐 5. What's Next: GitHub

So far, your project exists **only on your laptop**. If the laptop breaks, it's gone, and no teammate can see it. Next session, we connect to **GitHub**:

| Command / feature | Purpose |
|---|---|
| `git remote add origin URL` | Link your project to GitHub |
| `git push` | Upload your commits |
| `git pull` | Download teammates' commits |
| `git clone` | Copy a GitHub project to your laptop |
| **Pull Request** | Ask teammates to review and merge your branch |

---

### 🧰 6. Command Cheat Sheet (Everything from Today)

| Command | What it does |
|---|---|
| `git init` | Start a repository |
| `git status` | Show what changed |
| `git add file` / `git add .` | Stage changes |
| `git commit -m "msg"` | Save a snapshot |
| `git log --oneline` | Show history |
| `git diff` | Show unstaged changes |
| `git branch` | List branches |
| `git switch -c name` | Create and switch branch |
| `git switch name` | Switch branch |
| `git merge name` | Merge `name` into the current branch |
| `git branch -d name` | Delete a merged branch |
| `git restore file` | Discard edits |
| `git revert HEAD` | Safely cancel the last commit |
| `git stash` / `git stash pop` | Pause and resume work |
| `git tag v1.0` | Label a version |

---

## 💡 Real-Life Analogy

✍️ **Editing a handwritten letter.**

- `restore` = throwing away your rough draft and going back to the neat copy.
- `revert` = sending a **second letter** that says "ignore my previous letter". Nothing is secretly erased.
- `stash` = putting a half-written letter **in a drawer** while you answer the doorbell.
- `tag` = putting a **sticky note** on the final version: "Version 1".
- `reset` = tearing up a letter (powerful, but dangerous!).

---

## 💻 Real-World Application

| Where | Used for |
|---|---|
| 🚨 Production bug | `revert` the faulty release quickly |
| 🔀 Interruption | `stash`, fix the urgent bug, come back |
| 🚀 Releases | Tags like `v2.3.1` mark exactly what was shipped |
| 🕵️ Debugging | `blame` and `log` find where a bug started |
| 🌐 Teams | Push, pull, and pull requests (the next session) |

---

## 🔍 Industry Example

📘 **Scenario: A bad deployment at 5 PM**

1. 🔥 Staff report the patient page crashes after today's release.
2. 🔎 The lead runs `git log --oneline` and finds the commit "Change patient API response".
3. ↩️ She runs `git revert <commit>`. Git creates a new commit that undoes it.
4. 🚀 The previous working behaviour is live again within minutes.
5. 🧪 The original developer fixes the problem on a **branch**, tests it, and merges it the next day.
6. 🏷️ The team tags the fixed release `v1.4.1`. History shows exactly what happened, with nothing erased.

---

## 📊 Diagram

```
   Where is the mistake?                 Tool
 ┌─────────────────────────────┐
 │ Edited, not staged          │ ───►  git restore file
 │ Staged, not committed       │ ───►  git restore --staged file
 │ Committed (even if shared)  │ ───►  git revert <commit>   ✅ safe
 │ Unfinished, need to switch  │ ───►  git stash / git stash pop
 │ Want to label a version     │ ───►  git tag v1.0
 └─────────────────────────────┘

   revert:   A─B─C─D        becomes   A─B─C─D─D'   (D' cancels D, history kept)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`git restore` can be undone." | Discarded uncommitted edits are gone. Check `git diff` first. |
| "`revert` deletes the bad commit." | It adds a new commit that cancels it. |
| "`git reset --hard` is a harmless undo." | It can destroy work. Don't use it until you are taught. |
| "Stash is permanent storage." | It's a temporary drawer. Pop it soon. |
| "I need all these commands today." | The basic 9 commands are enough for daily work. |
| "Tags and branches are the same." | A branch moves as you commit. A tag stays on one commit forever. |

---

## 💬 Interview Corner

**Q1. What is the difference between `git revert` and `git reset`?**
`revert` adds a new commit that undoes an earlier one and keeps history. `reset` moves the branch backward and erases commits, which is risky on shared branches.

**Q2. What does `git stash` do?**
It temporarily saves your uncommitted changes and gives you a clean working directory. `git stash pop` brings them back.

**Q3. What is a Git tag?**
A permanent label on a specific commit, commonly used for release versions such as `v1.0`.

**Q4. What is the difference between `git fetch`/`pull` and `git push`?**
`pull` downloads and merges remote changes, and `push` uploads your commits to a remote like GitHub. (We cover this next session.)

---

## 📝 Quick Summary

- ↩️ `git restore file` discards edits (⚠️ permanent).
- 🔄 `git revert` is the **safe** way to cancel a commit.
- 🧨 `git reset` erases commits. Just know it exists.
- 🧳 `git stash` and `git stash pop` pause and resume work.
- 🏷️ `git tag v1.0` labels a version.
- 🕰️ `reflog`, `rebase`, `cherry-pick`, and `blame` are **names to remember** for later.
- 🌐 Next: **GitHub** with push, pull, clone, and pull requests.
- 💾 Commit often. Committed work is hard to lose.

---

## 🎯 Class Activity

**🛠️ Activity: "Try each tool once" (about 10 minutes)**

In your `hospital-app`:

1. Add a junk line to `app.py`, check `git status`, then discard it with `git restore`.
2. Commit a file called `bad.txt`, then cancel it with `git revert --no-edit HEAD`. Look at `git log --oneline`.
3. Edit `patients.py`, then `git stash`. Check that the file is back to normal. Then `git stash pop`.
4. Restore the practice edit, then create a tag: `git tag v1.0`, and list tags with `git tag`.
5. Run `git log --oneline --graph --all` one last time and compare it with a neighbour's.

---

# 📋 Assignments — A First Look at Advanced Git

| Assignment |
|---|
| Edit a file, discard the change with `git restore`, and write why you can't get it back. |
| Stage a file by mistake and unstage it with `git restore --staged`. Show `git status` before and after. |
| Commit a wrong file, then cancel it with `git revert`. Paste `git log --oneline` and explain each line. |
| Explain in 5 lines why `revert` is safer than `reset` for a team project. |
| Use `git stash` in the middle of an edit, switch to another branch, come back, and `git stash pop`. Describe each step. |
| Create tags `v1.0` and `v1.1` on two different commits, and use `git log --oneline` to show where each tag is. |
| Run `git show <tag>` and write what information you see. |
| Research (briefly) one of `rebase`, `cherry-pick`, or `reflog`, and write 5 lines about what it does. No need to practice yet. |
| Print the cheat sheet from this topic, and write one line beside each command in your own words. |
| Create a complete practice project from scratch: `git init`, 3 commits, 1 feature branch, 1 merge, and 1 tag. Submit a screenshot of `git log --oneline --graph --all`. |

# 📚 GitHub and Remote Repositories

## 🎯 Learning Objectives

- ☁️ Understand what a **remote** repository is
- 🆕 Create a GitHub account and repository
- 🔗 Connect a local repo to GitHub with `git remote add`
- ⬆️⬇️ Use `push`, `pull`, `fetch`, and `clone`
- 🔐 Authenticate using a **Personal Access Token** or **SSH key**
- 📝 Write a good **README.md**

---

## 📖 Introduction

So far, Git lived only on **your laptop**. If your laptop breaks, everything is lost, and teammates can't see your work.

**GitHub** is a website that stores a copy of your repository **in the cloud**. Your laptop's copy is the **local** repository, and the GitHub copy is the **remote** repository.

**Why is it important?** It gives you **backup**, **sharing**, **collaboration**, and a **portfolio** that recruiters can see.

**Where is it used?** Every company and open-source project hosts code on GitHub, GitLab, or Bitbucket.

> 🔎 **Note**
>
> This topic continues from the local Git session. You will upload the **same `hospital-app` project** (with all its commits and branches) that you built on your laptop.

---

## 🧠 Detailed Notes

### 🆕 1. Getting Started on GitHub

1. Sign up at **github.com** (use a professional username, since recruiters see it).
2. Click **New repository**.
3. Enter a name (for example `hospital-app`), choose **Public** or **Private**.
4. If you already have a local project, **don't** tick "Add a README" (to avoid conflicts).

---

### 🔗 2. Connecting Local to Remote

```bash
git remote add origin https://github.com/YOUR-USERNAME/hospital-app.git
git remote -v                 # show remotes
git branch -M main            # make sure branch is called main
git push -u origin main       # first push
```

| Word | Meaning |
|---|---|
| `origin` | The default **nickname** for your GitHub repo URL |
| `main` | The branch you are pushing |
| `-u` | Remember the link, so later you can just type `git push` |

---

### ⬆️ 3. Push, ⬇️ Pull, 🔄 Fetch, 📥 Clone

| Command | What it does |
|---|---|
| `git push` | Uploads your **commits** to GitHub |
| `git pull` | Downloads new commits **and merges** them into your branch |
| `git fetch` | Downloads new commits but **does not merge** (just look) |
| `git clone URL` | Copies a whole remote repo to your computer (first time) |

```bash
git clone https://github.com/someone/project.git
cd project
# ... work, commit ...
git pull          # get teammates' updates
git push          # share yours
```

> 💡 **Tip**
>
> `git pull` = `git fetch` + `git merge`. Make it a habit: **pull before you start working** and **pull before you push**.

🤔 **Quick thinking question:** You commit locally. Is the code on GitHub yet?

✅ **Answer:** No. A commit is saved **locally**. It reaches GitHub only after `git push`.

---

### 🔐 4. Authentication

GitHub **no longer accepts your account password** for `git push` over HTTPS. Use one of these:

| Method | How | Good for |
|---|---|---|
| **HTTPS + Personal Access Token (PAT)** | GitHub → Settings → Developer settings → Personal access tokens. Use the token as the password. Git Credential Manager (installed with Git on Windows) remembers it. | Easiest start |
| **SSH key** | Generate a key and add the **public** key to GitHub | Long-term, no repeated logins |


> 🪟 **On Windows**
>
> Git for Windows includes **Git Credential Manager**. On your first `git push` over HTTPS, a **browser sign-in window** opens. Log in to GitHub and click **Authorize**. Windows then remembers you, so you usually **don't need to create a token by hand**. The SSH commands below also work in **Git Bash**.

**SSH setup (optional):**

```bash
ssh-keygen -t ed25519 -C "you@example.com"
# press Enter for defaults, then show the PUBLIC key:
cat ~/.ssh/id_ed25519.pub
# paste it into GitHub → Settings → SSH and GPG keys → New SSH key
ssh -T git@github.com
```

Use the SSH URL: `git@github.com:YOUR-USERNAME/hospital-app.git`

> ⚠️ **Important**
>
> Never share or upload your **private** key (`id_ed25519`) or your token. Never paste a token inside code or commit it.

---

### 📝 5. README.md: Your Project's Front Page

`README.md` is shown automatically on the repo's page. Write it in Markdown.

````markdown
# 🏥 Hospital App

A React + FastAPI app to manage patients.

## Features
- Patient list with search
- Login and protected pages

## How to run
```bash
cd backend && uvicorn main:app --reload
cd frontend && npm install && npm run dev
```

## Tech stack
React, FastAPI, SQLite
````

A good README answers: **What is it? How do I run it? What does it use?**

---

### 🌿 6. Pushing Branches

```bash
git switch -c feature-login
git push -u origin feature-login    # publish the branch
```

Your branch appears on GitHub, and teammates can see it.

---

### 🧯 7. Common Push Problem: "rejected"

```
! [rejected]  main -> main (fetch first)
```

Meaning: GitHub has commits you don't have. Fix:

```bash
git pull          # bring them in (resolve conflicts if any)
git push
```

> ⚠️ **Important**
>
> Avoid `git push --force` unless you are 100% sure. It can **erase teammates' work** on GitHub.

---

## 💡 Real-Life Analogy

☁️ **Google Docs and your laptop copy.**

Your laptop repo is your **notebook**. GitHub is the **shared cloud folder**. `push` = uploading your pages. `pull` = downloading your friends' pages. `clone` = photocopying the whole shared notebook for the first time.

---

## 💻 Real-World Application

| Where | GitHub usage |
|---|---|
| 💼 Recruiters | Review candidates' repositories |
| 🌐 Open source | Python, React, and VS Code are all on GitHub |
| 🏢 Companies | Private repos for team projects |
| 🚀 Deployment | Render, Vercel, and Netlify deploy straight from a GitHub repo |
| 📚 Learning | Clone sample projects and study them |

---

## 🔍 Industry Example

📘 **Scenario: A new developer joins a hospital software team**

1. 📧 She gets access to the company's private repo `patient-portal`.
2. 📥 She runs `git clone <url>`, getting all code and history.
3. 🌿 She creates `feature-appointments`, works for two days, and commits regularly.
4. ⬇️ Before pushing she runs `git pull` to get her teammates' changes.
5. ⬆️ She runs `git push -u origin feature-appointments`.
6. 🔔 On GitHub, her teammates see the new branch and review it (next topic: pull requests).

---

## 📊 Diagram

```
   YOUR LAPTOP                              GITHUB (remote "origin")
 ┌─────────────────┐                       ┌─────────────────────┐
 │ working files   │                       │                     │
 │ staging         │                       │   hospital-app      │
 │ local commits   │ ──── git push ──────► │   (shared copy)     │
 │                 │ ◄─── git pull ─────── │                     │
 └─────────────────┘                       └─────────▲───────────┘
                                                      │
                                         git clone ───┘ (first time)
                                                      │
   TEAMMATE'S LAPTOP ◄──────────────────────────────  │
        push / pull  ◄──────────────────────────────►─┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Commit = uploaded to GitHub." | Commit is local. You must `git push`. |
| "I'll use my GitHub password on push." | Use a Personal Access Token or SSH key. |
| "`git push --force` fixes rejections." | It can destroy teammates' work. Pull first. |
| "Creating the repo with a README and also pushing my local one." | Creates unrelated histories. Start empty if you already have local code. |
| "Commit my token or `.env` to GitHub." | Anyone can read public repos. Keep secrets out and use `.gitignore`. |
| "`git clone` needs `git init` first." | Clone creates the folder and repo for you. |
| "`fetch` and `pull` are the same." | `fetch` only downloads. `pull` also merges. |

---

## 💬 Interview Corner

**Q1. What is a remote repository?**
A version of the repository hosted on a server (like GitHub) that team members push to and pull from.

**Q2. What is `origin`?**
The default name Git gives to the remote you cloned from or added.

**Q3. What is the difference between `git fetch` and `git pull`?**
`fetch` downloads remote changes without merging. `pull` fetches and then merges them.

**Q4. What does `git clone` do?**
It copies a remote repository, including its full history, to your computer.

---

## 📝 Quick Summary

- ☁️ GitHub hosts your repository online.
- 🔗 `git remote add origin URL` links local to remote.
- ⬆️ `git push` uploads commits, ⬇️ `git pull` downloads and merges.
- 🔄 `git fetch` only downloads.
- 📥 `git clone` copies a repo the first time.
- 🔐 Use a Personal Access Token or SSH key (not your password).
- 📝 Write a clear `README.md`.
- 🙅 Never push secrets, and avoid `--force`.

---

## 🎯 Class Activity

**🛠️ Activity: "Put your project on GitHub"**

1. Create a GitHub account and a new **empty** repository named `hospital-app`.
2. In your local repo, run `git remote add origin <your URL>`.
3. Run `git push -u origin main`, signing in with a token or SSH key.
4. Refresh the GitHub page and see your files and commit history.
5. Add a `README.md` locally, commit, and push again.
6. Ask a classmate to **clone** your repo and tell you what they see.
7. Edit a file directly on GitHub (pencil icon), then run `git pull` on your laptop.

---

# 📋 Assignments — GitHub and Remote Repositories

| Assignment |
|---|
| Create a GitHub account, add a profile picture and short bio, and share your profile URL. |
| Push your `hospital-app` repo to GitHub and share a screenshot of the commit list on GitHub. |
| Create a Personal Access Token (or SSH key), use it to push, and write which one you chose and why. (Do not share the token!) |
| Write a README for your hotel or hospital project with title, features, how to run, and tech stack. |
| Make a commit on GitHub's website (edit a file), then run `git pull` and show it appears locally. |
| Clone any public repository (for example a Python sample project) and list its files, then run `git log --oneline` there. |
| Create a rejected push on purpose: edit on GitHub, edit locally, try to push. Fix it using `git pull` and explain the steps. |
| Push a feature branch to GitHub and show it in the branch dropdown. |
| Run `git remote -v` and explain each line of the output. |
| Add `.env` to `.gitignore` before the first push, and show that it isn't on GitHub. |

---
---

# 📚 Collaboration on GitHub: Forks, Pull Requests, Issues

## 🎯 Learning Objectives

- 🔁 Follow the standard **feature-branch workflow**
- 📬 Create and review a **Pull Request (PR)**
- 🍴 Use **fork** to contribute to someone else's project
- 🐞 Use **Issues** to track tasks and bugs
- 🛡️ Understand **branch protection** and good PR habits
- 🤝 Handle updates from teammates

---

## 📖 Introduction

Real software is built by **teams**. Teams don't push straight to `main`. Instead, they ask others to **review** the changes first.

A **Pull Request (PR)** says: *"I finished my branch. Please review it and merge it into `main`."*

**Why is it important?** PRs catch bugs, share knowledge, and keep `main` clean. Every company works this way, and interviewers often ask about it.

**Where is it used?** Open-source projects and every professional dev team.

---

## 🧠 Detailed Notes

### 🔁 1. The Feature-Branch Workflow

```
1. Update main            git switch main && git pull
2. Create a branch        git switch -c feature-search
3. Code + commit          git add . && git commit -m "..."
4. Push the branch        git push -u origin feature-search
5. Open a Pull Request    (on GitHub)
6. Review + fix           (teammates comment, you push more commits)
7. Merge the PR           (on GitHub)
8. Update local main      git switch main && git pull
9. Delete the branch      git branch -d feature-search
```

---

### 📬 2. Creating a Pull Request

1. Push your branch. GitHub shows a **Compare & pull request** button.
2. Choose: **base** = `main` (where it should go), **compare** = your branch.
3. Write a clear **title and description**: what changed, why, how to test.
4. Pick **reviewers** and click **Create pull request**.

**A good PR description:**

```markdown
## What
Adds search box to the patients page.

## Why
Receptionists need to find patients quickly.

## How to test
1. Run the app and open /patients
2. Type "asha" and see 1 result

Closes #12
```

> 💡 **Tip**
>
> Writing `Closes #12` in a PR **automatically closes Issue #12** when the PR is merged.

---

### 👀 3. Code Review

Reviewers can:

| Action | Meaning |
|---|---|
| 💬 Comment | Ask a question or suggest an improvement on a line |
| ✅ Approve | Looks good to merge |
| ❌ Request changes | Must be fixed first |

After feedback, just **commit and push to the same branch**. The PR updates automatically.

**Merge options on GitHub:**

| Option | Result |
|---|---|
| Create a merge commit | Keeps all commits and adds a merge commit |
| Squash and merge | Combines all PR commits into **one** (clean history) |
| Rebase and merge | Replays commits on top of `main` |

For beginners, **Squash and merge** is a good default.

---

### 🍴 4. Fork and Contribute to Someone Else's Project

You can't push to a repo you don't own. Instead:

1. Click **Fork** on GitHub (copies the repo into **your account**).
2. `git clone` **your fork**.
3. Create a branch, make a change, commit, and push to your fork.
4. Click **Contribute → Open pull request** to ask the original owner to merge.

To keep your fork updated, add the original repo as `upstream`:

```bash
git remote add upstream https://github.com/ORIGINAL-OWNER/project.git
git fetch upstream
git switch main
git merge upstream/main
```

---

### 🐞 5. Issues

**Issues** are tasks, bugs, or ideas attached to a repository.

- Give each a clear **title** and description (steps to reproduce for bugs).
- Add **labels** (`bug`, `enhancement`) and **assignees**.
- Reference them in commits and PRs: `#12`.

---

### 🛡️ 6. Protecting `main`

In the repo's **Settings → Branches** you can add a **branch protection rule** so that:

- Nobody can push directly to `main`
- A PR needs at least 1 approval
- Tests must pass before merging

This is how companies keep `main` safe.

---

### 🤝 7. Collaborator Etiquette

| Do ✅ | Don't ❌ |
|---|---|
| Small PRs (one feature) | Giant PRs with 50 files |
| Pull before you start | Work on outdated code |
| Reply politely to review comments | Take feedback personally |
| Test before opening a PR | Open a PR with broken code |
| Describe what and why | Write "changes" as the title |

🤔 **Quick thinking question:** Your PR got a "request changes" review. Do you create a new PR after fixing it?

✅ **Answer:** No. Commit and push to the **same branch**. The existing PR updates automatically.

---

## 💡 Real-Life Analogy

📰 **A newspaper editor.**

A reporter (you) writes an article (feature branch). Before it's printed on the front page (`main`), the **editor reviews it** (Pull Request). The editor can say *"fix this paragraph"* (request changes) or *"print it"* (approve). The **fork** is like writing for a *different* newspaper: you propose your article, and their editor decides.

---

## 💻 Real-World Application

| Where | Pull Requests |
|---|---|
| 🏢 Product companies | Mandatory review before code reaches `main` |
| 🌐 Open source (Python, React, Django) | Thousands of PRs from strangers via forks |
| 🧪 CI/CD | Automated tests run on every PR |
| 📚 Documentation | Fix a typo in a project's docs as a first PR |
| 🎓 Portfolio | Contribution graph shows your activity |

---

## 🔍 Industry Example

📘 **Scenario: Adding "Delete patient" to a hospital app**

1. 🐞 The product manager creates **Issue #21**: "Staff cannot delete a patient".
2. 🌿 Developer Meera runs `git switch -c feature-delete-patient`.
3. 💻 She adds the button and a FastAPI endpoint, and commits in small steps.
4. ⬆️ She pushes and opens a PR titled "Add delete patient", with `Closes #21`.
5. 🤖 Automated tests run on the PR and pass ✅.
6. 👀 A senior developer comments: "Ask for confirmation before deleting." Meera fixes it and pushes again.
7. ✅ The reviewer approves. The PR is **squash-merged** into `main`, and Issue #21 closes automatically.
8. 🚀 The release goes out the next morning.

---

## 📊 Diagram

```
  GitHub: original repo (owner/project)
        ▲                │
        │ Pull Request   │ Fork
        │                ▼
  GitHub: your fork (you/project)
        ▲                │
        │ git push       │ git clone
        │                ▼
  Your laptop:  main ── feature-branch (commits)

  Team workflow (no fork):

  main ──●──────────────────────●── (merge)
          \                    /
           feature ●──●──●────   ← PR: review ► approve ► merge
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "PRs are only for open source." | Companies use them for every change. |
| "Push straight to `main`, it's faster." | You skip review and risk breaking `main`. |
| "Create a new PR for each review fix." | Push to the same branch. |
| "Fork and clone are the same." | Fork copies on GitHub. Clone copies to your laptop. |
| "A huge PR is efficient." | Reviewers can't review it well. Keep PRs small. |
| "Never update my branch from `main`." | Pull `main` regularly to avoid big conflicts. |
| "Forgot to say what the PR does." | Always write a title and description. |

---

## 💬 Interview Corner

**Q1. What is a pull request?**
A request to merge changes from one branch into another, giving teammates a chance to review and discuss before merging.

**Q2. What is the difference between fork and clone?**
A fork is a copy of a repo in your GitHub account. A clone is a copy of a repo on your computer.

**Q3. Describe your workflow for adding a feature.**
Update `main`, create a feature branch, commit, push, open a PR, address review comments, merge, and delete the branch.

**Q4. What is squash and merge?**
It combines all commits of a PR into a single commit on `main`, keeping history clean.

---

## 📝 Quick Summary

- 🌿 One branch per feature or fix.
- 📬 A Pull Request asks to merge your branch, with review.
- 👀 Reviewers comment, approve, or request changes.
- 🔁 Fix review comments by pushing to the same branch.
- 🍴 Fork = your own GitHub copy of someone else's repo.
- 🐞 Issues track bugs and tasks. `Closes #12` links a PR.
- 🛡️ Branch protection keeps `main` safe.
- 🧹 After merging, pull `main` and delete the branch.

---

## 🎯 Class Activity

**🛠️ Activity: "Peer pull request"**

1. Work in pairs. Student A owns a repo and adds Student B as a **collaborator** (Settings → Collaborators), or Student B **forks** it.
2. Student B clones, creates `feature-readme-update`, edits the README, commits, and pushes.
3. Student B opens a **Pull Request** with a clear title and description.
4. Student A **reviews** it: leaves one comment, then approves.
5. Student A **merges** the PR.
6. Both run `git switch main && git pull` and check the README changed.
7. Swap roles and repeat.

---

# 📋 Assignments — Collaboration on GitHub

| Assignment |
|---|
| Create an Issue in your own repo ("Add search feature") with a description and a label. |
| Create a branch for that issue, make a change, open a PR with `Closes #<issue number>`, merge it, and show that the issue closed automatically. |
| Fork any public practice repository, clone your fork, and make a small improvement on a branch. |
| Open a Pull Request from your fork to a classmate's repo, and write a good description. |
| Review a classmate's PR with at least one line comment and one approval. |
| Merge a PR using **Squash and merge**, and compare the history with a normal merge commit. |
| Set up `upstream`, then sync your fork with the original repo and show `git remote -v`. |
| Turn on a branch protection rule requiring a PR before merging and try pushing directly to `main`. Note the result. |
| Create a conflict between two PRs, resolve it on your branch, and write the steps. |
| Write a PR template file (`.github/pull_request_template.md`) with What / Why / How to test sections. |