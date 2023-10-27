from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from models.user import users
from models.station import stations
from schemas.station import StationPayload, StationResponse 

station = APIRouter()
auth_handler = AuthHandler()

@station.get("/", response_model=List[StationResponse])
async def get_add_station():
    return conn.execute(stations.select()).fetchall()

@station.get("/{id}", response_model=StationResponse)
async def get_station_by_id(id: int):
    return conn.execute(stations.select().where(stations.c.id == id)).first()

@station.post("/", response_model=StationResponse)
async def create_station(station: StationPayload, auth=Depends(auth_handler.auth_wrapper_admin)):
    owner_id = auth['id']
    query = conn.execute(stations.insert().values(**station.dict(), owner_id=owner_id))
    last_record_id = query.lastrowid
    return conn.execute(stations.select().where(stations.c.id == last_record_id)).first()

@station.put("/{id}", response_model=StationResponse)
async def update_station(id: int, station: StationPayload, auth=Depends(auth_handler.auth_wrapper_admin)):
    owner_id = auth.id
    query = stations.update().where(stations.c.id == id).values(**station.dict(), owner_id=owner_id)
    conn.execute(query)
    return conn.execute(stations.select().where(stations.c.id == id)).first()

@station.delete("/{id}")
async def delete_station(id: int, auth=Depends(auth_handler.auth_wrapper_admin)):
    owner_id = auth.id
    query = stations.delete().where(stations.c.id == id)
    conn.execute(query)
    return {"message": "Station with id: {} deleted successfully!".format(id)}