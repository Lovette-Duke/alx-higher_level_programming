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
        dim = ''
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                dim += ' '
            for w in range(self.width):
                dim += '#'
            if h < self.height - 1:
                dim += "\n"
        print(dim)

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """sets attributes in order """
        if args:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                elif a == 1:
                    self.width = args[1]
                elif a == 2:
                    self.height = args[2]
                elif a == 3:
                    self.x = args[3]
                elif a == 4:
                    self.y = args[4]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
