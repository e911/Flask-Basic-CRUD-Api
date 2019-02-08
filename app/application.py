import logging
import os

from flask import Flask
from werkzeug.utils import import_string
from . import config, db, io, bcrypt


logger = logging.getLogger(__name__)


def create_app(config_obj):
    """Creates a new Flask application and initialize application."""

    app = Flask(__name__, static_folder="../static/dist", template_folder="../static")
    app.config.from_object(config_obj)
    app.url_map.strict_slashes = False
    app.add_url_rule('/', 'home', home)

    register_blueprints(app)

    db.init_app(app)
    io.init_app(app)
    bcrypt.init_app(app)

    return app


def home():
    return dict(name='Cool, you have Flask App running !!!')


def register_blueprints(app):
    root_folder = 'app'

    for dir_name in os.listdir(root_folder):
        module_name = root_folder + '.' + dir_name + '.views'
        module_path = os.path.join(root_folder, dir_name, 'views.py')

        if os.path.exists(module_path):
            module = import_string(module_name)
            obj = getattr(module, 'app', None)
            if obj:
                app.register_blueprint(obj)
