from flask import jsonify, request

from app.api.common import PrivateAPIEndpoint
from app.service import money_service


class IncomeAPI(PrivateAPIEndpoint):
    def get(self, income_id=None):
        self.logger.debug('Getting Incomes')

        if income_id:
            return ""
        else:
            return money_service.get_incomes()

    def post(self):
        data = request.get_json()
        money_service.add_income(data['amount'], data['description'])
        return "", 204


class ExpenseAPI(PrivateAPIEndpoint):
    def get(self, expense_id=None):
        self.logger.debug('Getting Expenses')

        if expense_id:
            return ""
        else:
            return money_service.get_expenses()

    def post(self):
        data = request.get_json()
        money_service.add_expense(data['amount'], data['description'])
        return "", 204
