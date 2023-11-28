#!/usr/bin/python3
def remove_char_at(str, n):
    s = list(str)
    if n >= 0 and n < len(str):
        s[n] = ''
    return ''.join(s)
