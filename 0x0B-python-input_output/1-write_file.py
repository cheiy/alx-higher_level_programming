#!/usr/bin/python3
""" Module holds a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ Function writes a string to a text file and returns
    number of chars writte"""
    with open(filename, "w", encoding="utf-8") as f:
        chars_written = f.write(text)
    return chars_written
