#!/usr/bin/python3
"""Define a function that reads a text file"""


def read_file(filename=""):
    """
    the function will read the text file(UTF8)
    and will print to the stdout.
    """
    with open(filename, encoding="utf-8") as f:
        f_content = f.read()
        print(f_content, end="")
