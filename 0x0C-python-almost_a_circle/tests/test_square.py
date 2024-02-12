#!/usr/bin/python3
"""Unittest for Square([..])
"""


import unittest
import io
from contextlib import redirect_stdout
from models.square import Square
from models.square import Square


class TestSquare(unittest.TestCase):
    """testing Square"""

    def test_width(self):
        s1 = Square(20, 20, 20, 217)
        setattr(s1, "width", 50)
        self.assertEqual(s1.width, 50)
        self.assertRaises(ValueError, setattr, s1, "width", 0)
        self.assertRaises(ValueError, setattr, s1, "width", -100)
        self.assertRaises(TypeError, setattr, s1, "width", [])
        self.assertRaises(TypeError, setattr, s1, "width", [1])
        self.assertRaises(TypeError, setattr, s1, "width", None)
        self.assertRaises(TypeError, setattr, s1, "width", {})
        self.assertRaises(TypeError, setattr, s1, "width", {1: 2})
        self.assertRaises(TypeError, setattr, s1, "width", ())
        self.assertRaises(TypeError, setattr, s1, "width", (1,))
        self.assertRaises(TypeError, setattr, s1, "width", True)
        self.assertRaises(TypeError, setattr, s1, "width", "1")
        self.assertRaises(TypeError, setattr, s1, "width", {1, 2})

    def test_size(self):
        s1 = Square(20, 20, 20, 217)
        setattr(s1, "size", 50)
        self.assertEqual(s1.size, 50)
        self.assertRaises(ValueError, setattr, s1, "size", 0)
        self.assertRaises(ValueError, setattr, s1, "size", -100)
        self.assertRaises(TypeError, setattr, s1, "size", [])
        self.assertRaises(TypeError, setattr, s1, "size", [1])
        self.assertRaises(TypeError, setattr, s1, "size", None)
        self.assertRaises(TypeError, setattr, s1, "size", {})
        self.assertRaises(TypeError, setattr, s1, "size", {1: 2})
        self.assertRaises(TypeError, setattr, s1, "size", ())
        self.assertRaises(TypeError, setattr, s1, "size", (1,))
        self.assertRaises(TypeError, setattr, s1, "size", True)
        self.assertRaises(TypeError, setattr, s1, "size", "1")
        self.assertRaises(TypeError, setattr, s1, "size", {1, 2})

    def test_height(self):

        s1 = Square(20, 20, 20, 218)
        setattr(s1, "height", 50)
        self.assertEqual(s1.height, 50)
        self.assertRaises(ValueError, setattr, s1, "height", 0)
        self.assertRaises(ValueError, setattr, s1, "height", -100)
        self.assertRaises(TypeError, setattr, s1, "height", [])
        self.assertRaises(TypeError, setattr, s1, "height", [1])
        self.assertRaises(TypeError, setattr, s1, "height", None)
        self.assertRaises(TypeError, setattr, s1, "height", {})
        self.assertRaises(TypeError, setattr, s1, "height", {1: 2})
        self.assertRaises(TypeError, setattr, s1, "height", ())
        self.assertRaises(TypeError, setattr, s1, "height", (1,))
        self.assertRaises(TypeError, setattr, s1, "height", True)
        self.assertRaises(TypeError, setattr, s1, "height", "1")
        self.assertRaises(TypeError, setattr, s1, "height", {1, 2})

    def test_x(self):

        s1 = Square(20, 20, 20, 219)
        setattr(s1, "x", 50)
        self.assertEqual(s1.x, 50)
        setattr(s1, "x", 0)
        self.assertEqual(s1.x, 0)
        self.assertRaises(ValueError, setattr, s1, "x", -1)
        self.assertRaises(ValueError, setattr, s1, "x", -100)
        self.assertRaises(TypeError, setattr, s1, "x", [])
        self.assertRaises(TypeError, setattr, s1, "x", [1])
        self.assertRaises(TypeError, setattr, s1, "x", None)
        self.assertRaises(TypeError, setattr, s1, "x", {})
        self.assertRaises(TypeError, setattr, s1, "x", {1: 2})
        self.assertRaises(TypeError, setattr, s1, "x", ())
        self.assertRaises(TypeError, setattr, s1, "x", (1,))
        self.assertRaises(TypeError, setattr, s1, "x", True)
        self.assertRaises(TypeError, setattr, s1, "x", "1")
        self.assertRaises(TypeError, setattr, s1, "x", {1, 2})

    def test_y(self):

        s1 = Square(20, 20, 20, 220)
        setattr(s1, "y", 50)
        self.assertEqual(s1.y, 50)
        setattr(s1, "y", 0)
        self.assertEqual(s1.y, 0)
        self.assertRaises(ValueError, setattr, s1, "y", -1)
        self.assertRaises(ValueError, setattr, s1, "y", -100)
        self.assertRaises(TypeError, setattr, s1, "y", [])
        self.assertRaises(TypeError, setattr, s1, "y", [1])
        self.assertRaises(TypeError, setattr, s1, "y", None)
        self.assertRaises(TypeError, setattr, s1, "y", {})
        self.assertRaises(TypeError, setattr, s1, "y", {1: 2})
        self.assertRaises(TypeError, setattr, s1, "y", ())
        self.assertRaises(TypeError, setattr, s1, "y", (1,))
        self.assertRaises(TypeError, setattr, s1, "y", True)
        self.assertRaises(TypeError, setattr, s1, "y", "1")
        self.assertRaises(TypeError, setattr, s1, "y", {1, 2})

    def test_area(self):
        s1 = Square(20, 20, 20, 221)
        s2 = Square(1, 1, 1, 222)
        s3 = Square(20, 1, 1, 223)
        s4 = Square(20, 1, 1, 224)

        self.assertEqual(s1.area(), 400)
        self.assertEqual(s2.area(), 1)
        self.assertEqual(s3.area(), 400)
        self.assertEqual(s4.area(), 400)

    def test_display(self):
        s1 = Square(2, 2, 2, 225)
        buf = io.StringIO()
        with redirect_stdout(buf):
            s1.display()
        s2 = Square(2, 2, 1, 226)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            s2.display()
        self.assertEqual(buf2.getvalue(), "\n  ##\n  ##\n")
        s3 = Square(2, 2, 0, 227)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            s3.display()
        self.assertEqual(buf3.getvalue(), "  ##\n  ##\n")
        r4 = Square(2, 2, 1, 228)
        buf4 = io.StringIO()
        with redirect_stdout(buf4):
            r4.display()
        self.assertEqual(buf4.getvalue(), "\n  ##\n  ##\n")
        r5 = Square(2, 2, 2, 229)
        buf5 = io.StringIO()
        with redirect_stdout(buf5):
            r5.display()
        self.assertEqual(buf5.getvalue(), "\n\n  ##\n  ##\n")

    def test_str(self):
        s1 = Square(2, 2, 2, 230)
        buf = io.StringIO()
        with redirect_stdout(buf):
            print(s1)
        self.assertEqual(buf.getvalue(), "[Square] (230) 2/2 - 2\n")
        s2 = Square(5, 3, 9, 231)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            print(s2)
        self.assertEqual(buf2.getvalue(), "[Square] (231) 3/9 - 5\n")

    def test_update(self):
        s1 = Square(2, 2, 2, 300)
        s1.update(305, 3, 5, 102)
        buf = io.StringIO()
        with redirect_stdout(buf):
            print(s1)
        self.assertEqual(buf.getvalue(), "[Square] (305) 5/102 - 3\n")
        s1.update(312)
        buf2 = io.StringIO()
        with redirect_stdout(buf2):
            print(s1)
        self.assertEqual(buf2.getvalue(), "[Square] (312) 5/102 - 3\n")
        s1.update(315, 10)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            print(s1)
        self.assertEqual(buf3.getvalue(), "[Square] (315) 5/102 - 10\n")
        s1.update(317, 12, 13)
        buf3 = io.StringIO()
        with redirect_stdout(buf3):
            print(s1)
        self.assertEqual(buf3.getvalue(), "[Square] (317) 13/102 - 12\n")
        s1.update(320, 13, 14, 15)
        buf4 = io.StringIO()
        with redirect_stdout(buf4):
            print(s1)
        self.assertEqual(buf4.getvalue(), "[Square] (320) 14/15 - 13\n")
        s1.update(x=150, y=70, id=325)
        buf5 = io.StringIO()
        with redirect_stdout(buf5):
            print(s1)
        self.assertEqual(buf5.getvalue(), "[Square] (325) 150/70 - 13\n")
        s1.update(size=3)
        buf6 = io.StringIO()
        with redirect_stdout(buf6):
            print(s1)
        self.assertEqual(buf6.getvalue(), "[Square] (325) 150/70 - 3\n")
        s1.update(y=112, id=330, x=9, size=80)
        buf7 = io.StringIO()
        with redirect_stdout(buf7):
            print(s1)
        self.assertEqual(buf7.getvalue(), "[Square] (330) 9/112 - 80\n")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 351)
        s1_dictionary = s1.to_dictionary()
        buf = io.StringIO()
        with redirect_stdout(buf):
            print(s1_dictionary, end="")
        self.assertEqual(buf.getvalue(),
                         "{'id': 351, 'size': 10, 'x': 2, 'y': 1}")
