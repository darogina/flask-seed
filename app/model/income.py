from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType


class Income(Transaction):

    __mapper_args__ = {
        'polymorphic_identity': TransactionType.INCOME.value
    }

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data):
        return Income(**data)
