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
