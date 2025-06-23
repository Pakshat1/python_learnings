# find geometric mean of two numbers

# def geometric_mean(a, b):
#     mean = (a * b) / (a + b)
#     print("Geometric mean of", a, "and", b, "is", mean)

# def isGrater(a, b):
#     if (a > b):
#        print(a, "is greater than", b)
#     else:
#        print(b, "is greater than", a)

# def isless(a, b):
#     pass

# a=6
# b=8
# geometric_mean(a, b)
# isGrater(a, b)
               
# c=8
# d=3
# geometric_mean(c, d)
# isGrater(c, d)

# function returning multiple values
def calculate(a, b):
    sum = a + b
    diff = a - b
    prod = a * b
    div = a / b if b != 0 else None  # Avoid division by zero
    return sum, diff, prod, div

a=4
b=8
print(calculate(a, b))
