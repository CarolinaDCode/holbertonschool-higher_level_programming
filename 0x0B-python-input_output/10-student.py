#!/usr/bin/python3
"""Define a class called student"""


class Student:
    """constructor Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    Retrieves a dictionary
    representation of a Student instance
    """
    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(j) is str for j in attrs):
            dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__
