#!/usr/bin/python3
""" Module houses Rectangle class which inherits from the
BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Integer validation method """
        if isinstance(value, int) is False:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """Instantiation of the values"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ Area method """
        raise Exception('area() is not implemented')
