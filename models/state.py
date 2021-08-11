#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """
        return the cities with the same state_id
        """
        list_cities_state_id = []
        all_cities = models.storage.all(City)
        for value in all_cities.values():
            if value.state_id == self.id:
                list_cities_state_id.append(value)
        return list_cities_state_id
