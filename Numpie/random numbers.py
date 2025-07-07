# rannodm numbers in numpy

# | Function              | Description                                     |
# | --------------------- | ----------------------------------------------- |
# | `np.random.rand()`    | Random float numbers in \[0, 1)                 |
# | `np.random.randint()` | Random integers in a range                      |
# | `np.random.randn()`   | Random floats from standard normal distribution |
# | `np.random.choice()`  | Randomly select elements from a list or array   |
# | `np.random.shuffle()` | Shuffle an array in-place                       |
# | `np.random.seed()`    | Fix randomness for reproducibility              |


import numpy as np

# Fix the random seed for reproducibility
np.random.seed(42)

# 1. Generate random floats in range [0, 1)
rand_floats = np.random.rand(3)
print("Random floats in [0, 1):", rand_floats)

# 2. Generate random integers between 10 and 50 (exclusive)
rand_ints = np.random.randint(10, 50, size=5)
print("Random integers from 10 to 49:", rand_ints)

# 3. Random numbers from standard normal distribution (mean=0, std=1)
rand_normal = np.random.randn(4)
print("Random normal values:", rand_normal)

# 4. Randomly choose 3 values from a given list
choices = np.random.choice([100, 200, 300, 400], size=3)
print("Randomly selected values:", choices)

# 5. Shuffle an array in-place
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled array:", arr)

