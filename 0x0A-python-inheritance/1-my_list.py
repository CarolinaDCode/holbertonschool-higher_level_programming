#!/usr/bin/python3
"""
module containing class mylist
"""


class MyList(list):
    """
    this method print a sorted list
    """
    def print_sorted(self):
        print(sorted(self))
