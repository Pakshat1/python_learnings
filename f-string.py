
# Using f-strings for string formatting in Python
name="AK"
print(f"hello, {name}!")
# output: hello, AK!

# Corrected version
name = "AK"         
print(f"hello {name}!")
# output: hello AK!

# Using f-strings with expressions
age = 24        
print(f"{name} is {age} years old.")
# output: AK is 24 years old.

# Using f-strings with multiple variables
city = "New York"       
print(f"{name} lives in {city}.")
# output: AK lives in New York.

# Using f-strings with calculations
x = 5       
y = 10
print(f"The sum of {x} and {y} is {x + y}.")    
# output: 

# Using f-strings with method calls
def greet(name):
    return f"Hello, {name}!"    
print(f"{greet(name)} How are you?")
# output: Hello, AK! How are you?

# Using f-strings with dictionaries
person = {"name": "AK", "age": 24, "city": "New York"}
print(f"{person['name']} is {person['age']} years old and lives in {person['city']}.")
# output: AK is 24 years old and lives in New York.0

# Using f-strings with lists
fruits = ["apple", "banana", "cherry"]  
print(f"My favorite fruits are: {', '.join(fruits)}.")
# output: My favorite fruits are: apple, banana, cherry.

# Using f-strings with conditional expressions
is_student = True
is_student = False
print(f"{name} is {'a student' if is_student else 'not a student'}.")
# output: AK is a student.
# output: AK is not a student.

# Using f-strings with nested expressions
num1 = 3                
num2 = 4
print(f"The product of {num1} and {num2} is {num1 * num2}.")
# output: The product of 3 and 4 is 12.

# Using f-strings with escape characters
quote = "Python is awesome!"        
print(f"She said, \"{quote}\"")
# output: She said, "Python is awesome!"


# Using f-strings with special characters
special_char = "@"  
print(f"This is a special character: {special_char}.")
# output: This is a special character: @.

# Using f-strings with multiline strings
multiline_string = """This is a
multiline string."""
print(f"{multiline_string}")    
# output: This is a
# multiline string.


