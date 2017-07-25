import unittest
from loaded import RandomGen

class TestRandomGen(unittest.TestCase):

    def test_longer_probabilities_list(self):
        probabilities = [0.25, 0.25, 0.25, 0.25]
        random_nums = [1, 2, 3]
        with self.assertRaises(IndexError):
            load = RandomGen(random_nums=random_nums, probabilities=probabilities)

    def test_longer_random_nums_list(self):
        probabilities = [0.25, 0.25, 0.25]
        random_nums = [1, 2, 3, 4]
        with self.assertRaises(IndexError):
            load = RandomGen(random_nums=random_nums, probabilities=probabilities)

    def test_non_number_in_list(self):
        probabilities = [0.25, 0.25, 0.25, 0.25]
        random_nums = [1, 2, 3, "4"]
        with self.assertRaises(TypeError):
            load = RandomGen(random_nums=random_nums, probabilities=probabilities)

    def test_less_than_one_probabilities_list(self):
        probabilities = [0.25, 0.25, 0.25]
        random_nums = [1, 2, 3]
        with self.assertRaises(IndexError):
            load = RandomGen(random_nums=random_nums, probabilities=probabilities)

    def test_greater_than_one_probabilities_list(self):
        probabilities = [0.25, 0.25, 0.25, 0.25, 0.25]
        random_nums = [1, 2, 3, 4, 5]
        with self.assertRaises(IndexError):
            load = RandomGen(random_nums=random_nums, probabilities=probabilities)