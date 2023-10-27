from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from sqlalchemy import select
from models.comment import comments
from models.station import stations
from models.customer import customers
from schemas.comment import CommentPayload, CommentResponse, CommentUpdatePayload

comment = APIRouter()
auth_handler = AuthHandler()

def convert_to_comment_dict(comment):
    return {
        "id": comment["id"],
        "station_id": comment["station_id"],
        "title": comment["title"],
        "content": comment["content"],
        "rating": comment["rating"],
        "created_at": comment["created_at"],
        "customer": {
            "id": comment["customer_id"],
            "full_name": comment["full_name"],
            "phone": comment["phone"],
            "address": comment["address"],
        }
    }

@comment.get("/{station_id}", response_model=List[CommentResponse])
async def get_comments_by_station_id(station_id: int):
    query = select([comments, customers]).where(comments.c.station_id == station_id).select_from(comments.join(customers)).where(comments.c.customer_id == customers.c.id)
    result = conn.execute(query)
    return [convert_to_comment_dict(row) for row in result]

@comment.post("/", response_model=CommentResponse)
async def create_comment(payload: CommentPayload, auth = Depends(auth_handler.auth_wrapper_user)):
    customer_id = auth['id']

    # check station_id có tồn tại không
    query = select([stations]).where(stations.c.id == payload.station_id)
    station = conn.execute(query).first()
    if not station:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Station with id: {} not found".format(payload.station_id))

    query = comments.insert().values(**payload.dict(), customer_id=customer_id)
    last_record_id = conn.execute(query)
    
    # lấy thông tin comment vừa tạo với id vừa được tạo. và join với bảng customer để lấy thông tin customer
    query = select([comments, customers]).where(comments.c.id == last_record_id.lastrowid).select_from(comments.join(customers)).where(comments.c.id == last_record_id.lastrowid)
    new_comment = conn.execute(query).first()

    return convert_to_comment_dict(new_comment)

@comment.put("/{id}", response_model=CommentResponse)
async def update_comment(id: int, payload: CommentUpdatePayload, auth = Depends(auth_handler.auth_wrapper_user)):
    customer_id = auth['id']
    query = comments.update().where(comments.c.id == id).where(comments.c.customer_id == customer_id).values(**payload.dict())
    result = conn.execute(query)
    if not result.rowcount:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Comment with id: {} can not be updated".format(id))
    
    # lấy thông tin comment vừa update với id vừa được update. và join với bảng customer để lấy thông tin customer
    query = select([comments, customers]).where(comments.c.id == id).select_from(comments.join(customers)).where(comments.c.id == id)
    updated_comment = conn.execute(query).first()

    return convert_to_comment_dict(updated_comment)

@comment.delete("/{id}")
async def delete_comment(id: int, auth = Depends(auth_handler.auth_wrapper_user)):
    customer_id = auth['id']
    query = comments.delete().where(comments.c.id == id).where(comments.c.customer_id == customer_id)
    comment_delete = conn.execute(query)
    if not comment_delete.rowcount:
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Comment with id: {} can not be deleted".format(id))
    return {"message": "Comment with id: {} deleted successfully!".format(id)}

