#!/usr/bin/python3
def text_indentation(text):
    """ Function prints a text with 2 new lines after each of
    these characters: . , ? and : """

    try:
        prev_char = ""
        i = 0
        special_chars = ['.', '?', ':']
        if isinstance(text, str) is False:
            raise TypeError('text must be a string')
        for char in text:
            if char in special_chars:
                print(char)
                print()
            elif char.isupper() is False:
                print(char, end="")
            else:
                print(char, end="")
        print()
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
