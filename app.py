import streamlit as st
from agent_logic import get_risk_agent_response
from rag_module import query_uploaded_docs
from risk_model import assess_risk_profile, recommend_investments
import json

st.set_page_config(page_title="RiskRadar AI", layout="wide")
st.title("🛡️📈 RiskRadar AI – Smart Investment & Risk Assistant")

st.header("📊 Risk Assessment")
name = st.text_input("Name:")
age = st.slider("Age", 18, 70, 30)
income = st.number_input("Monthly Income (INR)", min_value=1000)
investment_goal = st.selectbox("What’s your primary investment goal?", ["Wealth Growth", "Retirement", "Education", "Short-term Savings"])
risk_answers = st.radio("How do you feel about high-risk investments?", ["Avoid them", "Sometimes okay", "Love the thrill"])

if st.button("🧠 Evaluate Risk Profile"):
    profile = assess_risk_profile(age, income, risk_answers)
    st.success(f"Risk Profile: {profile}")
    st.markdown("### 📌 Suggested Investment Mix:")
    st.markdown(recommend_investments(profile))

st.divider()
st.header("📄 Ask Questions from Investment PDFs (RAG)")
pdfs = st.file_uploader("Upload PDF documents", type="pdf", accept_multiple_files=True)
query = st.text_input("What would you like to ask?")
if query and pdfs:
    st.markdown(query_uploaded_docs(query, pdfs))

st.divider()
st.header("🧠 Ask Finance Agent")
prompt = st.text_input("Ask anything (e.g., What's a mutual fund?)")
if prompt:
    st.markdown(get_risk_agent_response(prompt))

st.divider()
st.header("📘 Glossary Lookup")
term = st.text_input("Lookup term (e.g., NAV, SIP, Risk Appetite)")
if term:
    glossary = json.load(open("glossary.json"))
    st.info(glossary.get(term.lower(), "Term not found."))
