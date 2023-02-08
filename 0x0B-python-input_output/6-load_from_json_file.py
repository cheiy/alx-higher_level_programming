#!/usr/bin/python3
""" Module holds function that creates an Object from a
JSON file"""


def load_from_json_file(filename):
    """ Function creates an Object from a JSON file """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        _obj = json.load(f)
        return (_obj)
