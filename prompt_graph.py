import networkx as nx
import re

def check_contradictory_intent(text):
    keywords = ["prepare", "build", "make", "manufacture", "construct", "bomb", "explosive", "weapon", "gun", "silencer", "detonator", "school", "student", "teacher", "classroom", "university", "educational", "safe", "training", "demo", "harmless", "experiment", "physics", "activity"]
    tokens = re.findall(r"\w+", text.lower())
    G = nx.Graph()
    for i, token1 in enumerate(tokens):
        for j in range(i + 1, len(tokens)):
            token2 = tokens[j]
            if token1 in keywords and token2 in keywords:
                G.add_edge(token1, token2)
    contradictions = [ ("educational", "bomb"), ("school", "explosive"), ("student", "weapon"), ("teacher", "silencer"), ("university", "gun"), ("classroom", "detonator"), ("safe", "explosive"), ("physics", "weapon"), ("activity", "bomb"), ("demo", "gun") ]
    return any(G.has_edge(a, b) for a, b in contradictions)
