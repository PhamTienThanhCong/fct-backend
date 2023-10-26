from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine

a = Table(
    "a",
    meta,
    Column("id", Integer, primary_key=True),
)

meta.create_all(engine)
