import numpy as np

# Array Joining, Stacking, and Splitting

# Joining arrays using concatenate
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined = np.concatenate((arr1, arr2))
print("Concatenated:", joined)

# Stacking arrays vertically and horizontally
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
v_stacked = np.vstack((arr3, arr4))
h_stacked = np.hstack((arr3, arr4))
print("Vertically stacked:\n", v_stacked)
print("Horizontally stacked:\n", h_stacked)

# Splitting arrays
arr5 = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.array_split(arr5, 3)
print("Split into 3 parts:", split_arr)

# Splitting 2D arrays
arr6 = np.array([[1, 2, 3], [4, 5, 6]])
split_2d = np.hsplit(arr6, 3)
print("2D horizontally split:", split_2d)

