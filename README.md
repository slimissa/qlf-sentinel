# QLF Sentinel: The AI Watchtower

Welcome to QLF Sentinel! This project is about building an AI system that watches financial data, but is strictly controlled by Python guardrails. The AI is not allowed to make decisions; it only extracts data, and our Python code decides if that data is safe to use.

## The Day 1 Contract

We have intentionally left one test failing in this repository. This is your "red line." Your first task is to turn it green.

When you finish this task, you will understand:
1. How to set up a Python project.
2. How the mock AI works.
3. Why the validator (the Python fence) is the most important part of the system.

## Step-by-Step Setup (Do this exactly)

**1. Clone the repository and enter the folder:**
```bash
git clone https://github.com/slimissa/qlf-sentinel.git
cd qlf-sentinel
```

**2. Create a Virtual Environment:**
A virtual environment (venv) keeps this project's dependencies separate from your computer's system Python.
```bash
python3 -m venv .venv
source .venv/bin/activate
```
*(You will know it worked if you see `(.venv)` at the start of your terminal prompt.)*

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```
*(You should see `qlf-sentinel` and `pytest` in the list of installed packages.)*

**4. Run the Tests:**
```bash
pytest tests/ -v
```
**You will see 1 failed, 6 passed.**
The failed test is `test_hallucination_mode_returns_wrong_mic`. This is intentional. Do not fix the test. Fix the mock.

**5. Test the CLI:**
```bash
qlf-sentinel scribe --mock
```
*(You should see "Running Scribe in Mock Mode..." and a mock GitHub comment.)*

## Your First Task (Issue #2)

1. Open `src/sentinel/core/llm.py`.
2. Find the `if os.environ.get("MOCK_HALLUCINATION") == "True":` block.
3. Replace the `NotImplementedError` with a hardcoded JSON string that simulates a hallucination (a valid London MIC for a Tokyo holiday).
   *Example: `return '{"mic": "XLON", "date": "2026-11-15"}'`*
4. Run `pytest tests/ -v` again. It should now say **7 passed**.
5. Create a branch, commit your fix, push it, and open a Pull Request. The GitHub Actions CI will turn green.

## Troubleshooting for Beginners

**I got `command not found: pytest`**
You forgot to activate the virtual environment. Run `source .venv/bin/activate` and try again.

**I got `ModuleNotFoundError: No module named 'sentinel'`**
You skipped Step 3 (`pip install -r requirements.txt`). The package must be installed for the CLI to work.

**I deleted my `.venv` folder and now nothing works**
Terminal environments get stuck. Close your terminal window completely, open a new one, and start from Step 2.

**The CI is red on my Pull Request**
Click "Details" next to the red X on GitHub. Read the error. It will tell you exactly which test failed and why.

## The 5 Rules
1. **Never commit an API key.** The CI has a secret scanner that will catch you.
2. **Run tests locally before pushing.** Do not make the Quality Manager review broken code.
3. **The AI proposes, Python validates.** If the LLM outputs bad data, the validator must catch it.
4. **The mock is your friend.** You do not need a real API key to pass the tests.
5. **Ask questions.** If you are stuck for more than 15 minutes, open a GitHub Issue.
