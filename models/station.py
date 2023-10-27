from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float
from config.db import meta, engine

stations = Table(
    "stations",
    meta,
    Column("id", Integer, primary_key=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
    Column("name", String(100), nullable=False),
    Column("description", String(255), nullable=True, default=""),
    Column("address", String(255), nullable=False),
    Column("local_x",Float, nullable=False),
    Column("local_y",Float, nullable=False),
    Column("phone", String(20), nullable=False),
    Column("email", String(250), nullable=False),
    Column("image", String(255), nullable=True),
    Column("open_time", String(20), nullable=True, default="00:00:00"),
    Column("close_time", String(20), nullable=True, default="00:00:00"),
    Column("is_order", Integer, nullable=True, default=0),
)

meta.create_all(engine)
