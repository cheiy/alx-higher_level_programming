#!/usr/bin/python3
""" Module contains the Base class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Constructor method """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ The __str__ overloading method"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.size))

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value
