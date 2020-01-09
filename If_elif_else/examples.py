import math
import os
import random
import re
import sys

# Example 1 
    n = int()

weird = "Weird";
notWeird = "Not Weird"

## check if input is even
if n % 2 == 0:
    # Print "Not Weird" if input is greater than 20
    if n > 20:
        print(notWeird)
    # Input is not greater than 20
    # Print "Weird" if input is greater than or equal to 6 (which checks range between 6 -20)
    elif n >= 6:
        print(weird)
    # Input is not in the range of 6 - 20
    # Print "Not Weird" if input is greater or equal to 2 (which checks range between 2 - 5)
    elif n >= 2:
        print(notWeird)
    else: 
        pass
else: print(weird)

# Example 2 

n = int ()

if n % 20 != 0:
    status = "Weird"
elif n in range(2,5):
    status = "Not Weird"
elif n range in(6,20):
    status = "Weird"
elif n > 20:
    status = "Not Weird"
else: 
    personaility = "Weird"

print(status)

# Example 3 

if n % 2 == 0:
    if n > 20:
        status = "Not Weird"
    elif n >= 6: 
        status = "Weird"
    elif n >= 2:
        status = "Not Weird"
    else:
        pass
else: 
   status = "Weird"

print(status)
