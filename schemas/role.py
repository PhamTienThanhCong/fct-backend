from typing import Optional
from pydantic import BaseModel, constr

class Role(BaseModel):
    name: constr(max_length=100)
    description: Optional[str] = None

class RoleAll(Role):
    id: int
