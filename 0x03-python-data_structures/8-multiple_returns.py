#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        res1 = (0, None)
        return res1
    else:
        res2 = (length, sentence[0:1])
        return res2
