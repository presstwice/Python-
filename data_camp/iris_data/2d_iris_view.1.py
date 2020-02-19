# Import modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
iris = pd.read_csv('iris_data/iris.txt', sep=',', 
                               names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

print(iris.head())

print(iris['species'].describe())

hello = iris[iris['species'] == 'Iris-setosa']

print(hello)


