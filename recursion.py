
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

