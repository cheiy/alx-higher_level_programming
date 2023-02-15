#!/usr/bin/python3
""" Module contains the Base class """


class Base:
    """ Defines the Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            import json
            js = json.dumps(list_dictionaries)
            return js
