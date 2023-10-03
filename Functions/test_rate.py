from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_rate1(self):
        self.assertEqual(10600, functions.rate(35))

    def test_rate2(self):
        self.assertEqual(16400, functions.rate(57))

    def test_rate3(self):
        self.assertEqual(20500, functions.rate(62))

    def test_rate4(self):
        self.assertEqual(49500, functions.rate(89))
