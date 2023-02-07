#!/usr/bin/python3
""" Module holds function that reads a text file """


def read_file(filename=""):
    """ Function reads a text file """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    print(data, end="")
