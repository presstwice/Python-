import scipy.io
import matplotlib.pyplot as pyplot
import numpy as np

mat = scipy.io.loadmat('ASCB/data1.mat')

print(type(mat))

# Print the keys of the MATLAB dictionary 
print(mat.keys())

