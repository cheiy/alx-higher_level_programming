#!/usr/bin/python3
"""
This module contains the model file for cities
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, ForeignKey, String


class City(Base):
    """
    City model class
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
