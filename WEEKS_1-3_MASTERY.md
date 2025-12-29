# 🚀 Zero-to-Engineer: Weeks 1-3 Mastery Log

## 1. Project Infrastructure (The Setup)
**Stop dragging folders. Build environments.**

| Goal | Command / Action |
| :--- | :--- |
| **New Project** | `mkdir -p ~/Projects/name && cd ~/Projects/name` |
| **Create Venv** | `uv venv` (Creates isolated .venv) |
| **Activate Venv** | `source .venv/bin/activate` |
| **Link VS Code** | `Cmd+Shift+P` -> "Python: Select Interpreter" -> Select `.venv` |
| **Git Ignore** | `echo ".venv/" > .gitignore` (Prevent uploading libraries) |

---

## 2. Advanced Debugging (VS Code)
**Stop printing. Start inspecting.**

* **Launch Config (`.vscode/launch.json`):**
    * Store arguments: `"args": ["input_value"]`
    * Stop tracing library code: `"justMyCode": true`
* **The Toolkit:**
    * **F5:** Start Debugging.
    * **F10 (Step Over):** Move to next line.
    * **F11 (Step Into):** Dive inside a function.
    * **Watch Window:** Track specific variables/math (e.g., `price * qty`).
    * **Debug Console:** Execute Python code live in paused app.
    * **Conditional Breakpoint:** Right-click Red Dot -> "Stop only if `i == 500`".

---

## 3. Professional Git Workflow
**Never commit to main. Sync often.**

1.  **Start (Branch):**
    `git checkout -b fix/feature-name`
2.  **Save (Commit):**
    `git add .`
    `git commit -m "Fix: Description of change"`
3.  **Upload (Push):**
    `git push -u origin fix/feature-name`
4.  **Review (Pull Request):**
    `gh pr create --title "Fix logic" --body "Details..."`
5.  **Merge (Ship It):**
    `gh pr merge --merge --delete-branch`
6.  **Sync Local (Crucial):**
    `git checkout main`
    `git pull origin main`
    `git branch -d fix/feature-name` (Cleanup)

---

## 4. Disaster Recovery (The Safety Nets)
**Panic buttons for when things break.**

| Scenario | Solution |
| :--- | :--- |
| **Need to switch context but work is messy?** | `git stash` (Hide work) -> `git stash pop` (Restore work) |
| **Typo in commit message?** | `git commit --amend` |
| **Committed garbage? (Soft Undo)** | `git reset --soft HEAD~1` (Un-commits, keeps code) |
| **Merge Conflict?** | Open VS Code -> Click "Accept Incoming" or "Current" |

---

## 5. Key Shortcuts
* **Cmd+Shift+P:** Command Palette (God Mode).
* **Ctrl+~:** Toggle Terminal.
* **Cmd+B:** Toggle Sidebar.
