#!/usr/bin/python3
""" Module holds function that returns the JSON represenation of a
string object """


def to_json_string(my_obj):
    """ Function retusn the JSON representation of a string object"""
    import json
    return (json.dumps(my_obj))
