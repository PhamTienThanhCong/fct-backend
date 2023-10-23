from pydantic import BaseModel


class SubCategory(BaseModel):
    name: str
    category_id: int
