from unittest import TestCase
from cls import dictionary_task


class Test(TestCase):
    def test_present(self):
        result = "Hi, precious, you are 27 years old."
        self.assertEqual(result, dictionary_task.student_ages({"dike": 33, "ope": 25, "melody": 20, "precious": 27}, "precious"))

    def test_added(self):
        result = "Hi, vera, you are 35 years old."
        self.assertEqual(result, dictionary_task.student_ages({"dike": 33, "ope": 25, "melody": 20, "precious": 27}, "vera", 35))

    def test_sum(self):
        self.assertEqual(33, dictionary_task.sum_nested_list([[2, 4, 5, 6], [2, 3, 5, 6]]))

    def test_sum(self):
        self.assertEqual(33, dictionary_task.sum_nested_list2([[2, 4, 5, 6], [2, 3, 5, 6]]))

    def test_sum(self):
        self.assertEqual([2, 4, 6, 8, 10, 12, 14], dictionary_task.even_integer_list())
