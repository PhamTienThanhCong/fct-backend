from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

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
    Column("title", String(100), nullable=False),
    Column("description", String(255), nullable=True),
)

meta.create_all(engine)
