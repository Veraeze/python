from unittest import TestCase
from Functions import tuples


class Test(TestCase):

    def test_reverse_tuple(self):
        self.assertEqual((50, 40, 30, 20, 10), tuples.reverse_tuple(10, 20, 30, 40, 50))

    def test_nested_tuple(self):
        self.assertEqual(((0, 20), (1, 25)), tuples.nested_tuple("Orange", [10, 20, 30], (5, 15, 25)))

    def test_swap_tuple(self):
        self.assertEqual((55, 15), tuples.swap_tuple(15, 25, 60, 50, 30, 40, 45, 55))

    def test_sort_tuple(self):
        self.assertEqual((('c', 11), ('a', 23), ('d', 29), ('b', 37)), tuples.sort_tuple(('a', 23), ('b', 37), ('c', 11), ('d', 29)))

    def test_return_duplicate(self):
        self.assertEqual((5, 10, 20), tuples.return_duplicate(20, 10, 15, 20, 5, 30, 10, 35, 10, 40, 45, 5))

    def test_sort_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], tuples.my_sort_method([1, 4, 6, 3, 2, 5]))
        self.assertEqual([6, 5, 4, 3, 2, 1], tuples.my_sort_method([1, 4, 6, 3, 2, 5], True))

