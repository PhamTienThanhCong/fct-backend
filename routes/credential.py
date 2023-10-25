from fastapi import APIRouter, Depends, HTTPException
from config.db import conn
from config.auth import AuthHandler
from schemes.index import User
from typing import List
from models.index import users

credential = APIRouter()
auth_handler = AuthHandler()


@credential.get("/", response_model=List[User])
async def read_users():
    return conn.execute(users.select()).fetchall()
@credential.post("/register", status_code=201, response_model=User)
async def register(user: User):
    data = conn.execute(users.select().where(users.c.email == user.email)).fetchall()
    if len(data) != 0:
        print(data)
        raise HTTPException(400, "Email already exist")

    hashed_password = auth_handler.get_password_hash(user.password)

    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = hashed_password
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@credential.post("/login")
async def login(email: str, password: str):
    all_users = conn.execute(users.select()).fetchall()

    user = None

    for x in all_users:
        if x.email == email:
            user = x

            break

    if(user is None):
        raise HTTPException(401, "Not user")
    elif (not auth_handler.verify_password(password, user.password)):
        raise HTTPException(401, "Invalid email or password")
    else:
        token = auth_handler.encode_token(user.email)

        return {"token": token}


@credential.get("/protected")
async def protected(email=Depends(auth_handler.auth_wrapper)):
    # return conn.execute(users.select().where(users.c.email == email)).fetchall()
    return {"email": email}
