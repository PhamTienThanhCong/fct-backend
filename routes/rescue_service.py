from fastapi import APIRouter, Depends
from config.auth import AuthHandler
from config.db import conn
from typing import List
from models.rescue_service import rescue_services
from schemas.rescue_service import RescueService, RescueServiceAll

rescue_service = APIRouter()
auth_handler = AuthHandler()

# get all rescue_service
@rescue_service.get("/", response_model=List[RescueServiceAll])
async def get_all_rescue_service():
    return conn.execute(rescue_services.select()).fetchall()

# create new rescue_service
@rescue_service.post("/", response_model=RescueServiceAll)
async def create_rescue_service(rescue_service: RescueService, auth=Depends(auth_handler.auth_wrapper_super_admin)):
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
async def update_rescue_service(id: str, rescue_service: RescueService, auth=Depends(auth_handler.auth_wrapper_super_admin)):
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
async def delete_rescue_service(id: str, auth=Depends(auth_handler.auth_wrapper_super_admin)):
    conn.execute(rescue_services.delete().where(rescue_services.c.id == id))
    return {
        "message": "Rescue Service with id '{}' has been deleted.".format(id),
        "id": id
    }
