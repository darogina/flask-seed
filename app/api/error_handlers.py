from flask import jsonify
from werkzeug.exceptions import HTTPException


def handle_http_exception(error):
    code = error.code if isinstance(error, HTTPException) else 500
    # if request.is_json:
    return jsonify({
        'status_code': code,
        'message': str(error),
        'description': error.description
    }), code

