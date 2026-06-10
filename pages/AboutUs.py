# import streamlit as st
# st.markdown("<u><h2>C V Analysis using <span style='color:red'>AI and Machine Learning</span></h2></u>",unsafe_allow_html=True)
# st.markdown("<h3><u>About Us</u></h3>",unsafe_allow_html=True)
# st.logo("cv.png",size="large")
# st.markdown("An AI CV analysis project automates resume screening by extracting candidate data, matching qualifications against job descriptions, and scoring candidates. Using Large Language Models (LLMs) and Optical Character Recognition (OCR), it highlights missing skills, formats JSON output, and ranks top talent to streamline the hiring process")
# st.subheader("Key Project Features")
# st.markdown("Document Parsing: Extracts raw text and structure from uploaded CV PDFs using OCR or libraries like PyPDF2.Semantic Keyword Matching: Uses text embeddings and cosine similarity (e.g., via OpenAI or HuggingFace) to score how closely a CV aligns with specific job requirements.AI-Driven Gap Analysis: Feeds the CV and job description into an LLM (like Google Gemini or GPT-4) to generate a customized match score, summarize strengths, and pinpoint missing skills.Structured Analytics: Outputs data into clean dashboards or spreadsheets (like Google Sheets) for HR teams to easily evaluate candidates")
# st.subheader("Python packages")
# st.code("import os")
# st.code("from fastapi import FastAPI, UploadFile, File, Form, HTTPException")
# st.code("from pydantic import BaseModel, Field")

# ---------------------------------------------------------------------------------

import streamlit as st



with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<div class="hero-box">
    <h1>🚀 About AI Resume Analyzer</h1>
    <h3>Smart Hiring Powered By Artificial Intelligence</h3>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class="feature-card">
    <h2>📌 Who We Are</h2>

    AI Resume Analyzer is an intelligent recruitment assistant
    that helps organizations and recruiters evaluate resumes
    efficiently using Artificial Intelligence and Machine Learning.

    
    The system automatically compares candidate resumes with
    job descriptions and provides accurate suitability scores.
    

</div>
""",unsafe_allow_html=True)

st.markdown("## ✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📄 Resume Parsing</h3>
        <p>Extract important information from resumes automatically.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Skill Matching</h3>
        <p>Compare candidate skills with job requirements.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>📊 AI Scoring</h3>
        <p>Generate suitability scores instantly.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("## 🛠 Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("🤖 Machine Learning")

with col3:
    st.info("📄 PyPDF")

with col4:
    st.info("🎨 Streamlit")


st.markdown("## 📈 Project Highlights")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Resume Parsing", "100%")

with c2:
    st.metric("AI Matching", "Smart")

with c3:
    st.metric("Analysis Speed", "< 5 Sec")

st.markdown("---")

st.markdown("""
<center>

Made by Tabish Anwar using Python, Streamlit and Machine Learning

</center>
""", unsafe_allow_html=True)