from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from config.db import meta, engine
import datetime

comments = Table(
    "comments",
    meta,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id")),
    Column("station_id", Integer, ForeignKey("stations.id")),
    Column("title", String(255), nullable=False),
    Column("content", String(255), nullable=False),
    Column("rating", Integer, nullable=False),
    Column("created_at", DateTime, nullable=False, default=datetime.datetime.now()),
)

meta.create_all(engine)
