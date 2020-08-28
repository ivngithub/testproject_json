import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'StapdpxtwVJJaEaOXJjGnGuwDIJElMDQXRrp#LviK%#Qk&Ck'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_FILE_PATH = os.path.join(app_dir, 'json_file.json')

POSTGRESQL = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
                os.environ['DB_USER'],
                os.environ['DB_PASSWORD'],
                os.environ['DB_HOST'],
                os.environ['DB_PORT'],
                os.environ['DB_NAME']
            )


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or POSTGRESQL


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or POSTGRESQL


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or POSTGRESQL
