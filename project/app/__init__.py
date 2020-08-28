import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CsrfProtect

import config

app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

csrf = CsrfProtect()
csrf.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app,  db)


from . import views
