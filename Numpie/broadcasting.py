# broadcasting
import numpy as np
# Broadcasting allows NumPy to perform operations on arrays of different shapes.
# It automatically expands the smaller array to match the shape of the larger one.

# Example 1: Adding a scalar to an array
array_1 = np.array([1, 2, 3])
scalar = 5
result_1 = array_1 + scalar
print("Result of adding scalar to array:", result_1)
# Output: Result of adding scalar to array: [6 7 8]

# Example 2: Adding two arrays of different shapes
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
array_3 = np.array([10, 20, 30])
result_2 = array_2 + array_3
print("Result of adding two arrays with broadcasting:\n", result_2)
# Output:
# Result of adding two arrays with broadcasting:
# [[11 22 33]
#  [14 25 36]]

# Example 3: Broadcasting with 2D and 1D arrays
array_4 = np.array([[1, 2, 3], [4, 5, 6]])
array_5 = np.array([[10], [20]])
result_3 = array_4 + array_5
print("Result of broadcasting 2D and 1D arrays:\n", result_3)
# Output:
# Result of broadcasting 2D and 1D arrays:
# [[11 12 13]
#  [24 25 26]]

# Example 4: Broadcasting with different dimensions
array_6 = np.array([[1, 2], [3, 4]])
array_7 = np.array([10, 20])
result_4 = array_6 + array_7[:, np.newaxis]
print("Result of broadcasting with different dimensions:\n", result_4)
# Output:
# Result of broadcasting with different dimensions:
# [[11 12]
#  [23 24]]

# Example 5: Broadcasting with higher dimensions
array_8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array_9 = np.array([[10, 20], [30, 40]])
result_5 = array_8 + array_9[:, np.newaxis, :]
print("Result of broadcasting with higher dimensions:\n", result_5)
# Output:
# Result of broadcasting with higher dimensions:
# [[[11 12]
#   [13 14]]
#  [[35 36]
#   [37 38]]]

              

