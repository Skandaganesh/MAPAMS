import networkx as nx
import re

def check_contradictory_intent(text):
    keywords = ["prepare", "bomb", "educational", "weapon", "school"]
    tokens = re.findall(r"\w+", text.lower())
    G = nx.Graph()
    for i, token1 in enumerate(tokens):
        for j in range(i + 1, len(tokens)):
            token2 = tokens[j]
            if token1 in keywords and token2 in keywords:
                G.add_edge(token1, token2)
    contradictions = [
        ("educational", "bomb"),
        ("school", "explosive"),
        ("student", "weapon")
    ]
    return any(G.has_edge(a, b) for a, b in contradictions)
