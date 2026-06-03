from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def match_resume(resume_text, job_text):
    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    if resume_text == "" or job_text == "":
        return 0

    tfidf = TfidfVectorizer(stop_words="english")
    matrix = tfidf.fit_transform([resume_text, job_text])

    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(score * 100, 2)

def get_feedback(score):
    if score >= 80:
        return "🔥 Excellent match"
    elif score >= 60:
        return "⚡ Good match"
    elif score >= 40:
        return "📊 Moderate match"
    else:
        return "📉 Low match"