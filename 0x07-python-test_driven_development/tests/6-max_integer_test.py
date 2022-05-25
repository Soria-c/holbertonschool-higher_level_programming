#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer()"""

    def test_negative_number(self):
        """One negative number in the list"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_only_negative(self):
        """List made only of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max_beggining(self):
        """Max number in the beggining of the list"""
        self.assertEqual(max_integer([24, 12, 9]), 24)

    def test_max_middle(self):
        """Max number in the middle of the list"""
        self.assertEqual(max_integer([10, 12, 9]), 12)

    def test_max_end(self):
        """Max number in the end of the list"""
        self.assertEqual(max_integer([10, 12, 90]), 90)

    def test_one_element(self):
        """List of only one element"""
        self.assertEqual(max_integer([100]), 100)

    def test_empty_list(self):
        """Empty list"""
        self.assertEqual(max_integer([]), None)
