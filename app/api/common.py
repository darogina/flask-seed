from flask import current_app, jsonify
from flask.views import MethodView
from flask_cors import cross_origin

from app.auth.auth import requires_auth


def json_converter(f):
    """Forces response to be JSON."""

    def decorator(*args, **kwargs):
        result = f(*args, **kwargs)

        return jsonify(result)

    return decorator


class PrivateAPIEndpoint(MethodView):
    # make converter run after every request handler method returns
    decorators = [json_converter,
                  requires_auth,
                  cross_origin(headers=['Content-Type', 'Authorization'])]

    def __init__(self, *args, **kwargs):
        super(PrivateAPIEndpoint, self).__init__(*args, **kwargs)
        self.logger = current_app.logger
