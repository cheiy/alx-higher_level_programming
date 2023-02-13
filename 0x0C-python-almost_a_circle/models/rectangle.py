#!/usr/bin/python3
""" Module contains the Rectange class which inherits
from the Base class"""


from models import Base


class Rectangle(Base):
    """ The Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle"""
        self.__width = width

    @property
    def height(self, width):
        """Gets the height of the rectangle"""
        return self.__width

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle"""
        self.__height = height

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x"""
        self.__x = x

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the value of y"""
        self.__y = y
