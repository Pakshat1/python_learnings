# sorting 

import numpy as np

# Original array
arr = np.array([12, 5, 7, 1, 20])
print("  Original Array:", arr)

#  np.sort() – Full sort
sorted_arr = np.sort(arr)
print("\n Sorted Array using np.sort():", sorted_arr)

#  np.argsort() – Get indices that would sort the array
sort_indices = np.argsort(arr)
print(" Sort Indices using np.argsort():", sort_indices)
print("    Sorted using indices:", arr[sort_indices])

#  np.searchsorted() – Where to insert elements in sorted array
to_insert = [10, 15]
insertion_indices = np.searchsorted(sorted_arr, to_insert)
print("\n Insert positions for [10, 15] in sorted array:", insertion_indices)

#  np.partition() – Partial sort: first 3 smallest elements
partitioned = np.partition(arr, 2)
print("\n Partitioned array (3 smallest elements first):", partitioned)
