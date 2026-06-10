import streamlit as st
import time

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------



st.markdown("""
<div class="hero-box">
    <h1>🤖 AI Resume Analyzer</h1>
    <h3>Smart Resume Screening Using Machine Learning</h3>
</div>
""", unsafe_allow_html=True)



st.image(
    "abc.png",
    use_container_width=True
)
# ------------------------------------------------------------------------


# st.logo("cv.png",size="large")
# st.subheader("Key Project Features")

# ------------------------------------------------------------------------

st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📄 Resume Parsing</h3>
        <p>Extract candidate details automatically.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Skill Matching</h3>
        <p>Compare resume with job description.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 AI Analysis</h3>
        <p>Generate suitability score instantly.</p>
    </div>
    """, unsafe_allow_html=True)
# ------------------------------------------------------------------------


# st.success("Document Parsing: ")
# st.write("Extracts raw text and structure from uploaded CV PDFs using OCR or libraries like PyPDF2.Semantic Keyword Matching: Uses text embeddings and cosine similarity (e.g., via OpenAI or HuggingFace) to score how closely a CV aligns with specific job requirements.AI-Driven Gap Analysis: Feeds the CV and job description into an LLM (like Google Gemini or GPT-4) to generate a customized match score, summarize strengths, and pinpoint missing skills.Structured Analytics: Outputs data into clean dashboards or spreadsheets (like Google Sheets) for HR teams to easily evaluate candidates")


# ------------------------------------------------------------------------
st.markdown("""
### 🚀 About Us

AI Resume Analyzer automates the hiring process by
analyzing resumes, matching skills with job requirements,
and generating smart suitability scores using Machine Learning.

""")
# ------------------------------------------------------------------------