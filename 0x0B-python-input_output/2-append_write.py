#!/usr/bin/python3
"""Defines a function that appends text to a text file"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f_content = f.write(text)
        return f_content
