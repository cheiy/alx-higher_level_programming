#!/usr/bin/python3
""" Module houses the add_integer function """


def add_integer(a, b=98):
    """Function adds 2 integers"""

    try:
        if isinstance(a, (float, int)) is False:
            raise TypeError('a must be an integer')
        else:
            a = int(a)
        if isinstance(b, (float, int)) is False:
            raise TypeError('b must be an integer')
        else:
            b = int(b)
        return (a + b)
    except TypeError as err:
        print(err)
        exit()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
