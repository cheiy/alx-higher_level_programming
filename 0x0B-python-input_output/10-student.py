#!/usr/bin/python3
""" Module holds Student class definition """


class Student:
    """ Defines the Student class"""
    def __init__(self, first_name, last_name, age):
        """ Instantiation method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, str):
            return (attrs)
        else:
            return (self.__dict__)
