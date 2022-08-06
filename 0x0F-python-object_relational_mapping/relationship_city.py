#!/usr/bin/python3
"""City model with foreign key"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

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
    name = Column(**_name)
    state_id = Column(*args, **_state_id)
