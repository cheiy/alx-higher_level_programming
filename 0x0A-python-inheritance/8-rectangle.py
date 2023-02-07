#!/usr/bin/python3
""" Module houses Rectangle class """


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        integer_validator(self, "width", width)
        integer_validator(self, "height", height)

    def area(self):
        """ Area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Integer validation method """
        if isinstance(value, int) is False:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
