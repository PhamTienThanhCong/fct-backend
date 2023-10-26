from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float
from config.db import meta, engine

stations = Table(
    "stations",
    meta,
    Column("id", Integer, primary_key=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
    Column("name", String(100), nullable=False),
    Column("address", String(255), nullable=False),
    Column("local_x",Float, nullable=False),
    Column("local_y",Float, nullable=False),
    Column("phone", String(20), nullable=False),
    Column("email", String(250), nullable=False),
    Column("description", String(255), nullable=True),
    Column("image", String(255), nullable=True),
    Column("open_time", String(20), nullable=True),
    Column("close_time", String(20), nullable=True),
    Column("is_order", Integer, nullable=False),
)

meta.create_all(engine)
