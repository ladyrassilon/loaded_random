==================
Loaded Random v0.1
==================

This is a simple library that allows you to generate random numbers as per specified probabilities.

.. code:: python

    from loaded import RandomGen

    probabilities = [0.02, 0.02, 0.02, 0.02, 0.02, 0.9]
    random_nums = [1, 2, 3, 4, 5, 6]

    dice = RandomGen(probabilities=probabilities, random_nums=random_nums)

    results = [dice.next_num() for _ in range(1000)]

    from collections import Counter

    counted = Counter(results)

    print(counted)
    # You'll get results of the form
    # Counter({1: 26, 2: 13, 3: 24, 4: 21, 5: 20, 6: 896})