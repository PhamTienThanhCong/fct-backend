from typing import Optional
from pydantic import BaseModel,constr
import datetime

class OrderPayload(BaseModel):
    charging_port_id: int
    status: int
    start_time: datetime.datetime
    end_time: datetime.datetime