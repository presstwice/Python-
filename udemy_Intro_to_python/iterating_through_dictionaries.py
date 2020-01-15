cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

# the below example just prints the keys from the dictionary above using a for loop
print("Iterating through keys:")
for key in cast:
    print(key)

# this is example iterates through both key and value pairs, using the inbuilt method .items
print("\nIterating through keys and values:")
for key, value in cast.items(): # using the cast.items and key, value you can print both the pairs
    print("Actor: {}    Role: {}".format(key, value)) # here we use the .format method to assign key and value a respective cast and role 

