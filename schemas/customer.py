from typing import Optional
from pydantic import BaseModel,constr
import datetime

class Customer(BaseModel):
    email: Optional[constr(min_length=5, max_length=250)]
    full_name: constr(min_length=5, max_length=100)
    phone: constr(min_length=10, max_length=35)
    address: Optional[constr(min_length=5, max_length=255)]
    birthday: Optional[datetime.date]
    card_id: Optional[constr(min_length=5, max_length=25)]

class CustomerRepose(Customer):
    id: int

class CustomerLogin(BaseModel):
    phone: constr(min_length=10, max_length=35)
    password: constr(min_length=8, max_length=255)

class CustomerRegister(BaseModel):
    phone: constr(min_length=10, max_length=35)
    full_name: constr(min_length=5, max_length=100)
    password: constr(min_length=8, max_length=255)
    

class CustomerPayload(BaseModel):
    email: Optional[constr(min_length=5, max_length=250)]
    full_name: constr(min_length=5, max_length=100)
    address: Optional[constr(min_length=5, max_length=255)]
    birthday: Optional[datetime.date]
    card_id: Optional[constr(min_length=5, max_length=25)]
    password: constr(min_length=8, max_length=255)