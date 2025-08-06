# from openai import OpenAI
# import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# MODELS = ["gpt-3.5-turbo"]

# def simulate_llm(prompt: str) -> dict:
#     results = {}
#     for model in MODELS:
#         try:
#             response = client.chat.completions.create(
#                 model=model,
#                 messages=[{"role": "user", "content": prompt}],
#                 max_tokens=100,
#                 temperature=0.7
#             )
#             results[model] = response.choices[0].message.content
#         except Exception as e:
#             results[model] = f"Error: {str(e)}"
#     return results
from openai import OpenAI
import os

# Use OpenRouter base URL and your key
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Set your OpenRouter key here
)

def simulate_llm(prompt: str) -> dict:
    results = {}
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # or "openai/gpt-4"
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        results["openrouter-gpt"] = response.choices[0].message.content
    except Exception as e:
        results["openrouter-gpt"] = f"Error: {str(e)}"
    return results
