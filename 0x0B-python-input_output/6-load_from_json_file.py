#!/usr/bin/python3
""" This is module 6-load_from_json_file.py """


import json


def load_from_json_file(filename):
    """ creats and object from a JSON file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
