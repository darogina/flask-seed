from .base import api_blueprint
from .transactions import IncomeAPI, ExpenseAPI

# Route URLs
api_blueprint.add_url_rule('/incomes/', view_func=IncomeAPI.as_view('incomes'))
api_blueprint.add_url_rule('/expenses/', view_func=ExpenseAPI.as_view('expenses'))
