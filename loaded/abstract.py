import random
from decimal import Decimal

class AbstractLoadedRandomGenerator:
    def __init__(self, random_items, probabilities, check_total=False):
        if len(random_items) != len(probabilities):
            raise IndexError(
                "{} is not the same length as {}".format(random_items, probabilities)
            )
        try: # This does not make me happy as a way to test
            total_probs = Decimal(sum(probabilities))
        except TypeError as e:
            raise TypeError("One of the items in random number list is not a number")
        if check_total and total_probs != Decimal("1.0"):
            raise ValueError(
                "Probabilities of {} do not add up to 1.0".format(probabilities)
            )
        self._additional_checks(random_items=random_items, probabilities=probabilities, total_probs=total_probs)
        self._setup_probabilities(random_items=random_items, probabilities=probabilities, total_probs=total_probs)

    def _additional_checks(self, random_items, probabilities, total_probs):
        pass

    def _setup_probabilities(self, random_items, probabilities, total_probs):
        raise NotImplementedError()

    def _random_element(self):
        """
        In current implementation just calls the standard random.random method
        however you could now subclass this class, and just override with
        a secure random number generator
        """
        next_random = random.random()
        return next_random
    
    def random(self):
        raise NotImplementedError()