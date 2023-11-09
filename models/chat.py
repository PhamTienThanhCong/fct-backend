from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, JSON
from config.db import meta, engine

chats = Table(
    "chats",
    meta,
    Column("tag", String(50), primary_key=True, unique=True),
    Column("patterns", JSON, nullable=False),
    Column("responses", JSON, nullable=False),
)

meta.create_all(engine)