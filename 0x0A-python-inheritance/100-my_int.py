#!/usr/bin/python3
""" MyInt  """


class MyInt(int):
    """ MyInt  """
    def __eq__(self, otherint):
        """ Equality method  """
        return int.__ne__(self, otherint)

    def __ne__(self, otherint):
        """ Inequality method  """
        return int.__eq__(self, otherint)
