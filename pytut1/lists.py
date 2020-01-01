lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Susan", "Tory", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)

#indexes [] start at 0 
#you can use negative indexes [-0] to start counting from the back of a list, if you start at the back the index starts a -1
#If you want to count indexes after a point [X:] will count that and anything past that
# .extend adds two list together 
# .append adds another item to the list at the end
# .insert(X) adds at the index assigned everything else is pushed to right
# .remove(X) removes from the list 
# .clear() removes everything off the list
# .pop() removes the last element in the list 
# .index(X) search for something and it returns which index it is at
# .count(X) tells you have many of these items appear on the list 
# .sort() sorts the list in ascending/aplhabetical order 
# .reverse() reverses the list
# .copy() copies from an existing list 