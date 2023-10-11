import unittest
from collections import Counter

from loaded import LoadedRandomNumberChooser, SystemLoadedRandomNumberChooser


class BasicLoadedFunctionality:
    def test_longer_probabilities_list(self):
        probabilities = [0.25, 0.25, 0.25, 0.25]
        random_items = [1, 2, 3]
        with self.assertRaises(IndexError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )

    def test_longer_random_items_list(self):
        probabilities = [0.25, 0.25, 0.25]
        random_items = [1, 2, 3, 4]
        with self.assertRaises(IndexError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )
    
    def test_non_number_in_probabilities(self):
        probabilities = [0.25, 0.25, 0.25, "0.25"]
        random_items = [1, 2, 3, 4]
        with self.assertRaises(TypeError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )
    
    def test_expected_results(self):
        """
        The trouble with pseudo-random number generators is that they are not
        perfect, espeunder limited time conditions, however given sufficiently
        diverse odds, you can realistically assume that each successive group
        of results will be greater if the odds are greater.
        """
        probabilities = [0.01, 0.1, 0.3, 0.59]
        random_items = [3, 7, 11, 13]
        load = self.random_generator(
            random_items=random_items, probabilities=probabilities
        )
        results = []
        number_of_results = 1000
        for x in range(number_of_results):
            results.append(load.random())
        counted = Counter(results)
        for idx, num in enumerate(random_items):
            if idx + 1 < len(random_items):
                this_result = counted[num]
                next_result = counted[random_items[idx + 1]]
                self.assertLess(this_result, next_result)

class ProbabilitiesMustEqualOne:
    def test_less_than_one_probabilities_list_checked(self):
        probabilities = [0.25, 0.25, 0.25]
        random_items = [1, 2, 3]
        with self.assertRaises(ValueError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities, check_total=True
            )

    def test_greater_than_one_probabilities_list_checked(self):
        probabilities = [0.25, 0.25, 0.25, 0.25, 0.25]
        random_items = [1, 2, 3, 4, 5]
        with self.assertRaises(ValueError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities, check_total=True
            )

class ProbabilitiesCanVary:
    def test_less_than_one_probabilities_list_not_checked(self):
        probabilities = [0.25, 0.25, 0.25]
        random_items = [1, 2, 3]
        try:
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )
        except Exception as e:
            self.fail("Failed - {}".format(e))
        
    def test_greater_than_one_probabilities_list_not_checked(self):
        probabilities = [0.25, 0.25, 0.25, 0.25, 0.25]
        random_items = [1, 2, 3, 4, 5]
        try:
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )
        except Exception as e:
            self.fail("Failed - {}".format(e))

class OnlyNumbers:
    def test_non_number_in_items(self):
        probabilities = [0.25, 0.25, 0.25, 0.25]
        random_items = [1, 2, 3, "4"]
        with self.assertRaises(TypeError):
            load = self.random_generator(
                random_items=random_items, probabilities=probabilities
            )

class TestLoadedRandomNumberChooser(BasicLoadedFunctionality, ProbabilitiesMustEqualOne, ProbabilitiesCanVary, OnlyNumbers, unittest.TestCase):
    random_generator = LoadedRandomNumberChooser


class TestSystemRandomGen(BasicLoadedFunctionality, ProbabilitiesMustEqualOne, OnlyNumbers, ProbabilitiesCanVary, unittest.TestCase):
    random_generator = SystemLoadedRandomNumberChooser
