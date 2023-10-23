from models.user import users
from models.category import categories
from models.sub_category import sub_categories
from models.location import locations
from models.suggestion import suggestions

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER='root'
DB_PASS=""
DB_HOST='localhost'
DB_PORT=3306
DATABASE='fastapi'

connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)

engine = create_engine(connect_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo các bảng trong database
users.create(engine)
categories.create(engine)
sub_categories.create(engine)
locations.create(engine)
suggestions.create(engine)

engine.connect()