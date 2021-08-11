#!/usr/bin/python3
"""Defines the DBStorage class"""
import json
from os import environ

from models.base_model import BaseModel, Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

classes = ["User", "State", "City", "Amenity", "Place", "Review"]


class DBStorage:
    """This class serializes/deserializes instances to a JSON file"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialice DBStorage paramethers"""

        engine_str = "mysql+mysqldb://{}:{}@{}/{}".format(
            environ.get("HBNB_MYSQL_USER"),
            environ.get("HBNB_MYSQL_PWD"),
            environ.get("HBNB_MYSQL_HOST"),
            environ.get("HBNB_MYSQL_DB"))

        self.__engine = create_engine(engine_str, pool_pre_ping=True)

        if environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return a list of objects"""

        query = []
        new_dict = {}
        if cls:
            query = self.__session.query(eval(cls)).all()
            for item in query:
                key = "{}.{}".format(item.__class__.__name__, item.id)
                new_dict[key] = item
        else:
            for class_name in classes:
                query = (self.__session.query(eval(class_name)).all())
                for item in query:
                    key = "{}.{}".format(item.__class__.__name__, item.id)
                    new_dict[key] = item

        return new_dict

    def new(self, obj):
        """Add a object"""
        self.__session.add(obj)

    def save(self):
        """Save changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete te current object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)()
