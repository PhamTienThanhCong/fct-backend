from fastapi import APIRouter
from config.db import conn
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from models.role import roles
from schemas.role import Role,RoleAll

role = APIRouter()

# get all role
@role.get("/", response_model=List[RoleAll])
async def get_all_role():
    return conn.execute(roles.select()).fetchall()

# create new role
@role.post("/")
async def create_role(role: Role):
    roleCreate = conn.execute(roles.insert().values(
        name=role.name,
        description=role.description
    ))
    # return role has been created
    return conn.execute(roles.select().where(roles.c.id == roleCreate.lastrowid)).first()


# delete role
@role.delete("/{id}")
async def delete_role(id: str):
    conn.execute(roles.delete().where(roles.c.id == id))
    return {
        "message": "Role with id '{}' deleted successfully.".format(id),
        "id": id
    }
