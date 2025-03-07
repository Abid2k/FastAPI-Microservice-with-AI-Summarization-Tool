# app/models.py
from transformers import pipeline
from app.config import MODEL_NAME

# Load model on startup
summarizer = pipeline("summarization", model=MODEL_NAME)

def summarize_text(text: str, max_length: int = 150, min_length: int = 50):
    """Summarize the input text using the preloaded model."""
    return summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
