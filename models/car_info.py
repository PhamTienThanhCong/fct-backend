from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

car_infos = Table(
    "car_infos",
    meta,
    Column("id", Integer, primary_key=True),
    Column("car_type_id", String(50), ForeignKey("car_types.id")),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("name_car", String(255), nullable=False),
    Column("license_plate", String(50), nullable=False),
    Column("vehicle_condition", String(255), nullable=True),
    Column("battery_status", String(100), nullable=True),
    Column("year_of_manufacture", Integer, nullable=True),
    Column("created_at", String(50), nullable=True)
)

meta.create_all(engine)
