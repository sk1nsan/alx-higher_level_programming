#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        r = list(a_dictionary.values())[0]
        for x, y in a_dictionary.items():
            if y > r:
                r = y
        return r
    return None
