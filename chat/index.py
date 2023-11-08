from fastapi import APIRouter
from chat.process import training, craw_app, chatbot

from schemas.chat_request import ChatRequest, ChatCrawRequest

# sleep
import time

chatRoute = APIRouter()

@chatRoute.get("/")
async def read_dataset():
    data = craw_app.read_json()
    return data or {"message": "fail"}

@chatRoute.post("/", response_model=ChatRequest)
async def chat(request: ChatRequest):
    message = request.message
    response = chatbot.chatResponse(message) or "I don't understand"
    return {"message": response}

@chatRoute.post("/training", response_model=ChatRequest)
async def train_your_dataset():
    if training.training():
        return {"message": "Training success please restart server"}
    else:
        return {"message": "Fail training, please check your data"}, 

@chatRoute.post("/craw", response_model=ChatRequest)
async def craw_data_from_api(request: ChatCrawRequest):
    name_craw = request.website
    if craw_app.crawl_website(name_craw):
        return {"message": "craw data success"}
    else:
        return {"message": "craw data fail"}