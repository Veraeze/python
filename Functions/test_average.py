from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_average(self):
        self.assertEqual(5.5, functions.average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
