#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cpy = my_list[::-1]
    for i in cpy:
        print("{:d}".format(i))
