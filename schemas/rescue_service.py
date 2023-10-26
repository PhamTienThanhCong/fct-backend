from typing import Optional
from pydantic import BaseModel, constr

class RescueService(BaseModel):
    name: constr(max_length=250)
    phone: constr(max_length=20)
    address: constr(max_length=250)
    email: constr(max_length=250)
    local_x: float
    local_y: float

class RescueServiceAll(RescueService):
    id: int