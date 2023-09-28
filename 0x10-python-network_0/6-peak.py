#!/bin/bash
""" Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in an integers's list """
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    n = int(length / 2)
    list_i = list_of_integers

    if n - 1 < 0 and n + 1 >= length:
        return list_i[n]
    elif n - 1 < 0:
        return list_i[n] if list_i[n] > list_i[n + 1] else list_i[n +1]
    elif n + 1 >= length:
        return list_i[n] if list_i[n] > list_i[n - 1] else list_i [n - 1]
    if list_i[n - 1] < list_i[n] > list_i[n + 1]:
        return list_i[n]
    if list_i[n + 1] > list_i[n - 1]:
        return find_peak(list_i[n:])
    return find_peak(list_i[:n])
