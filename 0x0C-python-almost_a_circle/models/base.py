#!/usr/bin/python3
""" This is the base model """


import json
import os
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes a csv file """
        file = cls.__name__ + '.csv'
        with open(file, 'w', newline='') as f:
            write = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == 'Square':
                    write.writerow([obj.id, obj.size, obj.x, obj.y])
                if cls.__name__ == 'Rectangle':
                    write.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes a csv file """
        objects = []
        file = cls.__name__ + '.csv'
        with open(file, 'r') as f:
            read = csv.reader(f)
            for line in read:
                if cls.__name__ == 'Square':
                    inst_dic = {'id': int(line[0]), 'size': int(line[1]),
                                'x': int(line[2]), 'y': int(line[3])}
                if cls.__name__ == 'Rectangle':
                    inst_dic = {'id': int(line[0]),
                                'width': int(line[1]), 'height': int(line[2]),
                                'x': int(line[3]), 'y': int(line[4])}
                obj = cls.create(**inst_dic)
                objects.append(obj)
        return objects
