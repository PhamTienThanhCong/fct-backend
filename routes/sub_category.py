from fastapi import APIRouter
from typing import Optional
from config.db import conn
from models.index import sub_categories
from schemes.index import SubCategory

sub_category = APIRouter()


@sub_category.get("/sub_categories")
async def select_sub_categories():
    return conn.execute(sub_categories.select()).fetchall()


@sub_category.get("/sub_categories/{id}")
async def select_sub_categories(id: int):
    return conn.execute(sub_categories.select().where(sub_categories.c.id == id)).fetchall()


@sub_category.get("/sub_categories/category/{id}")
async def select_sub_categories(id: int):
    return conn.execute(sub_categories.select().where(sub_categories.c.category_id == id)).fetchall()
