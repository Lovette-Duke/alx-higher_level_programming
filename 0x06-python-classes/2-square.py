#!/usr/bin/python3
"""Task 2"""


class Square:
    """This is a square class with an int enforced size. """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
