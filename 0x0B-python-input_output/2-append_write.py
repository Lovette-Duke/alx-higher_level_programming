#!/usr/bin/python3
""" This is module 2-append_write.py """


def append_write(filename="", text=""):
    """ appends to a text file
        Return: number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
