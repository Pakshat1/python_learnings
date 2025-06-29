
# recursion  
# factorial function
# This function calculates the factorial of a number using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
     
print(factorial(5))  #output: 120

#  fibonacci function
# This function calculates the nth Fibonacci number using recursion.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
print(fibonacci(10))  #output: 55

# gcd function
# This function calculates the greatest common divisor (GCD) of two numbers using recursion.
# The GCD is the largest positive integer that divides both numbers without leaving a remainder.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48, 18))  #output: 6    

# power function
# This function calculates the power of a number using recursion.   
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
print(power(3, 4))  #output: 81

# sum of digits function
# This function calculates the sum of the digits of a number using recursion.   
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(12345))  #output: 15

# reverse a string function
# This function reverses a string using recursion.  
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))  #output: "olleh"

# check if a string is a palindrome function
# This function checks if a string is a palindrome using recursion. 
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])
print(is_palindrome("racecar"))  #output: True
print(is_palindrome("hello"))    #output: False
