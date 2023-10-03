from unittest import TestCase
from Functions import functions


class Test(TestCase):
    def test_is_prime_number1(self):
        self.assertEqual(True, functions.is_prime_number(11))

    def test_is_prime_number2(self):
        self.assertEqual(False, functions.is_prime_number(20))
