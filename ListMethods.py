#LIST METHODS 

# list.append() - Adds an element to the end of the list.
l= [1, 2, 3]
l.append(4)
print(l)  
# Output: [1, 2, 3, 4]

# list.sort() - Sorts the list in ascending order.
l = [3, 1, 2]
l.sort()
print(l) 
# Output: [1, 2, 3] 

# list.sort(reverse=True) - Sorts the list in descending order.
l= [3, 1, 2]
l.sort(reverse=True)                        
print(l)
# Output: [3, 2, 1]

# list.reverse() - Reverses the order of the elements in the list.
l = [1, 2, 3, 4,  5, 6, 7, 8, 9, 10]
l.reverse()
print(l.index(5)) 
print(l)     
# Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Output: 5

# list.index(x) - Returns the index of the first occurrence of x in the list.
l = ["apple", "banana", "cherry", "date"]    
print(l.index("banana"))
# Output: 1

# list.count(x) - Returns the number of occurrences of x in the list.
l = [1, 2, 3, 1, 2, 1]
print(l.count(1))
# Output: 3

# list.copy() - Returns a shallow copy of the list.
l = [1, 2, 3]       
l_copy = l.copy()
print(l_copy)   
# Output: [1, 2, 3]

# list.insert(i, x) - Inserts an element x at index i.
l = [1, 2, 3]
l.insert(4, 4)
print(l)  
# Output: [1, 2, 3, 4]

# list.remove(x) - Removes the first occurrence of x from the list.
l = [1, 2, 3, 1, 2, 3]
l.remove(2)
print(l)    
# Output: [1, 3, 1, 2, 3]

# list.extend(iterable) - Extends the list by appending elements from the iterable.
l = [1, 2, 3]
k= [4, 5, 6]
l.extend(k)
print(l)
# Output: [1, 2, 3, 4, 5, 6]






