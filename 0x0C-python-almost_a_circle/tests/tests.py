#!/usr/bin/python
"""Tests for Almost a circle task"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTests(unittest.TestCase):
    """Tests for Base class"""
    def test_instance(self):
        """Checks if an instance's type is Base"""
        new = Base()
        self.assertEqual(str(type(new)), "<class 'models.base.Base'>")

    def test_id_check(self):
        """Checks the id of a Base instance"""
        new = Base()
        self.assertEqual(new.id, 1)
        new = Base(5)
        self.assertEqual(new.id, 5)
        new = Base()
        self.assertEqual(new.id, 2)


class RectangleTests(unittest.TestCase):
    """Test for Rectangle Class"""
    def test_instance(self):
        """Checks if an instance's type is Rectangle"""
        new = Rectangle(1, 1)
        expect = "<class 'models.rectangle.Rectangle'>"
        self.assertEqual(str(type(new)), expect)

    def test_inputs(self):
        """Checks for invalid inputs"""
        with self.assertRaises(ValueError):
            new = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            new = Rectangle(-1, -1)
        with self.assertRaises(ValueError):
            new = Rectangle(1, 2, -1, -1)
        with self.assertRaises(TypeError):
            new = Rectangle("a", 2)
        with self.assertRaises(TypeError):
            new = Rectangle(2, "a")
        with self.assertRaises(TypeError):
            new = Rectangle(2, 1, "a")
        with self.assertRaises(TypeError):
            new = Rectangle(2, 1, 3, "e")

    def test_values(self):
        """Checks attributes values at instantiation"""
        new = Rectangle(1, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_setters_getters(self):
        """Setters and getters check"""
        new = Rectangle(1, 2)
        new.height = 9
        new.width = 9
        self.assertEqual(new.height, 9)
        self.assertEqual(new.width, 9)
        new.x = 4
        new.y = 5
        self.assertEqual(new.x, 4)
        self.assertEqual(new.y, 5)

    def test_display(self):
        """Correct display of the shape in stdout"""
        new = Rectangle(3, 2)
        expected = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.height = 5
        new.width = 4
        expected = "####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.x = 1
        expected = " ####\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.y = 1
        expected = "\n ####\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)


class SquareTests(unittest.TestCase):
    """Test for Square class"""
    def test_instance(self):
        """Checks if an instance's type is Rectangle"""
        new = Square(1, 1)
        self.assertEqual(str(type(new)), "<class 'models.square.Square'>")

    def test_inputs(self):
        """Checks for invalid inputs"""
        with self.assertRaises(ValueError):
            new = Square(0, 0)
        with self.assertRaises(ValueError):
            new = Square(-1, -1)
        with self.assertRaises(ValueError):
            new = Square(1, 2, -1, -1)
        with self.assertRaises(TypeError):
            new = Square("a", 2)
        with self.assertRaises(TypeError):
            new = Square(2, "a")
        with self.assertRaises(TypeError):
            new = Square(2, 1, "a")

    def test_values(self):
        """Checks attributes values at instantiation"""
        new = Square(1, 2)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.x, 2)
        self.assertEqual(new.y, 0)

    def test_setters_getters(self):
        """Setters and getters check"""
        new = Square(1, 2)
        new.size = 9
        self.assertEqual(new.size, 9)
        self.assertEqual(new.height, 9)
        self.assertEqual(new.width, 9)
        new.x = 4
        new.y = 5
        self.assertEqual(new.x, 4)
        self.assertEqual(new.y, 5)

    def test_display(self):
        """Correct display of the shape in stdout"""
        new = Square(3)
        expected = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.size = 5
        expected = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.x = 1
        expected = " #####\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.y = 1
        expected = "\n #####\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
        new.size = 1
        expected = "\n #\n"
        with patch('sys.stdout', new=StringIO()) as out:
            new.display()
            self.assertEqual(out.getvalue(), expected)
