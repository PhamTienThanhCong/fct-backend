from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from constants.main import CHARING_PORT_STATUS, CHARING_STATUS_TEXT, ChargingPortStatus
from models.charging_port import charging_ports
from models.station import stations
from schemas.charging_port import ChargingPortPayload, ChargingPortResponse, ChargingPortUpload

charging_port = APIRouter()
auth_handler = AuthHandler()

def format_respond(data):
    return {
        "id": data["id"],
        "station_id": data["station_id"],
        "port_code": data["port_code"],
        "price": str(data["price"]) + " USD",
        "power": str(data["power"]) + " kW",
        "status": CHARING_STATUS_TEXT[data["status"]],
    }

async def check_station_owner(id: int, owner_id: int):
    query = charging_ports.select().where(charging_ports.c.id == id)
    charging_port = conn.execute(query).first()
    if not charging_port:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Charging port with given id not found")
    
    # check station is owner
    query = stations.select().where(stations.c.id == charging_port.station_id )
    station = conn.execute(query).first()
    if station.owner_id != owner_id:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="You are not owner of this station")
    
    return charging_port

@charging_port.get("/s/{station_id}", response_model=List[ChargingPortResponse])
async def get_all_charging_port_by_stations(station_id: int):
    query = charging_ports.select().where(charging_ports.c.station_id == station_id)
    data_responses = conn.execute(query).fetchall()
    return list(map(format_respond, data_responses))

@charging_port.get("/{id}", response_model=ChargingPortResponse)
async def get_charging_port(id: int):
    query = charging_ports.select().where(charging_ports.c.id == id)
    charging_port = conn.execute(query).first()
    if not charging_port:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Charging port not found")

    return format_respond(charging_port)


@charging_port.post("/", response_model=ChargingPortResponse)
async def create_charging_port(payload: ChargingPortPayload, auth=Depends(auth_handler.auth_wrapper_admin)):
    # check station_id exist
    owner_id = auth["id"]
    query = stations.select().where(stations.c.id == payload.station_id )
    station = conn.execute(query).fetchall()
    if not station:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Station with given id not found")
    if station[0].owner_id != owner_id:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="You are not owner of this station")

    # check port_code == port_code and station_id == station_id exist
    query = charging_ports.select().where(charging_ports.c.station_id == payload.station_id)
    charging_port = conn.execute(query).fetchall()
    if charging_port:
        for port in charging_port:
            if port.port_code == payload.port_code:
                raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Port code already exist")

    query = charging_ports.insert().values(**payload.dict())
    last_record_id = conn.execute(query).lastrowid
    data_response = conn.execute(charging_ports.select().where(charging_ports.c.id == last_record_id)).first()
    
    return format_respond(data_response)

@charging_port.put("/{id}", response_model=ChargingPortResponse)
async def update_charging_port(id: int, payload: ChargingPortUpload, auth=Depends(auth_handler.auth_wrapper_admin)):
    # check station_id exist
    owner_id = auth["id"]
    
    charging_port = await check_station_owner(id, owner_id)
    
    if charging_port.port_code != payload.port_code:
        # check port_code == port_code and station_id == station_id exist
        query = charging_ports.select().where(charging_ports.c.station_id == charging_port.station_id)
        charging_port = conn.execute(query).fetchall()
        if charging_port:
            for port in charging_port:
                if port.port_code == payload.port_code:
                    raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Port code already exist")

    query = charging_ports.update().where(charging_ports.c.id == id).values(**payload.dict())
    conn.execute(query)
    data_response = conn.execute(charging_ports.select().where(charging_ports.c.id == id)).first()
    return format_respond(data_response)

@charging_port.put("/{id}/{status}")
async def update_status_charging_port(id: int, status: ChargingPortStatus = ChargingPortStatus.free, 
        auth=Depends(auth_handler.auth_wrapper_admin)):
    # check station_id exist
    owner_id = auth["id"]
    
    charging_port = await check_station_owner(id, owner_id)
    
    if charging_port:
        query = charging_ports.update().where(charging_ports.c.id == id).values(status=CHARING_PORT_STATUS[status])
        conn.execute(query)
        data_response = conn.execute(charging_ports.select().where(charging_ports.c.id == id)).first()
        return format_respond(data_response)

@charging_port.delete("/{id}")
async def delete_charging_port(id: int, auth=Depends(auth_handler.auth_wrapper_admin)):
    # check station_id exist
    owner_id = auth["id"]

    await check_station_owner(id, owner_id)
    
    query = charging_ports.delete().where(charging_ports.c.id == id)
    conn.execute(query)
    return {"message": "Charging port with id: {} deleted successfully!".format(id)}