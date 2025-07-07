#  | Topic         | Function(s)                             | Description                                 |
# | ------------- | --------------------------------------- | ------------------------------------------- |
# | **Reshape**   | `reshape()`                             | Change the shape without changing data      |
# | **Flatten**   | `ravel()`, `flatten()`                  | Convert multi-dimensional → 1D              |
# | **Transpose** | `transpose()`, `.T`                     | Swap rows and columns                       |
# | **Resize**    | `resize()`                              | Resize array in-place (can fill with zeros) |
# | **Stacking**  | `hstack()`, `vstack()`, `concatenate()` | Join arrays along axes                      |


import numpy as np

# Step 1: Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])
print(" Original 1D array:")
print(arr)
print("Shape:", arr.shape)   # (6,)

# Step 2: Reshape to 2x3
reshaped_2x3 = arr.reshape(2, 3)
print("\n Reshaped to 2x3:")
print(reshaped_2x3)
print("Shape:", reshaped_2x3.shape)

# Step 3: Reshape to 3x2
reshaped_3x2 = arr.reshape(3, 2)
print("\n Reshaped to 3x2:")
print(reshaped_3x2)
print("Shape:", reshaped_3x2.shape)

# Step 4: Reshape to 6x1 (column vector)
reshaped_6x1 = arr.reshape(6, 1)
print("\n Reshaped to 6x1 (column vector):")
print(reshaped_6x1)
print("Shape:", reshaped_6x1.shape)

# Step 5: Flatten back to 1D using ravel() (view)
flat_ravel = reshaped_2x3.ravel()
print("\n Flattened using ravel():")
print(flat_ravel)
print("Shape:", flat_ravel.shape)

# Step 6: Flatten back to 1D using flatten() (copy)
flat_flatten = reshaped_2x3.flatten()
print("\n Flattened using flatten():")
print(flat_flatten)
print("Shape:", flat_flatten.shape)

# Step 7: Transpose the 2x3 array
transposed = reshaped_2x3.T
print("\n Transposed 2x3 → 3x2:")
print(transposed)
print("Shape:", transposed.shape)




