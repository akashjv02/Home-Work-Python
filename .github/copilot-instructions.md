## Purpose

This file contains concise, actionable guidance for AI coding agents working on this repository (a small set of standalone Python exercise scripts). Follow these notes to be immediately productive.

## Repo at-a-glance

- Root scripts: `Day1hwork.py`, `Day2hwork.py`, `Day3hwork.py`.
- These are simple, standalone exercise scripts (no package, no tests, no requirements file).
- Typical flow: compute values in top-level variables and print results to stdout. There are no classes or modules to import within the repo.

## What to expect when editing

- Keep changes minimal and local to a file unless you intentionally extract reusable functions.
- The scripts are executed directly (top-level code). If you add functions, also add a short guarded runner (if __name__ == "__main__") so the script remains runnable.
- Variable naming is inconsistent (e.g., `Rice`, `Sugar`, `Oil` in `Day1hwork.py` vs. `snake_case` elsewhere). Preserve existing casing for small edits to limit diffs; if you refactor names, do it across the file to remain consistent.

## Key files & discoverable patterns (examples)

- `Day1hwork.py` — procedural calculations, then printing. Uses `import random` and `random.randrange(5,10)` to compute a delivery charge. When modifying, keep the import at top and preserve the printed labels (e.g., "Total rice = ") if downstream checks rely on exact text.

- `Day2hwork.py` — works with a multiline string `para` and demonstrates slicing, `replace`, `split`, `strip`, and `format`. Prefer simple string operations that mirror existing style (no third-party libs).

- `Day3hwork.py` — boolean logic examples and arithmetic operations. Uses direct assignment and prints intermediate results.

## How to run (Windows PowerShell)

Run each script from the repository root using your Python 3 interpreter. Example:

```powershell
python .\Day1hwork.py
python .\Day2hwork.py
python .\Day3hwork.py
```

If your repository path contains spaces, quoting is optional when running from the repo root but keep the working directory set to the repo root.

## Developer workflow notes

- There is no build system, virtualenv, or test runner in this repo. Avoid adding external dependencies unless explicitly requested.
- For quick validation of changes, run the modified script and assert that expected printed lines are present. Example expected text from `Day1hwork.py`: `Total bill = ` and `Delivery charge = `.

## Conventions for automated edits

- Avoid large refactors across multiple files in a single patch unless asked. This repo is educational; users expect small, targeted changes.
- When adding features, keep public behavior (printed lines and their basic labels) stable unless the user requests output format changes.
- If introducing functions or tests, add them under the repo root and keep names descriptive (e.g., `compute_total()` in `Day1hwork.py`). Add a small `if __name__ == "__main__"` block to preserve direct execution.

## When to ask the user

- Ask before adding external dependencies or converting the repo to a package layout.
- Ask before renaming variables or changing printed output formats.

## Files to reference when proposing changes

- `Day1hwork.py`, `Day2hwork.py`, `Day3hwork.py` — these show the project's current coding style and output expectations.

---
If any part of this guidance is unclear or you'd like the agent to follow a different convention (for example, refactor to PEP8, add unit tests, or package the code), tell me how you'd like to proceed.
