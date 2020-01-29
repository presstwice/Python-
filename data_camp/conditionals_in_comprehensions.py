# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create a list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) > 6]

# Print the new list
print(new_fellowship)

# What if instread of not printing it, we instead inserted a empty string
other_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

print(other_fellowship)