import json
import re
from datetime import datetime

class ValidationError(Exception):
    pass

class MICValidationError(ValidationError):
    pass

class DateValidationError(ValidationError):
    pass

class CoverageValidationError(ValidationError):
    pass

class PromptInjectionError(ValidationError):
    pass

# A mock of the actual ISO 10383 registry for testing
VALID_MICS = {"XTKS", "XLON", "XNYS", "XNAS"}
VALID_COUNTRIES = {"JP", "UK", "US"}

def validate_mic(mic: str) -> str:
    if mic in VALID_COUNTRIES:
        raise MICValidationError(
            f"Expected a MIC (e.g., XTKS), got a country code ({mic}). Re-extract with the MIC."
        )
    if mic not in VALID_MICS:
        raise MICValidationError(f"Unknown MIC: {mic}")
    return mic

def validate_date(date_str: str) -> bool:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise DateValidationError(f"Invalid date format: {date_str}")
    
    if d.year < datetime.now().year:
        raise DateValidationError(f"Date {date_str} is in the past.")
    return True

def validate_coverage(mic: str, date_str: str) -> str:
    # Mock logic: XTKS is inside coverage, XLON is outside
    if mic == "XLON":
        return "outside"
    return "inside"

def validate_llm_output(raw_json: str) -> dict:
    # 1. Prompt Injection Check
    if "ignore previous instructions" in raw_json.lower():
        raise PromptInjectionError("Prompt injection attempt detected.")
    
    # 2. Parse JSON
    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError:
        raise ValidationError("LLM did not return valid JSON.")
    
    # 3. Validate MIC
    mic = data.get("mic")
    if not mic:
        raise MICValidationError("Missing MIC in LLM output.")
    validate_mic(mic)
    
    # 4. Validate Date
    date_str = data.get("date")
    if not date_str:
        raise DateValidationError("Missing date in LLM output.")
    validate_date(date_str)
    
    # 5. Validate Coverage
    coverage = validate_coverage(mic, date_str)
    data["coverage_status"] = coverage
    
    return data
