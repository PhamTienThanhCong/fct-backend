from fastapi import APIRouter
from config.db import conn
from models.index import locations
from schemes.index import Location

location = APIRouter()


@location.get("/locations")
async def select_locations():
    return conn.execute(locations.select()).fetchall()


@location.get("/locations/{id}")
async def select_locations(id: int):
    return conn.execute(locations.select().where(locations.c.id == id)).fetchall()
