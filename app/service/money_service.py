from app import db
from app.model.expense import Expense, ExpenseSchema
from app.model.income import Income, IncomeSchema


def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(Income.query.all())
    return incomes.data


def add_income(amount, description):
    income = IncomeSchema().load({'amount': amount, 'description': description})
    db.session.add(income.data)
    db.session.commit()


def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(Expense.query.all())
    return expenses.data


def add_expense(amount, description):
    expense = ExpenseSchema().load(amount=amount, description=description)
    db.session.add(expense.data)
    db.session.commit()
