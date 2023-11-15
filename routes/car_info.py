from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from models.car_info import car_infos
from models.car_type import car_types
from schemas.car_info import CarInfo, CarInfoId, CarInfoPayload 

car_info = APIRouter()
auth_handler = AuthHandler()

# get all car_info
@car_info.get("/", response_model=List[CarInfo])
async def get_all_car_info(
    skip: int = 0,
    limit: int = 10,
):
    query = car_infos.select().offset(skip).limit(limit)
    return conn.execute(query).fetchall()

# get car by id 
@car_info.get("/{id}", response_model=CarInfoId)
async def get_car_info_by_id(id: int):
    data = conn.execute(car_infos.select().where(car_infos.c.id == id)).first()
    if not data:
        raise HTTPException(HTTP_404_NOT_FOUND, "Car Info with id '{}' not found".format(id))
    return data

#get car by customer_id
@car_info.get("/customer/{customer_id}", response_model=List[CarInfo])
async def get_car_info_by_customer_id(customer_id: int):
    data = conn.execute(car_infos.select().where(car_infos.c.customer_id == customer_id)).fetchall()
    return data

# create new car_info
@car_info.post("/", response_model=CarInfo)
async def create_car_info(car_info: CarInfoPayload, auth=Depends(auth_handler.auth_wrapper_user)):
    id_user = auth["id"]
    # nếu car_type_id không tồn tại thì trả về lỗi
    check = conn.execute(car_types.select().where(car_types.c.id == car_info.car_type_id)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Type with id '{}' not found".format(car_info.car_type_id))
    # tạo mới car_info
    newCar = conn.execute(car_infos.insert().values(
        customer_id=id_user,
        car_type_id=car_info.car_type_id,
        name_car=car_info.name_car,
        license_plate=car_info.license_plate,
        vehicle_condition=car_info.vehicle_condition,
        battery_status=car_info.battery_status,
        year_of_manufacture=car_info.year_of_manufacture,
        created_at=car_info.created_at
    ))

    return conn.execute(car_infos.select().where(car_infos.c.id == newCar.lastrowid)).first()

# # edit
# # update car_info
@car_info.put("/{id}", response_model=CarInfoId)
async def update_car_info(id: int, car_info: CarInfoPayload, auth=Depends(auth_handler.auth_wrapper_user)):
    id_user = auth["id"]
    # nếu car_type_id không tồn tại thì trả về lỗi
    check = conn.execute(car_types.select().where(car_types.c.id == car_info.car_type_id)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Type with id '{}' not found".format(car_info.car_type_id))
    # nếu car_info_id không tồn tại thì trả về lỗi
    check = conn.execute(car_infos.select().where(car_infos.c.id == id)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Info with id '{}' not found".format(id))
    # nếu car_info_id không thuộc về user đang đăng nhập thì trả về lỗi
    check = conn.execute(car_infos.select().where(car_infos.c.id == id and car_infos.c.customer_id == id_user)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Info with id '{}' not belong to you".format(id))
    # update car_info
    conn.execute(car_infos.update().where(car_infos.c.id == id).values(
        car_type_id=car_info.car_type_id,
        name_car=car_info.name_car,
        license_plate=car_info.license_plate,
        vehicle_condition=car_info.vehicle_condition,
        battery_status=car_info.battery_status,
        year_of_manufacture=car_info.year_of_manufacture,
        created_at=car_info.created_at
    ))
    return conn.execute(car_infos.select().where(car_infos.c.id == id)).first()

# delete car_info
@car_info.delete("/{id}")
async def delete_car_info(id: int, auth=Depends(auth_handler.auth_wrapper_user)):
    id_user = auth["id"]
    # nếu car_info_id không tồn tại thì trả về lỗi
    check = conn.execute(car_infos.select().where(car_infos.c.id == id)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Info with id '{}' not found".format(id))
    # nếu car_info_id không thuộc về user đang đăng nhập thì trả về lỗi
    check = conn.execute(car_infos.select().where(car_infos.c.id == id and car_infos.c.customer_id == id_user)).fetchall()
    if not check:
        raise HTTPException(HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, "Car Info with id '{}' not belong to you".format(id))
    conn.execute(car_infos.delete().where(car_infos.c.id == id))
    return {
        "message": "Car Info with id '{}' deleted successfully.".format(id),
        "id": id
    }