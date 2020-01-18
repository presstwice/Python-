num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# start each of the values, how many odd numbers count_odd, the total of the odd numbers list_sum
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

#  while count_odd is less than 5 and use len(num_list) to look at number in the list
while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0: # using num_list[i] to go through the list % 2 != 0 to check if there is any carry if is then its an odd number
        list_sum += num_list[i] # add the number to the list_sum 
        count_odd += 1 # adds 1 to the counter list stops at 5
    i += 1 #adds 1 to the list index going to the next number in the list 

print ("The numbers of odd numbers added are: {}".format(count_odd)) 
print ("The sum of the odd numbers added is: {}".format(list_sum))