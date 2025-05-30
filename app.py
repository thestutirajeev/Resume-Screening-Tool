import streamlit as st
from resume_parser import extract_text, preprocess_text, match_skills
import json

# Load skills
with open("skills.json", "r") as f:
    skills_data = json.load(f)

st.title("📄 AI Resume Screening Tool")

job_role = st.selectbox("Select Job Role", list(skills_data.keys()))
uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)

results = []

if uploaded_files:
    required_skills = skills_data[job_role]
    total_skills = len(required_skills)

    for file in uploaded_files:
        text = extract_text(file)
        tokens = preprocess_text(text)
        matched, score = match_skills(tokens, required_skills)
        results.append({
            "filename": file.name,
            "matched": matched,
            "score": score,
            "total": total_skills,
            "file_data": file
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    st.subheader("📊 Resume Results")
    for res in results:
        match_ratio = res["score"] / res["total"]
        color = "green" if match_ratio >= 0.5 else "red"

        st.markdown(f"""
        <div style="border:1px solid {color}; padding:10px; border-radius:10px; margin-bottom:10px;">
            <strong>{res["filename"]}</strong><br>
            Matched Skills: {', '.join(res["matched"])}<br>
            <span style="color:{color}; font-weight:bold;">Score: {res["score"]}/{res["total"]}</span>
        </div>
        """, unsafe_allow_html=True)

        st.progress(match_ratio)

        st.download_button(
            label="Download Resume",
            data=res["file_data"],
            file_name=res["filename"]
        )
        st.markdown("---")
