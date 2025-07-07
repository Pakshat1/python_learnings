
# Aggregate & Statistical Functions

# | Function Type       | Examples                         | Use Case              |
# | ------------------- | -------------------------------- | --------------------- |
# | **Aggregate**       | `sum`, `prod`, `cumsum`          | Total, product        |
# | **Statistics**      | `mean`, `median`, `std`, `var`   | Central tendency      |
# | **Min/Max & Arg**   | `min`, `max`, `argmin`, `argmax` | Extremes & indices    |
# | **Axis Operations** | All above functions with `axis`  | Row/column-wise stats |

# example 1
import numpy as np 

# Basic Aggregate Functions
import numpy as np

arr= np.array([[1,2],
               [3,4]])

print(np.sum(arr))
print(np.sum(arr ,axis=0))
print(np.sum(arr, axis=1))

# output =10
# output = [4,6]
# output = [3,7]

#np.prod() – Product of all elements

print(np.prod(arr))           
print(np.prod(arr, axis=0))
print(np.prod(arr, axis=1))

# Statistical Functions
print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

print(np.median(arr))
print(np.std(arr))
print(np.var(arr))

# Min/Max & Arg Functions
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))

print(np.min(arr, axis=0))
print(np.max(arr, axis=1))
print(np.argmin(arr, axis=1))
print(np.argmax(arr, axis=0))

# Cumulative Functions
print(np.cumsum(arr))
print(np.cumsum(arr, axis=0))
print(np.cumsum(arr, axis=1)) 

# | Function          | Description            | Axis Support | Returns      |
# | ----------------- | ---------------------- | ------------ | ------------ |
# | `sum`             | Total                  | Yes          | Total/array  |
# | `prod`            | Product                | Yes          | Total/array  |
# | `cumsum`          | Cumulative sum         | Yes          | 1D array     |
# | `mean`            | Average                | Yes          | Float/array  |
# | `median`          | Middle value           | Yes          | Float        |
# | `std` / `var`     | Spread of values       | Yes          | Float        |
# | `min`/`max`       | Smallest/largest value | Yes          | Scalar/array |
# | `argmin`/`argmax` | Index of min/max       | No           | Integer      |







