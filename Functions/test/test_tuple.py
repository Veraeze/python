from unittest import TestCase
from Functions import tuple


class Test(TestCase):

    def test_reverse_tuple(self):
        self.assertEqual((50, 40, 30, 20, 10), tuple.reverse_tuple(10, 20, 30, 40, 50))

    def test_nested_tuple(self):
        self.assertEqual((0, 20), (1, 25), tuple.nested_tuple("Orange", [10, 20, 30], (5, 15, 25)))

    def test_swap_tuple(self):
        self.assertEqual((55, 15), tuple.swap_tuple(15, 25, 60, 50, 30, 40, 45, 55))

    def test_sort_tuple(self):
        self.assertEqual((('c', 11), ('a', 23), ('d', 29), ('b', 37)), tuple.sort_tuple(('a', 23), ('b', 37), ('c', 11), ('d', 29)))

    def test_return_duplicate(self):
        self.assertEqual((5, 10, 20), tuple.return_duplicate(20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5))
