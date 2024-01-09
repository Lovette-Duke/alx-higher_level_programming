#!/usr/bin/python3
""" This is module 5-save_to_json_file.py """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a test file using json representation """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
