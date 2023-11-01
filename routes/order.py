from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from sqlalchemy import select
from constants.main import CHARING_STATUS, CHARING_STATUS_TEXT, ORDER_STATUS, ORDER_STATUS_TEXT, AcceptType
from models.charging_port import charging_ports
from models.order import orders
from models.user import users
from models.station import stations
from models.customer import customers
from schemas.order import OrderPayload, OrderResponse

order = APIRouter()
auth_handler = AuthHandler()

def format_respond(data):
    return {
        "id": data["id"],
        "customer_id": data["customer_id"],
        "charging_port_id": data["charging_port_id"],
        "status": ORDER_STATUS_TEXT[data["status"]],
        "start_time": data["start_time"],
        "end_time": data["end_time"],
        "total_price": str(data["total_price"]) + " USD",
        "total_time": str(data["total_time"]) + " hours",
        "created_at": data["created_at"],
        "customer": {
            "id": data["customer_id"],
            "full_name": data["full_name"],
            "phone": data["phone"],
            "address": data["address"],
        }
    }

@order.get("/", response_model=List[OrderResponse])
async def get_all_orders(
    skip: int = 0,
    limit: int = 10,
    charging_port_id: int = None,
    customer_id: int = None,
    status: int = None,
):
    query = select([orders, customers]).select_from(orders.join(customers)).offset(skip).limit(limit)
    if charging_port_id:
        query = query.where(orders.c.charging_port_id == charging_port_id)
    if customer_id:
        query = query.where(orders.c.customer_id == customer_id)
    if status:
        query = query.where(orders.c.status == status)

    data = conn.execute(query).fetchall()
    return list(map(format_respond, data))

# 

@order.get("/{id}", response_model=OrderResponse)
async def get_order_by_id(id: int):
    query = select([orders, customers]).select_from(orders.join(customers)).where(orders.c.id == id)
    return format_respond(conn.execute(query).first())

@order.post("/create", response_model=OrderResponse)
async def create_order(payload: OrderPayload, auth = Depends(auth_handler.auth_wrapper_user)):
    # get charging_port by id
    customer_id = auth["id"]

    query = charging_ports.select().where(charging_ports.c.id == payload.charging_port_id)
    charging_port = conn.execute(query).first()
    port_price = charging_port["price"]

    if not charging_port:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Charging port not found")
    
    if charging_port["status"] != CHARING_STATUS["FREE"]:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Charging port is {}".format(CHARING_STATUS_TEXT[charging_port["status"]])) 
    
    total_time = payload.end_time - payload.start_time
    # convert total_time to hours
    total_time = total_time.total_seconds() / 3600

    if total_time < float(0):
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="End time must be greater than start time")
    
    total_price = total_time * port_price

    query = orders.insert().values(
        customer_id=customer_id,
        charging_port_id=payload.charging_port_id,
        start_time=payload.start_time,
        end_time=payload.end_time,
        total_price=total_price,
        total_time=total_time,
    )

    last_record_id = conn.execute(query).lastrowid

    # get order by id and inner join with customer table by customer_id
    query = select([orders, customers]).select_from(orders.join(customers)).where(orders.c.id == last_record_id)
    return format_respond(conn.execute(query).first())

# ACCEPT ORDER
@order.put("/{accept_type}/{id}", response_model=OrderResponse)
async def accept_order(
    id: int, 
    accept_type: AcceptType = AcceptType.accept,
    auth = Depends(auth_handler.auth_wrapper_admin)):
    # get charging_port by id
    owner_id = auth["id"]

    # Giả sử bạn đã có các đối tượng "orders", "charging_ports", "stations", và "id".

    query = select([orders,stations, charging_ports]).\
        select_from(
            orders.join(
                charging_ports,
                orders.c.charging_port_id == charging_ports.c.id
            ).join(
                stations,
                charging_ports.c.station_id == stations.c.id
            )
        ).where(orders.c.id == id)

    data = conn.execute(query).first()

    if not data:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Order not found")

    if data["owner_id"] != owner_id:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="You are not owner of this station")

    if data["status"] == ORDER_STATUS["FINISH_ORDER"]:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Order is finished")

    if accept_type == "accept":
        if data["status_1"] != CHARING_STATUS["FREE"]:
            raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Charging port is {}".format(CHARING_STATUS_TEXT[data["status"]]))    
        # cập nhật trạng thái của order
        query = orders.update().where(orders.c.id == id).values(status=ORDER_STATUS["CONFIRM_ORDER"])
        conn.execute(query)

        # cập nhật trạng thái của charging port
        query = charging_ports.update().where(charging_ports.c.id == data["charging_port_id"]).values(status=CHARING_STATUS["ORDERED"])
        conn.execute(query)
    
    if accept_type == "cancel":
        # cập nhật trạng thái của order
        query = orders.update().where(orders.c.id == id).values(status=ORDER_STATUS["CANCEL_ORDER"])
        conn.execute(query)

        # cập nhật trạng thái của charging port
        query = charging_ports.update().where(charging_ports.c.id == data["charging_port_id"]).values(status=CHARING_STATUS["FREE"])
        conn.execute(query)

    if accept_type == "finish":
        # cập nhật trạng thái của order
        query = orders.update().where(orders.c.id == id).values(status=ORDER_STATUS["FINISH_ORDER"])
        conn.execute(query)

        # cập nhật trạng thái của charging port
        query = charging_ports.update().where(charging_ports.c.id == data["charging_port_id"]).values(status=CHARING_STATUS["FREE"])
        conn.execute(query)

    query = select([orders, customers]).select_from(orders.join(customers)).where(orders.c.id == id)
    return format_respond(conn.execute(query).first())