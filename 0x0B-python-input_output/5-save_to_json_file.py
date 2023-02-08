#!/usr/bin/python3
""" Module holds function that writes an Object to a text file
using a JSON representation """


def save_to_json_file(my_obj, filename):
    """ Function writes an Object to a text file using JSON representation """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
