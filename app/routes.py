# app/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import summarize_text

router = APIRouter()

# Define request models
class QueryRequest(BaseModel):
    query: str

class SummarizationRequest(BaseModel):
    text: str

@router.post("/query")
async def process_query(request: QueryRequest):
    """Handles basic query processing."""
    return {"message": f"Received query: {request.query}"}

@router.post("/summarize")
async def summarize_text_api(request: SummarizationRequest):
    """Summarizes input text using AI model."""
    if len(request.text) < 50:
        raise HTTPException(status_code=400, detail="Text too short for summarization.")
    
    summary = summarize_text(request.text)
    return {"summary": summary}
