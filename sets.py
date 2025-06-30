# set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# union
set_union = set1.union(set2)
print("Union:", set_union)
# output: Union: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection
set_intersection = set1.intersection(set2)
print("Intersection:", set_intersection)
# output: Intersection: {4, 5}

# update
set1.update(set2)
print("Updated Set1:", set1)    
# output: Updated Set1: {1, 2, 3, 4, 5, 6, 7, 8}

# intersection update
set1.intersection_update(set2)  
print("Intersection Updated Set1:", set1)
# output: Intersection Updated Set1: {4, 5}

# difference
set_difference = set1.difference(set2)
print("Difference:", set_difference)
# output: Difference: {1, 2, 3}

# symmetric difference
set_symmetric_difference = set1.symmetric_difference(set2)  
print("Symmetric Difference:", set_symmetric_difference)
# output: Symmetric Difference: {1, 2, 3, 6, 7, 8}

# isdisjoint
is_disjoint = set1.isdisjoint(set2)
print("Is Disjoint:", is_disjoint)
# output: Is Disjoint: False

# isjioint with empty set
empty_set = set()   
is_disjoint_empty = set1.isdisjoint(empty_set)
print("Is Disjoint with Empty Set:", is_disjoint_empty)
# output: Is Disjoint with Empty Set: True

# issubset
is_subset = set1.issubset(set2) 
print("Is Subset:", is_subset)
# output: Is Subset: False

# issuperset
is_superset = set1.issuperset(set2)
print("Is Superset:", is_superset)
# output: Is Superset: False

# copy
set_copy = set1.copy()
print("Copied Set:", set_copy)
# output: Copied Set: {4, 5}

# clear
set1.clear()    
print("Cleared Set1:", set1)
# output: Cleared Set1: set()

# frozen set
frozen_set = frozenset([1, 2, 3,5, 6, 7, 8])
print("Frozen Set:", frozen_set)
# output: Frozen Set: frozenset({1, 2, 3, 5, 6, 7, 8})

# frozen set operations
frozen_set_union = frozen_set.union({9, 10})
print("Frozen Set Union:", frozen_set_union)
# output: Frozen Set Union: frozenset({1, 2, 3, 5, 6, 7, 8, 9, 10})

frozen_set_intersection = frozen_set.intersection({3, 4, 5})
print("Frozen Set Intersection:", frozen_set_intersection)
# output: Frozen Set Intersection: frozenset({3, 5})

frozen_set_difference = frozen_set.difference({1, 2})
print("Frozen Set Difference:", frozen_set_difference)
# output: Frozen Set Difference: frozenset({3, 5, 6, 7, 8})

frozen_set_symmetric_difference = frozen_set.symmetric_difference({5, 6, 9})
print("Frozen Set Symmetric Difference:", frozen_set_symmetric_difference)  
# output: Frozen Set Symmetric Difference: frozenset({1, 2, 3, 7, 8, 9})

# frozen set is immutable, so we cannot update it
# frozen_set.update({10})  # This will raise an AttributeError  
# but we can create a new frozen set
new_frozen_set = frozen_set.union({10}) 
print("New Frozen Set:", new_frozen_set)
# output: New Frozen Set: frozenset({1, 2, 3, 5, 6, 7, 8, 10})

# frozen set is hashable, so it can be used as a key in a dictionary
frozen_set_dict = {frozen_set: "This is a frozen set"}  
print("Frozen Set Dictionary:", frozen_set_dict)
# output: Frozen Set Dictionary: {frozenset({1, 2, 3, 5, 6, 7, 8}): 'This is a frozen set'}

# frozen set can be used in sets
frozen_set_in_set = {frozen_set, frozenset([9, 10])}
print("Frozen Set in Set:", frozen_set_in_set)
# output: Frozen Set in Set: {frozenset({1, 2, 3, 5, 6, 7, 8}), frozenset({9, 10})}

# frozen set can be used in lists
frozen_set_in_list = [frozen_set, frozenset([9, 10])]
print("Frozen Set in List:", frozen_set_in_list)    
# output: Frozen Set in List: [frozenset({1, 2, 3, 5, 6, 7, 8}), frozenset({9, 10})]

# frozen set can be used in tuples
frozen_set_in_tuple = (frozen_set, frozenset([9, 10]))
print("Frozen Set in Tuple:", frozen_set_in_tuple)
# output: Frozen Set in Tuple: (frozenset({1, 2, 3, 5, 6, 7, 8}), frozenset({9, 10}))

# frozen set can be used in dictionaries
frozen_set_in_dict = {frozen_set: "Frozen Set Value", frozenset([9, 10]): "Another Frozen Set Value"}
print("Frozen Set in Dictionary:", frozen_set_in_dict)  
# output: Frozen Set in Dictionary: {frozenset({1, 2, 3, 5, 6, 7, 8}): 'Frozen Set Value', frozenset({9, 10}): 'Another Frozen Set Value'}  


