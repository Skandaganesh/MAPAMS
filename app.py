import streamlit as st
from sanitize import sanitize_prompt
from classifier import is_toxic
from vector_match import vector_similarity_score
from simulate_llm import simulate_llm
from counterprompt import generate_counter_response

st.title("MAPAMS – Jailbreak Prompt Detection")

user_input = st.text_area("Enter your prompt:")

if st.button("Analyze"):
    with st.spinner("Sanitizing..."):
        clean_prompt = sanitize_prompt(user_input)

    with st.spinner("Checking toxicity..."):
        toxicity_score = is_toxic(clean_prompt)

    with st.spinner("Matching with known jailbreaks..."):
        sim_score = vector_similarity_score(clean_prompt)

    with st.spinner("Simulating Shadow LLM..."):
        shadow_response = simulate_llm(clean_prompt)

    with st.spinner("Generating countermeasure..."):
        reflexion = generate_counter_response(clean_prompt)

    st.subheader("Analysis Results")
    st.write(f"🧪 Sanitized Prompt: {clean_prompt}")
    st.write(f"☣️ Toxicity Score: {toxicity_score:.2f}")
    st.write(f"🔍 Similarity with known jailbreaks: {sim_score:.2f}")
    st.write(f"🧠 Shadow LLM Response:\n\n{shadow_response}")
    st.write(f"🛡️ Counterprompt / Reflexion:\n\n{reflexion}")

    if toxicity_score > 0.7 or sim_score > 0.8:
        st.error("⚠️ High risk of jailbreak prompt. Action: Block & Escalate.")
    else:
        st.success("✅ Prompt appears safe.")
