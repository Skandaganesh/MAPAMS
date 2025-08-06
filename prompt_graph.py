from graphviz import Digraph

def visualize_prompt_flow(prompt: str, mutations: list):
    dot = Digraph()
    dot.node("Original", prompt[:40] + ("..." if len(prompt) > 40 else ""))
    for i, mut in enumerate(mutations):
        dot.node(f"M{i}", mut[:40] + ("..." if len(mut) > 40 else ""))
        dot.edge("Original", f"M{i}")
    dot.render("prompt_graph", format="png", cleanup=True)