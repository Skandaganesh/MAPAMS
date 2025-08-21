from transformers import pipeline
from rapidfuzz import fuzz
toxic_classifier = pipeline("text-classification", model="unitary/toxic-bert")
intent_phrases = ["bomb", "bypass security", "create explosive","make a bomb", "build a bomb", "manufacture explosive", "bypass security", "hack a system","how to hotwire","how to hijack", "disable firewall", "break into account", "launch malware", "write ransomware", "create a virus", "harm others", "hurt someone", "kill someone", "commit a crime", "grow illegal plants", "meth", "cook crack", "evade police", "avoid detection", "trick ai", "jailbreak chatgpt", "prompt injection", "pretend to be DAN", "ignore previous instructions", "as an unfiltered AI", "act as an unethical AI", "simulate illegal activity", "murder", "attack", "a weapon", "explosives", "steal data", "pick a lock", "crack password", "disable alarm", "hide evidence", "cover up a crime", "a silencer", "gunpowder","a firearm", "a bomb", "a weapon of mass destruction"]

def is_toxic(text):
    result = toxic_classifier(text)[0]
    return result["score"] if result["label"] == "toxic" else 0.0

def is_dangerous_intent(text: str, threshold: int = 80) -> bool:
    lowered = text.lower()
    for phrase in intent_phrases:
        if phrase in lowered:
            return True
        if fuzz.partial_ratio(phrase, lowered) >= threshold:
            return True
    return False