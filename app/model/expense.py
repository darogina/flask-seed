from marshmallow import pre_load, post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Expense(Transaction):
    __mapper_args__ = {
        'polymorphic_identity': TransactionType.EXPENSE.value
    }

    def __repr__(self):
        return '<Expense(name={self.description!r})>'.format(self=self)


class ExpenseSchema(TransactionSchema):
    @pre_load
    def negate_amount(self, in_data):
        if in_data['amount'] > 0:
            in_data['amount'] = 0 - abs(in_data['amount'])
        return in_data

    @post_load
    def make_expense(self, data):
        return Expense(**data)
