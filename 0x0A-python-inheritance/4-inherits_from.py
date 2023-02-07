#!/usr/bin/python3
""" Module houses inherits_from method """


def inherits_from(obj, a_class):
    """ Function returns True if the object is an instance of
    a class that inherited from the specified class """
    if isinstance(obj, a_class) is True:
        if issubclass(a_class, a_class):
            return True
    else:
        return False
