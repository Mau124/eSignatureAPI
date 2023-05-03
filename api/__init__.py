import os

from flask import Flask
from . import routes

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(test_config)

    app.register_blueprint(routes.blueprint)

    if test_config is None:
        # Load the instance config, if it exits, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app