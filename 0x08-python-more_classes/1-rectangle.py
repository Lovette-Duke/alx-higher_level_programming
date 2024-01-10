#!/usr/bin/python3
"""This is module 1-rectangle.py """


class Rectangle():
    """ This is a rectangle class """
    def __init__(self, width=0, height=0):
        """ initializes the width and height of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter decorated function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter decorated function for the width
            raises error if the width is not an int or if it is negative"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter decorated function for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter decorated function for the height
            raises error if the height is not an int or if it is negative"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
