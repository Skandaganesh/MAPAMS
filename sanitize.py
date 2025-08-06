import re
import unicodedata

def sanitize_prompt(prompt: str) -> str:
   
    prompt = unicodedata.normalize('NFKC', prompt)
   
    prompt = re.sub(r"[^\x00-\x7F]+", " ", prompt)
    return prompt.lower()
