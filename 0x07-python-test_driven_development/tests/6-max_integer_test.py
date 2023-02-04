#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """ Function tests whether the max integer is returned"""

        list_1 = [1, 2, 3, 4, 5, 6, -10]
        list2 = [-1, -2, -3, 0]
        self.assertEqual(max_integer(list_1), 6)
        self.assertEqual(max_integer(list2), 0)

    def test_types(self):
        """ Function tests whether the max_integer function
        raises an error when wrong types are fed into it"""

        list_1 = ['some', 'string', 5, 6, 7]
        list_2 = [6.1, 5.4, -8.76, 'wow']
        self.assertRaises(TypeError, max_integer, list_1)
        self.assertRaises(TypeError, max_integer, list_2)
