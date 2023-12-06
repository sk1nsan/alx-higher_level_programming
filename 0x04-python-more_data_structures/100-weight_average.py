#!/usr/bin/python3
def weight_average(my_list=[]):
    r = 0
    if my_list:
        w = 0
        for i, j in my_list:
            r += i * j
            w += j
        r /= w
    return r
