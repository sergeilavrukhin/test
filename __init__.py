from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma
import os

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db, render_as_batch=True)

    from .group import bp_group
    from .user import bp_user
    from .groupuser import bp_groupuser
    from .subscribe import bp_subscribe
    app.register_blueprint(bp_group)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_groupuser)
    app.register_blueprint(bp_subscribe)
    return app