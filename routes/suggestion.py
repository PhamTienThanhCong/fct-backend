from fastapi import APIRouter
from config.db import conn
from models.index import suggestions
from schemes.index import Suggestion

suggestion = APIRouter()


@suggestion.get("/suggestions")
async def select_suggestions():
    return conn.execute(suggestions.select()).fetchall()


@suggestion.get("/suggestions/{id}")
async def select_suggestions(id: int):
    return conn.execute(suggestions.select().where(suggestions.c.id == id)).fetchall()


@suggestion.get("/suggestions/location/{id}")
async def select_suggestions(id: int):
    return conn.execute(suggestions.select().where(suggestions.c.location_id == id)).fetchall()
