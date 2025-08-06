from simulate_llm import simulate_llm

def generate_counter_response(prompt: str) -> str:
    prompt_input = f"You are an AI safety layer. A user asked: '{prompt}'. Explain why it may be unsafe and how to ask it safely."
    answers = simulate_llm(prompt_input)
    return answers.get("gpt-4") or list(answers.values())[0]