# opperations using numpy
import numpy as np
def array_operations():
    # Step 1: Create a 1D array of 6 elements
    array = np.array([1, 2, 3, 4, 5, 6])

    # Step 2: Reshape into a 2x3 array (2 rows, 3 columns)
    reshaped_array = array.reshape((2, 3))
    print("Original 2x3 Array:\n", reshaped_array)

    # Step 3: Transpose the array (flip rows and columns)
    transposed_array = reshaped_array.T
    print("Transposed 3x2 Array:\n", transposed_array)

    # Step 4: Iterate over all elements in the reshaped array using .flat
    print("Iterating over all elements in the reshaped array:")
    for element in reshaped_array.flat:
        print(element, end=' ') 
    print()  # New line after iteration


# array_operations() artihmetic operations using numpy
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print("Addition:     ", arr1 + arr2)     # [11 22 33]
print("Subtraction:  ", arr1 - arr2)     # [9 18 27]
print("Multiplication:", arr1 * arr2)    # [10 40 90]
print("Division:     ", arr1 / arr2)     # [10. 10. 10.]
print("Power:        ", arr1 ** 2)       # [100 400 900]

# Statistical & Aggregate Functions
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Sum:      ", np.sum(arr))        # 21
print("Mean:     ", np.mean(arr))       # 3.5
print("Max:      ", np.max(arr))        # 6
print("Row-wise sum:", np.sum(arr, axis=1))  # [6 15]
print("Col-wise max:", np.max(arr, axis=0))  # [4 5 6]

# Logical Operations
arr = np.array([1, 2, 3, 4, 5])
print("Greater than 3:", arr > 3)       
# [False False False  True True]
print("Logical AND:", np.logical_and(arr > 2, arr < 5))
# [False  True  True False False]
print("Logical OR:", np.logical_or(arr < 2, arr > 4))
# [ True False False False  True]

#  Universal Functions (ufuncs)
arr = np.array([1, 2, 3, 4, 5])
print("Square root:", np.sqrt(arr))    # [1.         1.41421356 1.73205081 2.         2.23606798]
print("Exponential:", np.exp(arr))     # [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
print("Logarithm:", np.log(arr))       # [0.         0. 69314718 1.09861229 1.38629436 1.60943791]  

# np.sin(), np.cos(), np.abs(), np.tan(), np.arcsin(), np.arccos(), np.arctan() can also be used for trigonometric and absolute value operations.
arr = np.array([0, np.pi/2, np.pi])
print("Sine:", np.sin(arr))            # [0. 1. 0.]
print("Cosine:", np.cos(arr))          # [ 1. 0. -1.]

#maths functions
# | Function        | Purpose                     | Example                                   |
# | --------------- | --------------------------- | ----------------------------------------- |
# | `np.add(a, b)`  | Element-wise addition       | `np.add([1, 2], [3, 4])` → `[4, 6]`       |
# | `np.subtract()` | Subtraction                 | `np.subtract([3, 5], [1, 2])` → `[2, 3]`  |
# | `np.multiply()` | Element-wise multiplication | `np.multiply([2, 3], [4, 5])` → `[8, 15]` |
# | `np.divide()`   | Element-wise division       | `np.divide([10, 20], [2, 5])` → `[5. 4.]` |
# | `np.power()`    | Exponentiation              | `np.power([2, 3], 2)` → `[4, 9]`          |
# | `np.mod()`      | Modulus (remainder)         | `np.mod([10, 20], [3, 4])` → `[1, 0]`     |

import numpy as np

# Arrays
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])

# Math operations
add_result = np.add(a, b)          # Element-wise addition
sub_result = np.subtract(a, b)     # Element-wise subtraction
mul_result = np.multiply(a, b)     # Element-wise multiplication
div_result = np.divide(a, b)       # Element-wise division
pow_result = np.power(a, 2)        # Square of each element in a
mod_result = np.mod(a, b)          # Remainder after division

# Display
print("a:           ", a)
print("b:           ", b)
print("Add:         ", add_result)
print("Subtract:    ", sub_result)
print("Multiply:    ", mul_result)
print("Divide:      ", div_result)
print("Power (a^2): ", pow_result)
print("Modulus:     ", mod_result)

# output:
# a:            [10 20 30]
# b:            [3 5 7]
# Add:          [13 25 37]
# Subtract:     [ 7 15 23]
# Multiply:     [30 100 210]
# Divide:       [3.33333333 4.         4.28571429]
# Power (a^2):  [100 400 900]
# modulus:      [1 0 2]


# Exponential & Logarithmic   
# | Function      | Description | Example                           |
# | ------------- | ----------- | --------------------------------- |
# | `np.exp(x)`   | `e^x`       | `np.exp([1, 2])` → `[2.71, 7.38]` |
# | `np.log(x)`   | Natural log | `np.log([1, np.e])` → `[0, 1]`    |
# | `np.log2(x)`  | Base-2 log  | `np.log2([1, 8])` → `[0, 3]`      |
# | `np.log10(x)` | Base-10 log | `np.log10([1, 100])` → `[0, 2]`   |

import numpy as np

# Array of positive numbers
x = np.array([1, 2, 4, 10, np.e, 100])

# Apply exponential and logarithmic functions
exp_result     = np.exp(x)       # e^x
log_result     = np.log(x)       # Natural log (ln x)
log2_result    = np.log2(x)      # Base-2 log
log10_result   = np.log10(x)     # Base-10 log

