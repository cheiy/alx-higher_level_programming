#!/usr/bin/python3
""" Module houses Square class which inherits from the
Rectangle class """


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
        area = self.__width * self.__height

        return area

    def __str__(self):
        """ __str__ dunder method """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Instantiation of the objects """
        self.__width = size
        self.__height = size
        super().integer_validator("size", self.__width)
        super().integer_validator("size", self.__height)

    def area(self):
        """ Area of square method """
        area = self.__width * self.__height
        return area

    def __str__(self):
        """ __str__ dunder method """
        return ("[Square] {}/{}".format(self.__width, self.__height))
