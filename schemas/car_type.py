from typing import Optional
from pydantic import BaseModel, constr

class CarType(BaseModel):
    id: constr(max_length=50)
    name: constr(max_length=250)
    country: constr(max_length=250)
    description: Optional[str] = None

class CarTypePayload(BaseModel):
    name: constr(max_length=250)
    country: constr(max_length=250)
    description: Optional[str] = None