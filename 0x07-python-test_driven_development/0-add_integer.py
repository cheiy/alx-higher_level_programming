#!/usr/bin/python3
def add_integer(a, b=98):
    """Function adds 2 integers"""

    try:
        if isinstance(a, (float, int)) is False:
            raise TypeError('a must be an integer')
        if isinstance(b, (float, int)) is False:
            raise TypeError('b must be an integer')
        if isinstance(a, float) is True:
            a = int(a)
        if isinstance(b, float) is True:
            b = int(b)
        return (a + b)
    except TypeError as err:
        print(err)
