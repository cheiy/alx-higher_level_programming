#!/usr/bin/python3
"""Module houses the Rectangle class"""


class Rectangle:
    """This is a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ Init method initializes width and height to 0

        Args:
            width (int): Initializes the width of the rectangle.
            height (int): Initializes the height of the rectangle.

        """
        try:
            if isinstance(width, int) is False:
                raise TypeError('width must be an integer')
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width
            if isinstance(height, int) is False:
                raise TypeError('height must be an integer')
            if height < 0:
                raise ValueError('height must be >=0')
            self.__height = height
        except TypeError as err1:
            print(err1)
        except ValueError as err2:
            print(err2)

    @property
    def width(self):
        """int: Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """See getter method above for this setter"""
        try:
            if isinstance(value, int) is False:
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)

    @property
    def height(self):
        """int: Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set getter method above for this setter"""
        try:
            if isinstance(value, int) is False:
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
