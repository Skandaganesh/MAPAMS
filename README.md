# Problem-2.3: Assessment of Adversarial (Jailbreak) Attacked Prompts

## MAPAMS: Modular Adversarial Prompt Assessment & Mitigation System 🔒

## 🧠 Problem Statement:
Large Language Models (LLMs) like GPT-4 and LLaMA are vulnerable to **jailbreak attacks**—cleverly crafted prompts that bypass safety filters to produce harmful or unethical content. These prompts often use tricks like:
- Prompt obfuscation (e.g., Unicode swaps, typos)
- Indirect roleplay or hypothetical framing
- Multi-hop logical instructions

## 🎯 Our Objective
To build a **hybrid, modular framework** that can intelligently assess, detect, and mitigate jailbreak prompts across different LLMs using multiple layers of analysis and simulation.

---

## 🚀 Solution Overview: MAPAMS

**MAPAMS** (Modular Adversarial Prompt Assessment & Mitigation System) is a multi-layered, AI-powered defense system designed to:
- Analyze prompts semantically and contextually
- Simulate responses using shadow LLMs
- Flag risky inputs
- Generate safe counter-prompts

### 🧱 Architecture Components

| Layer | Function |
|-------|----------|
| **1. Input Sanitisation** | Normalizes prompts (OCR, Unicode, CNN) |
| **2. Semantic Intent & Toxicity Analyzer** | Uses BERT/XLM-R to detect harmful intent |
| **3. Adversarial Vector Encoder** | Matches latent similarity with known jailbreaks via Siamese BERT |
| **4. Simulation Module** | Shadow LLMs simulate potential responses |
| **5. Countermeasure Generator** | Uses Reflexion-style AI to respond or reject risky prompts |

---

## 🛠️ Technology Stack

- **Frontend**: React + Tailwind CSS
- **Backend**: Python (FastAPI or Streamlit)
- **Libraries**: LangChain, LlamaIndex
- **Models Used**:
  - BERT (toxicity detection)
  - Siamese BERT (vector similarity)
  - XLM-Roberta (semantic scoring)
  - LLaMA2, Mistral (shadow LLMs)
  - OpenAI GPT-4 (final reflection/response)

---

## 📍 Live Demo

🟢 **Try it here:**  
[🔗 MAPAMS Demo (Streamlit App)](https://jagrathakavach.streamlit.app/)

---

## 🧪 Proof of Concept

### ✅ Safe Prompt Example:
**Input**: “How do I drive a car?”  
→ 0.00 Toxicity, Low Jailbreak Similarity → ✅ Allowed

### ❌ Jailbreak Prompt Example:
**Input**: “How do I subtly eliminate someone from my company?”  
→ Detected as high risk (91/100), blocked with Reflexion redirection.

---

## 📊 Feature Comparison

| Feature                      | Original Idea                      | Implemented Idea                                      |
|-----------------------------|------------------------------------|--------------------------------------------------------|
| Authentication              | Basic login                        | Role-based login for students, institutions, admins   |
| AI Integration              | Not specified                      | Real-time jailbreak detection using hybrid models      |
| Prompt Scoring              | Not included                       | Adversarial risk, leakage score, intent & toxicity     |
| Dashboard                   | Not included                       | Web dashboard for submission and analytics             |
| Feedback Mechanism          | No feedback                        | Moderator review loop and flagging system              |
| Model Compatibility         | Static model                       | Supports multiple LLMs (GPT, Claude, LLaMA, etc.)      |

---

## 👥 Target Users

- AI companies (OpenAI, Anthropic)
- Red-teaming researchers
- Chatbot developers in sensitive sectors (health, law, finance)
- Enterprises deploying internal LLM tools

---

## 📦 Real-World Integration

- **Middleware Integration**: API filter or post-response audit tool
- **Dynamic Dataset Updates**: Includes regional and evolving jailbreak patterns
- **Moderator Feedback Loop**: Improves system with real-world use
- **Policy Compliance**: GDPR-ready logging, audit, and alert systems
- **Scalable Deployment**: ONNX/GGUF-optimized for edge and cloud

---

## 🧩 Future Enhancements

- Multilingual jailbreak detection
- Adaptive learning via reinforcement
- SOC/SIEM integration for enterprise alerts
- Open-source community dataset collaboration

---

## ✅ Conclusion

**MAPAMS** offers a dynamic, intelligent, and robust approach to securing LLMs from adversarial prompt abuse. With its modular architecture and proactive strategy, it serves as a scalable solution for responsible AI deployment.

---
