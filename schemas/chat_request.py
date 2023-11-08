from pydantic import BaseModel

class ChatRequest(BaseModel):    
    message: str

class ChatCrawRequest(BaseModel):
    website: str