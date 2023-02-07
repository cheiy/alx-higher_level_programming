#!/usr/bin/python3
""" Module contains is_kind_of_class function that returns
True if the object passed is an instance of, or if the object is an
instance of a class that inherited from the specified class """


def is_kind_of_class(obj, a_class):
    """ Function returns true if obj is an instance of a_class or a_subclass"""

    if isinstance(obj, a_class) is True:
        if issubclass(a_class, a_class) is True:
            return True
    else:
        return False
