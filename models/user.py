from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, Date
from config.db import meta
from datetime import datetime


users = Table(
    'user',
    meta,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(55)),
    Column('lastname', String(45)),
    Column('email', String(45)),
    Column('password', String(255)),
    Column('avatar', String(255)),
    Column('location_id', Integer()),
    Column('gender', String(10)),
    Column('dob', String(10)),
    Column('created_at', TIMESTAMP(timezone=False),
           default=datetime.now()),
)
