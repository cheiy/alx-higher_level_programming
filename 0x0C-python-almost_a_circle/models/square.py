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

    def update(self, *args, **kwargs):
        """ Method assigns attributes """
        if args:
            if len(args) == 1:
                id = args[0]
            elif len(args) == 2:
                id = args[0]
                size = args[1]
            elif len(args) == 3:
                id = args[0]
                size = args[1]
                x = args[2]
            elif len(args) == 4:
                id = args[0]
                size = args[1]
                x = args[2]
                y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
