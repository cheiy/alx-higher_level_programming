#!/usr/bin/python3
""" Module contains the Base class """


class Base:
    """ Defines the Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """ Defines the Rectangle class which inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        self.__y = y
