from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

roles = Table(
    "roles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("description", String(255), nullable=True),
)

meta.create_all(engine)
