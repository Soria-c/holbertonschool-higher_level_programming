#!/usr/bin/python3
"""City model"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

_id = {
    'name': 'id',
    'type_': Integer,
    'primary_key': True,
    'autoincrement': 'auto',
    'nullable': False
}
_name = {
    'name': 'name',
    'nullable': False,
    'type_': String(128)
}
_state_id = {
    'name': 'state_id',
    'type_': Integer,
    'nullable': False
}
args = [ForeignKey('states.id', ondelete='CASCADE')]


class City(Base):
    """City model"""
    __tablename__ = 'cities'
    id = Column(**_id)
    state_id = Column(*args, **_state_id)
    name = Column(**_name)
    relationship('State', backref='cities')
