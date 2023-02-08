#!/usr/bin/python3
""" Module holds function that returns an object represented
by a JSON string """


def from_json_string(my_str):
    """ Function returns an object represented by a JSON string """
    import json
    return (json.loads(my_str))
