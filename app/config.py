# app/config.py
import os

MODEL_NAME = os.getenv("MODEL_NAME", "facebook/bart-large-cnn")  # Default summarization model
MAX_INPUT_LENGTH = 1024  # Max input characters
MAX_SUMMARY_LENGTH = 150  # Max summary length
