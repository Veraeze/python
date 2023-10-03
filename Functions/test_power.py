from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_raise_power(self):
        self.assertEqual(25, functions.raise_power(5, 2))

    def test_raise_power2(self):
        self.assertEqual(8, functions.raise_power(2, 3))
