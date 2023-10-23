from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemes.index import User

user = APIRouter()


@user.get("/users")
async def select_users():
    return conn.execute(users.select()).fetchall()


@user.get("/users/{id}")
async def select_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post("/users")
async def insert_user(user: User):
    conn.execute(users.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    ))

    return conn.execute(users.select()).fetchall()


@user.put("/users/{id}")
async def update_user(id: int, user: User):
    conn.execute(users.update().values(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))

    return conn.execute(users.select()).fetchall()


@user.delete("/users/{id}")
async def delete_user(id: int, user: User):
    conn.execute(users.delete().where(users.c.id == id))

    return conn.execute(users.select()).fetchall()
