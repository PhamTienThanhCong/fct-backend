from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta


categories = Table(
    'category',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('image', String(255)),
    Column('created_at', DateTime()),
)
