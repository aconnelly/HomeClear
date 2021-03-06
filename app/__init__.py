#Import all required modules
from flask import Flask,g
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.whooshalchemy as Whoosh
from config import config

from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()
db = SQLAlchemy()
bootstrap = Bootstrap()
moment = Moment()
bootstrap = Bootstrap()


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    #prevent circular imports

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
