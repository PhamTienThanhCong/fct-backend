from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Text
from config.db import meta, engine

car_types = Table(
    "car_types",
    meta,
    Column("id", String(50), primary_key=True),
    Column("name", String(255), nullable=False),
    Column("country", String(255), nullable=False),
    Column("description", Text, nullable=True),
)

meta.create_all(engine)
