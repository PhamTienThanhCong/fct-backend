from pydantic import BaseModel
from datetime import datetime


class Suggestion(BaseModel):
    title: str
    description: str
    image: str
    location_id: int
    start_at: str
    end_at: str
    like_count: int
    dislike_count: int
    tick_count: int
    save_count: int
    created_at: str
