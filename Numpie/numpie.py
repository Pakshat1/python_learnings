
# numpy is a powerful library for numerical computations in Python.
# It provides support for arrays, matrices, and many mathematical functions.    
import numpy as np
# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
# output: 1D Array: [1 2 3 4 5]

# Create a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
# output:
# 2D Array:
# [[1 2 3]      
#  [4 5 6]]

# show the shape, data type, number of dimensions, size, item size, and total bytes consumed by the array
print("Shape of 2D Array:", array_2d.shape)
# output: Shape of 2D Array: (2, 3) 
print("Data type of 2D Array:", array_2d.dtype)
# output: Data type of 2D Array: int64
print("Number of dimensions of 2D Array:", array_2d.ndim)
# output: Number of dimensions of 2D Array: 2
print("Size of 2D Array:", array_2d.size)
# output: Size of 2D Array: 6
print("Item size of 2D Array:", array_2d.itemsize)
# output: Item size of 2D Array: 8 (for int64)
print("Total bytes consumed by 2D Array:", array_2d.nbytes)
# output: Total bytes consumed by 2D Array: 48 (6 elements * 8 bytes each)

# Create a 3D array (tensor)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)
# output:
# 3D Array:
# [[[1 2]
# [3 4]]
# [[5 6]
# [7 8]]]
# # Show the shape, data type, number of dimensions, size, item size, and total bytes consumed by the 3D array
print("Shape of 3D Array:", array_3d.shape)
# output: Shape of 3D Array: (2, 2, 2)
print("Data type of 3D Array:", array_3d.dtype)
# output: Data type of 3D Array: int64
print("Number of dimensions of 3D Array:", array_3d.ndim)
# output: Number of dimensions of 3D Array: 3
print("Size of 3D Array:", array_3d.size)
# output: Size of 3D Array: 8
print("Item size of 3D Array:", array_3d.itemsize)
# output: Item size of 3D Array: 8 (for int64)
print("Total bytes consumed by 3D Array:", array_3d.nbytes)
# output: Total bytes consumed by 3D Array: 64 (8 elements * 8 bytes each)

# Create an array of zeros
array_zeros = np.zeros((2, 3))
print("Array of Zeros:", array_zeros)
# output: Array of Zeros:[0. 0. 0.]

# Create an array of ones
array_ones = np.ones((2, 3))
print("Array of Ones:", array_ones)
# output: Array of Ones:[1. 1. 1.]

# Create an array of a specific shape filled with a constant value
array_full = np.full((2, 3), 7)
print("Array filled with 7:\n", array_full)
# output:
# Array filled with 7:
# [[7 7 7]
#  [7 7 7]]

# Create an identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)
# output:
# Identity Matrix:
# [[1. 0. 0.]   
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Create a random array
random_array = np.random.rand(2, 3)
print("Random Array:\n", random_array)  
# output: Random Array:
# [[0.12345678 0.23456789 0.3456789 ]
#  [0.45678901 0.56789012 0.67890123]]

# Create a range of numbers
range_array = np.arange(10) 
print("Range Array:", range_array)
# output: Range Array: [0 1 2 3 4 5 6 7 8 9]

# Create a linearly spaced array
linspace_array = np.linspace(0, 1, 5)
print("Linearly Spaced Array:", linspace_array)
# output: Linearly Spaced Array: [0.   0.25 0.5  0.75 1.  ]

# Reshape an array
reshaped_array = np.arange(12).reshape((3, 4))
print("Reshaped Array:\n", reshaped_array)
# output:
# Reshaped Array:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Transpose an array
transposed_array = reshaped_array.T 
# or transposed_array = np.transpose(reshaped_array)
import numpy as np

# Step 1: Create a 1D array of 6 elements
array = np.array([1, 2, 3, 4, 5, 6])

# Step 2: Reshape into a 2x3 array (2 rows, 3 columns)
reshaped_array = array.reshape((2, 3))
print("Original 2x3 Array:\n", reshaped_array)

# Step 3: Transpose the array (flip rows and columns)
transposed_array = reshaped_array.T
print("Transposed 3x2 Array:\n", transposed_array)


# itrator over all array elements using .flat
print("Iterating over all elements in the reshaped array:")
for element in reshaped_array.flat:
    print(element, end=' ')
# output:
# Iterating over all elements in the reshaped array:    
# 1 2 3 4 5 6 
# convets to another data type
converted_array = reshaped_array.astype("bool ,float")
print("Converted Array to Float:\n", converted_array)
# output:
# Converted Array to Float:
# [[1. 2. 3.]
#  [4. 5. 6.]]
#   















