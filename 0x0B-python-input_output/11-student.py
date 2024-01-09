#!/usr/bin/python3
""" This is module 11-student.py """


class Student():
    """ Student class with attributes and a public method
        to retrive a dict representation of an instance
    """
    def __init__(self, first_name, last_name, age):
        """ initialise the attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrives a dict representation of an instance """
        if attrs:
            attr = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    attr[i] = self.__dict__[i]
            return attr
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attribute of the class """
        for key, value in json.items():
            setattr(self, key, value)
