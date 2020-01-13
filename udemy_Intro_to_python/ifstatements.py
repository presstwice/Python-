points = 174 # use this input to make your submission

# write your if statement here

points = 174

# their code 

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

# my code 

# write your if statement here

if points in range(51,150):
    print("Oh dear, no prize this time.")
else:
    if points in range(151,180):
        prize = "wafer-thin mint"
    if points in range(181,200):
        prize = "penguin"
    if points in range(1,50):
        prize = "wooden rabbit"
    print("Congratulations! You won a {}!".format(prize))
