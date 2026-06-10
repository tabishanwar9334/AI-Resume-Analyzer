# import streamlit as st
# from pypdf import PdfReader
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import os
# st.title("C.V A n a l y z e r")
# st.success("User CV")
# save_dir = "./uploaded_files"
# f1=st.file_uploader("Upload User CV")

# reader =PdfReader(f1)
# cv = "".join(page.extract_text() for page in reader.pages)
# st.write(cv)

# st.success("Job Description")
# f2=st.file_uploader("Upload Job Description")

# reader1 = PdfReader(f2)
# jd = "".join(page.extract_text() for page in reader1.pages)
# st.write(jd)

# x=CountVectorizer()
# matrix=x.fit_transform([jd,cv])

# similarity_matrix=cosine_similarity(matrix)
# st.write(similarity_matrix)

# st.write(str(similarity_matrix[1][0]*100)+'%')

# ------------------------------------------------------------------------

import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
# -------------------------------------------------------------------

# Page Title
# st.title("📄 CV Analyzer")
# -------------------------------------------------------------------

# Login Protection
if "username" not in st.session_state:
    st.error("🔒 Please Sign In First")
    st.stop()


st.markdown("""
<div class="hero-box">
    <h1>📄 AI Resume Matcher</h1>
    <h3>Upload Resume & Job Description</h3>
</div>
""", unsafe_allow_html=True)
# --------------------------------------------------------------

# Upload CV
# st.header("Upload User CV")
# f1 = st.file_uploader("Upload User CV (PDF)", type=["pdf"])

# # Upload Job Description
# st.header("Upload Job Description")
# f2 = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# --------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    f1 = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:
    f2 = st.file_uploader(
        "💼 Upload Job Description",
        type=["pdf"]
    )
# -----------------------------------------------------------------------------

# Process only when both files are uploaded
if f1 is not None and f2 is not None:

    with st.spinner("🔍 Analyzing Resume..."):
    
        # Read CV
        reader = PdfReader(f1)
        cv = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                cv += text

        # Read Job Description
        reader1 = PdfReader(f2)
        jd = ""

        for page in reader1.pages:
            text = page.extract_text()
            if text:
                jd += text

        # Display extracted text
        st.subheader("Extracted CV Text")
        st.write(cv)

        st.subheader("Extracted Job Description Text")
        st.write(jd)

        # Similarity Calculation
        vectorizer = CountVectorizer()

        matrix = vectorizer.fit_transform([jd, cv])

        similarity_matrix = cosine_similarity(matrix)

        score = similarity_matrix[0][1] * 100

        # Result
        st.subheader("Match Score")

        if score >= 80:
            st.success(f"Excellent Match: {score:.2f}%")
        elif score >= 60:
            st.warning(f"Good Match: {score:.2f}%")
        else:
            st.error(f"Low Match: {score:.2f}%")

        st.write("Similarity Matrix:")
        st.write(similarity_matrix)

else:
    st.info("Please upload both PDF files to analyze.")



