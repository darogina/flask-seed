from decimal import ROUND_UP
from marshmallow import fields
from app import db
from .base import BaseModel, BaseModelSchema


class Transaction(BaseModel):
    __tablename__ = 'transaction'

    description = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(precision=2), nullable=False)
    type = db.Column(db.String, index=True, nullable=False)

    __mapper_args__ = {
        'polymorphic_on': type
    }

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(BaseModelSchema):
    description = fields.Str(required=True)
    amount = fields.Decimal(places=2, rounding=ROUND_UP, required=True)
    type = fields.Str()
