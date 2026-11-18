# QLF Sentinel

## Day 1 Rules

1. Run `pytest -v` locally on clone. It must show **6 passed, 1 failed**.
2. The failed test is `test_hallucination_mode_returns_wrong_mic()`. This is intentional. Your first task is to implement `MOCK_HALLUCINATION` in `src/sentinel/core/llm.py`.
3. Run `python3 -m sentinel.cli scribe --mock`. It must succeed.
4. You do not have an API key. Use the Mock LLM.
5. To use a real API key, create `.env` with `OPENAI_API_KEY=...` and set `MOCK_LLM=False`. Never commit `.env`.
