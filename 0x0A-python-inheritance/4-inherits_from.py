#!/usr/bin/python3
""" This is module 4-inherits_from.py """


def inherits_from(obj, a_class):
    """
    Return:
    True if object is instance of a class inherited from specified class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
