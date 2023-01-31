#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """ Function prints the user's name """

    try:
        if isinstance(first_name, str) is False:
            raise TypeError('first_name must be a string')
        if isinstance(last_name, str) is False:
            raise TypeError('last_name must be a string')
        else:
            print("My name is {} {}".format(first_name, last_name))
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
