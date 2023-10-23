from sqlalchemy import create_engine, MetaData

DB_USER='root'
DB_PASS=""
DB_HOST='localhost'
DB_PORT=3306
DATABASE='fastapi'

connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

engine = create_engine(connect_string)

meta = MetaData()

conn = engine.connect()
