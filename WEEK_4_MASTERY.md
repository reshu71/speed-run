# 🤖 Week 4: Automation & Testing Mastery

## 1. The Core Concept
**Stop checking manually. Build a robot.**
* **Manual:** You run the code -> You look at the output -> You hope you didn't miss anything.
* **Automated:** You write code (Test) that checks your code (App).
* **CI (Continuous Integration):** A server (GitHub) runs your tests automatically on every push.

---

## 2. Local Testing (Pytest)
**The tool that checks your logic.**

| Action | Command / Rule |
| :--- | :--- |
| **Install** | `uv pip install pytest` |
| **Run Tests** | `pytest` |
| **File Name Rule** | Must start with `test_` (e.g., `test_app.py`). |
| **Function Name Rule** | Must start with `test_` (e.g., `def test_logic():`). |
| **The Keyword** | `assert` (e.g., `assert result == 100`). |

**Template (`test_app.py`):**
```python
import pytest
from app import my_function

def test_happy_path():
    # Arrange, Act, Assert
    assert my_function(10) == 100
```

---

## 3. The Bridge (Requirements)
**Telling the robot what to install.**

* **The Problem:** GitHub's computer is empty. It doesn't have pytest.
* **The Fix:** Create a shopping list of your libraries.
* **Command:** `uv pip freeze > requirements.txt`

---

## 4. The Robot (GitHub Actions)
**The automation script.**

* **Location:** `.github/workflows/ci.yml` (Must be exact).
* **The Logic:** "When I push code, wake up a Linux machine, install Python, read my requirements, and run pytest."

**The "Cheat Code" Configuration:**
```yaml
name: CI Robot
on: [push]  # Trigger

jobs:
  test:
    runs-on: ubuntu-latest  # The Machine
    steps:
      - uses: actions/checkout@v4       # 1. Download code
      - uses: actions/setup-python@v5   # 2. Get Python
        with:
          python-version: '3.12'
      - name: Install Libs              # 3. Read Shopping List
        run: pip install -r requirements.txt
      - name: Run Pytest                # 4. The Test
        run: pytest
```

---

## 5. The Workflow Summary
1.  **Write Code:** Update `app.py`.
2.  **Write Test:** Update `test_app.py`.
3.  **Local Check:** Run `pytest`. (If Red, fix it).
4.  **Freeze:** `uv pip freeze > requirements.txt` (If you added new libs).
5.  **Push:** `git push`.
6.  **Verify:** Check for the **Green Checkmark** on GitHub Actions tab.
