from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Text
from config.db import meta, engine
from constants.default_value import DEFAULT_CAR_TYPES

car_types = Table(
    "car_types",
    meta,
    Column("id", String(50), primary_key=True),
    Column("name", String(255), nullable=False),
    Column("country", String(255), nullable=False),
    Column("description", Text, nullable=True),
)

meta.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(car_types.select())
    existing_data = result.fetchone()

# Nếu bảng chưa có dữ liệu, thêm dữ liệu mặc định
if existing_data is None:
    
    with engine.connect() as conn:
        for default_car_type in DEFAULT_CAR_TYPES:
            conn.execute(car_types.insert().values(**default_car_type))
