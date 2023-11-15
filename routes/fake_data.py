import datetime
from config.auth import AuthHandler
from faker import Faker
from config.db import conn
from fastapi import APIRouter
from models.user import users
from models.customer import customers
from models.station import stations
from models.charging_port import charging_ports
from models.comment import comments
from models.order import orders

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

# fake station
@fake_data.post("/stations")
def generate_fake_stations(
    number_of_stations: int = 100,
):
    # Generate and insert 1000 fake stations
    # get all id of user
    all_user = conn.execute(users.select()).fetchall()
    all_user_id = []
    for user in all_user:
        all_user_id.append(user["id"])

    for _ in range(number_of_stations):
        fake_station = {
            "owner_id": all_user_id[fake.random_int(0, len(all_user_id)-1)],
            "name": fake.name() + " Station",
            "address": fake.address(),
            "local_x": fake.longitude(),
            "local_y": fake.latitude(),
            "phone": fake.phone_number(),
            "email": fake.email(),
            "image": "https://picsum.photos/200/300",
            "is_order": fake.random_int(0, 1),
            "open_time": "00:00:00",
            "close_time": "23:59:59",
            "description": "",
        }

        # Create a new station
        conn.execute(stations.insert().values(
            owner_id=fake_station["owner_id"],
            name=fake_station["name"],
            address=fake_station["address"],
            local_x=fake_station["local_x"],
            local_y=fake_station["local_y"],
            phone=fake_station["phone"],
            email=fake_station["email"],
            image=fake_station["image"],
            is_order=fake_station["is_order"],
            open_time=fake_station["open_time"],
            close_time=fake_station["close_time"],
        ))

    return {"message": "Fake stations created successfully"}

# fake station port
@fake_data.post("/charging-port")
def generate_fake_charging_ports(
    number_of_charging_ports: int = 1000,
):
    # get all id of station
    all_station = conn.execute(stations.select()).fetchall()
    all_station_id = []
    for station in all_station:
        all_station_id.append(station["id"])

    # Generate and insert 1000 fake charging ports
    for _ in range(number_of_charging_ports):
        fake_data = {
            "station_id": all_station_id[fake.random_int(0, len(all_station_id)-1)],
            "port_code": "port  " + fake.uuid4(),
            "price": fake.random_int(1000, 100000),
            "power": fake.random_int(1000, 100000),
            "status": fake.random_int(0, 4),
        }

        # Create a new charging port
        conn.execute(charging_ports.insert().values(
            station_id=fake_data["station_id"],
            port_code=fake_data["port_code"],
            price=fake_data["price"],
            power=fake_data["power"],
            status=fake_data["status"],
        ))

    return {"message": "Fake charging ports created successfully"}

# fake comment
@fake_data.post("/comments")
def generate_fake_comments(
    number_of_comments: int = 1000,
):
    # get all id of station
    all_station = conn.execute(stations.select()).fetchall()
    all_station_id = []
    for station in all_station:
        all_station_id.append(station["id"])

    # get all id of customer
    all_customer = conn.execute(customers.select()).fetchall()
    all_customer_id = []
    for customer in all_customer:
        all_customer_id.append(customer["id"])

    # Generate and insert 1000 fake comments
    for _ in range(number_of_comments):
        fake_data = {
            "station_id": all_station_id[fake.random_int(0, len(all_station_id)-1)],
            "customer_id": all_customer_id[fake.random_int(0, len(all_customer_id)-1)],
            "rating": fake.random_int(1, 5),
            "title": fake.text(),
            "content": fake.text(),
            "created_at": fake.date(),
        }

        # Create a new comment
        conn.execute(comments.insert().values(
            station_id=fake_data["station_id"],
            customer_id=fake_data["customer_id"],
            title=fake_data["title"],
            rating=fake_data["rating"],
            content=fake_data["content"],
            created_at=fake_data["created_at"],
        ))

    return {"message": "Fake comments created successfully"}

# fake order
@fake_data.post("/orders")
def generate_fake_orders(
    number_of_orders: int = 1000,
):
    # demo data
    all_customer = conn.execute(customers.select()).fetchall()
    all_customer_id = []
    for customer in all_customer:
        all_customer_id.append(customer["id"])

    all_port = conn.execute(charging_ports.select()).fetchall()

    # Generate and insert 1000 fake orders
    for _ in range(number_of_orders):
        index_ran = fake.random_int(0, len(all_port)-1)
        startTime = fake.date_time_this_decade()
        total_time = fake.random_int(1, 10)
        endTime = startTime + datetime.timedelta(hours=total_time)        

        total_price = total_time * all_port[index_ran]["price"]

        fake_data = {
            "customer_id": all_customer_id[fake.random_int(0, len(all_customer_id)-1)],
            "charging_port_id": all_port[index_ran]["id"],
            "status": fake.random_int(0, 4),
            "start_time": startTime,
            "end_time": endTime,
            "total_price": total_price,
            "total_time": total_time,
        }

        # Create a new order
        conn.execute(orders.insert().values(
            customer_id=fake_data["customer_id"],
            charging_port_id=fake_data["charging_port_id"],
            status=fake_data["status"],
            start_time=fake_data["start_time"],
            end_time=fake_data["end_time"],
            total_price=fake_data["total_price"],
            total_time=fake_data["total_time"],
        ))

    return {"message": "Fake orders created successfully"}