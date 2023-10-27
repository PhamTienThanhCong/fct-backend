from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, String
from config.db import meta, engine

charging_ports = Table(
    "charging_ports",
    meta,
    Column("id", Integer, primary_key=True),
    Column("station_id", Integer, ForeignKey("stations.id")),
    Column("port_code", String(50), nullable=False),
    Column("price", Float, nullable=False),
    Column("power", Float, nullable=False),
    Column("status", Integer, nullable=False, default=1),
)

meta.create_all(engine)
