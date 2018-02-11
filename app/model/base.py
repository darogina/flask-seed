from marshmallow import Schema, fields
from sqlalchemy.sql import func

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_onupdate=func.now(), nullable=False, default=func.now())


class BaseModelSchema(Schema):
    id = fields.Integer()
    created_at = fields.Date()
    updated_at = fields.Date()
