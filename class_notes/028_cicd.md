# 📚 What Is CI/CD? The Big Picture

## 🎯 Learning Objectives

- 🤔 Explain the problem CI/CD solves ("it works on my machine!")
- 🔁 Define **Continuous Integration (CI)**, **Continuous Delivery**, and **Continuous Deployment (CD)**
- 🧱 Describe the stages of a **pipeline**: code → build → test → deploy
- 📖 Use the key words: **pipeline, trigger, job, step, runner, artifact**
- 🧰 Name popular CI/CD tools and know which one we will use (**GitHub Actions**)

---

## 📖 Introduction

Imagine your whole team is building the hospital app. Each person writes code on their own laptop. Finally someone says: *"Let's join everything and release it on Friday."*

Friday arrives and... 💥 nothing works. Code written by different people doesn't fit together, nobody ran the tests, and the person who knows how to upload the app to the server is on leave. 😰

**CI/CD** is the habit (and the automatic system) that prevents this. Every time someone saves code, a **robot** automatically **checks it, tests it, and can even release it**.

**Why is it important?** It catches bugs minutes after they are written, not weeks later, and it makes releases boring and safe.

**Where is it used?** Every modern company: startups, banks, hospitals, and big tech. CI/CD knowledge is expected in almost every developer job.

> 💡 **Tip**
>
> You already know Git. **CI/CD starts the moment you `git push`.** Today we make GitHub do work for us after every push.

---

## 🧠 Detailed Notes

### 😫 1. The Problem: Life Without CI/CD

| Without CI/CD | What goes wrong |
|---|---|
| Everyone merges code once a month | Huge conflicts, "integration hell" |
| Testing is manual and optional | Bugs reach real users |
| "It works on my machine!" | Different laptop, different Python version, different result |
| Release = one person, 20 manual steps | Slow, risky, mistakes happen |
| Friday release panic | Nobody wants to deploy |

---

### 🔁 2. CI: Continuous Integration

> **CI = every time someone pushes code, the code is automatically built and tested.**

- Developers merge small changes **often** (daily, not monthly).
- A robot runs the **checks** (style check, tests) on every push.
- If something breaks, the team knows **within minutes**, while the change is still fresh in memory.

**Result:** the main branch stays healthy ✅.

---

### 📦 3. CD: Continuous Delivery vs Continuous Deployment

"CD" can mean **two** things:

| | **Continuous Delivery** | **Continuous Deployment** |
|---|---|---|
| After tests pass | Code is **ready** to release | Code is **released automatically** |
| Final release step | A human clicks **"Deploy"** | **No human**, fully automatic |
| Good for | Banks, hospitals, careful teams | Fast-moving web products |

Both mean: *releasing is a **button or an automatic step**, not a stressful manual job.*

🤔 **Quick thinking question:** A hospital billing system must be approved by a manager before every release. Is that Continuous Delivery or Continuous Deployment?

✅ **Answer:** **Continuous Delivery.** The pipeline gets the code ready, and a human approves the final release.

---

### 🧱 4. What Is a Pipeline?

A **pipeline** is the automatic chain of stages your code passes through after a push:

```
  ┌────────┐   ┌────────┐   ┌────────┐   ┌─────────┐   ┌──────────┐
  │  Code  │──►│ Build  │──►│  Test  │──►│ Package │──►│  Deploy  │
  │  push  │   │ install│   │ lint + │   │ (later) │   │ to server│
  └────────┘   │  deps  │   │ pytest │   └─────────┘   └──────────┘
               └────────┘   └────────┘
                 ✅ pass → go on        ❌ fail → STOP and tell the team
```

**The golden rule:** if any stage fails, the pipeline **stops**. Broken code never reaches users.

---

### 📖 5. Vocabulary You Must Know

| Word | Meaning | Hospital analogy |
|---|---|---|
| **Pipeline / Workflow** | The whole automatic process | The full patient journey: registration → tests → treatment → discharge |
| **Trigger** | What starts it (push, pull request, schedule) | The patient walks in |
| **Job** | A group of steps run on one machine | One department (e.g., Lab) |
| **Step** | One single task inside a job | One test inside the lab |
| **Runner** | The machine that runs the job (a fresh cloud computer) | The lab room and equipment |
| **Artifact** | A file produced by the pipeline (build, report) | The lab report |

---

### 🧰 6. Popular CI/CD Tools

| Tool | Notes |
|---|---|
| **GitHub Actions** | Built into GitHub. **We use this today.** |
| GitLab CI/CD | Built into GitLab |
| Jenkins | Older, very common in big companies, self-hosted |
| CircleCI, Travis CI | Cloud CI services |
| Azure DevOps, AWS CodePipeline | Cloud-vendor tools |

The **ideas are identical** in all of them. Learn one and the others are easy.

---

### ✅ 7. Benefits in One Table

| Benefit | How |
|---|---|
| 🐞 Fewer bugs | Tests run on **every** push |
| ⚡ Faster feedback | Know in minutes if something broke |
| 🧘 Calm releases | Same automatic steps every time |
| 🤝 Better teamwork | Everyone trusts the main branch |
| 📜 Traceability | Every run is logged |

---

## 💡 Real-Life Analogy

🏭 **A car factory assembly line with quality checks.**

Workers add parts (developers push code). After every station, a **robot inspector** checks quality (CI tests). If a part is faulty, the **line stops** immediately, and it never reaches the showroom. When all checks pass, the car is **driven automatically to the showroom** (CD). Without the line, you'd assemble all parts at the end and discover the problems in front of the customer. 🚗

---

## 💻 Real-World Application

| Where | CI/CD usage |
|---|---|
| 🛒 Amazon, Netflix | Release changes many times a day through automated pipelines |
| 🏥 Hospital software | Every change tested before release, for safety and audit |
| 🏦 Banks | Pipelines with approvals and security scans |
| 🌐 Open source (Python, React, FastAPI) | Every pull request is tested automatically |
| 📱 Mobile apps | Automatic builds for app stores |

---

## 🔍 Industry Example

📘 **Scenario: A developer fixes the billing bug**

1. 👩‍💻 Meera fixes the discount calculation and runs `git push`.
2. 🤖 GitHub notices the push and starts a **fresh cloud computer** (runner).
3. 📥 It downloads her code, installs Python and the libraries, and runs the **style check and tests**.
4. ❌ One test fails: she forgot a case. She gets an email within two minutes.
5. 🔧 She fixes it and pushes again. This time everything is ✅ **green**.
6. 🚀 A reviewer merges the change, and the pipeline **deploys** the new version automatically.

Total time from push to live: minutes, with **no manual copying of files** and **no forgotten tests**.

---

## 📊 Diagram

