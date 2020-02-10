# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gminder = pd.read_csv('gapminder_life_expectancy/life_expectancy_years.csv')

print(gminder.columns)

# change country to life expectancy
gminder_new = gminder.columns.values; gminder_new[0] = 'Life expectancy'

# Print gminder head
print(gminder.head())

# Melt gminder: gminder_melt
gminder_melt = pd.melt(frame=gminder, id_vars ='Life expectancy')

# Rename the columns 
gminder_melt.columns = ['Country', 'year', 'life_expectancy']

# Print the head of gminder_melt
print(gminder_melt.head())

# Check the column types to see if anything is not as expected
print(gminder_melt.dtypes)

# Convert the year column to numeric
gminder_melt.year = pd.to_numeric(gminder_melt['year'])

# Test if country is of type object
assert gminder_melt.Country.dtypes == np.object

# Test if year is of type int64
assert gminder_melt.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gminder_melt.life_expectancy.dtypes == np.float64

# Print again to see that year has been changed to numeric
print(gminder_melt.dtypes)

# Create the series of countries: countries
countries = gminder_melt['Country']

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)

print(gminder_melt.shape)

# Assert that country does not contain any missing values
assert pd.notnull(gminder_melt.Country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gminder_melt.year).all()

# Drop the missing values
gapminder = gminder_melt.dropna()

# Print the shape of gapminder
print(gminder_melt.shape)

# Add first subplot
plt.subplot(2, 1, 1) 

# Create a histogram of life_expectancy
gminder_melt.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gminder_melt_agg = gminder_melt.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gminder_melt_agg.head())

# Print the tail of gapminder_agg
print(gminder_melt_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gminder_melt_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gminder_melt.to_csv('gapminder_life_expectancy/gapminder.csv')
gminder_melt_agg.to_csv('gapminder_life_expectancy/gapminder_agg.csv')