from fastapi import APIRouter, HTTPException
from config.db import conn
from typing import List, Optional
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from models.car_type import car_types
from schemas.car_type import CarType, CarTypePayload

car_type = APIRouter()

# get all car_type
@car_type.get("/", response_model=List[CarType])
async def get_all_car_type():
    return conn.execute(car_types.select()).fetchall()

# create new car_type
@car_type.post("/", response_model=CarType)
async def create_car_type(car_type: CarType):
    # nếu tồn tại id thì trả về lỗi 
    check = conn.execute(car_types.select().where(car_types.c.id == car_type.id)).fetchall()
    if check:
        raise HTTPException(418, "Car Type with id '{}' already existe".format(car_type.id))
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
async def update_car_type(id: str, car_type: CarTypePayload):
    conn.execute(car_types.update().values(
        name=car_type.name,
        country=car_type.country,
        description=car_type.description
    ).where(car_types.c.id == id))
    data = conn.execute(car_types.select().where(car_types.c.id == id)).first()
    if not data:
        raise HTTPException(404, "Car Type with id '{}' not found".format(id))
    return data

# delete car_type
@car_type.delete("/{id}")
async def delete_car_type(id: str):
    conn.execute(car_types.delete().where(car_types.c.id == id))
    return {
        "message": "Car Type with id '{}' has been deleted.".format(id),
        "id": id
    }