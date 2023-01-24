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
            exit()
        except ValueError:
            print("{}".format("size must be >= 0"))
            exit()
