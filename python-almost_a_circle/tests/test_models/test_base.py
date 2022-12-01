#!/usr/bin/python3
"""Unit testing for the base class"""


import os
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(TestCase):
    """The Test class for the Base class in models"""
    def test_starting(self):
        """Test the starting point of creation of Base"""
        base = Base()
        first_base = Base()
        second_base = Base()
        base_with_39 = Base(39)
        self.assertEqual(base.id, 1)
        self.assertEqual(first_base.id, 2)
        self.assertEqual(second_base.id, 3)
        self.assertEqual(base_with_39.id, 39)

    def test_to_json_string(self):
        """Test the converting of lists to dicts"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([{'id': 10}]), '[{"id": 10}]')
        self.assertEqual(type(Base.to_json_string([{'id': 10}])), str)

    def test_save_to_file(self):
        """Test that the file saves list objects to  file"""
        Base._Base__nb_objects = 0
        Square.save_to_file(None)

        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')

        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
        Base._Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')

        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[]')
            self.assertEqual(type(file.read()), str)

        Rectangle.save_to_file([Rectangle(2, 3)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "width": 2, '
                             '"height": 3, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """Test """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[{"id": 23}]'), [{'id': 23}])
        self.assertEqual(type(Base.from_json_string('[{"id": 23}]')), list)
