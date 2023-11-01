
from config.auth import AuthHandler
import random

auth_handler = AuthHandler()
hash_password = auth_handler.get_password_hash("123456")

DEFAULT_ROLES = [
        {"name": "admin", "description": "Administrator"},
        {"name": "user", "description": "Regular User"},
    ]

DEFAULT_CAR_TYPES = [
    {
        "id": "vinfast",
        "name": "VinFast",
        "country": "Vietnam",
        "description": "VinFast is a Vietnamese automotive manufacturer based in Hanoi, Vietnam."
    },
    {
        "id": "thaco",
        "name": "Thaco",
        "country": "Vietnam",
        "description": "Trường Hải Auto Corporation (Thaco) is a major Vietnamese automobile manufacturer."
    },
    {
        "id": "samco",
        "name": "SAMCO",
        "country": "Vietnam",
        "description": "Sài Gòn Mechanical Engineering Corporation (SAMCO) is a leading manufacturer of buses and special-purpose vehicles in Vietnam."
    },
    {
        "id": "isuzu",
        "name": "Isuzu",
        "country": "Vietnam",
        "description": "Isuzu Vietnam is a subsidiary of Isuzu Motors Limited, a Japanese manufacturer of commercial vehicles."
    },
    {
        "id": "hino",
        "name": "Hino",
        "country": "Vietnam",
        "description": "Hino Motors Vietnam is a subsidiary of Hino Motors, a Japanese manufacturer of trucks and buses."
    },
    {
        "id": "suzuki",
        "name": "Suzuki",
        "country": "Vietnam",
        "description": "Suzuki Vietnam is a subsidiary of Suzuki Motor Corporation, a Japanese automaker."
    },
    {
        "id": "hyundai",
        "name": "Hyundai",
        "country": "Vietnam",
        "description": "Hyundai Thành Công Vietnam is a joint venture between Hyundai Motor Company and Thành Công Corporation in Vietnam."
    },
    {
        "id": "kia",
        "name": "Kia",
        "country": "Vietnam",
        "description": "Kia Motors Vietnam is a subsidiary of Kia Corporation, a South Korean automobile manufacturer."
    },
    {
        "id": "mercedes",
        "name": "Mercedes-Benz",
        "country": "Vietnam",
        "description": "Mercedes-Benz Vietnam is a subsidiary of Mercedes-Benz, a German luxury automobile manufacturer."
    },
    {
        "id": "ford",
        "name": "Ford",
        "country": "Vietnam",
        "description": "Ford Vietnam is a subsidiary of Ford Motor Company, an American automaker."
    },
    {
        "id": "chevrolet",
        "name": "Chevrolet",
        "country": "Vietnam",
        "description": "Chevrolet Vietnam is a subsidiary of Chevrolet, an American automobile brand."
    },
    {
        "id": "honda",
        "name": "Honda",
        "country": "Vietnam",
        "description": "Honda Vietnam is a subsidiary of Honda Motor Co., Ltd., a Japanese automaker."
    },
    {
        "id": "yamaha",
        "name": "Yamaha",
        "country": "Vietnam",
        "description": "Yamaha Motor Vietnam is a subsidiary of Yamaha Motor Co., Ltd., a Japanese motorcycle manufacturer."
    },
    {
        "id": "samsung",
        "name": "Samsung",
        "country": "Vietnam",
        "description": "Samsung Vietnam is a subsidiary of Samsung C&T Corporation, a South Korean company that manufactures commercial vehicles."
    },
    {
        "id": "mazda",
        "name": "Mazda",
        "country": "Vietnam",
        "description": "Mazda Vietnam is a subsidiary of Mazda Motor Corporation, a Japanese automaker."
    },
    {
        "id": "bmw",
        "name": "BMW",
        "country": "Vietnam",
        "description": "BMW Vietnam is a subsidiary of Bayerische Motoren Werke AG, a German luxury automobile and motorcycle manufacturer."
    },
    {
        "id": "peugeot",
        "name": "Peugeot",
        "country": "Vietnam",
        "description": "Peugeot Vietnam is a subsidiary of Stellantis, a French multinational automotive manufacturer."
    },
    {
        "id": "mitsubishi",
        "name": "Mitsubishi",
        "country": "Vietnam",
        "description": "Mitsubishi Motors Vietnam is a subsidiary of Mitsubishi Motors, a Japanese automaker."
    },
    {
        "id": "subaru",
        "name": "Subaru",
        "country": "Vietnam",
        "description": "Subaru Vietnam is a subsidiary of Subaru Corporation, a Japanese automobile manufacturer."
    },
]

def generate_fake_phone():
    phone = "0" + "".join([str(random.randint(0, 9)) for _ in range(9)])
    return phone

def generate_fake_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "viettel.com", "fpt.com"]
    name = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(8))
    domain = random.choice(domains)
    return f"{name}@{domain}"

DEFAULT_RESCUE_SERVICES = []
for i in range(50):
    repair_shop = {
        "name": f"Repair Shop {i+1}",
        "phone": generate_fake_phone(),
        "address": f"123 Street {i+1}, Hanoi, Vietnam",
        "email": generate_fake_email(),
        "local_x": random.uniform(20.9, 21.1),  # Vị trí x tạo ngẫu nhiên trong khoảng Hà Nội
        "local_y": random.uniform(105.6, 105.9),  # Vị trí y tạo ngẫu nhiên trong khoảng Hà Nội
    }
    DEFAULT_RESCUE_SERVICES.append(repair_shop)

DEFAULT_ADMIN = {
        "role_id": 1,
        "email": "admin@gmail.com",
        "full_name": "Phạm Tiến Thành Công",
        "phone": "0396396396",
        "address": "Hoàn Kiếm, Hà Nội",
        "card_id": "021551225400",
        "title": "Admin",
        "description": "admin",
        "password": hash_password
    }

