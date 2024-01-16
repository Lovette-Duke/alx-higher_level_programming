#!/usr/bin/python3
""" This is the base model """


import json


class Base():
    """ This is the Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This initializes the id attribute """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON representation of list_dictionaries """
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of list_objs """
        file = cls.__name__ + '.json'
        with open(file, 'a') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    list_dict = [obj.to_dictionary()]
                f.write(Base.to_json_string(list_dict))
