# string opperations

# upper() & lower()

str1="AbcDefGhi"
print(str1.upper())
print(str1.lower())

# rstrip()

name=("@xat,@x@r!!!!!!!")
print(name.rstrip("!"))

# replace()

a="@axt"
print(a.replace("@","A"))

# split()

A=("Akshat Akshar Akshay ")
print(A.split(" "))

# capatilize()

nm=("introduction to Python")
print(nm.capitalize())

# center()

AB=("welcome to Python")
print(AB.center(100))

# count()
A=("my name is AK, AK is a good guy, AK!")
print(A.count("AK"))

# endswith()

print(A.endswith("!"))

# find()
print(A.find("is"))

# isalnum & isalpha 

# A=("wellcomeToPython")
print(A.isalnum())
print(A.isalpha())

# islower()
C=("AKSHAT")
L=("akshat")
print(C.islower())
print(L.islower())
