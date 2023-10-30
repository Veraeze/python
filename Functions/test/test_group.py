from unittest import TestCase
from cls import group


class Test(TestCase):

    def test_list(self):
        self.assertEqual(list(range(1, 21)), group.create_list(  ))
