from fastapi import APIRouter
from config.db import conn
from models.index import categories
from schemes.index import Category

category = APIRouter()


@category.get("/categories")
async def select_categories():
    return conn.execute(categories.select()).fetchall()


@category.get("/categories/{id}")
async def select_categories(id: int):
    return conn.execute(categories.select().where(categories.c.id == id)).fetchall()
