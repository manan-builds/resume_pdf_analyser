import gradio as gr
from extractor import extract_text_from_pdf, extract_skills
from classifier import predict_role
from database import save_to_db

def analyze_resume(name, file):
    text = extract_text_from_pdf(file.name)
    skills = extract_skills(text)
    role, score = predict_role(text)

    save_to_db(name, skills, role, score)

    return f"Skills: {skills}\nRole: {role}\nScore: {score}%"

ui = gr.Interface(
    fn=analyze_resume,
    inputs=[
        gr.Textbox(label="Candidate Name"),
        gr.File(label="Upload Resume PDF")
    ],
    outputs="text",
    title="Resume Analyzer"
)

ui.launch()
