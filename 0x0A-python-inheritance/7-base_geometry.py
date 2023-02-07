#!/usr/bin/python3
""" Module houses BaseGeometry class """


class BaseGeometry:
    """ BaseGeometry class """

    def __init__(self, name="", value=0):
        self.name = name
        self.value = value

    def area(self):
        """ Area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Integer validation method """
        if isinstance(value, int) is False:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
