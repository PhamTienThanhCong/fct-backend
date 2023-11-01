from typing import Optional
from pydantic import BaseModel, constr


class ChargingPortUpload(BaseModel):
    port_code: constr(max_length=50, min_length=1)
    price: float
    power: float

class ChargingPortPayload(ChargingPortUpload):
    station_id: int

class ChargingPortResponse(BaseModel):
    id: int
    station_id: int
    port_code: str
    price: str
    power: str
    status: Optional[str]
