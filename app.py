import streamlit as st
from PyPDF2 import PdfReader
from utils import match_resume, get_feedback

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# ---------------- TITLE ----------------
st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume and compare it with a job description")

st.markdown("---")

# ---------------- INPUTS ----------------
resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_text = st.text_area("📝 Paste Job Description")

# ---------------- BUTTON ----------------
analyze = st.button("🚀 Analyze Resume")

# ---------------- MAIN LOGIC ----------------
if analyze:

    if resume_file is None:
        st.warning("Please upload a resume")
    elif job_text.strip() == "":
        st.warning("Please enter job description")
    else:

        # Extract PDF text (SAFE VERSION)
        pdf = PdfReader(resume_file)
        resume_text = ""

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

        # AI MATCH
        score = match_resume(resume_text, job_text)
        feedback = get_feedback(score)

        # RESULTS
        st.markdown("## 📊 Result")
        st.metric("Match Score", f"{score}%")
        st.progress(int(score))

        if score >= 75:
            st.success("HIGH MATCH ✔")
        elif score >= 50:
            st.warning("MODERATE MATCH ⚠")
        else:
            st.error("LOW MATCH ❌")

        st.markdown("## 💡 Feedback")
        st.info(feedback)