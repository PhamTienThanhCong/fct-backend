from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float, DateTime
from sqlalchemy import func
from config.db import meta, engine
from constants.main import CHARING_STATUS_TEXT

orders = Table(
    "orders",
    meta,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("charging_port_id", Integer, ForeignKey("charging_ports.id")),
    Column("status", Integer, nullable=False, server_default="1"),
    Column("start_time", DateTime, nullable=False),
    Column("end_time", DateTime, nullable=False),
    Column("total_price", Float, nullable=False),
    Column("total_time", Float, nullable=False),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
)

meta.create_all(engine)