# Display results
print("Original x:       ", x)
print("Exponential e^x:  ", exp_result)
print("Natural Log ln(x):", log_result)
print("Log base 2:       ", log2_result)
print("Log base 10:      ", log10_result)
# output:
# Original x:        [  1.           2.           4.           10.           2.71828183 100.        ]
# Exponential e^x:   [  2.71828183   7.3890561   54.59815003 22026.46579481   15.15426224 2.68811714e+43]
# Natural Log ln(x): [0.         0.69314718 1.38629436 2.30258509 1.         4.60517019]
# Log base 2:        [0.         1.         2.         3.32192809 1.44269504 6.64385619]
# log base 10:       [0.         0.30103    0.60205999 1.         0.43429448 2.         ]


# Trigonometric Functions
# | Function       | Description       | Example                              |
# | -------------- | ----------------- | ------------------------------------ |
# | `np.sin(x)`    | Sine              | `np.sin(np.pi/2)` → `1.0`            |
# | `np.cos(x)`    | Cosine            | `np.cos(0)` → `1.0`                  |
# | `np.tan(x)`    | Tangent           | `np.tan(np.pi/4)` → `1.0`            |
# | `np.arcsin()`  | Inverse sine      | `np.arcsin(1)` → `π/2`               |
# | `np.deg2rad()` | Degrees → Radians | `np.deg2rad([90, 180])` → `[π/2, π]` |
# | `np.rad2deg()` | Radians → Degrees | `np.rad2deg([np.pi])` → `180`        |

import numpy as np

# Step 1: Start with angles in degrees
angles_deg = np.array([0, 30, 45, 60, 90])

# Step 2: Convert degrees to radians
angles_rad = np.deg2rad(angles_deg)

# Step 3: Trigonometric functions
sin_values = np.sin(angles_rad)
cos_values = np.cos(angles_rad)
tan_values = np.tan(angles_rad)

# Step 4: Inverse trig (arcsin) — limited to values between -1 and 1
# We'll use the sin_values from step 3
arcsin_radians = np.arcsin(sin_values)
arcsin_degrees = np.rad2deg(arcsin_radians)

# Display all results
print("Angles (Degrees):   ", angles_deg)
print("Radians:            ", angles_rad)
print("Sine:               ", sin_values)
print("Cosine:             ", cos_values)
print("Tangent:            ", tan_values)
print("Arcsin (Radians):   ", arcsin_radians)
print("Arcsin (Degrees):   ", arcsin_degrees)
# output:
# Angles (Degrees):    [ 0 30 45 60 90]
# Radians:             [0.         0.52359878 0.78539816 1.04719755 1.57079633]
# Sine:                [0.         0.49999999 0.70710678 0.8660254  1.        ]
# Cosine:              [ 1.          0.8660254   0.70710678  0.49999999  6.123234e-17]
# Tangent:             [ 0.          0.57735027  1.          1.73205081  1.63312394e+16]
# Arcsin (Radians):    [0.         0.52359878 0.78539816 1.04719755 1.57079633]
# arcsin (Degrees):    [ 0. 30. 45. 60. 90.]


#  Rounding & Absolute
# | Function     | Description               | Example                         |
# | ------------ | ------------------------- | ------------------------------- |
# | `np.round()` | Rounds to nearest integer | `np.round(3.14159, 2)` → `3.14` |
# | `np.floor()` | Rounds **down**           | `np.floor([1.8])` → `1.0`       |
# | `np.ceil()`  | Rounds **up**             | `np.ceil([1.2])` → `2.0`        |
# | `np.abs()`   | Absolute value            | `np.abs([-2, 3])` → `[2, 3]`    |

import numpy as np

# Array with positive and negative decimal values
arr = np.array([-3.7, -2.2, -1.5, 0, 1.3, 2.6, 3.9])

# Rounding and absolute operations
rounded     = np.round(arr, 1)   # Round to 1 decimal place
floored     = np.floor(arr)      # Round down
ceiled      = np.ceil(arr)       # Round up
absolute    = np.abs(arr)        # Make all positive

# Display results
print("Original:       ", arr)
print("Rounded (1dp):  ", rounded)
print("Floored:        ", floored)
print("Ceiled:         ", ceiled)
print("Absolute:       ", absolute)
# output:
# Original:        [-3.7 -2.2 -1.5  0.   1.3  2.6  3.9]
# Rounded (1dp):   [-3.7 -2.2 -1.5  0.   1.3  2.6  3.9]
# Floored:         [-4. -3. -2.  0.  1.  2.  3.]
# Ceiled:          [-3. -2. -1.  0.  2.  3.  4.]
# absolute:        [3.7 2.2 1.5 0.  1.3 2.6 3.9]


#  Comparison Functions
# | Function         | Description | Example         |
# | ---------------- | ----------- | --------------- |
# | `np.greater()`   | `a > b`     | `[True, False]` |
# | `np.less()`      | `a < b`     |                 |
# | `np.equal()`     | `a == b`    |                 |
# | `np.not_equal()` | `a != b`    |                 |

import numpy as np

a = np.array([5, 10, 15, 20])
b = np.array([10, 10, 10, 10])

# Comparison operations
greater        = np.greater(a, b)        # a > b
less           = np.less(a, b)           # a < b
equal          = np.equal(a, b)          # a == b
not_equal      = np.not_equal(a, b)      # a != b
greater_equal  = np.greater_equal(a, b)  # a >= b
less_equal     = np.less_equal(a, b)     # a <= b

# Display results
print("a:              ", a)
print("b:              ", b)
print("a > b:          ", greater)
print("a < b:          ", less)
print("a == b:         ", equal)
print("a != b:         ", not_equal)
print("a >= b:         ", greater_equal)
print("a <= b:         ", less_equal)
# output:
# a:               [ 5 10 15 20]
# b:               [10 10 10 10]
# a > b:           [False False  True  True]
# a < b:           [ True False False False]
# a == b:          [False  True False False]
# a != b:          [ True False  True  True]
# a >= b:        [False  True  True  True]
# a <= b:        [ True  True False False]






    