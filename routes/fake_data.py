from config.auth import AuthHandler
from faker import Faker
from config.db import conn
from fastapi import APIRouter
from models.user import users
from models.customer import customers


fake_data = APIRouter()
fake = Faker()
auth_handler=AuthHandler()

@fake_data.post("/users")
def generate_fake_users(
    number_of_users: int = 100,
):
    # Generate and insert 1000 fake users
    for _ in range(number_of_users):
        hash_password = auth_handler.get_password_hash("123456")
        fake_user = {
            "role_id": "2",
            "email": fake.email(),
            "password": hash_password,
            "full_name": fake.name(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "title": fake.job(),
            "description": fake.text(),
            "card_id": "123456789",
        }

        # kiểm tra xem phone hoặc email đã tồn tại chưa
        check = conn.execute(users.select().where(users.c.phone == fake_user["phone"])).fetchall()
        if check:
            continue

        # Create a new user
        conn.execute(users.insert().values(
            role_id=fake_user["role_id"],
            email=fake_user["email"],
            password=hash_password,
            full_name=fake_user["full_name"],
            phone=fake_user["phone"],
            address=fake_user["address"],
            card_id=fake_user["card_id"],
            title=fake_user["title"],
            description=fake_user["description"],
        ))

    return {"message": "Fake users created successfully"}

@fake_data.post("/customers")
def generate_fake_customers(
    number_of_customers: int = 100,
):
    # Generate and insert 1000 fake customers
    for _ in range(number_of_customers):
        hash_password = auth_handler.get_password_hash("123456")

        fake_customer = {
            "email": fake.email(),
            "password": hash_password,
            "full_name": fake.name(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "birthday": fake.date(),
            "card_id": "123456789",
        }

        # kiểm tra xem phone hoặc email đã tồn tại chưa
        check = conn.execute(customers.select().where(customers.c.phone == fake_customer["phone"])).fetchall()
        if check:
            continue

        # Create a new customer
        conn.execute(customers.insert().values(
            email=fake_customer["email"],
            password=hash_password,
            full_name=fake_customer["full_name"],
            phone=fake_customer["phone"],
            address=fake_customer["address"],
            birthday=fake_customer["birthday"],
            card_id=fake_customer["card_id"],
        ))

    return {"message": "Fake customers created successfully"}