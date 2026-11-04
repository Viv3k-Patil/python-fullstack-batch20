# 📚 Version Control and Git Basics

## 🎯 Learning Objectives

- 🧠 Understand what **version control** is and why every developer uses it
- 🆚 Know the difference between **Git** and **GitHub**
- ⚙️ Install and configure Git on your laptop
- 📦 Create a repository and save snapshots with `add` and `commit`
- 🔍 Check progress using `status`, `diff`, and `log`
- 🙈 Use `.gitignore` to keep unwanted files out of Git

---

## 📖 Introduction

Have you ever saved files like `project_final.py`, `project_final_v2.py`, `project_final_REAL.py`? 😅 That is a manual (and messy) version control system.

**Git** is a tool that **remembers every version of your project**, tells you **what changed, when, and who changed it**, and lets you **go back** if something breaks.

**Why is it important?** Every software company uses Git. Without it, teams overwrite each other's work and nobody can undo mistakes.

**Where is it used?** Every project in this course (your hotel app, hospital app, FastAPI backend) should live in Git.

---

## 🧠 Detailed Notes

### 🧭 1. What Is Version Control?

A **Version Control System (VCS)** records changes to files over time.

| Without version control | With Git |
|---|---|
| Copy folders with names like `final_v3` | One folder, full history inside |
| "Who broke the code?" | `git log` shows who changed what |
| Fear of trying new ideas | Try on a branch, throw it away if it fails |
| Teammates overwrite each other | Changes are merged safely |

**Git is a *distributed* VCS:** every developer has a **full copy** of the history on their own computer, so you can work offline.

---

### 🆚 2. Git vs GitHub

| | **Git** | **GitHub** |
|---|---|---|
| What is it? | A **tool** installed on your computer | A **website** that hosts Git repositories |
| Works offline? | ✅ Yes | ❌ Needs internet |
| Made by | Linus Torvalds (2005) | GitHub (owned by Microsoft) |
| Job | Track versions | Share code, collaborate, backup |

> 💡 **Tip**
>
> Git is like **MS Word's version history**. GitHub is like **Google Drive** where you upload and share it. Alternatives to GitHub: GitLab and Bitbucket. They all use Git.

---

### ⚙️ 3. Installing and Configuring Git

1. Download from **git-scm.com** and install (on Windows this also gives you **Git Bash**).
2. Check it works:

```bash
git --version
```

3. Tell Git **who you are** (once per computer). This name and email go into every commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list
```

> ℹ️ **Note**
>
> Use the same email you use on GitHub, so your commits are linked to your profile.

---

### 📦 4. Creating a Repository

A **repository (repo)** is a project folder that Git is tracking. The history lives in a hidden folder called `.git`.

```bash
mkdir hospital-project
cd hospital-project
git init
```

Output: `Initialized empty Git repository ...`

> ⚠️ **Important**
>
> Never delete the `.git` folder. It **is** your history. Also never run `git init` inside another repo.

---

### 🗂️ 5. The Three Areas (Most Important Idea!)

```
 Working Directory  ──git add──►  Staging Area  ──git commit──►  Repository
  (your files)                  (ready to save)                 (saved history)
```

| Area | Meaning | Analogy |
|---|---|---|
| **Working directory** | Files you edit | Your desk |
| **Staging area** | Changes you chose to include in the next save | Items placed in a box |
| **Repository** | Permanent snapshots (commits) | Sealed and labeled boxes in a warehouse |

---

### 📸 6. Your First Commit

```bash
echo 'print("Hello Hospital")' > app.py
git status                       # app.py is "untracked"
git add app.py                   # move it to the staging area
git commit -m "Add first version of app.py"
```

- `git add .` stages **all** changes in the folder.
- A **commit** is a snapshot with a message, author, date, and a unique id (hash).

**Writing good commit messages:**

| ❌ Bad | ✅ Good |
|---|---|
| `update` | `Add patient search to patients page` |
| `fixed stuff` | `Fix crash when age is empty` |
| `asdf` | `Add .gitignore for Python` |

Rule of thumb: start with a verb, keep it under about 50 characters, describe **what** and **why**.

🤔 **Quick thinking question:** You edited three files but want to commit only two of them. How?

✅ **Answer:** Stage only those two: `git add file1.py file2.py`, then `git commit`. The third stays modified but uncommitted. This is why the staging area exists.

---

### 🔍 7. Looking Around: `status`, `diff`, `log`

```bash
git status            # what changed? what's staged?
git diff              # changes NOT yet staged
git diff --staged     # changes staged for the next commit
git log               # full history
git log --oneline     # one line per commit (great for quick view)
git log --oneline --graph --all
```

---

### 🙈 8. `.gitignore`: Files Git Should Skip

Some files must **never** be committed: virtual environments, secrets, caches, database files.

Create a file named `.gitignore`:

```gitignore
# Python
__pycache__/
*.pyc
venv/
.venv/

