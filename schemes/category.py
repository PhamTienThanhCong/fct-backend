from pydantic import BaseModel
from datetime import datetime


class Category(BaseModel):
    name: str
    image: str
    created_at: str
