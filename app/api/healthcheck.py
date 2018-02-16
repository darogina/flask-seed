from http import HTTPStatus

from flask import Blueprint, jsonify

from app import db

api_healthcheck_blueprint = Blueprint('api', __name__)


@api_healthcheck_blueprint.route('/health/', methods=['GET'])
def healthcheck():
    is_healthy = True
    http_status = HTTPStatus.OK
    try:
        with db.engine.connect() as db_connection:
            db_connection.execute('SELECT 1')
    except:
        is_healthy = False
        http_status = HTTPStatus.SERVICE_UNAVAILABLE

    return jsonify({'is_healthy': is_healthy, 'status': http_status}), http_status
