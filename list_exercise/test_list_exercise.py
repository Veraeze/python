from unittest import TestCase
from list_exercise import sum_list
from Functions import functions


class Test(TestCase):

    def test_sum_of_list(self):
        self.assertEqual(95, sum_list.sum_of_list([15, 20, 25, 20, 10, 5]))      

    def test_triple_list(self):
        self.assertEqual(functions.triple([3, 7, 2, 6, 5]), [27, 343, 8, 216, 125])
