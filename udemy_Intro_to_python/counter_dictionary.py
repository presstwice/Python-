book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}
word_counter1 = {}


# example 1
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

#example 2
for word in book_title:
    word_counter1[word] = word_counter1.get(word, 0) + 1

print(word_counter1)

if word_counter == word_counter1:
    print ("It is!")
else:
    print("It's not")