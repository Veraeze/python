from unittest import TestCase
from Functions import functions

class Test(TestCase):
    def test_divide(self):
        self.assertEqual(2, functions.divide(10, 5))
