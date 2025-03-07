
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Summarization Microservice")

app.include_router(router)

# Run with: uvicorn app.main:app --reload
