#!/usr/bin/python3
"""Test the Rectangle Class of the projects"""

import unittest
from io import StringIO
from unittest.mock import patch
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test the Reactangle"""

    def test_instance(self):
        """Create a new test for """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r8 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r8.id, 5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r11 = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r12 = Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r9 = Rectangle(-1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r10 = Rectangle(1, -2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r13 = Rectangle(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r14 = Rectangle(1, 2, 3, -4)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("1", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(1, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(1, 2, 3, "4")


    def test__str__(self):
        """Create a new test for string representation"""
        Base._Base__nb_objects = 0
        rectangle = Rectangle(7, 3)
        with patch("sys.stdout", new=StringIO()) as trial_rect:
            print(rectangle)
            self.assertEqual(trial_rect.getvalue(),
                             "[Rectangle] (1) 0/0 - 7/3\n")

    def test_update(self):
        """update method on the given dictionary"""
        Base._Base__nb_objects = 0
        rect_test = Rectangle(4, 2)

        rect_test.update()
        self.assertEqual(rect_test.id, 1)

        rect_test.update(20)
        self.assertEqual(rect_test.id, 20)

        rect_test.update(10, 4)
        self.assertEqual(rect_test.id, 10)
        self.assertEqual(rect_test.width, 4)

        rect_test.update(12, 4, 5)
        self.assertEqual(rect_test.id, 12)
        self.assertEqual(rect_test.width, 4)
        self.assertEqual(rect_test.height, 5)

        rect_test.update(5, 2, 3, 4)
        self.assertEqual(rect_test.id, 5)
        self.assertEqual(rect_test.width, 2)
        self.assertEqual(rect_test.height, 3)
        self.assertEqual(rect_test.x, 4)

        rect_test.update(9, 10, 5, 2, 1)
        self.assertEqual(rect_test.id, 9)
        self.assertEqual(rect_test.width, 10)
        self.assertEqual(rect_test.height, 5)
        self.assertEqual(rect_test.x, 2)
        self.assertEqual(rect_test.y, 1)

        rect_test.update(**{"id": 23})
        self.assertEqual(rect_test.id, 23)

        rect_test.update(**{'id': 34, 'width': 5})
        self.assertEqual(rect_test.id, 34)
        self.assertEqual(rect_test.width, 5)

        rect_test.update(**{'id': 9, 'width': 4, 'height': 10})
        self.assertEqual(rect_test.id, 9)
        self.assertEqual(rect_test.width, 4)
        self.assertEqual(rect_test.height, 10)

        rect_test.update(**{'id': 6, 'width': 4, 'height': 6, 'x': 7})
        self.assertEqual(rect_test.id, 6)
        self.assertEqual(rect_test.width, 4)
        self.assertEqual(rect_test.height, 6)
        self.assertEqual(rect_test.x, 7)

        rect_test.update(**{'id': 4, 'width': 5, 'height': 7, 'x': 9, 'y': 1})
        self.assertEqual(rect_test.id, 4)
        self.assertEqual(rect_test.width, 5)
        self.assertEqual(rect_test.height, 7)
        self.assertEqual(rect_test.x, 9)
        self.assertEqual(rect_test.y, 1)


    def test_area(self):
        """Create a new test for the area f the reactangle"""
        rectangle = Rectangle(5, 2)
        self.assertEqual(rectangle.area(), 10)


    def test_display(self):
        """Check if the display is the rightful dispaly"""
        r1 = Rectangle(5, 3)
        r2 = Rectangle(5, 3, 3)
        r3 = Rectangle(4, 2, 3, 2)
        with patch("sys.stdout", new=StringIO()) as trial_out_rect:
            r1.display()
            self.assertEqual(trial_out_rect.getvalue(),
                             "#####\n#####\n#####\n")
        with patch("sys.stdout", new=StringIO()) as trial_out_rect:
            r2.display()
            self.assertEqual(trial_out_rect.getvalue(),
                             "   #####\n   #####\n   #####\n")
        with patch("sys.stdout", new=StringIO()) as trial_out_rect:
            r3.display()
            self.assertEqual(trial_out_rect.getvalue(),
                             "\n\n   ####\n   ####\n")
    def test_load_from_file(self):
        """Create a new test for """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        from_file = Rectangle.load_from_file()
        self.assertEqual(type(from_file), list)
        self.assertEqual(from_file[0].width, 1)
        self.assertEqual(from_file[0].height, 2)

    def test_to_dictionary(self):
        """Test for the list to dict conversion of the input data"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(6, 3)
        self.assertEqual(r1.to_dictionary(),
                         {'id': 1, 'width':6, 'height': 3, 'x': 0, 'y': 0})

    
    def test_create(self):
        """Create a new test for creation of a new one"""

        rect = Rectangle.create(**{'id': 3})
        self.assertEqual(rect.id, 3)

        rect = Rectangle.create(**{'id': 6, 'width': 2})
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 2)

        rect = Rectangle.create(**{'id': 72, 'width': 7, 'height': 27})
        self.assertEqual(rect.id, 72)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 27)

        rect = Rectangle.create(**{'id': 56, 'width': 2, 'height': 22, 'x': 13})
        self.assertEqual(rect.id, 56)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 22)
        self.assertEqual(rect.x, 13)

        rect = Rectangle.create(**{'id': 10, 'width': 3,
                                 'height': 5, 'x': 1, 'y': 2})
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_save_to_file(self):
        """Create a new test for saving the rectangle to a file"""
        Base._Base__nb_objects = 45

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Rectangle.save_to_file([Rectangle(3, 4)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 46, "width": 3, '
                             '"height": 4, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")
            self.assertEqual(type(file.read()), str)        

  