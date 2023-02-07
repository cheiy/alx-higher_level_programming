#!/usr/bin/python3
""" Module holds function that appends a string at the end of a text
file and returns the number of chars added """


def append_write(filename="", text=""):
    """ Function appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        chars_added = f.write(text)
    return chars_added
