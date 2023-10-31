import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from constants.env_value import DB_USER, DB_HOST, DB_PORT, DB_NAME

load_dotenv()

DB_PASS = os.getenv('DB_PASS')

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME))

meta = MetaData()

conn = engine.connect()