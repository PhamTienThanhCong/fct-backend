from fastapi import APIRouter
from chat.process import training
from chat.process import craw_app
from chat.process import chatbot

from schemas.chat_request import ChatRequest

# sleep
import time

chatRoute = APIRouter()

@chatRoute.get("/")
def index():
    return {"message": "Hello World"}

@chatRoute.post("/chat")
async def chat(request: ChatRequest):
    message = request.message
    response = chatbot.chatResponse(message) or "I don't understand"
    return JSONResponse(content={"chat": response})

# @chatRoute.get("/training")
# async def train():
#     if training.training():
#         return {"train": "success"}
#     else:
#         return {"train": "fail"}

# @chatRoute.get("/craw")
# async def craw():
#     name_craw = "https://nhat-desu-server.onrender.com/v1/chat"
#     if craw_app.crawl_website(name_craw):
#         return {"craw": "success"}
#     else:
#         return {"craw": "fail"}

# @chatRoute.get("/read")
# async def read():
#     data = craw_app.read_json()
#     return data or {"read": "fail"}