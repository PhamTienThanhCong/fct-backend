from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta, engine
from constants.default_value import DEFAULT_ROLES

roles = Table(
    "roles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("description", String(255), nullable=True),
)

meta.create_all(engine)

# Kiểm tra xem bảng "roles" đã có dữ liệu chưa
with engine.connect() as conn:
    result = conn.execute(roles.select())
    existing_data = result.fetchone()

# Nếu bảng chưa có dữ liệu, thêm dữ liệu mặc định
if existing_data is None:
    
    with engine.connect() as conn:
        for default_role in DEFAULT_ROLES:
            conn.execute(roles.insert().values(**default_role))