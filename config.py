from os.path import abspath, dirname

# App config
DEBUG = True
SECRET_KEY = 'supersecret123'
THREADS_PER_PAGE = 2

# Database
BASE_DIR = abspath(dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/app/database/db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
