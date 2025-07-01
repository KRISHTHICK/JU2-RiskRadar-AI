# JU2-RiskRadar-AI
Gen Ai

🛡️📈 RiskRadar AI – Intelligent Risk Profiling & Investment Assistant
🧠 Project Idea:
RiskRadar AI is an AI-powered tool designed to assess a user's risk profile, recommend investment products, and answer questions from uploaded PDFs like risk policy disclosures or fund documents using RAG (Retrieval-Augmented Generation). The app is tailored for BFSI companies offering personalized wealth management and investment advisory.

🔑 Key Features:
Feature	Description
🧠 AI Risk Assessment Agent	Chat with an agent that evaluates your responses to determine your risk type
📄 RAG over Investment Docs (PDF)	Upload PDFs (e.g., fund T&Cs) and ask specific questions
📊 Dynamic Risk-Based Investment Map	Recommend investment types (e.g., bonds, equities, SIPs) based on profile
🧾 Investment Glossary	Lookup complex finance/investment terms
🔄 Profile-based Rebalancing Tip	Suggests when and how to rebalance portfolio

git clone https://github.com/yourusername/RiskRadar-AI.git
cd RiskRadar-AI

pip install -r requirements.txt
ollama pull tinyllama

streamlit run app.py
