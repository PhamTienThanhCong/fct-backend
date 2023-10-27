from typing import Optional
from pydantic import BaseModel, constr, conint

class CarInfoPayload(BaseModel):
    car_type_id: constr(max_length=50)
    name_car: constr(min_length=5, max_length=255)
    license_plate: constr(min_length=3, max_length=50)
    vehicle_condition: Optional[constr(max_length=255)]
    battery_status: Optional[constr(max_length=100)]
    year_of_manufacture: Optional[constr(max_length=50)]
    created_at: Optional[conint(gt=1900, lt=2100)]

class CarInfo(CarInfoPayload):
    customer_id: int
    
class CarInfoId(CarInfo):
    id: int