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
        """ Static metod that prints dictionaries as json"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        else:
            import json
            js = json.dumps(list_dictionaries)
            return js

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON string rep of list_objs"""
        new_list = []
        f_name = cls.__name__ + ".json"
        if list_objs is None:
            new_list.append(" ")
        for item in list_objs:
            new_list.append(item.to_dictionary())
        with open(f_name, "w") as f:
            f.write(cls.to_json_string(new_list))
