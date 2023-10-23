from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta


suggestions = Table(
    'suggestion',
    meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('description', String(255)),
    Column('image', String(255)),
    Column('location_id', Integer),
    Column('start_at', String(22)),
    Column('end_at', String(22)),
    Column('like_count', Integer),
    Column('dislike_count', Integer),
    Column('tick_count', Integer),
    Column('save_count', Integer),
    Column('created_at', DateTime()),
)
