from unittest import TestCase
from cls import weekend_functions


class Test(TestCase):
    def test_list_to_dictionary(self):
        sample_input = ['apple', 'banana', 'coconut']
        sample_output = {'a': 'apple', 'b': 'banana', 'c': 'coconut'}
        self.assertEqual(sample_output, weekend_functions.list_to_dictionary(sample_input))

    def test_list_to_dictionary2(self):
        sample_input = ['apple', 'banana', 'coconut', 'corn']
        sample_output = {'a': 'apple', 'b': 'banana', 'c': 'coconut', 'C': 'corn'}
        self.assertEqual(sample_output, weekend_functions.list_to_dictionary(sample_input))

    def test_two_list_to_dictionary(self):
        input1 = ['a', 'b', 'c', 'd', 'e']
        input2 = [1, 2, 3, 4, 5]
        sample_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sample_output, weekend_functions.two_list_to_dictionary(input1, input2))

    def test_largest_minus_smallest(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        self.assertEqual(70, weekend_functions.largest_minus_smallest(sample_input))

    def test_greater_than_value(self):
        sample_input = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
        sample_output = [1, 2, 5]
        self.assertEqual(sample_output, weekend_functions.greater_than_value(sample_input, 2))

    def test_empty_string(self):
        sample_input = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
        sample_output = ['ABC', 'xyz', 'abc', 'XYZ']
        self.assertEqual(sample_output, weekend_functions.empty_string(sample_input))

    def test_split_list(self):
        sample_input = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
        sample_output = [10, 75, 20, 30, 15], [5, 40, 25, 40, 35]
        self.assertEqual(sample_output, weekend_functions.split_list(sample_input))


