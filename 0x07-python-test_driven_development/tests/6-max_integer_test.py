#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """ Function tests whether the max integer is returned"""

        list_1 = [1, 2, 3, 4, 5, 6, -10]
        list2 = [-1, -2, -3, 0]
        list3 = [1]
        self.assertEqual(max_integer(list_1), 6)
        self.assertEqual(max_integer(list2), 0)
        self.assertEqual(max_integer(list3), 1)

    def test_types(self):
        """ Function tests whether the max_integer function
        raises an error when wrong types are fed into it"""

        list_1 = ['some', 'string', 5, 6, 7]
        list_2 = [6.1, 5.4, -8.76, 'wow']
        self.assertRaises(TypeError, max_integer, list_1)
        self.assertRaises(TypeError, max_integer, list_2)

    def test_max_at_start(self):
        """ Function test whether the first item in the list is the largest"""

        list1 = [100, 5, 6, 3, 4]
        self.assertEqual(max_integer(list1), 100)

    def test_empty(self):
        """ Function tests whether the list is empty """

        empty_list = []
        self.assertEqual(max_integer(empty_list), "")


