from fastapi import APIRouter, Depends, HTTPException
from config.db import conn
from models.user import users
from schemas.user import UserLogin
from sqlalchemy import select
from config.auth import AuthHandler

from cryptography.fernet import Fernet

auth = APIRouter()
auth_handler = AuthHandler()

@auth.post("/login", tags=["auth"], description="Login with an existing user")
async def login(userPayload: UserLogin):
    # get user by email
    user = conn.execute(users.select().where(users.c.email == userPayload.email)).first()

    if(user is None):
        raise HTTPException(401, "Invalid email or password")
    elif (not auth_handler.verify_password(userPayload.password, user.password)):
        raise HTTPException(401, "Invalid email or password")
    else:
        token = auth_handler.encode_token(user.id)
        return {"token": token}
    
@auth.get("/get_user", tags=["auth"], description="Get user by token")
async def get_user_by_token(id=Depends(auth_handler.auth_wrapper)):
    user_query = select([users.c.id, users.c.email, users.c.name]).where(users.c.id == id)
    user = conn.execute(user_query).first()
    return user
