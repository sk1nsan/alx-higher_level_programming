#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        r = 0
        for x in a_dictionary.keys():
            if a_dictionary[x] > r:
                r = a_dictionary[x]
        return r
