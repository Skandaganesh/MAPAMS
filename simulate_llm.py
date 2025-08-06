
from openai import OpenAI
import os


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)

def simulate_llm(prompt: str) -> dict:
    results = {}
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        results["openrouter-gpt"] = response.choices[0].message.content
    except Exception as e:
        results["openrouter-gpt"] = f"Error: {str(e)}"
    return results
