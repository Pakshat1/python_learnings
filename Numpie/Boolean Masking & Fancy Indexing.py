import numpy as np

# Boolean Masking & Fancy Indexing

# | Topic               | Function/Concept                         | What it does                               |
# | ------------------- | ---------------------------------------- | ------------------------------------------ |
# | **Boolean Masking** | `arr > 5`, `arr == val`                  | Select elements based on condition         |
# | **`np.where()`**    | `np.where(condition, if_true, if_false)` | Replace or choose values conditionally     |
# | **Fancy Indexing**  | `arr[[0, 2, 4]]`                         | Access multiple indices using list/array   |
# | **`np.nonzero()`**  | `np.nonzero(condition)`                  | Get positions of non-zero or True elements |

# example
arr = np.array([1, 4, 6, 8, 3, 7, 2])

# Boolean Masking: select elements greater than 5
mask = arr > 5
print("Elements > 5:", arr[mask])  # [6 8 7]

# np.where: replace values less than 5 with 0, others with 1
result = np.where(arr < 5, 0, 1)
print("np.where result:", result)  # [0 0 1 1 0 1 0]

# Fancy Indexing: access elements at positions 0, 2, 4
fancy = arr[[0, 2, 4]]
print("Fancy indexing:", fancy)  # [1 6 3]

# np.nonzero: get indices where elements are even
even_indices = np.nonzero(arr % 2 == 0)
print("Indices of even elements:", even_indices[0])  # [1 2 3 6]

# | Function        | Use Case                                | 
# | --------------- | --------------------------------------- |
# | `np.argwhere()` | Like `nonzero()` but returns 2D indices | 
# | `np.extract()`  | Extract values using a condition mask   | 
# | Chained masking | `(arr > 5) & (arr < 10)`                | 

# np.argwhere: returns indices where condition is True (as 2D array)
argwhere_indices = np.argwhere(arr % 2 == 0)
print("np.argwhere (even elements):", argwhere_indices.flatten())  # [1 2 3 6]

# np.extract: extract values using a condition mask
extracted = np.extract(arr > 5, arr)
print("np.extract (elements > 5):", extracted)  # [6 8 7]

# Chained masking: elements greater than 5 and less than 10
chained_mask = (arr > 5) & (arr < 10)
print("Chained mask (6 < arr < 10):", arr[chained_mask])  # [6 8 7]