# Secrets and local settings
.env

# Databases and logs
*.db
*.log

# Node / React
node_modules/
dist/

# Editors / OS
.vscode/
.DS_Store
```

```bash
git add .gitignore
git commit -m "Add .gitignore"
```

> ⚠️ **Important**
>
> `.gitignore` only affects files **not yet tracked**. If you already committed a secret like `.env`, adding it to `.gitignore` later does **not** remove it from history. Never commit passwords or API keys.

---

## 💡 Real-Life Analogy

🎮 **Saving points in a video game.**

Each **commit** is a **save point**. You can keep playing, and if you die (break your code), you **load an earlier save**. The **staging area** is deciding *which* progress goes into the next save. **GitHub** is the cloud where you back up all your save files.

---

## 💻 Real-World Application

| Where | Git usage |
|---|---|
| 🐧 Linux kernel | Git was created for it; thousands of contributors |
| 🏢 Google, Microsoft, Amazon | Teams store code in Git repositories |
| 🏥 Hospital software teams | Track every change for audits and bug tracing |
| 🎓 Students | Portfolio projects shown to recruiters |
| 📄 Docs and config | Even documents and server configs are versioned |

---

## 🔍 Industry Example

📘 **Scenario: A bug appears after Friday's release**

1. 🐞 The billing page shows wrong totals on Monday.
2. 🔍 A developer runs `git log --oneline` and sees a commit "Change tax calculation" from Friday.
3. 🔬 She runs `git diff` between the commits and spots a `*` that should have been `+`.
4. 🩹 She fixes it and commits: "Fix tax calculation operator".
5. 📜 The history now shows **what broke, who changed it, when, and how it was fixed**. Without Git, this would take hours of guessing.

---

## 📊 Diagram

```
        YOUR COMPUTER
 ┌────────────────────────────────────────────────┐
 │  Working Directory      Staging Area    .git   │
 │  ┌──────────────┐      ┌──────────┐   ┌──────┐│
 │  │ app.py (edit)│─add─►│ app.py   │─►│commit││
 │  │ style.css    │      │          │   │ #1   ││
 │  └──────────────┘      └──────────┘   │ #2   ││
 │         ▲                              │ #3   ││
 │         └────────── checkout ──────────┴──────┘│
 └────────────────────────────────────────────────┘

 Commit history (oldest → newest):
   #1 ── #2 ── #3   ← HEAD (where you are now)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Git and GitHub are the same." | Git is the tool. GitHub is a website that hosts Git repos. |
| "`git add` saves my work." | It only **stages**. Saving happens with `git commit`. |
| "I can commit without `git config` name and email." | Git will ask or use wrong details. Configure first. |
| "Commit message: `update`." | Write clear messages for your future self. |
| "Adding `.env` to `.gitignore` removes it from history." | It does not. Never commit secrets. |
| "Commit everything with `git add .` blindly." | Check `git status` first so you don't commit junk. |
| "Running `git init` in my Documents folder." | Only run it inside the project folder. |

---

## 💬 Interview Corner

**Q1. What is Git?**
A distributed version control system that tracks changes in files and lets multiple people collaborate.

**Q2. What is the difference between Git and GitHub?**
Git is the local tool for version control. GitHub is an online service that hosts Git repositories for sharing and collaboration.

**Q3. What is the staging area?**
A holding area where you choose which changes will go into the next commit.

**Q4. What does `git init` do?**
It creates a hidden `.git` folder and turns the current folder into a Git repository.

---

## 📝 Quick Summary

