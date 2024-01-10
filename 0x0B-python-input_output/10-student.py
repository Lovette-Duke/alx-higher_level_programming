#!/usr/bin/python3
""" This is module 10-student.py """


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
        elif attrs is None:
            return self.__dict__
