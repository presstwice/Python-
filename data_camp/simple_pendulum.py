# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :b # The goal is to get offset to always equal 0 
    print("correcting...") # Prints correcting to clearly state the loop point
    if offset > 0: # You start the if statement by checking if the offset is positive
        offset = offset - 1 # If so bring the offset closer to 0 by -1
    else:
        offset = offset + 1 # if its not positive then it must be negative bring it closer to 0 + 1 
    print(offset)