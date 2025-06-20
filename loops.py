# for loop

color="red blue green yellow"
for color in color:
    print(color)
   
for i in color:
    print(i)


# practice 1

colors="red blue green yellow"
for color in colors:
    print(color )


#   range()

for k in range(0,10):
    print(k+2)

# calculate factorial
n=(int(input("enter the number")))
factorial=1
if n<0:
    print("factorial does not exixt for negative number")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}.")

# range(start , stop , step)

for k in range(2,20,2):
    print(k)
