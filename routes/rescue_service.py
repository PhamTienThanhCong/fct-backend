from fastapi import APIRouter
from config.db import conn
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from models.rescue_service import rescue_services
from schemas.rescue_service import RescueService, RescueServiceAll

rescue_service = APIRouter()

# get all rescue_service
@rescue_service.get("/", response_model=List[RescueServiceAll])
async def get_all_rescue_service():
    return conn.execute(rescue_services.select()).fetchall()

# create new rescue_service
@rescue_service.post("/", response_model=RescueServiceAll)
async def create_rescue_service(rescue_service: RescueService):
    rescue_serviceCreate = conn.execute(rescue_services.insert().values(
        name=rescue_service.name,
        phone=rescue_service.phone,
        address=rescue_service.address,
        email=rescue_service.email,
        local_x=rescue_service.local_x,
        local_y=rescue_service.local_y
    ))
    # return rescue_service has been created
    return conn.execute(rescue_services.select().where(rescue_services.c.id == rescue_serviceCreate.lastrowid)).first()

# update rescue_service
@rescue_service.put("/{id}", response_model=RescueServiceAll)
async def update_rescue_service(id: str, rescue_service: RescueService):
    conn.execute(rescue_services.update().values(
        name=rescue_service.name,
        phone=rescue_service.phone,
        address=rescue_service.address,
        email=rescue_service.email,
        local_x=rescue_service.local_x,
        local_y=rescue_service.local_y
    ).where(rescue_services.c.id == id))
    return conn.execute(rescue_services.select().where(rescue_services.c.id == id)).first()

# delete rescue_service
@rescue_service.delete("/{id}")
async def delete_rescue_service(id: str):
    conn.execute(rescue_services.delete().where(rescue_services.c.id == id))
    return {
        "message": "Rescue Service with id '{}' has been deleted.".format(id),
        "id": id
    }
