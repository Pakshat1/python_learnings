# Dictionary in Python  
# A dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
# Dictionaries are defined using curly braces `{}` with key-value pairs separated by a colon `:`.

# Example of a dictionary
my_dict = {"name": "Alice","age": 30,"city": "New York"}
# Accessing values in a dictionary
print("Name:", my_dict["name"])  # Output: Name: Alice
print("Age:", my_dict["age"])    # Output: Age: 30
print("City:", my_dict["city"])  # Output: City: New York

# Adding a new key-value pair
my_dict["country"] = "USA"
print("Updated Dictionary:", my_dict)
# Output: Updated Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair
del my_dict["age"]
print("Dictionary after deletion:", my_dict)
# Output: Dictionary after deletion: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice   
# city: New York
# country: USA      

# Checking if a key exists in a dictionary
if "name" in my_dict:
    print("Name exists in the dictionary")  
else:
    print("Name does not exist in the dictionary")
# Output: Name exists in the dictionary

# Dictionary methods
# Getting keys, values, and items   

my_dict = {"name": "Alice", "city": "New York", "country": "USA"}
print("Keys:", my_dict.keys())      # Output: Keys: dict_keys(['name', 'city', 'country'])
print("Values:", my_dict.values())  # Output: Values: dict_values(['Alice', 'New York', 'USA'])
print("Items:", my_dict.items())    # Output: Items: dict_items([('name', 'Alice'), ('city', 'New York'), ('country', 'USA')])

# Copying a dictionary
dict_copy = my_dict.copy()
print("Copied Dictionary:", dict_copy)
# Output: Copied Dictionary: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# Clearing a dictionary
my_dict.clear()
print("Cleared Dictionary:", my_dict)
# Output: Cleared Dictionary: {}

# Reinitializing the dictionary for further examples
my_dict = {"name": "Alice", "age": 30, "city": "New York"}      
# Merging dictionaries
another_dict = {"country": "USA", "occupation": "Engineer"}
merged_dict = {**my_dict, **another_dict}
print("Merged Dictionary:", merged_dict)

# Output: Merged Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA', 'occupation': 'Engineer'}   

# Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print("Nested Dictionary:", nested_dict)
# Output: Nested Dictionary: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}

# Accessing nested dictionary values
print("Person1 Name:", nested_dict["person1"]["name"])  # Output: Person1 Name: Alice
print("Person2 Age:", nested_dict["person2"]["age"])    # Output: Person2 Age: 25  

# Dictionary with mixed data types
mixed_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "grades": [85, 90, 95],
    "address": {"city": "New York", "zip": "10001"}
}
print("Mixed Dictionary:", type(mixed_dict))
# Output: Mixed Dictionary: <class 'dict'>
print("Mixed Dictionary:", mixed_dict)
# Output: Mixed Dictionary: {'name': 'Alice', 'age': 30, 'is_student': False, 'grades': [85, 90, 95], 'address': {'city': 'New York', 'zip': '10001'}}

