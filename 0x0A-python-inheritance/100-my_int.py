#!/usr/bin/python3
""" Module houses MyInt class"""


class MyInt(int):
    """ Class that inherits from int """

    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return (str(self.__num))

    def __eq__(self, num):
        return False

    def __ne__(self, num):
        return True