```
   Developer                GitHub                         Server / Users
   ─────────                ──────                         ──────────────
   git push  ───────────►  trigger fires
                              │
                       ┌──────▼───────┐
                       │   CI PIPELINE │
                       │ 1. checkout   │
                       │ 2. install    │
                       │ 3. lint       │
                       │ 4. test       │
                       └──────┬───────┘
                       ✅ pass │  ❌ fail ──► email / red ✗ on the commit
                              ▼
                       ┌──────────────┐
                       │ CD: deploy   │ ──────────────────►  new version live 🎉
                       └──────────────┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "CI/CD is a tool I install." | It's a **practice**. Tools like GitHub Actions help you do it. |
| "CI and CD are the same." | CI = build and test on every push. CD = release automatically (or at a button press). |
| "Pipelines are only for big companies." | Even a student project benefits from automatic tests. |
| "If tests pass, there are no bugs." | Tests only catch what they check. Write good tests. |
| "CI/CD replaces testing." | It **runs** your tests. You must still write them. |
| "Deploy first, test later." | The pipeline tests first, and deploys only on success. |
| "CD always means no human." | Continuous **Delivery** keeps a human approval. |

---

## 💬 Interview Corner

**Q1. What is CI/CD?**
A practice where code changes are automatically built and tested (CI) and then delivered or deployed to users (CD) through an automated pipeline.

**Q2. What is the difference between Continuous Delivery and Continuous Deployment?**
In Delivery, the code is always ready to release but a human approves the release. In Deployment, every change that passes the tests is released automatically.

**Q3. What is a pipeline?**
An automated sequence of stages (build, test, deploy) that runs after code changes, and stops if any stage fails.

**Q4. Why is CI important for a team?**
It finds integration bugs early, keeps the main branch working, and gives quick feedback to developers.

---

## 📝 Quick Summary

- 😫 Without CI/CD: late merges, manual testing, scary releases.
- 🔁 **CI** = automatic build and test on every push.
- 📦 **CD** = automatic (or one-click) release.
- 🧱 A **pipeline** = stages that stop on the first failure.
- 📖 Key words: trigger, job, step, runner, artifact.
- 🧰 Tools: GitHub Actions, GitLab CI, Jenkins, and more.
- ✅ Goal: fast feedback and a **always-working** main branch.

---

## 🎯 Class Activity

**🛠️ Activity: "Peek into real pipelines" (about 5 minutes)**

1. Open a popular public repository on GitHub, for example `fastapi/fastapi`.
2. Click the **Actions** tab at the top.
3. Open any recent run. Count the **jobs** and find one **green ✅** and (if you can) one **red ❌** run.
4. In pairs, list the **manual steps you do today** before sharing your hotel or hospital project (running it, checking it, uploading it). Which of them could a robot do?

---

# 📋 Assignments — What Is CI/CD? The Big Picture

| Assignment |
|---|
| Write the steps you currently follow to check your own project before submitting it. Mark which steps a robot could automate. |
| Open the **Actions** tab of two public repositories and note the workflow names, how long a run took, and whether it passed. |
| Draw the CI/CD pipeline for a hospital app on paper, with at least 4 stages and what happens when a stage fails. |
| Write 5 real-life examples (not software) of "check before you continue" systems, such as airport security. |
| Create a table comparing Continuous Delivery and Continuous Deployment with your own example for each. |
| Explain "it works on my machine" with a real example from your own coding experience. |
| Find the **status badge** (the green "passing" icon) on the README of a public repository, and write what it tells visitors. |
| Research one CI/CD tool (Jenkins, GitLab CI, or CircleCI) and write 5 lines on how it is different from GitHub Actions. |

---
---

# 📚 Hands-On: Your First CI Pipeline with GitHub Actions

## 🎯 Learning Objectives

- 🧪 Write simple automated **tests** with `pytest`
- 📄 Understand the structure of a **workflow YAML file**
- 🚀 Create a workflow that runs **style checks and tests** on every push
- 👀 Read the **Actions tab** (green ✅ and red ❌ runs)
- 🔴 **Break** the code on purpose, see the pipeline fail, then fix it

---

## 📖 Introduction

Time to build a real CI pipeline! You will take a tiny Python project, put it on GitHub, and teach GitHub to **test it automatically on every push**.

**GitHub Actions** is GitHub's built-in CI/CD service. You describe your pipeline in a **YAML file** inside your repo, and GitHub runs it on a free cloud computer.

> 🔎 **Note**
>
> You need: **Git** (from the earlier sessions), a **GitHub account**, **VS Code**, and **Python**. Use **Git Bash** on Windows. Make your GitHub repository **Public** (public repos get free Actions minutes and free branch protection).

---

## 🧠 Detailed Notes

### 🪜 Step 1. Create the Project

In Git Bash:

```bash
cd ~
mkdir hospital-ci
cd hospital-ci
code .
```

In VS Code, create these three files.

**📁 `app.py`**

```python
def calculate_bill(days, rate_per_day, discount_percent=0):
    """Total bill for a hospital stay, after discount."""
    total = days * rate_per_day
    discount = total * discount_percent / 100
    return total - discount


def is_valid_phone(phone):
    """A valid phone has exactly 10 digits."""
    return phone.isdigit() and len(phone) == 10


def age_group(age):
    """Return Child, Adult or Senior."""
    if age < 18:
        return "Child"
    if age < 60:
        return "Adult"
    return "Senior"
```

**📁 `test_app.py`**

```python
from app import age_group, calculate_bill, is_valid_phone


def test_bill_without_discount():
    assert calculate_bill(3, 2000) == 6000


def test_bill_with_discount():
    assert calculate_bill(2, 1000, 10) == 1800


def test_valid_phone():
    assert is_valid_phone("9876543210") is True


def test_invalid_phone():
    assert is_valid_phone("98765") is False
    assert is_valid_phone("98765abcde") is False


def test_age_groups():
    assert age_group(8) == "Child"
    assert age_group(30) == "Adult"
    assert age_group(65) == "Senior"
```

**📁 `requirements.txt`**

```
pytest
flake8
```

**📁 `.gitignore`**

```
__pycache__/
.pytest_cache/
venv/
.env
```

> ⚠️ **Important (Windows)**
>
> Create `.gitignore` in **VS Code** (not Notepad), so it isn't saved as `.gitignore.txt`.

🧠 **What is a test?** A test is a small function that **calls your code and checks the answer** with `assert`. If the answer is wrong, the test **fails**. Example: `calculate_bill(2, 1000, 10)` must give `1800` (2000 minus 10%).

---

### 🪜 Step 2. Run It on Your Own Laptop First

Always make it work locally before automating it.

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

Expected (versions and times will differ):

```
test_app.py::test_bill_without_discount PASSED                           [ 20%]
test_app.py::test_bill_with_discount PASSED                              [ 40%]
test_app.py::test_valid_phone PASSED                                     [ 60%]
test_app.py::test_invalid_phone PASSED                                   [ 80%]
test_app.py::test_age_groups PASSED                                      [100%]

============================== 5 passed in 0.02s ===============================
```

Now the style checker (**flake8** finds unused imports, bad spacing, and so on):

```bash
python -m flake8 . --max-line-length=100
```

**No output means no problems.** ✅

✅ **Checkpoint 1:** `5 passed`, and flake8 prints nothing. This is exactly what the robot will do for us.

---

### 🪜 Step 3. Save It in Git

```bash
git init
git add .
git status
git commit -m "Add hospital functions and tests"
```

(Check `git status` first: `__pycache__` and `.pytest_cache` must **not** be listed.)

---

### 🪜 Step 4. Create the Workflow File

GitHub looks for workflows in a special folder: **`.github/workflows/`** (note the dot at the start).

```bash
mkdir -p .github/workflows
```

In VS Code, create **`.github/workflows/ci.yml`**:

**📁 `.github/workflows/ci.yml`**

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Get the code
        uses: actions/checkout@v7

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: python -m pip install -r requirements.txt

      - name: Check code style
        run: python -m flake8 . --max-line-length=100

      - name: Run tests
        run: python -m pytest -v
```

> ⚠️ **Important**
>
> YAML uses **spaces for indentation, never Tab**. One wrong space breaks the file. VS Code is set to insert spaces for `.yml` files by default, but check the bottom bar if you see errors.

---

### 📖 Step 5. Understand the File Line by Line

