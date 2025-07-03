# indexing  in numpy

import numpy as np
# Indexing in NumPy arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])    # 10
print(arr[-1])   # 50 (last element)
print(arr[1:4])  # [20 30 40] (elements from index 1 to 3)
print(arr[:3])   # [10 20 30] (first three elements)

# 2D and 3D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[0, 1])   # 2 (row 0, column 1)
print(arr2d[1][2])   # 6 (same, using chained indexing)
print(arr2d[:, 1])   # [2 5] (all rows, column 1)
print(arr2d[1, :])   # [4 5 6] (row 1, all columns)
print(arr2d[0:2, 1:3])  # [[2 3] [5 6]] (subarray from rows 0-1 and columns 1-2)

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d[0, 1, 0])  # 3 (first 2D array, second row, first column)
print(arr3d[:, 0, 1])  # [2 6] (all first rows, second column)
print(arr3d[1, :, 0])  # [5 7] (second 2D array, all rows, first column)
print(arr3d[0:2, 1, :])  # [[3 4] [7 8]] (subarray from both 2D arrays, second row, all columns)

# Boolean indexing
arr = np.array([5, 10, 15, 20])
print(arr[arr > 10])   # [15 20]
print(arr[arr < 15])   # [5 10]
print(arr[arr % 5 == 0])  # [ 5 10 15 20]

# Conditional indexing with 2D arrays
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d[arr2d > 2])  # [3 4]

# Fancy indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])  # [10 30 50]

# Fancy indexing with 2D arrays
arr2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2d[[0, 2]])    # rows 0 and 2
print(arr2d[[0, 1], [1, 0]])  # [2 3] (manual pair selection)


# Combining boolean and fancy indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 20][[0, 1]])
# [30 40] (first two elements greater than 20)

# Combining boolean and fancy indexing with 2D arrays
arr2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2d[arr2d[:, 0] > 2][[0, 1]])  
# [[3 4] [5 6]] (rows where first column > 2, then select first two rows)

# Combining boolean and fancy indexing with 3D arrays
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d[arr3d[:, :, 0] > 2][[0, 1]])
# [[[5 6] [7 8]]] (3D array where first column > 2, then select first two elements) 


# slicilng in numpy
# Slicing in NumPy arrays   

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # [2 3 4] (elements from index 1 to 3)
print(arr[:3])   # [1 2 3] (first three elements)   

print(arr[2:])   # [3 4 5] (elements from index 2 to end)
print(arr[-3:])  # [3 4 5] (last three elements

print(arr[::2])  # [1 3 5] (every second element)
print(arr[::-1])  # [5 4 3 2 1] (reversed array)    

# Slicing in 2D arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])  
# [[2 3] [5 6]] (subarray from rows 0-1 and columns 1-2)
print(arr2d[:, 1])  
# [2 5 8] (all rows, column 1)
print(arr2d[1, :])  
# [4 5 6] (row 1, all columns)
print(arr2d[0:2, :])  
# [[1 2 3] [4 5 6]] (subarray from rows 0-1, all columns)

# Slicing in 3D arrays
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d[0, :, :])
# [[1 2] [3 4]] (first 2D array, all rows and columns)
print(arr3d[:, 0, :])
# [[1 2] [5 6]] (all first rows, all columns)
print(arr3d[:, :, 1])
# [[2 4] [6 8]] (all 2D arrays, second column)
print(arr3d[0:2, 1, :])
# [[[3 4] [7 8]]] (subarray from both 2D arrays, second row, all columns)   

arr = np.array([0, 10, 20, 30, 40, 50, 60])
print(arr[1:5])       # [10 20 30 40]
print(arr[:3])        # [0 10 20]
print(arr[::2])       # [0 20 40 60]
print(arr[::-1])      # reversed: [60 50 40 30 20 10 0]


# 2D array slicing
import numpy as np

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print(arr2d[0:2, 1:3])  # [[20 30] [50 60]] (subarray from rows 0-1 and columns 1-2)
print(arr2d[:, 1])      # [20 50 80] (all rows, column 1)
print(arr2d[1, :])      # [40 50 60] (row 1, all columns)
print(arr2d[0:2, :])    # [[10 20 30] [40 50 60]] (subarray from rows 0-1, all columns)

# 3D array slicing
arr3d = np.array([[[1, 2], [3, 4]], 
                   [[5, 6], [7, 8]]])
print(arr3d[0, :, :])  # [[1 2] [3 4]] (first 2D array, all rows and columns)
print(arr3d[:, 0, :])  # [[1 2] [5 6]] (all first rows, all columns)
print(arr3d[:, :, 1])  # [[2 4] [6 8]] (all 2D arrays, second column)
print(arr3d[0:2, 1, :])  # [[[3 4] [7 8]]] (subarray from both 2D arrays, second row, all columns)

# 
print(arr2d[0])  # [10 20 30]

print(arr2d[:, 0])  # [10 40 70]
print(arr2d[0, :])  # [10 20 30]
print(arr2d[1, 1])  # 50 (element at row 1, column 1)
print(arr2d[1:3, 0:2])  # [[40 50] [70 80]] (subarray from rows 1-2 and columns 0-1)

print(arr2d[0:2, 1:3])  # [[20 30]
                        #  [50 60]]
print(arr2d[:, 1])      # [20 50 80] (all rows, column 1)
print(arr2d[1, :])      # [40 50 60] (row 1, all columns)
print(arr2d[0:2, :])    # [[10 20 30]
                        #  [40 50 60]] (subarray from rows 0-1, all columns)    

print(arr2d[-1])  # [70 80 90]
print(arr2d[:, -1])  # [30 60 90] (all rows, last column)
print(arr2d[-1, :])  # [70 80 90] (last row, all columns)
print(arr2d[-2:, -2:])  # [[50 60]













