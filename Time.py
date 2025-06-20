
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
#  Your program should use time module to get the current hour.

import time
current_hour=time.localtime().tm_hour

if 5<= current_hour <= 12:
    Greetings="Good Morning sir"
elif 12<= current_hour<=17:
    Greetings="Good afternoon Sir"
elif 17<= current_hour<=21:
    Greetings="Good evening sir"
else:
    Greetings="it's too late Sir, take some rest"

print(Greetings)