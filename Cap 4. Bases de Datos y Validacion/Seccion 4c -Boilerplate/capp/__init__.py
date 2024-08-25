from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
# application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

### Code Computer
application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'

# Base de datos
DBVAR = 'sqlite:///user.db'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] ={'sentence': 'sqlite:///sentence_table.db'}
db = SQLAlchemy(application)

# Bcrypt
bcrypt = Bcrypt(application)

# Login
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.business.routes import business
from capp.light_talk_app.routes import light_talk_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(business)
application.register_blueprint(light_talk_app)
application.register_blueprint(users)

