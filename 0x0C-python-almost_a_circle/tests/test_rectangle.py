#!/usr/bin/python3
"""Unittest for Base([..])
"""


import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testing Rectangle"""

    def test_width(self):
        r1 = Rectangle(20, 20)
        setattr(r1, "width", 50)
        self.assertEqual(r1.width, 50)
        self.assertRaises(ValueError, setattr, r1, "width", 0)
        self.assertRaises(ValueError, setattr, r1, "width", -100)
        self.assertRaises(TypeError, setattr, r1, "width", [])
        self.assertRaises(TypeError, setattr, r1, "width", [1])
        self.assertRaises(TypeError, setattr, r1, "width", None)
        self.assertRaises(TypeError, setattr, r1, "width", {})
        self.assertRaises(TypeError, setattr, r1, "width", {1: 2})
        self.assertRaises(TypeError, setattr, r1, "width", ())
        self.assertRaises(TypeError, setattr, r1, "width", (1,))
        self.assertRaises(TypeError, setattr, r1, "width", True)
        self.assertRaises(TypeError, setattr, r1, "width", "1")
        self.assertRaises(TypeError, setattr, r1, "width", {1, 2})

    def test_height(self):

        r1 = Rectangle(20, 20)
        setattr(r1, "height", 50)
        self.assertEqual(r1.height, 50)
        self.assertRaises(ValueError, setattr, r1, "height", 0)
        self.assertRaises(ValueError, setattr, r1, "height", -100)
        self.assertRaises(TypeError, setattr, r1, "height", [])
        self.assertRaises(TypeError, setattr, r1, "height", [1])
        self.assertRaises(TypeError, setattr, r1, "height", None)
        self.assertRaises(TypeError, setattr, r1, "height", {})
        self.assertRaises(TypeError, setattr, r1, "height", {1: 2})
        self.assertRaises(TypeError, setattr, r1, "height", ())
        self.assertRaises(TypeError, setattr, r1, "height", (1,))
        self.assertRaises(TypeError, setattr, r1, "height", True)
        self.assertRaises(TypeError, setattr, r1, "height", "1")
        self.assertRaises(TypeError, setattr, r1, "height", {1, 2})

    def test_x(self):

        r1 = Rectangle(20, 20)
        setattr(r1, "x", 50)
        self.assertEqual(r1.x, 50)
        setattr(r1, "x", 0)
        self.assertEqual(r1.x, 0)
        self.assertRaises(ValueError, setattr, r1, "x", -1)
        self.assertRaises(ValueError, setattr, r1, "x", -100)
        self.assertRaises(TypeError, setattr, r1, "x", [])
        self.assertRaises(TypeError, setattr, r1, "x", [1])
        self.assertRaises(TypeError, setattr, r1, "x", None)
        self.assertRaises(TypeError, setattr, r1, "x", {})
        self.assertRaises(TypeError, setattr, r1, "x", {1: 2})
        self.assertRaises(TypeError, setattr, r1, "x", ())
        self.assertRaises(TypeError, setattr, r1, "x", (1,))
        self.assertRaises(TypeError, setattr, r1, "x", True)
        self.assertRaises(TypeError, setattr, r1, "x", "1")
        self.assertRaises(TypeError, setattr, r1, "x", {1, 2})

    def test_y(self):

        r1 = Rectangle(20, 20)
        setattr(r1, "y", 50)
        self.assertEqual(r1.y, 50)
        setattr(r1, "y", 0)
        self.assertEqual(r1.y, 0)
        self.assertRaises(ValueError, setattr, r1, "y", -1)
        self.assertRaises(ValueError, setattr, r1, "y", -100)
        self.assertRaises(TypeError, setattr, r1, "y", [])
        self.assertRaises(TypeError, setattr, r1, "y", [1])
        self.assertRaises(TypeError, setattr, r1, "y", None)
        self.assertRaises(TypeError, setattr, r1, "y", {})
        self.assertRaises(TypeError, setattr, r1, "y", {1: 2})
        self.assertRaises(TypeError, setattr, r1, "y", ())
        self.assertRaises(TypeError, setattr, r1, "y", (1,))
        self.assertRaises(TypeError, setattr, r1, "y", True)
        self.assertRaises(TypeError, setattr, r1, "y", "1")
        self.assertRaises(TypeError, setattr, r1, "y", {1, 2})

    def test_area(self):
        r1 = Rectangle(20, 20)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(20, 1)
        r4 = Rectangle(20, 1)

        self.assertEqual(r1.area(), 400)
        self.assertEqual(r2.area(), 1)
        self.assertEqual(r3.area(), 20)
        self.assertEqual(r4.area(), 20)

    def test_display(self):
        r1 = Rectangle(2, 2)
        buf = io.StringIO()
        with redirect_stdout(buf):
            r1.display()
        r2 = Rectangle(2, 2, 1, 1)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            r2.display()
        self.assertEqual(buf2.getvalue(), "\n ##\n ##\n")
        r3 = Rectangle(2, 2, 0, 1)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            r3.display()
        self.assertEqual(buf3.getvalue(), "\n##\n##\n")
        r4 = Rectangle(2, 2, 1, 0)
        buf4 = io.StringIO()
        with redirect_stdout(buf4):
            r4.display()
        self.assertEqual(buf4.getvalue(), " ##\n ##\n")
        r5 = Rectangle(2, 2, 2, 2)
        buf5 = io.StringIO()
        with redirect_stdout(buf5):
            r5.display()
        self.assertEqual(buf5.getvalue(), "\n\n  ##\n  ##\n")

    def test_str(self):
        r1 = Rectangle(2, 2)
        buf = io.StringIO()
        with redirect_stdout(buf):
            print(r1)
        self.assertEqual(buf.getvalue(), "[Rectangle] (13) 0/0 - 2/2\n")
        r2 = Rectangle(5, 3, 9, 10, 100)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            print(r2)
        self.assertEqual(buf2.getvalue(), "[Rectangle] (100) 9/10 - 5/3\n")

    def test_update(self):
        r1 = Rectangle(2, 2)
        r1.update(102, 3, 5, 7, 10)
        buf = io.StringIO()
        with redirect_stdout(buf):
            print(r1)
        self.assertEqual(buf.getvalue(), "[Rectangle] (102) 7/10 - 3/5\n")
        r1.update(105)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            print(r1)
        self.assertEqual(buf2.getvalue(), "[Rectangle] (105) 7/10 - 3/5\n")
        r1.update(110, 10)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            print(r1)
        self.assertEqual(buf3.getvalue(), "[Rectangle] (110) 7/10 - 10/5\n")
        r1.update(112, 12, 13)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            print(r1)
        self.assertEqual(buf3.getvalue(), "[Rectangle] (112) 7/10 - 12/13\n")
        r1.update(114, 13, 14, 15)
        buf4 = io.StringIO()
        with redirect_stdout(buf4):
            print(r1)
        self.assertEqual(buf4.getvalue(), "[Rectangle] (114) 15/10 - 13/14\n")
        r1.update(x=150, y=70, id=140)
        buf5 = io.StringIO()
        with redirect_stdout(buf5):
            print(r1)
        self.assertEqual(buf5.getvalue(), "[Rectangle] (140) 150/70 - 13/14\n")
        r1.update(height=3)
        buf6 = io.StringIO()
        with redirect_stdout(buf6):
            print(r1)
        self.assertEqual(buf6.getvalue(), "[Rectangle] (140) 150/70 - 13/3\n")
        r1.update(height=151, y=112, id=107, x=9, width=80)
        buf7 = io.StringIO()
        with redirect_stdout(buf7):
            print(r1)
        self.assertEqual(buf7.getvalue(), "[Rectangle] (107) 9/112 - 80/151\n")
