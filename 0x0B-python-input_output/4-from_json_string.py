#!/usr/bin/python3
""" This is module 4-from_json_string.py """


import json


def from_json_string(my_str):
    """ returns an object in JSON string format """
    return json.loads(my_str)
