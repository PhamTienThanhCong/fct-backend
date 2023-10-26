from sqlalchemy import create_engine, MetaData
from config.env_value import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME))

meta = MetaData()

conn = engine.connect()