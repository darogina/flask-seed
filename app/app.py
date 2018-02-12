import importlib
import logging
import os

from flask import Flask
from flask_cors import CORS

import config
from app import commands, db, migrate, ROOT_PROJECT_DIR

# from app.model.example import Example
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.bcrypt import Bcrypt
# from flask.ext.login import LoginManager
# from .errors import ErrorHandler


# bcrypt = Bcrypt()
# login_manager = LoginManager()

MODEL_DIRS = [
    'model',
    'model.inner_package'
]

MODEL_EXCLUDE_FILES = [
    '__init__.py',
]


def scan_models():
    for dirpath, dirnames, filenames in os.walk('.'):
        head, tail = os.path.split(dirpath)
        if tail in MODEL_DIRS:
            # there should be models
            for filename in filenames:
                if filename.endswith('.py') and \
                        filename not in MODEL_EXCLUDE_FILES:
                    # lets import the module
                    filename_no_ext, _ = os.path.splitext(
                        os.path.join(
                            dirpath, filename
                        )
                    )
                    # remove first . character
                    filename_no_ext = filename_no_ext[2:]
                    module_path = filename_no_ext.replace(os.sep, '.')
                    importlib.import_module(module_path)


CONFIGS = {
    'local': config.LocalConfig,
    'dev': config.DevelopmentConfig,
    'prod': config.ProductionConfig,
    'test': config.TestConfig
}


def create_app(env=None):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/.
        :param env: The configuration object to use.
        """
    app = Flask(__name__, static_folder=None, instance_path=os.path.join(ROOT_PROJECT_DIR, 'instance'))

    setup_config(app, env)

    if app.config.get('LOG_LEVEL') is not None:
        print('Setting Log Level to %s' % (app.config.get('LOG_LEVEL')))
        logging.basicConfig(level=logging.getLevelName(app.config.get('LOG_LEVEL')))

    # scan_models()
    from .model import import_models
    import_models()

    db.app = app
    db.init_app(app)

    migrate.init_app(app=app, db=db)

    # populated regions table required for adverts form. Must be imported
    # before blueprints
    # from data.generator import Generator
    # generator = Generator()
    # generator.create_regions()
    #
    # bcrypt.init_app(app)
    # login_manager.init_app(app)
    #
    # if not app.debug:
    #     ErrorHandler(app)

    register_commands(app)

    load_blueprints(app)

    CORS(app)

    return app


def setup_config(app, env):
    if env is None or env not in CONFIGS:
        raise Exception('Error: Could not locate application config. Make sure environment variable {}_CONFIG '
                        'is set or an environment name is passed in to app.create_app()'.format(config.ENVIRON_PREFIX))
    _config = CONFIGS[env]

    # Load the default configuration
    app.config.from_object(_config)

    # app.config.from_object(config)

    # Load the configuration from the instance folder
    app.config.from_pyfile(os.path.join(app.instance_path, 'config_override.py'), silent=True)

    # Load the file specified by the APP_CONFIG environment variable
    # Variables defined here will override those in the default configuration
    # app.config.from_envvar('APP_CONFIG')


def _initialize_errorhandlers(app):
    from flask import jsonify
    from werkzeug.exceptions import default_exceptions, InternalServerError

    def _handle_http_exception(error):
        """JSON Exceptions"""
        status_code = error.code if hasattr(error, 'code') else 500
        description = error.description if hasattr(error, 'description') else InternalServerError.description
        return jsonify({
            'code': status_code,
            'message': str(error),
            'description': description
        }), status_code

    # Catch all exceptions
    app.register_error_handler(Exception, _handle_http_exception)

    # Catch all HTTPExceptions
    for code, ex in default_exceptions.items():
        app.errorhandler(code)(_handle_http_exception)


def _initialze_api_versions(app):
    from app.api.v1.views import api_blueprint as api_v1_blueprint
    # from .oauth.views import oauth_blueprint
    # from .pages.views import pages_blueprint

    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
    # app.register_blueprint(oauth_blueprint, url_prefix='/oauth')
    # app.register_blueprint(pages_blueprint)


def load_blueprints(app):
    """Load blueprints."""
    _initialize_errorhandlers(app)
    _initialze_api_versions(app)


def register_commands(app):
    """Register Click commands."""
    # app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
    app.cli.add_command(commands.create_db)
