#!/usr/bin/python3
def print_square(size):
    """ Function prints a square with the character #. """

    try:
        i = j = 0
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        while i < size:
            while j < size:
                print('#', end="")
                j += 1
            print()
            j = 0
            i += 1
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
