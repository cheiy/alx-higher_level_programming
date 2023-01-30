#!/usr/bin/python3
"""Module houses the Rectangle class"""


class Rectangle:
    """This is a class that defines a rectangle"""

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
        except TypeError as err:
            print(err)
            exit()
        except ValueError as err:
            print(err)
            exit()
        else:
            self.__width = value

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
        except TypeError as err:
            print(err)
            exit()
        except ValueError as err:
            print(err)
            exit()
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """ Init method initializes width and height to 0

        Args:
            width (int): Initializes the width of the rectangle.
            height (int): Initializes the height of the rectangle.

        """
        self.height = height
        self.width = width
