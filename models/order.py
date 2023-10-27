from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float, DateTime
from config.db import meta, engine

orders = Table(
    "orders",
    meta,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("charging_port_id", Integer, ForeignKey("charging_ports.id")),
    Column("status", Integer, nullable=False),
    Column("start_time", DateTime, nullable=False),
    Column("end_time", DateTime, nullable=False),
    Column("total_price", Float, nullable=False),
    Column("total_time", Integer, nullable=False),
)

meta.create_all(engine)
