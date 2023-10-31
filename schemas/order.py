from typing import Optional
from pydantic import BaseModel,constr
import datetime

class OrderPayload(BaseModel):
    charging_port_id: int
    status: int
    start_time: datetime.datetime
    end_time: datetime.datetime

class OrderResponse(OrderPayload):
    id: int
    customer_id: int
    total_price: float
    total_time: int
    created_at: datetime.datetime
    