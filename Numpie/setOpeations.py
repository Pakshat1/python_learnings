# set operations and unique handallings 

# | Function           | Description                       | Output Type   |
# | ------------------ | --------------------------------- | ------------- |
# | `np.unique()`      | Remove duplicates, return sorted  | Sorted array  |
# | `np.intersect1d()` | Elements common in both arrays    | Sorted array  |
# | `np.union1d()`     | All unique elements from both     | Sorted array  |
# | `np.setdiff1d()`   | Elements in `a` but not in `b`    | Sorted array  |
# | `np.in1d()`        | Membership check for each element | Boolean array |

import numpy as np

# Define two arrays
a = np.array([1, 2, 3, 4, 5, 5, 6])
b = np.array([4, 5, 6, 7, 8])

print("Array a:", a)
print("Array b:", b)

# 1. Unique values in array a
unique_a = np.unique(a)
print("\nUnique values in a:", unique_a)  # [1 2 3 4 5 6]

# 2. Common elements in a and b (intersection)
common = np.intersect1d(a, b)
print("Common elements (a ∩ b):", common)  # [4 5 6]

# 3. Union of a and b (all unique values from both)
union = np.union1d(a, b)
print("Union of a and b:", union)  # [1 2 3 4 5 6 7 8]

# 4. Elements in a but not in b (difference)
diff = np.setdiff1d(a, b)
print("Elements in a but not in b:", diff)  # [1 2 3]

# 5. Check which elements of a are in b (membership mask)
mask = np.in1d(a, b)
print("Boolean mask (a[i] in b):", mask)
print("Values from a that are also in b:", a[mask])  # [4 5 5 6]

