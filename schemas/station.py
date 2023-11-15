from typing import Optional
from pydantic import BaseModel, constr
import datetime

class StationPayload(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: Optional[str]
    address: constr(min_length=1, max_length=255)
    local_x: float
    local_y: float
    phone: constr(min_length=1, max_length=35)
    email: constr(min_length=1, max_length=250)
    image: Optional[constr(min_length=1, max_length=255)]
    open_time: Optional[datetime.time]
    close_time: Optional[datetime.time]
    is_order: Optional[int]

class StationResponse(StationPayload):
    id: int
    owner_id: int