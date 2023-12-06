#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = a_dictionary
    if a:
        for i in range(len(a_dictionary)):
            print("{}: {}".format(sorted(a)[i], a[sorted(a)[i]]))
