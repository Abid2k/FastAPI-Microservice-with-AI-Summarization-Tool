from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str

class SummarizeRequest(BaseModel):
    text: str
