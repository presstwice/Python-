import re

string_1 = 'I eat 5 vegatables and 2 fruit a day'

vegfruit = re.findall('\d+', string_1)

print(vegfruit)