- 🧠 Git records **every version** of your project.
- 🆚 Git = tool, GitHub = hosting website.
- ⚙️ Set `user.name` and `user.email` once.
- 📦 `git init` starts a repository.
- 🗂️ Files travel: working directory → staging area → repository.
- 📸 `git add` then `git commit -m "message"`.
- 🔍 `status`, `diff`, and `log` show what is going on.
- 🙈 `.gitignore` hides secrets, caches, and `venv`.

---

## 🎯 Class Activity

**🛠️ Activity: "Your first repository"**

1. Install Git and run `git --version`.
2. Set your name and email with `git config --global`.
3. Create a folder `git-practice` and run `git init`.
4. Create `hello.py` with `print("Hello Git")`. Run `git status`.
5. Stage and commit it with a good message.
6. Edit the file, run `git diff`, then commit again.
7. Run `git log --oneline` and show your two commits to a classmate.
8. Create a `.gitignore` that ignores `venv/` and `.env`, then commit it.

---

# 📋 Assignments — Version Control and Git Basics

| Assignment |
|---|
| Install Git, run `git --version`, and take a screenshot of your configured name and email using `git config --list`. |
| Create a repository for a small Python script and make at least 5 commits, each with a meaningful message. |
| Edit two files, stage only one, run `git status`, and explain what you see. |
| Use `git diff` and `git diff --staged` on the same change and explain the difference in 3 lines. |
| Run `git log --oneline --graph` and paste the output with your explanation of each line. |
| Create a `.gitignore` for a Python project, create a fake `.env` and a `venv/` folder, and prove they are ignored using `git status`. |
| Find the hidden `.git` folder on your computer, list its contents, and explain what `objects` and `HEAD` are (research briefly). |
| Write 5 bad commit messages and rewrite each one as a good commit message. |
| Create an empty folder, run `git status` before `git init`, and write what error appears and why. |
| Make a repository for your earlier hotel or hospital project and commit its current state. |

---
---

# 📚 Branching and Merging

## 🎯 Learning Objectives

- 🌿 Explain what a **branch** is and why teams use branches
- 🔀 Create, switch, list, and delete branches
- 🤝 Merge a branch into `main`
- 💥 Resolve a **merge conflict** step by step
- 🧭 Understand `HEAD` and the commit graph

---

## 📖 Introduction

Imagine you are adding a **login feature** while your friend fixes a **bug**. If you both edit the same folder, you will break each other's work.

A **branch** is a separate line of development. You work on your own branch, and when the feature is ready, you **merge** it back into the main line.

**Why is it important?** Branches keep `main` always working, and let many people work at the same time.

**Where is it used?** Every professional team uses a branch for each feature, bug fix, or experiment.

---

## 🧠 Detailed Notes

### 🌿 1. What Is a Branch?

A branch is just a **movable label** pointing to a commit. Creating one is instant and costs almost nothing.

- `main` is the default branch (the "official" version).
- `HEAD` points to the branch you are on right now.

```
 main:     A ── B ── C
                      \
 feature-login:        D ── E
```

---

### 🛠️ 2. Branch Commands

```bash
git branch                    # list branches (* = current)
git branch feature-search     # create a branch
git switch feature-search     # move to it
git switch -c feature-login   # create AND switch (most used)
git branch -d feature-search  # delete a merged branch
```

> ℹ️ **Note**
>
> Older tutorials use `git checkout`. `git switch` is the newer, clearer command for changing branches.

---

### ✍️ 3. Working on a Branch

```bash
git switch -c feature-login
# edit files...
git add .
git commit -m "Add login form"
git switch main               # your login files disappear (they live on the other branch)
git switch feature-login      # they come back
```

> 💡 **Tip**
>
> Commit or stash your work before switching branches, so changes don't get in the way.

---

### 🔀 4. Merging

To bring a branch's work into `main`:

```bash
git switch main
git merge feature-login
```

Two situations:

| Type | When | Result |
|---|---|---|
| **Fast-forward** | `main` has no new commits since you branched | Git simply moves the `main` label forward |
| **Merge commit** | Both branches have new commits | Git creates a new commit joining both lines |

```
 Fast-forward:                Merge commit:
 main: A─B                    main:  A─B─C──────M
            \                            \     /
 feat:       C─D  → main: A─B─C─D   feat:   D─E
```

After merging, delete the finished branch:

```bash
git branch -d feature-login
```

