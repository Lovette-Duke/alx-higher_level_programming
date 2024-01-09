#!/usr/bin/python3
""" This is module 7-add_item.py 
    adds all arguments to a python list and saves to file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

try:
    list_json = load_from_json_file(filename)
except FileNotFoundError:
    list_json = []


save_to_json_file(list_json + argv[1:], filename)
