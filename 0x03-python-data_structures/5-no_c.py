#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i in range(len(s)):
        if s[i] in "cC":
            s[i] = ''
    return ''.join(s)
