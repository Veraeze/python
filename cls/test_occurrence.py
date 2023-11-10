from unittest import TestCase
from cls import occurrence


class Test(TestCase):
    def test_occurrences(self):
        self.assertEqual('resta$t', occurrence.occurrences('restart', '$', 1))

    def test_occurrences2(self):
        self.assertEqual('as%urance', occurrence.occurrences('assurance', '%', 2))

    def test_occurrences3(self):
        self.assertEqual('rest', occurrence.occurrences('rest', '#', 1))
