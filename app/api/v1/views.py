from flask import Blueprint, current_app, jsonify, redirect, request
from flask_cors import cross_origin
from werkzeug.local import LocalProxy

from app.auth.auth import requires_auth, requires_scope, AuthError

import app.service.money_service as money_service

api_blueprint = Blueprint(
    'api.v1', __name__
)

LOG = LocalProxy(lambda: current_app.logger)

# @api_blueprint.route("/api/v1/")
# # @cross_origin(headers=['Content-Type', 'Authorization'])
# def index():
#     return redirect('/incomes/')


@api_blueprint.route("/incomes/", methods=['GET'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def get_incomes():
    LOG.debug('Getting Incomes')
    return money_service.get_incomes()


@api_blueprint.route('/incomes', methods=['OPTIONS', 'POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def add_income():
    data = request.get_json()
    money_service.add_income(data['amount'], data['description'])
    return "", 204


@api_blueprint.route("/expenses/")
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def get_expenses():
    from werkzeug.exceptions import BadRequest
    raise Exception('blah')
    return money_service.get_expenses()


@api_blueprint.route('/expenses', methods=['POST'])
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def add_expense():
    data = request.get_json()
    money_service.add_expense(data['amount'], data['description'])
    return "", 204


@api_blueprint.route("/api/private-scoped")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private_scoped():
    """A valid access token and an appropriate scope are required to access this route
    """
    if requires_scope("read:messages"):
        response = "All good. You're authenticated and the access token has the appropriate scope."
        return jsonify(message=response)
    raise AuthError({
        "code": "Unauthorized",
        "description": "You don't have access to this resource."
    }, 403)
