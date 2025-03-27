# NumPy Array Shape
# The shape of an array i the number of elements in each dimension 

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that retruns a tuple with each index having the number of corresponding elements 

import numpy as np 
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)

# Create an array with 5 dimension using ndmin using a vector with values 1,2,3,4, and verify that lat dimension has value 4: 

import numpy as np 
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('Shape of array :', arr.shape)

# What does a tuple represent? 
# Integers at every index tells about the number of elements the corresponding dimension has.
# In the example above at index-4 we have value 4, so we can say that 5th (4 + 1th) dimension has 4 elements 