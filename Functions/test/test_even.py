from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_is_even1(self):
        self.assertEqual(True, functions.is_even(86))

    def test_is_even2(self):
        self.assertEqual(False, functions.is_even(31))