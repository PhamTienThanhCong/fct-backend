from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta, engine

charging_ports = Table(
    "charging_ports",
    meta,
    Column("id", Integer, primary_key=True),
    Column("station_id", Integer, ForeignKey("stations.id")),
    Column("port_number", Integer, nullable=False),
    Column("price", Float, nullable=False),
    Column("power", Float, nullable=False),
    Column("status", Integer, nullable=False),
)

meta.create_all(engine)
