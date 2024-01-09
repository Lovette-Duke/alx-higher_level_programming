#!/usr/bin/python3
""" This is module 8-class_to_json.py """


def class_to_json(obj):
    """ Return:
            dictionary description of a data structure
            for JSON serialization of an object
    """
    return obj.__dict__
