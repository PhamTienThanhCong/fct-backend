from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DATABASE")

if DB_USER is None or DB_PASS is None or DB_HOST is None or DB_PORT is None or DATABASE is None:
    raise Exception("Không tìm thấy biến môi trường")

connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

engine = create_engine(connect_string)

meta = MetaData()

conn = engine.connect()
