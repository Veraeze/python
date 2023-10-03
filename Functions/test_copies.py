from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_copy1(self):
        self.assertEqual(2000, functions.copy(3))

    def test_copy2(self):
        self.assertEqual(1800, functions.copy(7))

    def test_copy3(self):
        self.assertEqual(1600, functions.copy(22))

    def test_copy4(self):
        self.assertEqual(1500, functions.copy(39))

    def test_copy5(self):
        self.assertEqual(1300, functions.copy(64))

    def test_copy6(self):
        self.assertEqual(1200, functions.copy(105))

    def test_copy7(self):
        self.assertEqual(1100, functions.copy(282))

    def test_copy1(self):
        self.assertEqual(1000, functions.copy(710))

    def test_copy1(self):
        self.assertEqual(2000, functions.copy(3))