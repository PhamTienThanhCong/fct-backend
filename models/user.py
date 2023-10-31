from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine
from constants.default_value import DEFAULT_ADMIN

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("email", String(250), nullable=False),
    Column("password", String(255), nullable=False),
    Column("full_name", String(100), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("address", String(255), nullable=False),
    Column("card_id", String(25), nullable=False),
    Column("title", String(100), nullable=True),
    Column("description", String(255), nullable=True),
)

meta.create_all(engine)

# Kiểm tra xem bảng "roles" đã có dữ liệu chưa
with engine.connect() as conn:
    result = conn.execute(users.select())
    existing_data = result.fetchone()

# Nếu bảng chưa có dữ liệu, thêm dữ liệu mặc định
if existing_data is None:
    
    with engine.connect() as conn:
        conn.execute(users.insert().values(**DEFAULT_ADMIN))