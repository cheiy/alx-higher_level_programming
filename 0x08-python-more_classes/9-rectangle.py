#!/usr/bin/python3
"""Module houses the Rectangle class"""


class Rectangle:
    """This is a class that defines a rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init method initializes width and height to 0

        Args:
            width (int): Initializes the width of the rectangle.
            height (int): Initializes the height of the rectangle.

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """See getter method above for this setter"""
        try:
            if isinstance(value, int) is False:
                raise TypeError('[TypeError] width must be an integer')
            if value < 0:
                raise ValueError('[ValueError] width must be >= 0')
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
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
                raise TypeError('[TypeError] height must be an integer')
            if value < 0:
                raise ValueError('[ValueError] height must be >= 0')
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
        else:
            self.__height = value

    def area(self):
        """Public method that returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Public instance method that returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """__str__ method prints rectangle as #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            ret = ""
            ret_len = 0
            i = j = 0
            while j < self.__height:
                while i < self.__width:
                    ret += "#"
                    i += 1
                if j == self.__height and i == self.__width:
                    ret += ""
                else:
                    ret += "\n"
                i = 0
                j += 1
            ret_len = len(ret)
            ret = ret[0:ret_len-1]
        return (ret)

    def __repr__(self):
        """The repr method for the class"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Object Deletion method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to find if two rects are equal"""
        err_msg = '[TypeError] rect_1 must be an instance of Rectangle'
        err_msg2 = '[TypError] rect_2 must be an instance of Rectangle'
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError(err_msg)
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError(err_msg2)
        if rect_1.area() < rect_2.area():
            return rect_2
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Method returns a new Rectangle instance with width=height=size"""
        Rectangle.__width = size
        Rectangle.__height = size
        new_rect = Rectangle(size, size)
        return (new_rect)
