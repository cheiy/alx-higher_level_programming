#!/usr/bin/python3
""" Module houses the lookup method """


def lookup(obj):
    """ Function reutns the list of available attributes and methods
    of an object """

    a_n_m = []

    a_n_m = dir(obj)

    return (a_n_m)
