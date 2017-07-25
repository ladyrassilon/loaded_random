import random

class RandomGen(object):
    # Mutable objects should NEVER be exclusively defined in object scope, 
    # It MUST be overriden in instantiation.
    # http://blog.halfapenguin.com/posts/2015/07/23/mutable-global-scope-in-class-definitions/
    # Values that may be returned by next_num()
    _random_nums = []
    # Probability of the occurence of random_nums
    _probabilities = []

    def __init__(self, random_nums, probabilities):
        if sum(probabilities) != 1.0:
            raise IndexError("Probabilities of {} do not add up to 1.0".format(
                probabilities))
        try:
            test_total = sum(random_nums)
        except TypeError as e:
            raise TypeError("One of the items in random number list is not a number")
        if len(random_nums) != len(probabilities):
            raise IndexError("{} is not the same length as {}".format(
                random_nums, probabilities))

        self._random_nums = random_nums
        self._probabilities = probabilities

        self._probability_map = {}
        self._ordered_probabilities = []
        previous_probability = 0
        for idx, prob in enumerate(self._probabilities):
            probability_key = prob + previous_probability
            self._probability_map[probability_key] = self._random_nums[idx]
            self._ordered_probabilities.append(probability_key)
            previous_probability = probability_key


    def get_random(self):
        """
        In current implementation just calls the standard random.random method
        however you could now subclass this class, and just override with a secure
        random number generator
        """
        next_random = random.random()
        return next_random

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        next_random = self.get_random()
        for prob in self._ordered_probabilities:
            if next_random <= prob:
                return self._probability_map[prob]

        raise IndexError("This should never happen")


try:
    #This seems to be the least worst way to check if SystemRandom is available
    test_random = random.SystemRandom().random()
    class SystemRandomGen(RandomGen):
        """
        This is an example implementation using the SystemRandom generator 
        as an alternative random number source.
        """
        def get_random(self):
            next_random = random.SystemRandom().random()
            return next_random
except NotImplementedError:
    SystemRandomGen = RandomGen
