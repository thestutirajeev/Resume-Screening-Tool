import fitz  # PyMuPDF
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

# 📝 Extract text from PDF or DOCX
def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""
        
# 🔍 Preprocess: tokenize, remove stopwords, lemmatize
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

# 🎯 Match required skills
def match_skills(tokens, required_skills):
    tokens_set = set(tokens)
    matched = [skill for skill in required_skills if skill.lower() in tokens_set]
    return matched, len(matched)
