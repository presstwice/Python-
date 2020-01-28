# zip accepts an arbitary number of itterables and returns a itterators of tuples 

avengers = ['hawkeye', 'iron man', 'thor', 'quicksilver']
names = ['barton', 'stark', 'odinson', 'maximoff']

z = zip(avengers, names)
print(*z)