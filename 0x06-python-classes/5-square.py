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

    def area(self):
        """My first public instance method

        Returns:
            Area of the square.


        """
        try:
            area = self.__size * self.__size
            if isinstance(self.__size, int) is False:
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except TypeError:
            print("{}".format("size must be an integer"))
            exit()
        except ValueError:
            print("{}".format("size myst be >= 0"))
            exit()
        else:
            return area

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
        """try:
            self.__size = value
            if isinstance(int, value) is not True:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("{}".format("size must be an integer"))
        except ValueError:
            print("{}".format("size must be >= 0"))"""
        self.__size = value

    def my_print(self):
        """Public instance method that prints the square

        Returns:
            Nothing.


        """
        if self.size == 0:
            print()
        else:
            i = j = 0
            while i < self.__size:
                while j < self.__size:
                    print("{}".format("#"), end="")
                    j += 1
                print()
                i += 1
                j = 0
