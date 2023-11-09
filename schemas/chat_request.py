from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):    
    message: str

class ChatCrawRequest(BaseModel):
    website: str

class ChatModelUpdate(BaseModel):
    patterns: list
    responses: list
    
class ChatModel(BaseModel):
    tag: str
    patterns: list
    responses: list

class ChatModelResponseList(BaseModel):
    intents: List[ChatModel]
