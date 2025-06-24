

# operatipns on tuples
# Tuples are immutable sequences in Python, often used to store collections of heterogeneous data.
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Concatenating tuples
another_tuple = (6, 7, 8)   
combined_tuple = my_tuple + another_tuple
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Repeating tuples  
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking membership
print(3 in my_tuple)  # Output: True        

# Finding length
print(len(my_tuple))  # Output: 5   

# Iterating through a tuple
for item in my_tuple:
    print(item, end=' ')  # Output: 1 2 3 4 5
print()         

# Unpacking a tuple
a, b, c, d, e = my_tuple    
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))  
print(nested_tuple[1])  # Output: (2, 3)

# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Output: [1, 2, 3, 4, 5]     

# Converting a list to a tuple
list_to_tuple = tuple(tuple_to_list)        
print(list_to_tuple)  # Output: (1, 2, 3, 4, 5)

# Counting occurrences of an element
print(my_tuple.count(3))  # Output: 1   

# Finding the index of an element
print(my_tuple.index(3))  # Output: 2   

