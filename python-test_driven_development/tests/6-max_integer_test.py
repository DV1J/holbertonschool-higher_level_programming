#!/usr/bin/pyhton3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -1, -9, -2, -3]), -1)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.0, 2.3, -2.8, 3.9, 3.923, 3.9238]), 3.9238)

    def test_max_beginning(self):
        self.assertEqual(max_integer([10, 3, 4, 5, 1, 0, -10]), 10)

    def test_max_middle(self):
        self.assertEqual(max_integer([0, 19, 3]), 19)

    def test_one_argument(self):
        self.assertEqual(max_integer([19]), 19)