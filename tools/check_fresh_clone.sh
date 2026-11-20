#!/usr/bin/env bash
set -euo pipefail

# tools/check_fresh_clone.sh
# The gate: a fresh clone must reproduce the Day 1 state exactly.
# Exits 0 if the expected state is reproduced, 1 otherwise.

REPO_URL="${REPO_URL:-https://github.com/slimissa/qlf-sentinel.git}"
TIMESTAMP=$(date +%s)
WORKDIR="/tmp/check-${TIMESTAMP}"

echo "==> Cloning into ${WORKDIR}"
git clone --quiet "${REPO_URL}" "${WORKDIR}"
cd "${WORKDIR}"

echo "==> Creating fresh venv"
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
which python3

echo "==> Installing dependencies"
pip install --quiet -r requirements.txt

echo "==> Verifying package is installed"
if ! pip show qlf-sentinel > /dev/null 2>&1; then
  echo "FAIL: qlf-sentinel package not installed"
  exit 1
fi

echo "==> Running pytest"
PYTEST_OUTPUT=$(pytest tests/ -v 2>&1 || true)
echo "${PYTEST_OUTPUT}"

echo "==> Asserting the Day 1 state"
if ! echo "${PYTEST_OUTPUT}" | grep -q "1 failed, 6 passed"; then
  echo "FAIL: expected 1 failed, 6 passed"
  exit 1
fi

if ! echo "${PYTEST_OUTPUT}" | grep -q "test_hallucination_mode_returns_wrong_mic"; then
  echo "FAIL: expected the red line to be test_hallucination_mode_returns_wrong_mic"
  exit 1
fi

if ! echo "${PYTEST_OUTPUT}" | grep -q "NotImplementedError: Implement the hallucination mock"; then
  echo "FAIL: expected NotImplementedError on the hallucination mock"
  exit 1
fi

echo "==> Running CLI"
if ! qlf-sentinel --help > /dev/null 2>&1; then
  echo "FAIL: qlf-sentinel --help failed"
  exit 1
fi

echo "==> Running scribe --mock"
if ! qlf-sentinel scribe --mock | grep -q "Running Scribe in Mock Mode"; then
  echo "FAIL: scribe --mock did not print expected output"
  exit 1
fi

echo ""
echo "=================================================="
echo "PASS: Fresh clone reproduces the Day 1 state."
echo "  - 1 failed, 6 passed"
echo "  - Red line: test_hallucination_mode_returns_wrong_mic"
echo "  - Failure: NotImplementedError (the assignment)"
echo "  - CLI: qlf-sentinel --help and scribe --mock both work"
echo "=================================================="
exit 0
