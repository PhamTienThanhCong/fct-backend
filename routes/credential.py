from fastapi import APIRouter, Depends, HTTPException
from config.db import conn
from config.auth import AuthHandler
from schemes.index import User
from models.index import users

credential = APIRouter()
auth_handler = AuthHandler()


@credential.post("/register", status_code=201)
async def register(user: User):
    all_users = conn.execute(users.select()).fetchall()
    if any(x['email'] == user.email for x in all_users):
        raise HTTPException(400, 'Email is taken')

    hashed_password = auth_handler.get_password_hash(user.password)

    conn.execute(users.insert().values(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=hashed_password,
        avatar=user.avatar,
        location_id=user.location_id,
        gender=user.gender,
        dob=user.dob
    ))

    return conn.execute(users.select().where(users.c.email == user.email)).fetchall()


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
