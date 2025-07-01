# error handling (try, except, else, finally)


# def divide_numbers(num1, num2):
#     try:
#         result = num1 / num2
#     except ZeroDivisionError as e:
#         print(f"Error: Cannot divide by zero. {e}")
#         return None
#     except TypeError as e:
#         print(f"Error: Invalid input type. {e}")
#         return None
#     else:
#         return result
#     finally:
#         print("Execution of divide_numbers completed.")
# print(divide_numbers(10, 0))       
# print(divide_numbers(10, 'a'))
# print(divide_numbers(10, 5))
# Output:
# Error: Cannot divide by zero. division by zero    
# Execution of divide_numbers completed.
# Error: Invalid input type. unsupported operand type(s) for /: 'int' and 'str'
# Execution of divide_numbers completed.
# 2.0
# Execution of divide_numbers completed.
# Note: The finally block always executes, regardless of whether an exception occurred or not.
# This is useful for cleanup actions, such as closing files or releasing resources. 


# Example of using try, except, else, and finally
import os   

# Step 1: Create 'example.txt' if it doesn't exist
example_file_path = 'example.txt'
if not os.path.exists(example_file_path):
    with open(example_file_path, 'w') as file:
        file.write("Hello, Ak!")

# Step 2: Function to read files with exception handling
def read_file(file_path):
    try:
        file = open(file_path, 'r')
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        return None
    else:
        content = file.read()
        return content
    finally:
        if 'file' in locals():
            file.close()
            print("File closed.")

# Step 3: Test both files
print(read_file('non_existent_file.txt'))
print(read_file('example.txt'))
# Output:
# Error: File not found. [Errno 2] No such file or directory: 'non_existent_file.txt'
# File closed.  
# None
# Hello, Ak!
# File closed.
# Note: The finally block ensures that the file is closed whether an exception occurs or not.
# This is important for resource management and preventing memory leaks.    
# Step 4: Clean up by removing 'example.txt'
if os.path.exists(example_file_path):
    os.remove(example_file_path)
    print(f"Removed {example_file_path}")
else:
    print(f"{example_file_path} does not exist.")
# Output:
# Removed example.txt   
# Note: The code above demonstrates how to handle file operations with error handling.
# It ensures that resources are properly managed and exceptions are handled gracefully.


# Example of using try, except, else, and finally with a custom exception
class CustomError(Exception):
    """Custom exception for demonstration purposes."""
    pass
def risky_operation():
    try:
        # Simulating a risky operation that raises a custom exception
        raise CustomError("light weigth!! BUDDY .")
    except CustomError as e:
        print(f"CustomError caught: {e}")
    else:
        # This block executes if no exceptions were raised
        print("No errors occurred.")
    finally:
        print("Risky operation completed.")
# Step 5: Test the risky operation
print(risky_operation( ))
# Output:
# CustomError caught: This is a custom error message.   
# Risky operation completed.
# None  
# Note: This example shows how to define and raise a custom exception.
# It demonstrates the use of try, except, else, and finally blocks to handle errors gracefully
# and ensure that cleanup actions are performed.

# Example of using try, except, else, and finally with a context manager
class FileManager:
    """Context manager for file operations."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        print("FileManager context exited.")
# Step 6: Use the context manager to write to a file
def write_to_file(file_path, content):  
    try:
        with FileManager(file_path) as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    else:
        print("File written successfully.")
# Step 7: Test the context manager
write_to_file('context_example.txt', 'Hello, Context Manager!') 
# Output:
# File written successfully.
# FileManager context exited.
# # Note: This example demonstrates how to use a context manager to handle file operations.
# It ensures that the file is properly closed after use, even if an error occurs.
# # The context manager simplifies resource management and makes the code cleaner.
# # Step 8: Clean up by removing 'context_example.txt'
if os.path.exists('context_example.txt'):
   os.remove('context_example.txt')
print("Removed context_example.txt")  
# Output:
# Removed context_example.txt
      

# raising costom error
class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    pass
def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 120:
        raise InvalidAgeError("Age is unrealistically high.")
    else:
        print(f"Valid age: {age}")
# Step 9: Test the validate_age function
try:
    validate_age(-5)    
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
try:
    validate_age(150)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
try:
    validate_age(25)
except InvalidAgeError as e:
    print(f"InvalidAgeError caught: {e}")
# Output:
# InvalidAgeError caught: Age cannot be negative.
# InvalidAgeError caught: Age is unrealistically high. 
# Valid age: 25
# Note: This example demonstrates how to define and raise a custom exception for input validation.
# It shows how to handle specific error conditions and provide meaningful error messages.








