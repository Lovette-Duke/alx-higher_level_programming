#!/usr/bin/python3
"""Task 6"""


class Square:
    """This is a square class with an int enforced size and an area
        Args:
            size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
        (not isinstance(value[0], int) and not isinstance(value[1], int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')

        for p in range(self.__position[1]):
            print('')

        for i in range(self.__size):
            for p in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end="")
            print('')
