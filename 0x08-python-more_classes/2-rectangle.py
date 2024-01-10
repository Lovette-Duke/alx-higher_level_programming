#!/usr/bin/python3
"""This is module 2-rectangle.py """


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

    def area(self):
        """ This computes the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ This computes the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2*self.width) + (2*self.height)
