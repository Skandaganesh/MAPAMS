import re
import unicodedata

def sanitize_prompt(prompt: str) -> str:
    # Normalize Unicode
    prompt = unicodedata.normalize('NFKC', prompt)
    # Remove unwanted characters
    prompt = re.sub(r"[^\x00-\x7F]+", " ", prompt)
    return prompt.lower()
