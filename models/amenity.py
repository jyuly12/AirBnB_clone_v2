#!/usr/bin/python3
""" State Module for HBNB project """


from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    """class amenity"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secundary="place_amenity")
