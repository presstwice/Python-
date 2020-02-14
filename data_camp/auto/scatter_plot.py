import pandas as pd
import matplotlib.pyplot as plt

# Import the data
df = pd.read_csv('auto/auto-mpg.txt', names=['mpg', 'cyl', 'displ', 'hp', 'weight', 'accel' 'yr', 'origin'], delim_whitespace=True)

# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg')

# Add the title
plt.title('Fuel efficiency vs Horse-Power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()

# Make a list of column names to be plotted:
cols = ['weight', 'mpg']

# Generate the plot
df[cols].plot(kind='box', subplots=True)

# Display the plot
plt.show()