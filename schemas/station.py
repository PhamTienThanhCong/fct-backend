from typing import Optional
from pydantic import BaseModel, constr

class StationPayload(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: Optional[constr(min_length=1, max_length=1000)]
    address: constr(min_length=1, max_length=255)
    local_x: float
    local_y: float
    phone: constr(min_length=1, max_length=20)
    email: constr(min_length=1, max_length=250)
    image: Optional[constr(min_length=1, max_length=255)]
    open_time: Optional[constr(min_length=1, max_length=20)]
    close_time: Optional[constr(min_length=1, max_length=20)]
    is_order: Optional[int]

class StationResponse(StationPayload):
    id: int
    owner_id: int