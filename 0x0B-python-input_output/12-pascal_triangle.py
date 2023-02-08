#!/usr/bin/python3
""" Module contains pascal_triangle function"""


def pascal_triangle(n):
    """ Function returns a list of integers representing the
    Pascal's triangle of n"""
    ls = []
    if n <= 0:
        return ls
    else:
        while n > 0:
            ls.append(str(n))
            n -= 1
        return (ls)
