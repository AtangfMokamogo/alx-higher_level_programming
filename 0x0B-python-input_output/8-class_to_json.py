#!/usr/bin/python3
"""
This function returns dictionary defination for JSON serialisation of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    tmp = {}
    if hasattr(obj, "__dict__"):
        tmp = obj.__dict__.copy()
    return tmp