🤔 **Quick thinking question:** After `git merge feature-login`, which branch contains the new code, `main` or `feature-login`?

✅ **Answer:** Both. The merge happens **into** the branch you are on (`main`). `feature-login` is unchanged and can be deleted.

---

### 💥 5. Merge Conflicts

A conflict happens when **two branches changed the same lines** of the same file. Git can't decide, so it asks **you**.

Git marks the file like this:

```
<<<<<<< HEAD
print("Welcome to City Hospital")
=======
print("Welcome to Sunrise Hospital")
>>>>>>> feature-rename
```

| Marker | Meaning |
|---|---|
| `<<<<<<< HEAD` | Your current branch's version starts |
| `=======` | Divider |
| `>>>>>>> feature-rename` | The incoming branch's version ends |

**Steps to resolve:**

1. Run `git status` to see which files conflict.
2. Open the file and **edit it** to the final version you want (remove the 3 marker lines).
3. Stage it: `git add app.py`
4. Finish: `git commit` (or `git merge --continue`).

If you panic: `git merge --abort` goes back to before the merge.

> 💡 **Tip**
>
> VS Code shows buttons: *Accept Current*, *Accept Incoming*, *Accept Both*. Always **read and test** the code afterwards.

---

### 🧭 6. Good Branch Habits

| Habit | Example |
|---|---|
| One branch per task | `feature-login`, `fix-age-validation` |
| Meaningful names, lowercase, hyphens | `feature/patient-search` |
| Keep branches short-lived | Merge within days, not months |
| Keep `main` working | Never commit half-finished code to it |

---

## 💡 Real-Life Analogy

📝 **Writing a book with an editor.**

`main` is the **published manuscript**. You make a **copy** (branch) to rewrite Chapter 3. Meanwhile the editor fixes typos in the main manuscript. When you finish, you **merge** your chapter in. If you both rewrote the **same paragraph**, you sit together and decide which version stays. That is a **merge conflict**.

---

## 💻 Real-World Application

| Where | Branching |
|---|---|
| 🏢 Companies | One branch per ticket or feature |
| 🚀 Releases | `release/2.0` branch for stabilizing |
| 🧪 Experiments | Try risky ideas, delete if failed |
| 🆘 Hotfix | Quick branch to fix a production bug |
| 🌐 Open source | Contributors work on their own branches |

---

## 🔍 Industry Example

📘 **Scenario: Two developers, one page**

1. 👩‍💻 Riya creates `feature-search` to add a search box to the patients page.
2. 👨‍💻 Arjun creates `fix-table-style` to fix the table CSS.
3. ✅ Arjun finishes first and merges into `main`.
4. 🔄 Riya finishes later and runs `git merge main` into her branch (or merges into `main`). Both edited `App.css`, so Git reports a **conflict**.
5. 🧩 Riya opens the file, keeps both sets of CSS, runs `git add App.css`, and commits.
6. 🎉 `main` now has both the search box and the fixed table.

---

## 📊 Diagram

