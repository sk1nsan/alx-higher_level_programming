#!/usr/bin/python3
"""Unittest for Base([..])
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ testing Base """
    def test_id(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)
