from typing import Optional
from pydantic import BaseModel,constr

class User(BaseModel):
    role_id: int
    email: constr(max_length=250)
    full_name: constr(max_length=100)
    phone: constr(max_length=20)
    address: constr(max_length=255)
    card_id: constr(max_length=25)
    title: constr(max_length=100)
    description: Optional[str]

class UserPayload(User):
    password: constr(min_length=3, max_length=100)

class UserAll(User):
    id: int

class UserLogin(BaseModel):
    email: constr(max_length=250)
    password: constr(min_length=3, max_length=100)