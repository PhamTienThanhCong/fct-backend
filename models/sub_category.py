from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta


sub_categories = Table(
    'sub_category',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('category_id', Integer())
)
