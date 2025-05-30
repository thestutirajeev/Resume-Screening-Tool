# 📄 Resume Screening Tool

A powerful and user-friendly Streamlit app that automatically screens multiple resumes based on required skills.
## Live: https://resume-screening-tool-k0df.onrender.com
---

## 🚀 Features

* ✅ **Supports PDF & DOCX files**
* 📂 **Upload multiple resumes at once**
* 📊 **Scores each resume based on matched skills**
* 📈 **Displays results sorted by score (highest first)**
* 🎨 **Color-coded results:**

  * 🟩 Green if score ≥ 50%
  * 🟥 Red if score < 50%
* 📤 **Download Resume** button for each file
* ⏳ **Animated progress bar while processing**

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – for the interactive UI
* **spaCy** – for natural language processing (tokenization, stopword removal, lemmatization)
* **PyMuPDF (fitz)** – for extracting text from PDFs
* **python-docx** – for extracting text from DOCX files

---
## 🧠 How It Works

1. **Upload Resumes**: Upload one or more `.pdf` or `.docx` files.
2. **Skill Matching**: The app extracts and preprocesses text using spaCy, then matches it with a predefined list of required skills.
3. **Scoring**: Resumes are scored based on how many required skills they include.
4. **Results**: Color-coded resume blocks show matched skills, scores, and allow for downloading the resume.

---
