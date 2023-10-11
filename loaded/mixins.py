from decimal import Decimal
import random

class ListItemsOnly:
    # Mutable objects should NEVER be exclusively defined in object scope,
    # It MUST be overriden in instantiation.
    # http://blog.halfapenguin.com/posts/2015/07/23/mutable-global-scope-in-class-definitions/
    # Itmes that may be returned by random()
    _random_nums = None
    # Probability of the occurence of random_nums
    _probabilities = None
    _probability_map = None
    _ordered_probabilities = None
    
    def _setup_probabilities(self, random_items, probabilities, total_probs):
        self._random_items = random_items
        self._probabilities = [Decimal(rn) / total_probs for rn in probabilities]
    

        self._probability_map = {}
        self._ordered_probabilities = []
        previous_probability = 0
        for idx, prob in enumerate(self._probabilities):
            probability_key = prob + previous_probability
            self._probability_map[probability_key] = self._random_items[idx]
            self._ordered_probabilities.append(probability_key)
            previous_probability = probability_key

    def random(self):
        random_element = self._random_element()
        for prob in self._ordered_probabilities:
            if random_element <= prob:
                return self._probability_map[prob]

class NumberOnly:
    def _additional_checks(self, random_items, probabilities, total_probs):
        super()._additional_checks(random_items, probabilities, total_probs)
        try:
            test_total = sum(random_items)
        except TypeError as e:
            raise TypeError("One of the items in random number list is not a number")        

class SimpleMap:
    pass

class BestFitMap:
    pass

class UseSystemRandom:
    def get_random_element(self):
        next_random = random.SystemRandom().random()
        return next_random
