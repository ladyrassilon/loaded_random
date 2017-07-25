import unittest
from collections import Counter

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

    def test_expected_results(self):
        """
        The trouble with pseudo-random number generators is that they are not 
        perfect, espeunder limited time conditions, however given sufficiently
        diverse odds, you can realistically assume that each successive group
        of results will be greater if the odds are greater.
        """
        probabilities = [0.01, 0.1, 0.3, 0.59]
        random_nums = [3, 7, 11, 13]
        load = RandomGen(random_nums=random_nums, probabilities=probabilities)
        results = []
        number_of_results = 1000
        for x in range(number_of_results):
            results.append(load.next_num())
        counted = Counter(results)
        for idx, num in enumerate(random_nums):
            if idx + 1 < len(random_nums):
                this_result = counted[num]
                next_result = counted[random_nums[idx + 1]]
                self.assertLess(this_result, next_result)
