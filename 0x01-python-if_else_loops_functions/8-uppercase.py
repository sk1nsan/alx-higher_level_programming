#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i.islower():
            i = chr(ord(i) - 32)
        print(i, end="")
    print()
