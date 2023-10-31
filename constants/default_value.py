
from config.auth import AuthHandler


auth_handler = AuthHandler()
hash_password = auth_handler.get_password_hash("123456")

DEFAULT_ROLES = [
        {"name": "admin", "description": "Administrator"},
        {"name": "user", "description": "Regular User"},
    ]

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

