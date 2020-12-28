from flask import Flask

from lab.config import Config
from lab.db import db


def create_app(test_config=None):
    app = Flask(__name__)

    # load config
    app.config.from_object(Config)


    configure_database(app)

    return app


def configure_database(app):
    engine_opts = app.config.get("SQLALCHEMY_ENGINE_OPTIONS", {})

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = engine_opts

    db.init_app(app)  # init sqlalchemy
