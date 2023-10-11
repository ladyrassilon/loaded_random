==================
Loaded Random v0.2
==================

Introduction
************
This is a simple library that I originally wrote as part of an interview process, but I got thinking about how I'd rewrite it with what I now know.

The interface is relatively simple, you instantiate the class, with a list of weights, and results for those weights, you then call random() to get your result.

Example Usage
*************

For an example, here's an example showing the result of 2 D6 dice, and the output of the product.

.. csv-table:: Probabilities for totals
   :file: docs/2d6_weighting.csv
   :widths: 4, 25, 8
   :header-rows: 1

So to implement this using the basic ``LoadedRandomNumberChooser``

.. code-block:: python3
    

    from loaded import LoadedRandomNumberChooser

    probabilities = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    random_items = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    two_d6 = LoadedRandomNumberChooser(probabilities=probabilities, random_items=random_items)

    results = [two_d6.random() for _ in range(1000)]

    from collections import Counter

    counted = Counter(results)

    print(counted)

You'll get results of the form

``Counter({7: 146, 6: 137, 8: 126, 5: 125, 10: 101, 9: 100, 4: 85, 3: 65, 11: 62, 12: 34, 2: 19})``

Available implemented loaded choosers
=====================================

* LoadedRandomItemChooser - Choose from a list of items
* LoadedRandomNumberChooser - Choose from a list of numbers
* SystemLoadedRandomItemChooser - Choose from a list of items using the system's more secure random number generator
* SystemLoadedRandomNumberChooser - Choose from a list of numbers using the system's more secure random number generator