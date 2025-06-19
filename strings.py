# taking input from user 

a=input("enter your name:")
print("my name is",a)

x=input("enter the value: ")
y=input("enter the value: ")
print(int(x)+int(y))

# strings 

name="Akshat"

print("hello,"+ name)


# multistring

fruits="""apple,
banana,
cat"""
print(fruits)

# indxing the string

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print("lets use for loop\n")
for character in fruits:
    print(character)

#  length of a string

name="Akshat,Akshar,Shubham"
print(len(name))

 # slicing

name="Akshat,Akshar"
print(name[0:3])
print(name[-6:-3])
print(len(name))

nm="Harry"
print(nm[-4:-2])

