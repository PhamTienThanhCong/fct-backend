from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from models.chat import chats
from schemas.chat_request import ChatModel, ChatModelUpdate, ChatModelResponseList

chat = APIRouter()
auth_handler = AuthHandler()

@chat.get("/", response_model=ChatModelResponseList)
async def get_chat_intents():
    data = conn.execute(chats.select()).fetchall()
    return {"intents": data}

@chat.get("/{tag}", response_model=ChatModel)
async def get_chat_by_tag(tag: str):
    return conn.execute(chats.select().where(chats.c.tag == tag)).first()

@chat.post("/", status_code=201, response_model=ChatModel)
async def create_chat(chat: ChatModel, auth=Depends(auth_handler.auth_wrapper_admin)):
    # kiểm tra nếu đã có tag thì không cho tạo
    check = conn.execute(chats.select().where(chats.c.tag == chat.tag)).first()
    if check:
        raise HTTPException(status_code=400, detail="Tag already exists")

    conn.execute(chats.insert().values(
        tag=chat.tag,
        patterns=chat.patterns,
        responses=chat.responses
    ))
    return conn.execute(chats.select().where(chats.c.tag == chat.tag)).first()

@chat.put("/{tag}", status_code=201, response_model=ChatModel)
async def update_chat(tag: str, chat: ChatModelUpdate, auth=Depends(auth_handler.auth_wrapper_admin)):
    # kiểm tra nếu chưa có tag thì không cho update
    check = conn.execute(chats.select().where(chats.c.tag == tag)).first()
    if not check:
        raise HTTPException(status_code=400, detail="Tag not exists")
    conn.execute(chats.update().where(chats.c.tag == tag).values(
        patterns=chat.patterns,
        responses=chat.responses
    ))
    return conn.execute(chats.select().where(chats.c.tag == tag)).first()

@chat.delete("/{tag}", status_code=HTTP_204_NO_CONTENT)
async def delete_chat(tag: str, auth=Depends(auth_handler.auth_wrapper_admin)):
    conn.execute(chats.delete().where(chats.c.tag == tag))
    return None