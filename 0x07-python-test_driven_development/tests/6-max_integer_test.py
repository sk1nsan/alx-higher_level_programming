#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-2, 0, -100 , -1250 ,-999999]), 0)
