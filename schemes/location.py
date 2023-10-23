from pydantic import BaseModel
from datetime import datetime


class Location(BaseModel):
    name: str
