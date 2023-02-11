#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ instantiate  Basemodel class """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of an object
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of
        of the instance:
        only instance attributes set will be returned by using self.__dict__
        a key __class__ must be added to this dictionary
        with the class name of the object
        created_at and updated_at converted to string object in ISO format
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
