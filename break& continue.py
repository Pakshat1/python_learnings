
# | Statement  | What it does               | When to use                       |
# | ---------- | -------------------------- | --------------------------------- |
# | `break`    | Exits the loop immediately | You want to stop completely       |
# | `continue` | Skips current iteration    | You want to skip but keep looping |

# break at 5!
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# Third miltiple of 7:
count = 0

for i in range(1, 100):  
    if i % 7 == 0:
        count += 1
        if count == 3:
            print("Third multiple of 7 is:", i)
#             break


# Use"r input until correct password
while True:
     password= input("Enter Password : ")
     if password == "open123":
          print("Access Granted")
          break
     else:
          print("Try Again")

# mulitiples of 5

for i in range (15):
       print("5 X", i+1,"=",5*(i+1))
       if(i==9):
          break

#  continue statemnt 
for i in range(1,11 ):
    if i %2 == 0:
        continue
    print(i)

# skip specfic value
for i in range(1, 6):
    if i == 4:
        continue
    print(i)

# skipping empty string
names = ["Alice", "", "Bob", "", "Charlie"]
for name in names:
    if name == "":
        continue
    print(name)

