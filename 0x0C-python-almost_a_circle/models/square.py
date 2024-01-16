#!/usr/bin/python3
""" This is the Square Model """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialises the square attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <size> """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ The getter decorted size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ The setter function for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ defines args and keyword args for the square attributes """
        if args:
            for a in range(len(args)):
                if a == 0:
                    self.id = args[0]
                elif a == 1:
                    self.size = args[1]
                elif a == 2:
                    self.x = args[2]
                elif a == 3:
                    self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
