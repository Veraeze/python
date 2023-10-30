from unittest import TestCase
from cls import biggestodd
from cls import cornflakes


class Test(TestCase):

    def test_list(self):
        self.assertEqual("9", biggestodd.biggest_odd("92356"))

    def test_corn(self):
        self.assertTrue(cornflakes.equal_strings("evol", "love"))
        self.assertFalse(cornflakes.equal_strings("love", "evir"))
