# import packages
import pandas as pd
import numpy as np

# Import the CSV to a DataFrame
ebola = pd.read_csv('cleaning_data/ebola_data.csv')

print(type(ebola))

# Print the head of ebola_melt
print(ebola.head())