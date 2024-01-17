#!/usr/bin/python3
""" This is the base model """


import json
import os


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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of list_objs """
        file = cls.__name__ + '.json'
        with open(file, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of a JSON string representation """
        if json_string is None:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create an instance and sets all its attributes """
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        file = cls.__name__ + ".json"
        list_inst = []
        if os.path.exists(file):
            with open(file, 'r') as f:
                content = f.read()
                if content:
                    inst = cls.from_json_string(content)
                    for k, v in enumerate(inst):
                        list_inst.append(cls.create(**inst[k]))
        return list_inst
