#!/usr/bin/python3
""" This is module 1-write_file.py """


def write_file(filename="", text=""):
    """ writes a string to a text file in utf-8
        Return: number of characters writen
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
