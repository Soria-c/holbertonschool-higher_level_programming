#!/usr/bin/python3
"""Script to create a model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


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
Base = declarative_base()


class State(Base):
    """State model"""
    __tablename__ = 'states'
    id = Column(**_id)
    name = Column(**_name)