| Line | Meaning |
|---|---|
| `name: CI` | The workflow's name, shown in the Actions tab |
| `on:` | **Triggers**: when should it run? |
| `push: branches: [main]` | When someone pushes to `main` |
| `pull_request: branches: [main]` | When a pull request targets `main` |
| `jobs:` | The list of jobs (we have one, called `test`) |
| `runs-on: ubuntu-latest` | Use a fresh **Linux** cloud computer |
| `steps:` | The ordered tasks. Each begins with `-` |
| `uses: actions/checkout@v7` | Use a **ready-made action** that downloads your repository code |
| `uses: actions/setup-python@v7` | Ready-made action that installs Python |
| `with: python-version: "3.12"` | Settings for the action |
| `run: ...` | Run a **command**, just like in your terminal |

🤔 **Quick thinking question:** Why does the first step have to be `actions/checkout`?

✅ **Answer:** The runner is a **brand-new, empty computer**. It knows nothing about your code. `checkout` downloads your repository onto it, and every later step needs those files.

> ℹ️ **Note**
>
> Action versions change over time (`@v7` is the latest at the time of writing). Older versions keep working, and you can find the newest on the action's GitHub page.

---

### 🪜 Step 6. Put It on GitHub

1. On github.com click **New repository**, name it `hospital-ci`, choose **Public**, and **do not** add a README. Click **Create**.
2. Back in Git Bash:

```bash
git add .
git commit -m "Add CI workflow"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/hospital-ci.git
git push -u origin main
```

(On Windows a browser sign-in window may open. Sign in and authorize.)

---

### 🪜 Step 7. Watch the Robot Work 🤖

1. Open your repository on GitHub and click the **Actions** tab.
2. You will see a run named **"Add CI workflow"**.

| Icon | Meaning |
|---|---|
| 🟡 Yellow circle | Running |
| ✅ Green check | All steps passed |
| ❌ Red cross | A step failed |

3. Click the run, then the job **test**. Expand each step and read the output. You will see the same `5 passed` as on your laptop.

✅ **Checkpoint 2:** You see a **green ✅** run in the Actions tab.

---

### 🪜 Step 8. Break It On Purpose 💥

Open `app.py` and change the last line of `calculate_bill` from:

```python
    return total - discount
```

to:

```python
    return total + discount
```

(A "sneaky bug": the discount now **increases** the bill.)

```bash
python -m pytest -q
```

Locally you will see:

```
FAILED test_app.py::test_bill_with_discount - assert 2200.0 == 1800
1 failed, 4 passed
```

Push the bug anyway:

```bash
git commit -am "Change discount calculation"
git push
```

Go to the **Actions** tab. After a minute, the run shows ❌ **red**. Click it, open the **Run tests** step, and read:

```
>       assert calculate_bill(2, 1000, 10) == 1800
E       assert 2200.0 == 1800
```

GitHub also sends you an **email** about the failed run. 📧

> 💡 **Tip**
>
> The pipeline **stopped** at the failing step, which is the whole point. In a real team, this bug would be caught **before** it reaches users.

---

### 🪜 Step 9. Fix It and Go Green Again ✅

Change `+` back to `-`:

```python
    return total - discount
```

```bash
python -m pytest -q
git commit -am "Fix discount calculation"
git push
```

The Actions tab now shows a new ✅ run. Click on the history. You can see **both** the red and the green runs, a full record of what happened.

✅ **Checkpoint 3:** You have seen a red ❌ run and a green ✅ run for your own project.

---

### 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| No run appears | Is the file exactly at `.github/workflows/ci.yml`? Is the branch `main`? |
| "Invalid workflow file" | Indentation problem. Use spaces (no tabs) and compare with the notes. |
| flake8 fails: `F401 imported but unused` | You imported something you didn't use. Remove it. |
| flake8 fails: `E501 line too long` | Shorten the line (limit is 100 here). |
| `python` not recognized on your laptop | Install Python and tick "Add python.exe to PATH". |
| Pushing asks for a password | Sign in through the browser window (Git Credential Manager). |
| Tests pass locally but fail on GitHub | Maybe a file is not committed. Check `git status`. |

---

## 💡 Real-Life Analogy

🍳 **A restaurant kitchen with a quality inspector.**

The `.yml` file is the **recipe card** for the inspector: *"1. Get the ingredients (checkout). 2. Preheat the oven (install). 3. Check hygiene (flake8). 4. Taste the dish (pytest)."* Every time a cook finishes a dish (push), a **brand-new inspector in a clean kitchen** (runner) follows the card **exactly**. If the dish fails the taste test, it never leaves the kitchen.

---

## 💻 Real-World Application

| Where | Same idea |
|---|---|
| 🐍 Python and FastAPI projects | Tests run on every pull request |
| ⚛️ React projects | `npm test` and `npm run build` run automatically |
| 🏥 Hospital apps | Calculation rules (billing, dosage) are checked by tests on every change |
| 🏢 Startups | A green pipeline is required before merging |
| 📦 Libraries (pip packages) | Tests run on several Python versions |

---

## 🔍 Industry Example

📘 **Scenario: A billing rule changes**

1. 🏥 The hospital introduces a 10% senior-citizen discount.
2. 👩‍💻 A developer changes `calculate_bill` and pushes to a branch.
3. 🤖 GitHub Actions starts a clean Ubuntu runner, installs Python 3.12, installs `pytest` and `flake8`, and runs both.
4. ❌ A test written months ago for the **old** rule fails. The developer sees the red cross and realises a related feature also needed an update.
5. 🛠️ She fixes it in the same branch and pushes. The run turns ✅.
6. 💰 A wrong-bill bug that could have affected real patients **never reached production**.

---

## 📊 Diagram