```
                 git switch -c feature-login
 main     A ── B ── C ───────────────── M   ← git merge feature-login
                     \                 /
 feature-login        D ── E ── F ────

 Conflict flow:
   git merge ─► CONFLICT ─► edit file ─► git add ─► git commit ─► done
                    │
                    └─► (or) git merge --abort ─► back to safety
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "A branch is a full copy of my files." | It's a lightweight pointer to a commit. |
| "I merge `main` into my feature to update main." | `git merge X` brings X **into the current branch**. Switch to the target first. |
| "Conflict means I broke something." | It's normal. Two people edited the same lines. |
| "Leave the `<<<<<<<` markers in the file." | Remove all markers, and the code must run. |
| "Work directly on `main`." | Use a feature branch and merge when it's ready. |
| "Forgetting which branch I'm on." | Check with `git status` or `git branch`. |
| "Delete a branch before merging it." | `git branch -d` protects you, but check first. |

---

## 💬 Interview Corner

**Q1. What is a branch in Git?**
A lightweight, movable pointer to a commit that lets you develop features independently.

**Q2. What is a merge conflict and how do you resolve it?**
It happens when two branches change the same lines. You edit the file to the final version, `git add` it, and commit.

**Q3. What is a fast-forward merge?**
When the target branch has no new commits, Git just moves its pointer forward without creating a merge commit.

**Q4. What is `HEAD`?**
A pointer to the current branch (and so the commit you are working on).

---

## 📝 Quick Summary

- 🌿 A branch is a separate line of work.
- 🆕 `git switch -c name` creates and switches.
- 🔀 `git merge branch` merges **into the current branch**.
- ⏩ Fast-forward = pointer move, merge commit = join of two lines.
- 💥 Conflicts happen on same-line edits. Fix, `add`, `commit`.
- 🛑 `git merge --abort` cancels a messy merge.
- 🧹 Delete merged branches with `git branch -d`.
- ✅ Keep `main` working at all times.

---

## 🎯 Class Activity

**🛠️ Activity: "Create a conflict on purpose"**

1. In your `git-practice` repo, create `welcome.py` with `print("Welcome to City Hospital")` and commit it.
2. Create a branch `feature-rename`, change the text to "Sunrise Hospital", and commit.
3. Switch back to `main`, change the same line to "Green Valley Hospital", and commit.
4. Run `git merge feature-rename` and see the conflict.
5. Fix the file, `git add`, and commit.
6. Run `git log --oneline --graph --all` and look at the shape.
7. Delete the branch.

---

# 📋 Assignments — Branching and Merging

| Assignment |
|---|
| Create three branches (`feature-a`, `feature-b`, `fix-c`), make one commit on each, and show `git branch` output. |
| Make a fast-forward merge and prove it with `git log --graph` (no merge commit). |
| Make a merge that creates a merge commit and show the graph. |
| Create a merge conflict, resolve it manually in VS Code, and write the 4 steps you did. |
| Start a merge conflict and cancel it using `git merge --abort`. Explain what state your files are in. |
| Edit a file on `main`, switch to another branch without committing, and explain what Git says. Then fix it by committing or stashing. |
| Create a branch, delete it safely with `-d`, then try to delete an **unmerged** branch and note what Git says. |
| Draw (on paper or in text) the commit graph for a project with `main` and two feature branches. |
| Rename a branch with `git branch -m old new` and show the result. |
| On your hospital or hotel project, create `feature-search`, make a small change, and merge it back into `main`. |

---
---

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

1. Create a GitHub account and a new **empty** repository named `git-practice`.
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
| Push your `git-practice` repo to GitHub and share a screenshot of the commit list on GitHub. |
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

---
---

# 📚 Undoing Changes and Useful Git Commands

## 🎯 Learning Objectives

- ↩️ Undo mistakes safely at every stage
- 📂 Discard changes, unstage files, and amend commits
- 🧨 Understand `reset` vs `revert`
- 🧳 Use `stash` to save unfinished work
- 🏷️ Tag releases
- 🕰️ Use `reflog` as a safety net

---

## 📖 Introduction

Everyone makes mistakes: wrong file committed, bad commit message, broken code. The best thing about Git is that **almost everything can be undone**, if you choose the right command.

**Why is it important?** Knowing how to undo calmly separates confident developers from scared ones.

**Where is it used?** Daily. Every developer undoes, amends, or stashes something every week.

---

## 🧠 Detailed Notes

### 🗺️ 1. Which Undo Do I Need?

| Situation | Command |
|---|---|
| Edited a file, want to **discard** the edit | `git restore file` |
| Staged a file by mistake, want to **unstage** | `git restore --staged file` |
| Last commit has a typo in the message | `git commit --amend -m "new msg"` |
| Forgot a file in the last commit | `git add file` then `git commit --amend --no-edit` |
| Undo a commit **already pushed** (shared) | `git revert <hash>` |
| Undo local commits and rewrite history | `git reset` |
| Not ready to commit but need to switch branch | `git stash` |

---

### 📂 2. Discard and Unstage

```bash
git restore app.py              # throw away unsaved edits in app.py
git restore --staged app.py     # unstage (keeps your edits)
```

> ⚠️ **Important**
>
> `git restore file` **permanently deletes** uncommitted edits. There is no undo for it. Check with `git diff` first.

---

### ✏️ 3. Amend the Last Commit

```bash
git commit --amend -m "Add patient search feature"
```

> ⚠️ **Important**
>
> Amend **rewrites** the commit. Only do it for commits that are **not pushed yet**.

---

### 🧨 4. `reset`: Move Backwards

`git reset` moves the current branch back to an earlier commit.

| Mode | Commits | Staging area | Your files |
|---|---|---|---|
| `--soft` | removed | **kept** (staged) | kept |
| `--mixed` (default) | removed | cleared | **kept** |
| `--hard` | removed | cleared | **deleted** ⚠️ |

```bash
git reset --soft HEAD~1     # undo last commit, keep changes staged
git reset HEAD~1            # undo last commit, keep changes unstaged
git reset --hard HEAD~1     # undo last commit AND destroy changes
```

`HEAD~1` means "one commit before the current one".

> ⚠️ **Important**
>
> Don't `reset` commits that you have already **pushed** and others may have pulled. It rewrites shared history.

---

### 🔄 5. `revert`: The Safe Undo for Shared Commits

`git revert` creates a **new commit** that does the opposite of an old commit. History is kept intact.

```bash
git log --oneline           # find the hash, e.g. a1b2c3d
git revert a1b2c3d
git push
```

| | `reset` | `revert` |
|---|---|---|
| How | Moves branch back (erases commits from the branch) | Adds a new commit that cancels an old one |
| History | Rewritten | Preserved |
| Safe after push? | ❌ No | ✅ Yes |

🤔 **Quick thinking question:** A buggy commit is already on GitHub `main` and teammates pulled it. `reset` or `revert`?

✅ **Answer:** `revert`. It adds a new commit without rewriting history that teammates already have.

---

### 🧳 6. `stash`: Pause Your Work

You are in the middle of something but need to switch branches urgently:

```bash
git stash                   # hide current changes
git switch hotfix-branch    # do the urgent work...
git switch feature-search
git stash list              # see saved stashes
git stash pop               # bring the changes back
```

---

### 🏷️ 7. Tags: Marking Releases

A **tag** is a permanent label for a commit, such as a version number.

```bash
git tag v1.0
git tag -a v1.1 -m "Release 1.1"
git tag                     # list tags
git push origin v1.0        # share a tag (or: git push --tags)
```

---

### 🕰️ 8. `reflog`: Your Safety Net

Even after a `reset --hard`, Git remembers where `HEAD` has been for a while:

```bash
git reflog                  # list recent HEAD positions
git reset --hard <hash>     # jump back to a lost commit
```

Committed work is very hard to lose. **Uncommitted** work is not recoverable, so commit often.

---

### 🧰 9. Handy Extras

| Command | Use |
|---|---|
| `git show <hash>` | See what a commit changed |
| `git blame file` | Who last changed each line |
| `git log --author="Name"` | Filter history |
| `git rm file` | Delete a file and stage the deletion |
| `git mv old new` | Rename a file |
| `git branch -vv` | See which branches track which remote |
| `git clean -n` | Preview untracked files that would be deleted |

---

## 💡 Real-Life Analogy

✍️ **Editing a handwritten letter.**

- `restore` = throwing away your **rough draft** and starting from the neat copy.
- `amend` = fixing a typo on the letter **before posting**.
- `revert` = sending a **second letter** that says "ignore my previous letter" (history stays, nothing is secretly erased).
- `reset` = **tearing up** a letter that hasn't left your house.
- `stash` = putting the half-written letter **in a drawer** while you answer the doorbell.

---

## 💻 Real-World Application

| Where | Used for |
|---|---|
| 🚨 Production bug | `git revert` the faulty release commit quickly |
| 🤦 Wrong commit message | `--amend` before pushing |
| 🔀 Context switch | `stash` while handling an urgent bug |
| 🚀 Releases | Tags like `v2.3.1` mark exactly what was shipped |
| 🕵️ Debugging | `blame` and `show` find the origin of a bug |

---

## 🔍 Industry Example

📘 **Scenario: A bad deployment at 5 PM**

1. 🔥 Staff report that the patient page crashes after today's release.
2. 🔎 The lead runs `git log --oneline` and finds `f4e9a1c "Change patient API response"`.
3. ↩️ She runs `git revert f4e9a1c`, which creates a new commit undoing the change.
4. ⬆️ She pushes. The deploy pipeline releases the reverted version in minutes.
5. 🧪 The developer who wrote the original commit fixes it on a **branch**, tests it, and sends a new PR the next day.
6. 🏷️ After the fix, the team tags `v1.4.1`.

History shows exactly what happened, and nothing was rewritten.

---

## 📊 Diagram

```
   Where is the mistake?                    Fix
 ┌──────────────────────────┐
 │ Edited, not staged       │ ───────────► git restore file
 ├──────────────────────────┤
 │ Staged, not committed    │ ───────────► git restore --staged file
 ├──────────────────────────┤
 │ Committed, not pushed    │ ───────────► git commit --amend  /  git reset
 ├──────────────────────────┤
 │ Pushed (shared)          │ ───────────► git revert <hash>
 ├──────────────────────────┤
 │ Unfinished, must switch  │ ───────────► git stash / git stash pop
 └──────────────────────────┘

   reset:   A─B─C─D          ► A─B─C          (D is removed)
   revert:  A─B─C─D          ► A─B─C─D─D'     (D' undoes D)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "`git reset --hard` is a harmless undo." | It deletes uncommitted work permanently. |
