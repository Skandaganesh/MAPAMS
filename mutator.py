from transformers import pipeline
import random

paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase-Paws")

def mutate_prompt(prompt: str) -> str:
    paraphrased = paraphraser(f"paraphrase: {prompt} ", max_length=60, num_return_sequences=3, do_sample=True)
    variants = [x['generated_text'] for x in paraphrased]
    return random.choice(variants)