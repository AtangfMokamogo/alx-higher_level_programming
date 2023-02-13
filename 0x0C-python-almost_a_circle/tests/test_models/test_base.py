#!/usr/bin/python3
"""Defines unittests for base.py."""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """TestBaseClass class to test the Base class"""

    def test_instance_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_instance(self):
        r1 = Rectangle(10, 10)
        r2 = Rectangle(10, 10)
        s1 = Square(10)
        s2 = Square(10)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(id(r1) != id(r2))
        self.assertTrue(id(s1) != id(s2))

    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_id_base(self):
        base_inst_1 = Base(1)
        base_inst_2 = Base(2)
        base_inst_3 = Base(3)
        base_inst_4 = Base(12)
        self.assertEqual(base_inst_1.id, 1)
        self.assertEqual(base_inst_2.id, 2)
        self.assertEqual(base_inst_3.id, 3)
        self.assertEqual(base_inst_4.id, 12)

    def test_er_type_base(self):
        with self.assertRaises(TypeError):
            b1 = Base(10, 2)
        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])
        with self.assertRaises(TypeError):
            Square.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], [])

        with self.assertRaises(TypeError):
            Rectangle.from_json_string("[]", "[]")
        with self.assertRaises(TypeError):
            Square.from_json_string("[]", "[]")

        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])
        with self.assertRaises(TypeError):
            Square.load_from_file([])

        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string()
        with self.assertRaises(TypeError):
            list_output = Square.from_json_string()

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary) is dict)
        self.assertTrue(type(json_dictionary) is str)
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
        self.assertEqual(Base.to_json_string([dictionary]),
                         json.dumps([dictionary]))

    def test_save_to_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(file.read())
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
            a = json.loads(json_string)
            self.assertTrue(type(a) is list)
            self.assertTrue(type(a[0]) is dict)
            self.assertTrue(type(a[1]) is dict)
            self.assertEqual(a[0], r1.to_dictionary())
            self.assertEqual(a[1], r2.to_dictionary())
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
            a = json.loads(json_string)
            self.assertTrue(type(a) is list)
            self.assertTrue(a == [])
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            json_string = file.read()
            a = json.loads(json_string)
            self.assertTrue(type(a) is list)
            self.assertTrue(a == [])

    def test_save_to_file_squa(self):
        s1 = Square(10, 7, 2)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertTrue(file.read())
        with open("Square.json", "r") as file:
            json_string = file.read()
            b = json.loads(json_string)
            self.assertTrue(type(b) is list)
            self.assertTrue(type(b[0]) is dict)
            self.assertTrue(type(b[1]) is dict)
            self.assertEqual(b[0], s1.to_dictionary())
            self.assertEqual(b[1], s2.to_dictionary())
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            json_string = file.read()
            a = json.loads(json_string)
            self.assertTrue(type(a) is list)
            self.assertTrue(a == [])
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            json_string = file.read()
            a = json.loads(json_string)
            self.assertTrue(type(a) is list)
            self.assertTrue(a == [])

    def test_json_string_to_dict_rect(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)
        self.assertDictEqual(list_input[0], list_output[0])

        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(type(list_input) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)

        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_json_string_to_dict_squa(self):
        list_input = [
            {'id': 89, 'size': 10},
            {'id': 7, 'size': 4}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(list_input) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)
        self.assertDictEqual(list_input[0], list_output[0])

        list_input = []
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertTrue(type(list_input) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertTrue(type(list_output) is list)
        self.assertEqual(list_input, list_output)

        list_output = Square.from_json_string("")
        self.assertEqual(list_output, [])

        list_output = Square.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_create_rect(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertDictEqual(r1_dictionary, r2_dictionary)
        self.assertFalse(r1_dictionary is r2_dictionary)
        self.assertTrue(r1_dictionary == r2_dictionary)
        self.assertFalse(r1 == r2)

    def test_create_squa(self):
        s1 = Square(3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertDictEqual(s1_dictionary, s2_dictionary)
        self.assertFalse(s1_dictionary is s2_dictionary)
        self.assertTrue(s1_dictionary == s2_dictionary)
        self.assertFalse(s1 == s2)

    def test_file_to_instance_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for i in range(len(list_rectangles_input)):
            self.assertNotEqual(id(list_rectangles_input[i]),
                                id(list_rectangles_output[i]))
            self.assertEqual(str(list_rectangles_input[i]),
                             str(list_rectangles_output[i]))

    def test_file_to_instance_squa(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for i in range(len(list_squares_input)):
            self.assertNotEqual(id(list_squares_input[i]),
                                id(list_squares_output[i]))
            self.assertEqual(str(list_squares_input[i]),
                             str(list_squares_output[i]))

    def test_file_csv_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        for i in range(len(list_rectangles_input)):
            self.assertNotEqual(id(list_rectangles_input[i]),
                                id(list_rectangles_output[i]))
            self.assertEqual(str(list_rectangles_input[i]),
                             str(list_rectangles_output[i]))

    def test_file_csv_squa(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        for i in range(len(list_squares_input)):
            self.assertNotEqual(id(list_squares_input[i]),
                                id(list_squares_output[i]))
            self.assertEqual(str(list_squares_input[i]),
                             str(list_squares_output[i]))


if __name__ == '__main__':
    unittest.main()
