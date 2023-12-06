#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        r = list(a_dictionary.keys())[0]
        for x, y in a_dictionary.items():
            if y > a_dictionary[r]:
                r = x
        return r
