from transformers import pipeline

# Load AI summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
