from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("jailbreak_bank.json", "r") as f:
    jailbreak_prompts = json.load(f)
    jailbreak_embeddings = model.encode(jailbreak_prompts, convert_to_tensor=True)

def vector_similarity_score(user_prompt: str) -> float:
    user_embedding = model.encode(user_prompt, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, jailbreak_embeddings)
    return float(cosine_scores.max())
