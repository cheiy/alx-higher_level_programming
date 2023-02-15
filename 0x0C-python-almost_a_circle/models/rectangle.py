#!/usr/bin/python3
""" Module contains the Base class """


from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle class which inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width"""
        self.width = width
        """if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height"""
        self.height = height
        """if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        else:
            if x <= 0:
                raise ValueError("x must be an integer")
            else:
                self.__x = x"""
        self.x = x
        """if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        else:
            if y <= 0:
                raise ValueError("y must be an integer")
            else:
                self.__y = y"""
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) is False:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, int) is False:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    def area(self):
        """ Method that returns the area of a rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """ Method prints a rectangle instance using # """
        a = b = i = j = 0
        for v in range(self.y):
            print("")
        for r in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def __str__(self):
        """ Overrides the __str__ method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self
                .__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Method assigns an argument to each attribute """
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.width = args[1]
        elif len(args) == 3:
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 4:
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 5:
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
