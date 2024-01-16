#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """

    __tablename__ = 'review'

    place_id = Column(String(1024), nullable=False)
    user_id = Column(String(60), ForeignKey="places.id", nullable=False)
    text = Column(String(60), ForeignKey="users.id", nullable=False)
