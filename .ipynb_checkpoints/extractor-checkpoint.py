import pdfplumber
from utils.skills import SKILLS_DB
def extract_text_from_pdf(pdf_file):
    text=""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            t=page.extract_text()
            if t:
                text+=t.lower()
    return text

def extract_skills(text):
    return list(set([s for s in SKILLS_DB if s in text]))