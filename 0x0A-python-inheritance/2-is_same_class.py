#!/usr/bin/python3
""" Module contains is_same_class function that returns
True if the object passed is exactly an instance of the
specified class """


def is_same_class(obj, a_class):
    """ Function returns true if obj is an instance of a_class"""

    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
