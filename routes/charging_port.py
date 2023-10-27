from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from models.charging_port import charging_ports
from models.station import stations
from schemas.charging_port import ChargingPortPayload, ChargingPortResponse, ChargingPortUpload

charging_port = APIRouter()
auth_handler = AuthHandler()

@charging_port.get("/stations/{station_id}", response_model=List[ChargingPortResponse])
async def get_all_charging_port(station_id: int):
    query = charging_ports.select().where(charging_ports.c.station_id == station_id)
    return conn.execute(query).fetchall()

@charging_port.get("/{id}", response_model=ChargingPortResponse)
async def get_charging_port(id: int, auth=Depends(auth_handler.auth_wrapper_admin)):
    query = charging_ports.select().where(charging_ports.c.id == id)
    charging_port = conn.execute(query).first()
    if not charging_port:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Charging port not found")
    return charging_port

@charging_port.post("/", response_model=ChargingPortResponse)
async def create_charging_port(payload: ChargingPortPayload):
    # check station_id exist
    query = stations.select().where(stations.c.id == payload.station_id)
    station = conn.execute(query).fetchall()
    if not station:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Station with given id not found")
    
    # check port_code == port_code and station_id == station_id exist
    query = charging_ports.select().where(charging_ports.c.station_id == payload.station_id)
    charging_port = conn.execute(query).fetchall()
    if charging_port:
        for port in charging_port:
            if port.port_code == payload.port_code:
                raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Port code already exist")

    query = charging_ports.insert().values(**payload.dict())
    last_record_id = conn.execute(query).lastrowid
    return conn.execute(charging_ports.select().where(charging_ports.c.id == last_record_id)).first()

@charging_port.put("/{id}", response_model=ChargingPortResponse)
async def update_charging_port(id: int, payload: ChargingPortUpload):
    query = charging_ports.update().where(charging_ports.c.id == id).values(**payload.dict())
    conn.execute(query)
    return conn.execute(charging_ports.select().where(charging_ports.c.id == id)).first()

@charging_port.delete("/{id}")
async def delete_charging_port(id: int):
    query = charging_ports.delete().where(charging_ports.c.id == id)
    conn.execute(query)
    return {"message": "Charging port with id: {} deleted successfully!".format(id)}