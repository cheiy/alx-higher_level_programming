#!/usr/bin/python3
"""Module houses one class that defines a square."""


class Square():
    """Class Square defines a square"""
    def __init__(self, size=0):
        """Init method that instantiates __size__ with None


        Args:
            size (:obj: `int`): The size of the square.

        """
        try:
            self.__size = size
            if isinstance(size, int) is False:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("{}".format("size must be an integer"))
        except ValueError:
            print("{}".format("size must be >= 0"))

    def area(self):
        """My first public instance method

        Returns:
            Area of the square.


        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method for size

        Returns:
            The size of the square.


        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method of size

        Returns:
            Nothing.


        """
        try:
            self.__size = value
            if isinstance(int, value) is not True:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("{}".format("size must be an integer"))
        except ValueError:
            print("{}".format("size must be >= 0"))
