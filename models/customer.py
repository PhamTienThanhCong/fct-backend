from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

customers = Table(
    "customers",
    meta,
    Column("id", Integer, primary_key=True),
    Column("email", String(250), nullable=False),
    Column("password", String(255), nullable=False),
    Column("full_name", String(100), nullable=False),
    Column("phone", String(20), nullable=False),
    Column("address", String(255), nullable=True),
    Column("birthday", String(20), nullable=True),
    Column("card_id", String(25), nullable=False),
)

meta.create_all(engine)
