# import pandas as pd
import pandas as pd

# Take the cars dataset
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names , 'drives_right':dr , 'cars_per_cap':cpc}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# Adapt for loop to print out country_label and only cars per cap
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row["cars_per_cap"]))

# code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

print(cars)

# Using .apply() is a more effiecient way to add a column by calling a function 
cars["COUNTRY"] = cars["country"].apply(str.upper)