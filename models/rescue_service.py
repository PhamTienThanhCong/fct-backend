from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer, Float
from config.db import meta, engine
from constants.default_value import DEFAULT_RESCUE_SERVICES

rescue_services = Table(
    "rescue_services",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("address", String(255), nullable=False),
    Column("email", String(255), nullable=True),
    Column("local_x",Float, nullable=False),
    Column("local_y",Float, nullable=False),
)

meta.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(rescue_services.select())
    existing_data = result.fetchone()

# Nếu bảng chưa có dữ liệu, thêm dữ liệu mặc định
if existing_data is None:
    
    with engine.connect() as conn:
        for default_rescue_service in DEFAULT_RESCUE_SERVICES:
            conn.execute(rescue_services.insert().values(**default_rescue_service))