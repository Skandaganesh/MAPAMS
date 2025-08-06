# app.py
import streamlit as st
from sanitize import sanitize_prompt
from classifier import is_toxic, is_dangerous_intent
from vector_match import vector_score
from counterprompt import reflexion_score
from simulate_llm import simulate_llm
from prompt_graph import check_contradictory_intent
import json

st.title("🛡️ MAPAMS: Multi-Agent Prompt Attack Mitigation System")

user_prompt = st.text_area("Enter a prompt:")
if st.button("Analyze"):
    with st.spinner("Sanitizing and Analyzing..."):
        cleaned = sanitize_prompt(user_prompt)
        toxicity = is_toxic(cleaned)
        similarity = vector_score(cleaned)
        llm_response = simulate_llm(cleaned)
        reflexion = reflexion_score(cleaned, llm_response)
        dangerous_intent = is_dangerous_intent(cleaned)
        contradictory_flag = check_contradictory_intent(cleaned)

        # Compute final risk
        score = 0
        score += 0.8 * toxicity
        score += 0.6 * similarity
        score += 0.6 * reflexion
        score += 0.7 if dangerous_intent else 0
        score += 0.7 if contradictory_flag else 0

        risk_level = (
            "🔴 High(Jail break Prompt)" if score >= 0.75 else
            "🟡 Medium risk" if score >= 0.4 else
            "🟢 Safe"
        )

        st.subheader("Analysis Results")
        st.markdown(f"🧪 **Sanitized Prompt:** {cleaned}")
        st.markdown(f"☣️ **Toxicity Score:** {toxicity:.2f}")
        st.markdown(f"🔍 **Similarity with known jailbreaks:** {similarity:.2f}")
        if score<0.4:
            st.markdown(f"🧠 Shadow LLM Response:\n\n{list(llm_response.values())[0]}")
        else:
            st.markdown(f"🧠 Shadow LLM Response: Null (Jailbreak detected)")
        st.markdown(f"🛡️ **Counterprompt / Reflexion Score:** {reflexion:.2f}")
        st.markdown(f"❗ **Dangerous Intent Detected:** {'Yes' if dangerous_intent else 'No'}")
        st.markdown(f"🔐 **Contradictory Intent via Graph:** {'Yes' if contradictory_flag else 'No'}")
        st.success(f"✅ **Final Risk Level:** {risk_level}")
