from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from sqlalchemy import func, select
from models.car_type import car_types
from schemas.car_type import CarType, CarTypePayload

car_type = APIRouter()
auth_handler = AuthHandler()

# get all car_type
@car_type.get("/", response_model=List[CarType])
async def get_all_car_type(
    skip: int = 0,
    limit: int = 10,
):
    query = car_types.select().offset(skip).limit(limit)
    return conn.execute(query).fetchall()

# create new car_type
@car_type.post("/", response_model=CarType)
async def create_car_type(car_type: CarType, auth=Depends(auth_handler.auth_wrapper_super_admin)):
    # nếu tồn tại id thì trả về lỗi 
    check = conn.execute(car_types.select().where(car_types.c.id == car_type.id)).fetchall()
    if check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Type with id '{}' already existe".format(car_type.id))
    # nếu không tồn tại id thì thêm mới
    conn.execute(car_types.insert().values(
        id=car_type.id,
        name=car_type.name,
        country=car_type.country,
        description=car_type.description
    ))
    # return car_type has been created
    return conn.execute(car_types.select().where(car_types.c.id == car_type.id)).first()

# update car_type
@car_type.put("/{id}", response_model=CarType)
async def update_car_type(id: str, car_type: CarTypePayload, auth=Depends(auth_handler.auth_wrapper_super_admin)):
    conn.execute(car_types.update().values(
        name=car_type.name,
        country=car_type.country,
        description=car_type.description
    ).where(car_types.c.id == id))
    data = conn.execute(car_types.select().where(car_types.c.id == id)).first()
    if not data:
        raise HTTPException(HTTP_404_NOT_FOUND, "Car Type with id '{}' not found".format(id))
    return data

# delete car_type
@car_type.delete("/{id}")
async def delete_car_type(id: str, auth=Depends(auth_handler.auth_wrapper_super_admin)):
    conn.execute(car_types.delete().where(car_types.c.id == id))
    return {
        "message": "Car Type with id '{}' has been deleted.".format(id),
        "id": id
    }