from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    avatar: str
    location_id: int
    gender: str
    dob: str
