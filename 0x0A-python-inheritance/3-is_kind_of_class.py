#!/usr/bin/python3
"""
contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """true if obj is an instance or inherited from a_class, else false"""
    return (isinstance(obj, a_class))