| "I can `reset` a pushed commit." | It rewrites shared history. Use `revert`. |
| "`git restore` can be undone." | Discarded uncommitted edits are gone. Check `git diff` first. |
| "`--amend` is fine after pushing." | It rewrites the commit and causes trouble for teammates. |
| "Stash is permanent storage." | It's temporary. Pop it soon. |
| "Reverting deletes the bad commit." | It adds a new commit that cancels it. |
| "Lost commits are gone forever." | `git reflog` often brings them back. |

---

## 💬 Interview Corner

**Q1. What is the difference between `git reset` and `git revert`?**
`reset` moves the branch back and rewrites history. `revert` adds a new commit that undoes an earlier one, so it is safe for shared branches.

**Q2. What does `git stash` do?**
It saves your uncommitted changes temporarily and gives you a clean working directory, so you can restore them later with `git stash pop`.

**Q3. How do you change the last commit message?**
`git commit --amend -m "new message"` (only if it hasn't been pushed).

**Q4. What is a Git tag?**
A named, permanent pointer to a commit, commonly used to mark release versions.

---

## 📝 Quick Summary

- ↩️ `git restore file` discards edits, `--staged` unstages.
- ✏️ `git commit --amend` fixes the last commit (before pushing).
- 🧨 `git reset` rewrites local history. `--hard` deletes changes.
- 🔄 `git revert` safely undoes a pushed commit.
- 🧳 `git stash` and `git stash pop` pause and resume work.
- 🏷️ Tags mark versions like `v1.0`.
- 🕰️ `git reflog` can rescue "lost" commits.
- 💾 Commit often. Committed work is much safer.

---

## 🎯 Class Activity

**🛠️ Activity: "Break it, then fix it"**

In `git-practice`:

1. Edit `hello.py`, then discard the edit with `git restore`.
2. Stage a file, then unstage it with `git restore --staged`.
3. Make a commit with a typo in the message, then fix it with `--amend`.
4. Make 3 commits. Use `git reset --soft HEAD~1`, check `git status`, and recommit.
5. Make a "bad" commit, find its hash, and undo it with `git revert`.
6. Start editing a file, run `git stash`, check the folder is clean, then `git stash pop`.
7. Create a tag `v1.0`, then push it with `git push origin v1.0`.
8. Run `git reflog` and find an earlier commit.

---

# 📋 Assignments — Undoing Changes and Useful Git Commands

| Assignment |
|---|
| Edit a file, discard the change with `git restore`, and explain why it can't be undone afterwards. |
| Stage two files by mistake and unstage them using `git restore --staged`. |
| Make a commit with a spelling mistake in the message and fix it using `git commit --amend`. |
| Use `git reset --soft`, `--mixed`, and `--hard` on three test commits and write what happened to your files each time. |
| Push a "bad" commit to GitHub, then undo it with `git revert` and push again. Show the history. |
| Explain, in 5 lines, why `revert` is better than `reset` for pushed commits. |
| Use `git stash` to switch branches in the middle of an edit, then `git stash pop` and show the result. |
| Create two tags, `v1.0` and `v1.1`, push them, and find them on GitHub's Releases or Tags page. |
| Do a `git reset --hard` to lose a commit on purpose, then recover it using `git reflog`. |
| Use `git blame` and `git show` to find who last changed a specific line in a file and what else was in that commit. |