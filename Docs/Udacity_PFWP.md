# Lesson 2: Data Types and Operators 

## Artihmetic Operators

### Question 1: My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result

#### Answer: print((23 +32 +64) / 3)

### Question 3 : My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result.

#### print(((3+ 32))+ -15//2) Bad Formatting
#### print((17 - 6)%(5 + 2)) Good Formatting
#### print ((1 + 2 + 4) / 13) Bad Formatting
#### print(4/2 - 7*7) Good Formatting

# Lesson 5 - Variables and Asisnment Operators

### mv_population = 74728 
* where mv_population is the variable 
* = is the assignment operator
* 74728 is the value of the variable

### Assign and modify variables

#### My Answer: 

* The current volume of a water reservoir (in cubic metres)

reservoir_volume = 4.445e8

* The amount of rainfall from a storm (in cubic metres)

rainfall = 5e6

* decrease the rainfall variable by 10% to account for runoff
    
rainfall = rainfall + (rainfall * -0.1)

* add the rainfall variable to the reservoir_volume variable

reservoir_volume = rainfall + reservoir_volume

* increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm

reservoir_volume = reservoir_volume + (reservoir_volume * 0.05)

* decrease reservoir_volume by 5% to account for evaporation

reservoir_volume = reservoir_volume + (reservoir_volume * -0.05)

* subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume -= 2.5e5

* print the new value of the reservoir_volume variable

print(reservoir_volume)

* Answer 

   447627500.0 

* The current volume of a water reservoir (in cubic metres)

reservoir_volume = 4.445e8

* The amount of rainfall from a storm (in cubic metres)

rainfall = 5e6

* decrease the rainfall variable by 10% to account for runoff

rainfall *= .9

* add the rainfall variable to the reservoir_volume variable

reservoir_volume += rainfall

* increase reservoir_volume by 5% to account for stormwater that flows
* into the reservoir in the days following the storm

reservoir_volume *= 1.05

* decrease reservoir_volume by 5% to account for evaporation

reservoir_volume *= 0.95

* subtract 2.5e5 cubic metres from reservoir_volume to account for water
* that's piped to arid regions.

reservoir_volume -= 2.5e5 

* print the new value of the reservoir_volume variable

print(reservoir_volume)

# Integers and Floats 

* There are two Python data types that could be used for numeric values:

int - for interger values
float - for decimal or floating point values

x = int(4.7) # x is now an integer 4
y = float(4) # y is now a float of 4.0

# you can check the type by using the 'type' function:

>>> print(type(x))
int

>>> print(type(y))
float

#### you can check length of strings using len()

name_length = len(given_name + middle_names + family_name)

# Data Types in Python

* int example 4
* float example 4.2
* boolean example True
* string example "hi"

#Converting types 

* you can convert types like this str(9) this would convert the number 9 into a string
* int(4.4) would result in 4 as it converted the float into a interger 

#Methods 

* Methods are a function that "belongs" to an object, that object in this case is a string 

## The .format method

my_dog = "Sam"
my_name = "Doug"

### one way

print ("My name is {}, my dogs name is {}".format(my_name, my_dog))

### another way

my_sentence = "My name is {}, my dogs name is {}"
print(my_sentence.format(my_name, my_dog))

# The .split method 

* .split splits the string into a list

# \n 

* By using the \n you cause a line break which creates a new line in the same string

# Other String Methods 

* len() find the length of the string
* .index() finds the first occurance in the string
* .rindex() find the last occurance in the string
* .count() finds the total amount of times 'it' is used in the string

# List and Membership Operators 

## Slicing

* You can pull more than one value from a list at a time by using the slicing. When using slicing remember **lower** index is **inclusive** and the **upper** indexdd is **exclusive**

>>> list_of_random_things = [1, 3.4, 'a string', True]

* includes index at 1 but is exclusive of the index at 2 
>>> list_of_random_things[1:2]
[3.4]

* return all elements upto but not including the listed index
>>> list_of_random_things[:2]
[1, 3.4]

* return all elements to the end of the list
>>> list_of_random_things[1:]
[3.4, 'a string', True]

# Mutability 

* Whether an object can change its values after it has been created 
    * Lists are a mutable data type 
    * Strings are an immutable data type

## Keep in mind

**It's important to keep in mind two things for each data type you are using:**

1. Are the mutable?
2. Are they ordered?

# List Methods 

* len() returns how many elements are in a list
* max() returns the greatest element of the list. How the greatest element is determined. For a number is would be the highest number or the highest alphabetical
* min() is the opposite of max
* sorted() returns a copy of the list in order from smallest to largest leaving the list unchanged
    * You can use the reverse=True argument to sort the list in reverse
* join() 

# Data Types

* An integer is a data type. But it isn't a data structure
    * A data type is just a way to classify data. A list is a data structure and a data type. 
* A data type is just a type that classifies data. This can include a primitive (basic) data types like integers, booleans and strings, as well as data structure like lists. 
* Data structures are containers that organise and group data types together. 

# Tuple
 
* A data type for immutable ordered sequences of elements 
* Tuples are contained within parentheses ()
* Tuples can be indexed and sliced like a list

# Set 

* A data type for mutable unordered collections of **unique elements**
* you can add an element to a set with add()
* Using pop() you can remove a random element from the set
* A set cannot be sliced like a list or a tuple
* A set is defined with {} like dictionaries 

set_example = {element1, element2, element3}

# Dictionary 

* A dictionary is a mutable, unordered data structure that contains mappings of keys to values. Because these keys are used to index values, they must be unique and immutable

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

* Dictionaries can have keys of any immutable type, whether it be integers, tuples or strings

* A data type for mutable objects that store mappings of unique keys to values 
    * So they are like lists and sets but they store pairs of values 
    * A key for a dictionary must be immutable, like str, int, float or boolean

dictionary_example = {}

* In python if you use a empty set of {} python will assign it an empty dictionary to that variable
    * You can use set() to define an empty set
    * OR dict() to define an empty dictionary too

## Identity Operators 

* is  - evaualates if both sides have the same identity
* is not - evaulates if both sides have different identities

## get with a Default Value 

>>> elements.get('dilithium')
None
>>> elements['dilithium']
KeyError: 'dilithium'
>>> elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"


