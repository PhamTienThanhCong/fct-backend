from typing import Optional
from pydantic import BaseModel, constr


class ChargingPortUpload(BaseModel):
    port_code: constr(max_length=50, min_length=1)
    price: float
    power: float
    status: Optional[int]

class ChargingPortPayload(ChargingPortUpload):
    station_id: int

class ChargingPortResponse(ChargingPortPayload):
    id: int
