from transformers import pipeline
from rapidfuzz import fuzz
toxic_classifier = pipeline("text-classification", model="unitary/toxic-bert")
intent_phrases = ["bomb", "bypass security", " explosive"," a bomb", "make a bomb", "build a bomb", "manufacture explosive", "bypass security", "hack a system", "disable firewall", "break into account", "launch malware", "write ransomware", "create a virus", "harm others", "hurt someone", "kill someone", "commit a crime", "grow illegal plants", "make meth", "cook crack", "evade police", "avoid detection", "trick ai", "jailbreak chatgpt", "prompt injection", "pretend to be DAN", "ignore previous instructions", "as an unfiltered AI", "act as an unethical AI", "simulate illegal activity", "murder", "attack", "make a weapon", "make explosives", "steal data", "pick a lock", "crack password", "disable alarm", "hide evidence", "cover up a crime", "make a silencer", "make gunpowder"]

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