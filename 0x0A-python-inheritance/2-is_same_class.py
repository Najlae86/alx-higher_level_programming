#!/usr/bin/python3
"""
this module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """returns true if the exact class a_class, otherwise false)"""
    return (type(obj) == a_class)
