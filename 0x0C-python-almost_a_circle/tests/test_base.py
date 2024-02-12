#!/usr/bin/python3
"""Unittest for Base([..])
"""
import unittest
import io
import os
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """testing Base"""

    def test_id(self):
        b1 = Base()
        b2 = Base(10)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 10)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 123)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            json_dictionary, '[{"id": 123, "width": 10,'
            ' "height": 7, "x": 2, "y": 8}]'
        )

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 125)
        r2 = Rectangle(2, 4, 8, 3, 198)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            json_file = file.read()
        self.assertEqual(
            json_file,
            '[{"id": 125, "width": 10, "height": 7, "x": 2, "y": 8},'
            ' {"id": 198, "width": 2, "height": 4, "x": 8, "y": 3}]',
        )
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            json_file = file.read()
        self.assertEqual(json_file, "[]")

    def test_from_json_string(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(
            list_output,
            [{"height": 4, "width": 10, "id": 89},
             {"height": 7, "width": 1, "id": 7}],
        )
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        json_list_input = Rectangle.to_json_string(None)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 19, 198)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        buffer1 = io.StringIO()
        with redirect_stdout(buffer1):
            print(r2, end="")
        self.assertEqual(buffer1.getvalue(), "[Rectangle] (198) 1/19 - 3/5")

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 212)
        r2 = Rectangle(2, 4, 8, 12, 213)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        buffer2 = io.StringIO()
        with redirect_stdout(buffer2):
            print(list_rectangles_output[0], end="")
        self.assertEqual(buffer2.getvalue(), "[Rectangle] (212) 2/8 - 10/7")
        buffer3 = io.StringIO()
        with redirect_stdout(buffer3):
            print(list_rectangles_output[1], end="")
        self.assertEqual(buffer3.getvalue(), "[Rectangle] (213) 8/12 - 2/4")
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8, 410)
        r2 = Rectangle(2, 4, 8, 15, 411)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        buffer1 = io.StringIO()
        with redirect_stdout(buffer1):
            print(list_rectangles_output[0], end="")
        self.assertEqual(buffer1.getvalue(), "[Rectangle] (410) 2/8 - 10/7")
        buffer2 = io.StringIO()
        with redirect_stdout(buffer2):
            print(list_rectangles_output[1], end="")
        self.assertEqual(buffer2.getvalue(), "[Rectangle] (411) 8/15 - 2/4")
    def test_load_from_file_csv(self):
        s1 = Square(5, 10, 12, 420)
        s2 = Square(7, 9, 1, 421)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        buffer1 = io.StringIO()
        with redirect_stdout(buffer1):
            print(list_squares_output[0], end="")
        self.assertEqual(buffer1.getvalue(), "[Square] (420) 10/12 - 5")
        buffer2 = io.StringIO()
        with redirect_stdout(buffer2):
            print(list_squares_output[1], end="")
        self.assertEqual(buffer2.getvalue(), "[Square] (421) 9/1 - 7")
