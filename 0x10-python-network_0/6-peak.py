#!/bin/bash
""" Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in an integers's list """
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    i = int(length / 2)
    list_i = list_of_integers

    if i - 1 < 0 and i + 1 >= length:
        return list_i[i]
    elif i - 1 < 0:
        return list_i[i] if list_i[i] > list_i[i + 1] else list_i[i + 1]
    elif i + 1 >= length:
        return list_i[i] if list_i[i] > list_i[i - 1] else list_i [i - 1]
    if list_i[i - 1] < list_i[i] > list_i[i + 1]:
        return list_i[i]
    if list_i[i + 1] > list_i[i - 1]:
        return find_peak(list_i[i:])
    return find_peak(list_i[:i])
