#!/usr/bin/python3
""" Mylist Class """


class MyList(list):
    """ Mylist Class """
    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
