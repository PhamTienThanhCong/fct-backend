from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from sqlalchemy import select
from models.station import stations
from models.order import orders
from schemas.order import OrderPayload, OrderResponse

order = APIRouter()
auth_handler = AuthHandler()

@order.get("/all", response_model=List[OrderResponse])
async def get_all_orders():
    query = orders.select()
    return conn.execute(query).fetchall()

@order.get("/{id}", response_model=OrderResponse)
async def get_order_by_id(id: int):
    query = orders.select().where(orders.c.id == id)
    return conn.execute(query).first()

@order.post("/create")
async def create_order(payload: OrderPayload, auth = Depends(auth_handler.auth_wrapper_user)):
    # get charging_port by id
    customer_id = auth["id"]

    query = stations.select().where(stations.c.id == payload.charging_port_id)
    charging_port = conn.execute(query).first()
    
    if not charging_port:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Charging port not found")
    
