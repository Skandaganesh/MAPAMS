from transformers import pipeline

classifier = pipeline("text-classification", model="unitary/toxic-bert", truncation=True)

def is_toxic(prompt: str) -> float:
    result = classifier(prompt)[0]
    if result["label"].lower() == "toxic":
        return result["score"]
    return 0.0
