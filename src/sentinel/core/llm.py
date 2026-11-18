import os

class LLMError(Exception):
    pass

def generate(prompt: str) -> str:
    """
    Mock LLM client. 
    MOCK_LLM=True returns a valid JSON string.
    MOCK_HALLUCINATION=True is intentionally unimplemented in the seed.
    """
    if os.environ.get("MOCK_HALLUCINATION") == "True":
        raise NotImplementedError(
            "Implement the hallucination mock: return a wrong MIC for a Tokyo holiday."
        )
    
    # Default mock behavior (Valid extraction)
    # Simulates finding a holiday for the Tokyo Stock Exchange (XTKS)
    return '{"mic": "XTKS", "date": "2026-11-15", "event_type": "holiday"}'
