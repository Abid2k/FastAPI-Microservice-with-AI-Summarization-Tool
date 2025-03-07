from fastapi import APIRouter, HTTPException
from app.summarizer import generate_summary
from pydantic import BaseModel

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class SummarizeRequest(BaseModel):
    text: str

@router.post("/query")
async def process_query(request: QueryRequest):
    return {"message": f"Received query: {request.query}"}

@router.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    if len(request.text) < 50:
        raise HTTPException(status_code=400, detail="Input text too short to summarize.")
    summary = generate_summary(request.text)
    return {"summary": summary}
