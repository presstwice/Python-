
# Question 1
start_num = 5 #provide some start number
end_num = 20 #provide some end number that you stop when you hit
count_by = 4 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# Question 2 my answer
start_num = 21 #provide some start number
end_num = 20 #provide some end number that you stop when you hit
count_by = 4 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
result = start_num


if start_num > end_num: 
    print("Oops! Looks like your start value is greater than the end value. Please try again.")
else:
    while result < end_num:
        result += count_by
    print(result)

    # Question 2 their answer 

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)