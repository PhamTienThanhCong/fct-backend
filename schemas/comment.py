from typing import Optional
from pydantic import BaseModel,constr,conint
import datetime

class CommentPayload(BaseModel):
    station_id: int
    title: constr(max_length=255)
    content: constr(max_length=255)
    rating: conint(ge=1, le=5)

class CustomerResponse(BaseModel):
    id: int
    full_name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    created_at: datetime.datetime

class CommentResponse(CommentPayload):
    id: int
    customer: CustomerResponse
    # user: dict

class CommentUpdatePayload(BaseModel):
    title: Optional[constr(max_length=255)]
    content: Optional[constr(max_length=255)]
    rating: Optional[conint(ge=1, le=5)]