```
   git push ──► GitHub finds .github/workflows/ci.yml
                         │
                 ┌───────▼────────┐   (a fresh Linux runner, empty)
                 │   job: test    │
                 │                │
                 │ 1. checkout    │──► downloads your code
                 │ 2. setup-python│──► installs Python 3.12
                 │ 3. pip install │──► pytest, flake8
                 │ 4. flake8      │──► style OK?   ── ❌ stop
                 │ 5. pytest      │──► tests OK?   ── ❌ stop
                 └───────┬────────┘
                         ▼
                   ✅ green check on your commit


   Workflow file anatomy:

   name ─ on (triggers) ─ jobs ─┬─ job "test" ─ runs-on ─ steps ─┬─ uses (ready-made)
                                │                                 └─ run  (command)
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I'll test it only on GitHub." | Run the commands locally first. It is faster to debug. |
| "Tabs and spaces are the same in YAML." | YAML allows **only spaces**. |
| "The runner already has my code." | It is empty. You need `actions/checkout`. |
| "The workflow can be anywhere." | It must be in `.github/workflows/`. |
| "A red ❌ means GitHub is broken." | It means **your code** failed a check. Read the logs. |
| "Install packages from my laptop." | The runner installs from `requirements.txt`. Keep it updated. |
| "Ignore failures and push again." | Read the failing step. The log tells you what's wrong. |
| "Use `pytest` without `python -m`." | `python -m pytest` avoids PATH problems, especially on Windows. |

---

## 💬 Interview Corner

**Q1. What is GitHub Actions?**
GitHub's built-in CI/CD service that runs automated workflows, defined in YAML files, in response to events like pushes and pull requests.

**Q2. Where do workflow files live?**
In the `.github/workflows/` folder of the repository.

**Q3. What is the difference between `uses` and `run` in a step?**
`uses` runs a ready-made, reusable action (like `actions/checkout`). `run` executes a shell command.

**Q4. What is a runner?**
The machine (a fresh virtual computer, like `ubuntu-latest`) where a job executes.

---

## 📝 Quick Summary

- 🧪 Tests are small functions with `assert` that check your code.
- 📄 A workflow is a YAML file in `.github/workflows/`.
- ⚡ `on:` sets triggers, `jobs:` holds the work, `steps:` are the tasks.
- 📥 `actions/checkout` is almost always the first step.
- 🔧 `uses` = ready-made action, `run` = command.
- 👀 The **Actions tab** shows 🟡 running, ✅ passed, ❌ failed.
- 🔴 A failing step **stops** the pipeline.
- 🏃 Always make it pass **locally** first.

---

## 🎯 Class Activity

**🛠️ Activity: "Make it green, break it, fix it" (about 25 minutes)**

1. Follow Steps 1 to 7 and reach a **green ✅** run (Checkpoint 2).
2. Break the code (Step 8), push, and find the **red ❌** run. Read the failing line in the logs.
3. Fix it (Step 9) and confirm the **green ✅** again.
4. **On your own:** add a new function `is_emergency(severity)` that returns `True` when severity is 4 or 5, plus **one test** for it. Push and watch the new test run in the pipeline.
5. Show your Actions tab (with both red and green runs) to your neighbour.

---

# 📋 Assignments — Hands-On: Your First CI Pipeline with GitHub Actions

| Assignment |
|---|
| Complete the lab and submit a screenshot of your Actions tab showing at least one red ❌ run and one green ✅ run. |
| Add 3 more tests (for example `calculate_bill` with 0 days, or `age_group` at exactly 18 and 60). Push and show that they run on GitHub. |
| Add a new function and a test for it, but **forget to commit the test file**. Describe what happens in the pipeline. |
| Introduce a flake8 error on purpose (like an unused import). Show the red run and read which line the log points to. |
| Change the Python version in the workflow to `"3.11"` and run again. Compare the "Set up Python" step output. |
| Add an extra step to the workflow that prints `python --version`. Find its output in the logs. |
| Break the YAML indentation on purpose and push. Describe the error message you see on GitHub. |
| Add the CI status badge to your `README.md`: `![CI](https://github.com/YOUR-USERNAME/hospital-ci/actions/workflows/ci.yml/badge.svg)`. Show how it turns red and green. |
| Write a 6-line explanation of the workflow in your own words, as if you were teaching a friend. |
| Apply the same idea to your own hotel or hospital Python project: add a simple `pytest` test and a workflow, and push it. |

---
---

# 📚 Hands-On: CD, Pull Requests, and Secrets

## 🎯 Learning Objectives

- 🚀 Add a **deploy job** that runs only after the tests pass
- 🎛️ Control **when** a job runs using `needs` and `if`
- 🔀 See CI protect `main` through a **pull request**
- 🔑 Store a **secret** safely (never in code!)
- 🛡️ Require passing checks before merging
- 🏅 Add a status badge to your README

---

## 📖 Introduction

Your pipeline now **tests**. That's the **CI** half. Now the **CD** half: after the tests pass on `main`, the pipeline should **deploy**.

Real deployment (to a cloud server) needs an account and a secret key, which is out of scope today. So we use a **practice deploy** that just prints a message, and a **real example** that you can switch on later. The pipeline shape is **exactly the same** as the real thing.

> 🔎 **Note**
>
> Continue in the same `hospital-ci` repository. Make sure your latest run is green ✅ first.

---

## 🧠 Detailed Notes

### 🚀 1. Add a Deploy Job

Add this **below** the `test` job in `ci.yml` (same indentation level as `test:`, so it's inside `jobs:`):

**📁 `deploy-job.yml`**

```yaml
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy (practice version)
        run: echo "Deploying hospital-ci to production..."
```

| Line | Meaning |
|---|---|
| `needs: test` | Run **only after** the `test` job succeeds. If tests fail, deploy is **skipped** |
| `if: ...` | Run only for a **push to `main`**, not for pull requests or other branches |
| `echo "Deploying..."` | A stand-in for a real deploy command |

```
   push to main ──► [ test ] ──✅──► [ deploy ]
                       │
                      ❌ ──► deploy is SKIPPED
```

Commit and push:

```bash
git add .
git commit -m "Add deploy job"
git push
```

In the Actions tab you now see **two jobs** connected by an arrow: `test` then `deploy`.

✅ **Checkpoint 4:** Both jobs are green, and the deploy log shows `Deploying hospital-ci to production...`.

🤔 **Quick thinking question:** You push a bug to `main`. The `test` job is ❌ red. What happens to `deploy`?

✅ **Answer:** It is **skipped** (grey), because of `needs: test`. Broken code is never deployed.

---

### 🔀 2. Pull Requests: CI Protects `main`

In real teams, nobody pushes straight to `main`. They use a **branch and a pull request**, and CI checks the change **before** it is merged. Let's try that.

**Step 1. Create a branch:**

```bash
git switch -c feature-senior-discount
```

**Step 2. Add a function to `app.py`:**

```python
def senior_discount(age):
    """Seniors (60+) get 10 percent discount."""
    return 10 if age >= 60 else 0
```

**Step 3. Add a test, but with a deliberate mistake.** In `test_app.py`, change the import line to:

```python
from app import age_group, calculate_bill, is_valid_phone, senior_discount
```

and add at the end:

```python
def test_senior_discount():
    assert senior_discount(65) == 15
    assert senior_discount(30) == 0
```

(We wrote `15` by mistake. It should be `10`.)

**Step 4. Push the branch and open a pull request:**

```bash
git add .
git commit -m "Add senior discount"
git push -u origin feature-senior-discount
```

On GitHub click **Compare & pull request**, then **Create pull request**.

**Step 5. Look at the PR page.** At the bottom you'll see the checks:

```
❌ CI / test (pull_request)   Failing
(deploy is not run for pull requests)
```

The PR is telling reviewers: **do not merge, the tests fail.** 🛑

**Step 6. Fix the test** (`15` to `10`), then:

```bash
git commit -am "Fix senior discount test"
git push
```

The PR **updates automatically**, and the check turns ✅ green.

**Step 7. Merge the pull request** (click **Merge pull request**) and go to the **Actions** tab. A new run starts on `main`, and this time **both `test` and `deploy` run**. 🎉

```bash
git switch main
git pull
```

✅ **Checkpoint 5:** You saw a red PR check, fixed it, merged, and watched `deploy` run on `main`.

---

### 🔑 3. Secrets: Never Put Passwords in Code

A real deploy needs a **secret** (an API key, a deploy URL, a password). If you write it in the YAML or code, **everyone who can see the repo can see it**, and bots scan GitHub for leaked keys within minutes. ⚠️

**The safe way:**

1. On GitHub: **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
2. Name: `DEPLOY_URL`, Value: any text (for practice, `hello123`). Click **Add secret**.
3. Use it in the workflow:

```yaml
      - name: Use a secret
        run: echo "The secret has ${#DEPLOY_URL} characters"
        env:
          DEPLOY_URL: ${{ secrets.DEPLOY_URL }}
```

(This prints only the **length**, never the secret itself.)

Facts to remember:

- GitHub **hides** secret values in logs (you'll see `***`).
- You can't read a secret back after saving it. You can only replace it.
- Secrets are **not** available to pull requests from forks (for safety).

**A real deploy** might look like this (for example, a Render "deploy hook" URL saved as the secret `RENDER_DEPLOY_HOOK`). Don't run it today; it's an **example** of what replaces our `echo`:

```yaml
      - name: Trigger deploy on Render
        run: curl -X POST "$HOOK"
        env:
          HOOK: ${{ secrets.RENDER_DEPLOY_HOOK }}
```

---

### 🛡️ 4. Protect `main`: Make the Checks Mandatory

So far a person could still ignore a red PR and merge. Let's **forbid** it:

1. Repository **Settings** → **Branches** (or **Rules → Rulesets**) → **Add rule** for `main`.
2. Tick **Require a pull request before merging**.
3. Tick **Require status checks to pass before merging** and select the check named **test**.
4. Save.

Now GitHub will **block** the merge button while tests are red. This is how companies guarantee that `main` always works. (For private repositories, this feature may need a paid plan.)

---

### 🏅 5. Status Badge

Add to the top of your `README.md`:

```markdown
![CI](https://github.com/YOUR-USERNAME/hospital-ci/actions/workflows/ci.yml/badge.svg)
```

The badge shows **passing** (green) or **failing** (red) for everyone who visits your repo. Recruiters like it. 😎

---

## 💡 Real-Life Analogy

✈️ **An airline's pre-flight checklist and boarding gate.**

The **tests** are the pre-flight inspection. The plane (`deploy`) is **allowed to take off only if** the inspection passed (`needs: test`). Passengers (pull requests) cannot board until the gate agent sees the green light (**required checks**). The **secret** is the cockpit key: kept in a locked safe (GitHub Secrets), never written on a sticky note on the plane's door (your code).

---

## 💻 Real-World Application

| Where | Usage |
|---|---|
| 🏢 Every professional team | PRs must pass CI before merge |
| 🚀 Web deployments | Deploy only from `main` after tests pass |
| 🔐 Cloud keys, DB passwords | Stored as secrets, never in code |
| 🏥 Regulated software | Required checks and approvals create an audit trail |
| 🌐 Open source | Maintainers ignore PRs with red checks |

---

## 🔍 Industry Example

📘 **Scenario: Releasing a hospital app update**

1. 👨‍💻 Arjun creates `feature-lab-reports`, pushes, and opens a PR.
2. 🤖 CI runs tests and style checks. It's ✅.
3. 👀 Two teammates review the code. A rule requires **1 approval + green checks**.
4. ✅ The PR is merged into `main`.
5. 🚀 The **deploy job** starts automatically. It reads the deploy key from **GitHub Secrets** and tells the server to update.
6. 🏷️ In a regulated company, a manager must click **Approve** on a "production" environment before the last step (that is **Continuous Delivery**).
7. 📜 Every step is logged: who merged, what was tested, and when it was deployed.

---

## 📊 Diagram

```
   feature branch ──push──► Pull Request
                                │
                          ┌─────▼──────┐
                          │ CI: test   │ ──❌──► PR blocked 🛑 (fix and push again)
                          └─────┬──────┘
                              ✅ │  + review approval
                                ▼
                          merge into main
                                │
                          ┌─────▼──────┐
                          │ CI: test   │
                          └─────┬──────┘
                              ✅ │
                          ┌─────▼──────┐   uses  ┌──────────────┐
                          │ CD: deploy │ ◄────── │ 🔑 Secrets   │
                          └─────┬──────┘         └──────────────┘
                                ▼
                         production updated 🎉
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "Put the API key in the YAML for now." | Never. Use **Secrets**. Leaked keys get abused fast. |
| "`deploy` doesn't need `needs`." | Without `needs`, it may run **in parallel** with tests. |
| "Push straight to `main`, it's quicker." | Use PRs, so CI can check **before** merging. |
| "A red PR can still be merged, so it's fine." | Turn on **required status checks** to block it. |
| "Deploy on every branch." | Use `if:` so only `main` deploys. |
| "I committed a secret, so I'll delete the file." | It stays in Git history. **Change the secret immediately.** |
| "Print the secret to debug." | Never echo secrets into logs. |

---

## 💬 Interview Corner

**Q1. What does `needs` do in a GitHub Actions job?**
It makes a job wait for another job and run only if that job succeeds.

**Q2. Why do we use GitHub Secrets?**
To store sensitive values like API keys and passwords outside the code, so they aren't exposed in the repository or logs.

**Q3. What is branch protection with required status checks?**
A repository rule that blocks merging into a branch (like `main`) until selected CI checks pass, usually along with a review.

**Q4. Why run the deploy job only on `main`?**
So that only reviewed, tested code is released, and feature branches or pull requests never deploy to production.

---

## 📝 Quick Summary

- 🚀 CD = add a `deploy` job that runs after the tests pass.
- 🔗 `needs: test` makes deploy wait for tests (and skip on failure).
- 🎯 `if: github.ref == 'refs/heads/main'` limits deploy to `main`.
- 🔀 Pull requests show CI results **before** merging.
- 🔑 Secrets live in Settings, and you read them as `${{ secrets.NAME }}`.
- 🛡️ Branch protection makes green checks **mandatory**.
- 🏅 A README badge shows the build status.
- 🙅 Never commit passwords or keys.

---

## 🎯 Class Activity

**🛠️ Activity: "From PR to production" (about 20 minutes)**

1. Add the `deploy` job and see it run on `main` (Checkpoint 4).
2. Create the branch `feature-senior-discount`, push the function with the **wrong test**, and open a PR. Find the red check.
3. Fix the test, push, and watch the PR turn green. Merge it and watch the deploy run (Checkpoint 5).
4. Add a repository secret `DEPLOY_URL` and print its **length** in a workflow step. Confirm the actual value is **not visible** in the logs.
5. Turn on **branch protection** and try to merge a PR with a failing test. What does GitHub say?

---

# 📋 Assignments — Hands-On: CD, Pull Requests, and Secrets

| Assignment |
|---|
| Complete the full lab and submit screenshots of: the red PR check, the green PR check, and the Actions run with both `test` and `deploy`. |
| Remove `needs: test` from the deploy job, push a failing test to `main`, and describe what happens. Then restore it. |
| Change the `if:` condition so `deploy` also runs for a branch called `release`. Test it by pushing to that branch. |
| Create a secret, use it in a step through `env:`, and show that the log displays `***` if you try to print it. |
| Turn on branch protection (required status check `test`) and show the screenshot of a blocked merge. |
| Add the CI status badge to your README and take screenshots of it when passing and failing. |
| Create a second workflow file `hello.yml` that only prints "Hello from CI" on every push. Find both workflows in the Actions tab. |
| Search the internet for "GitHub leaked API key" and write 5 lines on what can go wrong and how Secrets avoid it. |
| Write a one-page plan for how your own hotel or hospital app could be deployed automatically (where would it run, what secrets would it need?). |
| Make a PR from a branch where you intentionally introduce a flake8 error, and show how the check blocks the merge. |

---
---

# 📚 CI/CD Tools in Big Projects: The DevOps Loop (Introduction)

## 🎯 Learning Objectives

- ♾️ Describe the **DevOps loop** and its 8 stages
- 🧰 Match common tools (Jira, Git, Maven, Selenium, Jenkins, Docker, Kubernetes, Ansible, Datadog...) to the right stage
- 🐳 Explain in one line what **Docker**, **Kubernetes**, and **SonarQube** do
- 🧭 Know where our GitHub Actions pipeline fits in the big picture
- 🗺️ Know which tools to learn first

> 🔎 **Note**
>
> This topic is an **introduction only**. We learn the **names and jobs** of the tools, not how to operate each one.

---

## 📖 Introduction

So far, our pipeline was small: **push, test, deploy**. In a big company with hundreds of developers, the same idea is spread over **many tools**, each doing one job well.

Don't worry about the long list of logos. They all fit into **one picture**: the **DevOps loop** (the infinity sign ♾️). Learn the picture, and each new tool becomes "just another tool for stage X".

**Why is it important?** Job descriptions and interviews are full of these names. Knowing what each one is for makes you sound like a professional.

---

## 🧠 Detailed Notes

### ♾️ 1. The DevOps Loop: 8 Stages

```
        ┌───────────── DEV ─────────────┐ ┌───────────── OPS ─────────────┐
         PLAN ──► CODE ──► BUILD ──► TEST ──► RELEASE ──► DEPLOY ──► OPERATE ──► MONITOR
          ▲                                                                          │
          └──────────────── feedback and new ideas come back to PLAN ◄───────────────┘
```

| Stage | What happens | Hospital app example |
|---|---|---|
| 📝 **Plan** | Decide what to build, track tasks | "Add senior discount" ticket |
| 💻 **Code** | Write code, keep versions | Git branch and pull request |
| 🏗️ **Build** | Turn code into a runnable package | Install libraries, build the app |
| 🧪 **Test** | Check it works and is safe | `pytest`, browser tests |
| 📦 **Release** | Approve and store the finished version | Version `1.4` marked ready |
| 🚀 **Deploy** | Put it on servers | Update the live website |
| ⚙️ **Operate** | Keep servers running and configured | Scale up on busy mornings |
| 📊 **Monitor** | Watch health and errors, then feed back | Alert: "login page is slow" |

It's a **loop**: monitoring finds problems and ideas, which go back to **Plan**. That is why DevOps never "ends".

---

### 🧰 2. Tools by Stage

The picture you saw shows classic tools. Here they are, together with the modern ones used today:

| Stage | Classic tools (in the picture) | Other popular tools |
|---|---|---|
| 📝 Plan | **Jira**, **Confluence** | Trello, Azure Boards, Notion |
| 💻 Code | **Git** | GitHub, GitLab, Bitbucket |
| 🏗️ Build | **Maven**, **sbt** (Java/Scala builds) | `pip`, `npm`, Vite, Gradle, **Docker** |
| 🧪 Test | **JUnit** (Java), **Selenium** (browser) | `pytest`, Playwright, Cypress, **SonarQube**, Trivy |
| 📦 Release | **Jenkins**, CodeShip | **GitHub Actions**, GitLab CI, Docker Hub, Nexus, Artifactory |
| 🚀 Deploy | **Docker**, **AWS**, DC/OS | **Kubernetes**, Helm, Argo CD, Azure, Google Cloud |
| ⚙️ Operate | **Ansible**, **Chef**, **Kubernetes** | **Terraform**, Puppet |
| 📊 Monitor | **Nagios**, **Splunk**, **Datadog** | Prometheus + Grafana, ELK stack, Sentry |

> ℹ️ **Note**
>
> That picture is a classic, and some tools in it are older (DC/OS and CodeShip are rarely used today). Newer tools do the same jobs, so focus on the **idea of each stage** and not on memorizing logos.

---

### 🐳 3. Docker: "Pack the App in a Box"

**The problem:** the app works on your laptop but breaks on the server (different Python version, missing library).

**The fix:** put the app **and everything it needs** inside a **container**. It then runs the same everywhere.

| Word | Meaning |
|---|---|
| **Image** | The packed box (a read-only template) |
| **Container** | A running copy of the image |
| **Dockerfile** | The recipe that builds the image |
| **Registry** | A store for images (Docker Hub, AWS ECR, GitHub's registry) |

A tiny Dockerfile for a Python app (illustration):

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

Read it top to bottom: *start from Python, go to `/app`, install libraries, copy code, run it.*

---

### ☸️ 4. Kubernetes (K8s): "Manager of Many Containers"

One container is easy. A big system has **hundreds** of containers across many servers. **Kubernetes** runs and manages them:

| Kubernetes does | Example |
|---|---|
| 🔁 **Self-healing** | A container crashes, K8s starts a new one |
| 📈 **Scaling** | Busy morning: 3 copies become 10 automatically |
| 🔄 **Rolling updates** | New version replaces old, one copy at a time, with no downtime |
| ↩️ **Rollback** | Bad release? Go back to the last version |

Words to recognize: **Pod** (smallest unit, holds containers), **Deployment** (says "keep 3 copies running"), **Service** (stable address for pods), **Helm** (packages K8s files), **Argo CD** (keeps the cluster matching what's in Git, called **GitOps**).

🤔 **Quick thinking question:** Docker or Kubernetes: which one packs the app, and which one manages many copies of it?

✅ **Answer:** **Docker packs** the app into a container. **Kubernetes manages** many containers (start, scale, heal, update).

---

### 🔍 5. SonarQube and Security Scanners: "Quality Inspectors"

Tests check that the code **works**. These tools check that the code is **clean and safe**:

| Tool | What it checks |
|---|---|
| **SonarQube** | Code quality: bugs, **code smells**, duplicate code, test coverage, some security issues |
| **Trivy**, **Snyk** | Known vulnerabilities in libraries and Docker images |
| **Gitleaks** | Passwords or keys accidentally committed |
| **Dependabot** | Opens PRs to update outdated libraries |

**Quality Gate:** SonarQube's pass/fail rule (for example, "no new bugs and coverage at least 80%"). If the gate **fails**, the pipeline **fails**, and the code is not released.

> 🔎 **Note**
>
> SonarQube comes as a **free Community Build**, paid **Server** editions you host yourself, and **SonarQube Cloud**, a hosted version.

---

### ⚙️ 6. Infrastructure and Monitoring (Names Only)

| Tool | Job |
|---|---|
| **Terraform** | Create servers and networks **from code** (Infrastructure as Code) |
| **Ansible**, **Chef** | Configure servers (install software, set files) automatically |
| **Prometheus + Grafana** | Collect numbers (CPU, requests) and show dashboards |
| **Splunk**, **ELK** | Search and analyze logs |
| **Datadog**, **Nagios** | Watch systems and send alerts |
| **Sentry** | Catch application errors |

---

### 🧭 7. Where Does Our Pipeline Fit? What to Learn First

```
   PLAN    CODE      BUILD    TEST      RELEASE    DEPLOY    OPERATE   MONITOR
   Jira    Git ──────── GitHub Actions (what we built) ─────────►
           GitHub                                  │
                                                   ▼
                                    Docker ─► Cloud / Kubernetes ─► Grafana, Datadog
```

**A sensible learning order for you:**

| Level | Learn | You are here |
|---|---|---|
| 1 | Git, GitHub, **GitHub Actions** (tests, deploy) | ✅ Today |
| 2 | **Docker** (build and run a container) | Next |
| 3 | Deploy to a cloud (Render, AWS) | After Docker |
| 4 | Kubernetes, Terraform, SonarQube, monitoring | Job-ready extras |

---

## 💡 Real-Life Analogy

🚢 **A big shipping port.**

**Docker** is the **standard shipping container**: any goods, same box, fits any ship. **Kubernetes** is the **port manager** deciding which container goes on which truck, replacing a damaged one, and adding trucks on busy days. **SonarQube** and **Trivy** are the **customs and quality inspectors**. **Terraform** is the **blueprint** used to build the port itself. **Datadog and Grafana** are the **control-room screens**. And **Jenkins/GitHub Actions** is the **conveyor system** connecting it all.

---

## 💻 Real-World Application

| Where | Tools used |
|---|---|
| 🛒 E-commerce giants | Git, Jenkins or GitLab CI, Docker, Kubernetes, Datadog |
| 🏦 Banks | SonarQube, security scanners, approvals, Jira |
| 🏥 Hospital software firms | Quality gates and audit trails with Jira, Git, and CI |
| 🚀 Startups | GitHub Actions, Docker, one cloud, Sentry |
| ☁️ Cloud teams | Terraform and Kubernetes for everything |

---

## 🔍 Industry Example

📘 **Scenario: A hospital group's patient app**

1. 📝 The manager creates a **Jira** ticket: "Show lab reports in the app."
2. 💻 A developer works on a **Git** branch and opens a pull request on **GitHub**.
3. 🏗️ **Jenkins / GitHub Actions** starts: it installs libraries and builds a **Docker image**.
4. 🧪 `pytest` and browser tests (**Selenium/Playwright**) run. **SonarQube** checks quality, and **Trivy** scans the image for vulnerable libraries.
5. 📦 All good, so the image is stored in a **registry** with a version number.
6. 🚀 **Argo CD / Helm** update the **Kubernetes** cluster on **AWS** using a rolling update.
7. ⚙️ **Terraform** and **Ansible** keep the servers configured the same way.
8. 📊 **Prometheus, Grafana, and Datadog** watch the app. An alert about slow reports goes into a new Jira ticket, and the loop starts again. ♾️

---

## 📊 Diagram

```
                 ♾️  THE DEVOPS LOOP WITH TOOLS

   PLAN ───► CODE ───► BUILD ───► TEST ───► RELEASE ───► DEPLOY ───► OPERATE ───► MONITOR
   Jira      Git       Maven      JUnit     Jenkins      Docker      Ansible      Datadog
   Confluence GitHub   npm/pip    pytest    GitHub       Kubernetes  Terraform    Grafana
                       Docker     Selenium  Actions      AWS/Azure   Chef         Splunk
                                  SonarQube Registry     Argo CD     Kubernetes   Sentry
                                  Trivy
     ▲                                                                                │
     └─────────────── bugs, alerts and new ideas return to PLAN ◄────────────────────┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I must master every tool." | Learn the **stages** first, then tools one at a time. |
| "Docker and Kubernetes are the same." | Docker packages apps. Kubernetes manages many containers. |
| "SonarQube replaces testing." | It checks code quality. You still need tests. |
| "Jenkins, GitHub Actions, and GitLab CI are totally different." | They do the same job with different syntax. |
| "Big projects don't use simple tools like Git." | Everything starts from Git. |
| "Tools in old diagrams are what companies use today." | Some are older. The **stages** are what stay the same. |
| "Small projects need Kubernetes." | Often one server or a simple cloud service is enough. |

---

## 💬 Interview Corner

**Q1. What is the DevOps lifecycle?**
A continuous loop of plan, code, build, test, release, deploy, operate, and monitor, where monitoring feedback goes back into planning.

**Q2. What is the difference between Docker and Kubernetes?**
Docker builds and runs containers. Kubernetes orchestrates many containers across servers (scaling, healing, updates).

**Q3. What is SonarQube used for?**
Automatic code-quality analysis (bugs, code smells, duplication, coverage), with a Quality Gate that can fail the pipeline.

**Q4. Name tools for the different CI/CD stages.**
Git/GitHub (code), Maven/npm/Docker (build), JUnit/pytest/Selenium (test), Jenkins/GitHub Actions (release), Kubernetes/AWS (deploy), Terraform/Ansible (operate), Prometheus/Grafana/Datadog (monitor).

---

## 📝 Quick Summary

- ♾️ DevOps is a loop of **8 stages**: plan, code, build, test, release, deploy, operate, monitor.
- 🧰 Each stage has its own tools, and **the stages matter more than the logos**.
- 🐳 **Docker** packs the app in a container.
- ☸️ **Kubernetes** runs and scales many containers.
- 🔍 **SonarQube** and **Trivy** check quality and security. A failed **Quality Gate** stops the pipeline.
- 🏗️ **Terraform** and **Ansible** create and configure servers from code.
- 📊 **Grafana, Datadog, and Splunk** monitor the live system.
- 🗺️ Learn in order: GitHub Actions ➜ Docker ➜ Cloud ➜ Kubernetes and the rest.

---

## 🎯 Class Activity

**🛠️ Activity: "Label the loop" (about 5 minutes)**

1. Look at the DevOps loop picture on the screen.
2. For each logo (Jira, git, Maven, Selenium, JUnit, Jenkins, Docker, AWS, Ansible, Kubernetes, Datadog, Splunk), write **which stage** it belongs to and **one line** on what it does.
3. Then mark where your own `hospital-ci` workflow fits (which stages does it cover? which are missing?).
4. Compare with a neighbour.

---

# 📋 Assignments — CI/CD Tools in Big Projects: The DevOps Loop

| Assignment |
|---|
| Draw the DevOps loop on paper with all 8 stages, and write two tools next to each stage. |
| Take your `hospital-ci` pipeline and list which DevOps stages it covers and which ones are missing. |
| Write 5 lines explaining Docker to a friend using the "shipping container" idea. Include the words image and container. |
| Read the sample Dockerfile line by line and write what each of its 6 lines does. |
| Write 5 lines on the difference between Docker and Kubernetes, with your own example. |
| Research SonarQube: write what a **code smell** and a **Quality Gate** are, with one example of each. |
| Make a table of 6 tools from the picture (Jenkins, Maven, Selenium, Ansible, Splunk, Datadog) with the stage and a one-line job for each. |
| Find a job posting for a "DevOps Engineer" or "Python Developer", and list every CI/CD tool it mentions with the stage it belongs to. |
| Write your own plan for learning DevOps tools over the next 3 months (what first, what next). |

---
---

# 📚 A First Look at Advanced CI/CD

## 🎯 Learning Objectives

- 🧩 Know the names and purposes of common advanced CI/CD features
- 🔁 See how a **matrix build** tests several Python versions
- ⚡ See how **caching** speeds pipelines up
- ⏰ See how **schedules** and manual triggers work
- ⚛️ See what a **React/Node** pipeline looks like
- ✋ Know why **environments, approvals, and rollbacks** matter

> 🔎 **Note**
>
> This topic is an **introduction only**. We just look at the ideas so you know they exist. You'll practice them in later sessions.

---

## 📖 Introduction

You now have a complete beginner pipeline: **push → test → deploy**. Real-world pipelines grow from this base. This topic is a **map** of what you will meet next, so no word in a job description feels scary.

---

## 🧠 Detailed Notes

### 🔁 1. Matrix Builds: Test Many Versions at Once

Your users may run different Python versions. A **matrix** repeats the same job for each:

**📁 `adv-matrix.yml`**

```yaml
name: Matrix demo

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12", "3.13"]
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest
```

GitHub starts **three jobs in parallel**, one for each version. ✅✅✅

---

### ⚡ 2. Caching: Don't Re-Download Every Time

Installing libraries takes time on every run. Add **one line** and pip packages are cached between runs:

```yaml
      - uses: actions/setup-python@v7
        with:
          python-version: "3.12"
          cache: pip
```

Faster pipelines mean happier developers (and lower cost on big projects).

---

### ⏰ 3. Schedules and Manual Triggers

Pipelines don't only run on push:

**📁 `adv-schedule.yml`**

```yaml
name: Nightly check

on:
  schedule:
    - cron: "30 20 * * *"
  workflow_dispatch:

jobs:
  nightly:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running the nightly checks"
```

- `schedule` runs it automatically (this example: every day at 20:30 UTC).
- `workflow_dispatch` adds a **"Run workflow" button** in the Actions tab, for manual runs.

---

### ⚛️ 4. A Frontend (React) Pipeline

The same shape works for your React project, just with `npm` commands:

**📁 `adv-react.yml`**

```yaml
name: React CI

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: 22
      - run: npm ci
      - run: npm run lint
      - run: npm run build
```

- `npm ci` = clean, exact install from `package-lock.json` (preferred in CI).
- `npm run build` checks that your app **compiles**.

---

### 🗺️ 5. Words You Will Meet Next (Introduction Only)

| Concept | One-line meaning |
|---|---|
| 🌍 **Environments** | Separate stages like `dev`, `staging`, `production`, each with its own secrets and approvals |
| ✋ **Manual approval** | A human must approve before deploying to production (Continuous **Delivery**) |
| 📦 **Artifacts** | Files saved from a run (build output, test reports) |
| ↩️ **Rollback** | Quickly return to the previous working version |
| 🐤 **Canary / blue-green deploys** | Release to a few users (or a parallel copy) first, to reduce risk |
| ♻️ **Reusable workflows** | Share one pipeline across many repositories |

---

### 🧭 6. Where Does Your Learning Go Next?

```
   Git ──► GitHub ──► CI (tests) ──► CD (deploy)
                                       │
                          Docker ──► Cloud (AWS / Azure / Render) ──► Monitoring
```

You are already on this road. 🚶‍♀️

🤔 **Quick thinking question:** Why would a team test on Python 3.11, 3.12, **and** 3.13?

✅ **Answer:** Users and servers run different versions. A matrix **proves the code works on all of them** before release.

---

## 💡 Real-Life Analogy

🏥 **A hospital with many departments and safety rules.**

A small clinic (our simple pipeline) becomes a big hospital (a real pipeline): **several labs run tests in parallel** (matrix), **frequent supplies are stocked nearby** (cache), **night-shift staff run rounds automatically** (schedule), a **senior doctor must sign** before major surgery (manual approval), and there's a **plan to move a patient back** if treatment fails (rollback). The principles are the same, just more careful.

---

## 💻 Real-World Application

| Where | Advanced CI/CD |
|---|---|
| 📦 Python libraries | Matrix testing across many Python versions |
| 🛒 E-commerce | Canary releases to a small percentage of users first |
| 🏦 Banks and hospitals | Manual approvals and security scans |
| 🚀 Startups | Docker images built and deployed on each merge |
| 🌐 Big tech | Hundreds of pipelines, automated rollbacks, monitoring |

---

## 🔍 Industry Example

📘 **Scenario: Shipping a new version of a patient portal**

1. 👩‍💻 A developer merges a pull request.
2. 🤖 The pipeline runs tests on **three Python versions** (matrix) using **cached libraries**, finishing in two minutes instead of six.
3. 🐳 It builds a **Docker image** and stores it as an artifact.
4. 🔒 A **security scan** checks libraries for known vulnerabilities.
5. 🧪 The image is deployed to **staging**. Automated checks run there.
6. ✋ A lead approves the **production** environment.
7. 🐤 The release goes to 5% of users first (canary). Monitoring looks healthy, so it goes to everyone.
8. ↩️ Had errors appeared, an automatic **rollback** would restore the last good version.

---

## 📊 Diagram

```
   push ──► CI ───────────────────────────────────────────────┐
            ├─ test on 3.11 ┐                                 │
            ├─ test on 3.12 ├─ (matrix, in parallel, cached)  │
            └─ test on 3.13 ┘                                 │
                     │ ✅                                      │
                     ▼                                        │
              build Docker image ──► security scan            │
                     │                                        │
                     ▼                                        │
               deploy: STAGING ──► automatic checks           │
                     │                                        │
                 ✋ approval                                   │
                     ▼                                        │
              deploy: PRODUCTION (canary → everyone)          │
                     │                                        │
              problem? ──► ↩️ rollback ◄──────────────────────┘
```

---

## ⚠️ Common Mistakes

| ❌ Wrong Belief | ✅ Correct Understanding |
|---|---|
| "I must learn all these features today." | Today is an introduction. Master the basic pipeline first. |
| "Bigger pipelines are always better." | Keep them as simple as your project needs. |
| "Cache makes results unreliable." | Caches speed up installs, and tests still run every time. |
| "CI/CD is only for web apps." | Mobile apps, libraries, data pipelines, and infrastructure use it too. |
| "Docker is the same as CI/CD." | Docker packages apps. CI/CD automates testing and releasing them. |
| "Production = my laptop with the app running." | Production is the real, shared environment users access. |
| "Rollback means I failed." | Rollbacks are a **normal safety tool**. |

---

## 💬 Interview Corner

**Q1. What is a matrix build?**
A configuration that runs the same job multiple times with different values (for example, several Python versions) in parallel.

**Q2. What is the purpose of caching in a pipeline?**
To reuse downloaded dependencies between runs, making pipelines faster.

**Q3. What are environments such as staging and production?**
Separate deployment targets: staging mimics production for final testing, and production is what real users use.

**Q4. What is a rollback?**
Returning the system to a previous known-good version after a bad release.

---

## 📝 Quick Summary

- 🔁 **Matrix** = same job, many versions, in parallel.
- ⚡ **Cache** = faster installs.
- ⏰ **Schedule** and **workflow_dispatch** = timed and manual runs.
- ⚛️ React pipelines use `npm ci`, `npm run lint`, and `npm run build`.
- 🐳 Docker, Kubernetes, and SonarQube were introduced in the previous topic.
- 🌍 **Environments** and ✋ **approvals** give safe releases.
- ↩️ **Rollback**, 🐤 **canary**, and 🔒 **security scans** reduce risk.
- 🎯 These are **names to remember**, and we practice them later.

---

## 🎯 Class Activity

**🛠️ Activity: "Add one upgrade" (about 10 minutes)**

In your `hospital-ci` repository, choose **one**:

1. Add `cache: pip` to the `setup-python` step. Compare the "Install dependencies" step time before and after, on the second run.
2. Add the `matrix` with Python 3.11, 3.12, and 3.13 and see three jobs in the Actions tab.
3. Add `workflow_dispatch:` under `on:` and click **Run workflow** in the Actions tab.

Check your workflow stays valid. If it turns red because of a YAML mistake, compare indentation with the notes.

---

# 📋 Assignments — A First Look at Advanced CI/CD

| Assignment |
|---|
| Add a matrix for three Python versions to your `hospital-ci` workflow and take a screenshot of the three parallel jobs. |
| Add `cache: pip` and compare the install-step time between the first run and the second run. Write your observation. |
| Add `workflow_dispatch:` to your workflow and trigger it manually from the Actions tab. |
| Create a scheduled workflow that runs every day, and explain the meaning of the five fields in `cron: "30 20 * * *"`. |
| Write the GitHub Actions workflow you would use for your React project (`npm ci`, `npm run lint`, `npm run build`), and push it to a React repo. |
| Research Docker in 8 to 10 lines: what is an image, what is a container, and why do teams use it? |
| Draw your dream pipeline for a hospital app with at least these stages: test, security scan, staging, approval, production. |
| Research "rollback" and "blue-green deployment" and explain each in 4 lines with a real-life example. |
| Compare GitHub Actions and Jenkins in a table with 5 rows (hosting, setup, config file, popularity, cost). |
| List 5 job titles (DevOps Engineer, SRE, etc.) and write how they use CI/CD in their day-to-day work. |