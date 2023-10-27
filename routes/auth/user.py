from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from sqlalchemy import func, select
from models.user import users
from models.role import roles
from schemas.user import UserLogin, UserPayload, UserAll
from cryptography.fernet import Fernet

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)
auth_handler = AuthHandler()

async def checkUser(user):
        # nếu tồn tại phone hoặc email thì trả về lỗi
    check = conn.execute(users.select().where(users.c.phone == user.phone)).fetchall()
    if check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "User with phone '{}' already existe".format(user.phone))
    check = conn.execute(users.select().where(users.c.email == user.email)).fetchall()
    if check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "User with email '{}' already existe".format(user.email))

    # kiểm tra role_id có tồn tại không
    check = conn.execute(roles.select().where(roles.c.id == user.role_id)).fetchall()
    if not check:
        raise HTTPException(HTTP_404_NOT_FOUND, "Role with id '{}' not found".format(user.role_id))

@user.post("/login", tags=["Admin Auth"], description="Login with an existing user")
async def login(userPayload: UserLogin):
    # get user by email
    user = conn.execute(users.select().where(users.c.email == userPayload.email)).first()

    if(user is None):
        raise HTTPException(401, "Invalid email or password")
    elif (not auth_handler.verify_password(userPayload.password, user.password)):
        raise HTTPException(401, "Invalid email or password")
    else:
        token = auth_handler.encode_token({"id": user.id, "role_id": user.role_id})
        return {"token": token}
    
@user.get("/get_user", tags=["Admin Auth"], description="Get user by token", response_model=UserAll)
async def get_user_by_token(auth=Depends(auth_handler.auth_wrapper_admin)):
    # get user by id
    return conn.execute(users.select().where(users.c.id == auth['id'])).first()


@user.get('/', response_model=List[UserAll])
async def get_all_users():
    return conn.execute(users.select()).fetchall()

# get user by id
@user.get('/{id}', response_model=UserAll)
async def get_user_by_id(id: int):
    data = conn.execute(users.select().where(users.c.id == id)).first()
    if not data:
        raise HTTPException(HTTP_404_NOT_FOUND, "User with id '{}' not found".format(id))
    return data

# create new user
@user.post('/', response_model=UserAll)
async def create_user(user: UserPayload, auth=Depends(auth_handler.auth_wrapper_super_admin)):

    await checkUser(user)

    hash_password = auth_handler.get_password_hash(user.password)
    new_user = conn.execute(users.insert().values(
        role_id = user.role_id,
        email = user.email,
        full_name = user.full_name,
        phone = user.phone,
        address = user.address,
        card_id = user.card_id,
        title = user.title,
        password = hash_password,
        description = user.description
    ))
    resData = conn.execute(users.select().where(users.c.id == new_user.lastrowid)).first()
    return resData

# update user
@user.put('/{id}', response_model=UserAll)
async def update_user(id: int, user: UserPayload, auth=Depends(auth_handler.auth_wrapper_admin)):
    # kiểm tra user có tồn tại không
    check = conn.execute(users.select().where(users.c.id == id)).first()
    if not check:
        raise HTTPException(HTTP_404_NOT_FOUND, "User with id '{}' not found".format(id))

    # kiểm tra role_id có tồn tại không
    check = conn.execute(roles.select().where(roles.c.id == user.role_id)).fetchall()
    if not check:
        raise HTTPException(HTTP_404_NOT_FOUND, "Role with id '{}' not found".format(user.role_id))

    hash_password = auth_handler.get_password_hash(user.password)
    conn.execute(users.update().where(users.c.id == id).values(
        role_id = user.role_id,
        email = user.email,
        full_name = user.full_name,
        phone = user.phone,
        address = user.address,
        card_id = user.card_id,
        title = user.title,
        password = hash_password,
        description = user.description
    ))
    resData = conn.execute(users.select().where(users.c.id == id)).first()
    return resData

# delete user
@user.delete('/{id}')
async def delete_user(id: int, auth=Depends(auth_handler.auth_wrapper_super_admin)):
    # kiểm tra user có tồn tại không
    check = conn.execute(users.select().where(users.c.id == id)).first()
    if not check:
        raise HTTPException(HTTP_404_NOT_FOUND, "User with id '{}' not found".format(id))

    conn.execute(users.delete().where(users.c.id == id))
    return {
        'status': True,
        'message': 'Delete user successfully'
    }
    