#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, relationship


class Amenity(BaseModel):
    """Amneity model"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # place_amenities = relationship('Place', ba
