#!/usr/bin/python3
""" This is the rectangle model """


from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialise the rectangle attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter decorated function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter decorated function for the x
            raises error if the x is not an int or if it is negative"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter decorated function for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter decorated function for the y
            raises error if the y is not an int or if it is negative"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This computes the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """ prints '#' to the stdout to display
        the dimensions of the rectangle """
        dim = ""
        for h in range(self.height):
            for w in range(self.width):
                dim += "#"
            if h < self.height - 1:
                dim += "\n"
        print(dim)
