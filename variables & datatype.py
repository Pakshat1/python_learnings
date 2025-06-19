#  input 2 numbres and print sum

first=int(input("enter first number: "))
second=int(input("enter second number: "))

print("sum= " ,(first + second))


# input side of a squre and print area

side=float(input("enter the value of side:"))

print("area=",(side*side))

# # input 2 floating number and print the avrage

a=float(input("enter a:"))
b=float(input("enter b:"))

print("avg=",(a+b)/2)

# input 2 int numbers,a and b print if a is grater or equal to b , if not print false

a=int(input("enter a:"))
b=int(input("enter b:"))

print(a>=b)

# # Define a function named string_length that takes one argument, str1.
def stringth_length(str):
    count=0
    for char in str:
        count+= 1
    return count
print(stringth_length("hello my name is Akshat"))


# # WAP to input users first name and print the length

name=input("enrtr your name: ")
print("length of your name is",len(name))

