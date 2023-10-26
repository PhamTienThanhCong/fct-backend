from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer, Float
from config.db import meta, engine

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
