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
            list_objs = []
        for item in list_objs:
            new_list.append(item.to_dictionary())
        with open(f_name, "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Method returns the list of the json string representation
        json_string"""
        if json_string is None:
            return []
        import json
        str_json = json.loads(json_string)
        return (str_json)

    @classmethod
    def create(cls, **dictionary):
        """ Method that returns an instance with all attributes already
        set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            dummy = cls(1, 0, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Method returns a list of instances """
        f_name = cls.__name__ + ".json"
        instances = []
        try:
            with open(f_name, 'r') as f:
                for instance in cls.from_json_string(f.read()):
                    instances.append(cls.create(**instance))
        except Exception as e:
            pass
        return (instances)
