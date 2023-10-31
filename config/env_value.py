from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')
DESCRIPTION_APP= os.getenv('DESCRIPTION_APP')

DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')

SECRET_KEY = os.getenv('SECRET_KEY')