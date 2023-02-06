#!/usr/bin/python3
""" Module houses class MyList """


class MyList(list):
    """ Class inherits from the list class """
    """
    def __init__(self, some_list=[]):
        super().__init__(int(item) for item in some_list)

    def append(self, item):
        super().append(int(item))
    """
    def print_sorted(self):
        """ Method prints a list, but sorted in ascending
        order"""

        new_list = self[:]
        new_list.sort()
        print(new_list)
