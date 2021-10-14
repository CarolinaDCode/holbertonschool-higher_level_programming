#!/usr/bin/python3
"""Define a class called student"""


class Student:
    """constructor Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    retrieves a dictionary representation of student
    """
    def to_json(self):
        return self.__dict__
