from fastapi import APIRouter, Depends, HTTPException
from config.auth import AuthHandler
from config.db import conn
from typing import List
from starlette.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, HTTP_404_NOT_FOUND
from models.customer import customers
from schemas.customer import CustomerRepose, CustomerLogin, CustomerPayload, CustomerRegister

customer = APIRouter()
auth_handler = AuthHandler()

# login
@customer.post("/login")
async def login(customer: CustomerLogin):
    user = conn.execute(customers.select().where(customers.c.phone == customer.phone)).first()
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Phone or password is incorrect")
    elif not auth_handler.verify_password(customer.password, user.password):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Phone or password is incorrect")
    else:
        token = auth_handler.encode_token({"id": user.id, "role_id": 0})
        return {"token": token}

# get current user
@customer.get("/me", response_model=CustomerRepose)
async def get_me(auth=Depends(auth_handler.auth_wrapper_user)):
    return conn.execute(customers.select().where(customers.c.id == auth["id"])).first()

@customer.get("/", response_model=List[CustomerRepose])
async def get_all_customers(
    skip: int = 0,
    limit: int = 10,
):
    query = customers.select().offset(skip).limit(limit)
    return conn.execute(query).fetchall()

# get customer by id
@customer.get("/{id}", response_model=CustomerRepose)
async def get_customer_by_id(id: int):
    data = conn.execute(customers.select().where(customers.c.id == id)).first()
    if not data:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Not found")
    return data

@customer.post("/", response_model=CustomerRepose)
async def create_customer(customer: CustomerRegister):
    password_hash = auth_handler.get_password_hash(customer.password)
    # check if phone exists
    if conn.execute(customers.select().where(customers.c.phone == customer.phone)).first():
        raise HTTPException(status_code=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, detail="Phone already exists")
    # insert to db
    new_customer = {"full_name": customer.full_name, "phone": customer.phone, "password": password_hash}
    result = conn.execute(customers.insert().values(new_customer))
    return conn.execute(customers.select().where(customers.c.id == result.lastrowid)).first()

# edit customer
@customer.put("/{id}", response_model=CustomerRepose)
async def update_customer(id: int, customer: CustomerPayload, auth=Depends(auth_handler.auth_wrapper_user)):
    if (auth["id"] != id):
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Not found")
    password_hash = auth_handler.get_password_hash(customer.password)
    conn.execute(customers.update().where(customers.c.id == id).values(
        full_name=customer.full_name,
        email=customer.email,
        password=password_hash,
        address=customer.address,
        birthday=customer.birthday,
        card_id=customer.card_id
    ))
    return conn.execute(customers.select().where(customers.c.id == id)).first()