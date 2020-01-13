verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary

# apprently this isn't the answer
unique_values = [key for (key,value) in verse_dict.items() if value == 1]
print (len(unique_values))

# this is the answer
num_keys = len(verse_dict)
print(num_keys


# find whether 'breathe' is a key in the dictionary
if 'breathe' in verse_dict:
    print('Breathe is here!')
if 'breathe' not in verse_dict:
    print('Your an idiot!')


# create and sort a list of the dictionary's keys
sorted_keys = verse_dict.keys()

print(sorted_keys)
# get the first element in the sorted list of keys
keycap = sorted(sorted_keys)
print(keycap)

# find the element with the highest value in a list of values
highest_value = max(verse_dict, key=lambda key: verse_dict[key])
print(highest_value)

# find the element with the highest value in the list of keys
highest_keywords = max(verse_dict)
print(highest_keywords)
