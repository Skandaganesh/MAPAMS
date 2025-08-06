from sentence_transformers import SentenceTransformer, util
import json
import torch

model = SentenceTransformer("all-MiniLM-L6-v2")
with open("jailbreak_bank.json") as f:
    bank = json.load(f)
    vectors = model.encode([item["prompt"] for item in bank], convert_to_tensor=True)

def vector_score(input_text):
    input_vec = model.encode(input_text, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(input_vec, vectors)[0]
    return float(torch.max(cosine_scores))