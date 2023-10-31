from typing import Optional
from pydantic import BaseModel,constr
import datetime

class OrderPayload(BaseModel):
    charging_port_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime

class CustomerResponse(BaseModel):
    id: int
    full_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]

class OrderResponse(OrderPayload):
    id: int
    customer_id: int
    charging_port_id: int
    status: str
    total_price: str
    total_time: str
    created_at: datetime.datetime
    customer: CustomerResponse
    