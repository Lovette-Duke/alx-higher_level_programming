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