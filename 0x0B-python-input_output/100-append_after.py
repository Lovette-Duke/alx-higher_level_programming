#!/usr/bin/python3
""" This is module 100-append_after.py """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text after each line """
    with open(filename, "r+", encoding='utf-8') as file:
        text = ''
        for line in file:
            text += line

            if search_string in line:
                text += new_string

        file.seek(0)
        file.write(text)
