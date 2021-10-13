#!/usr/bin/python3
"""Defines a function that adds arguments"""
import json


def load_from_json_file(filename):
    """
    funtion that add arguments to a python list and
    save them in to a file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
