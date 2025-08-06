import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

MODELS = ["gpt-4", "gpt-3.5-turbo"]

def simulate_llm(prompt: str) -> dict:
    results = {}
    for model in MODELS:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            results[model] = response['choices'][0]['message']['content']
        except Exception as e:
            results[model] = f"Error: {str(e)}"
    return results