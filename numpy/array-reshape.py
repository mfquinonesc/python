# Numpy Array Reshaping 
# Reshaing arrays 
# Reshaping means changing the shape of an array
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension 

# Reshape From 1-D to 2-D

# Convert the following 1-D array with 12 elements into an 2-D array 
# The outermost dimension will have 4 arrays, each with 3 elements: 

import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)


# Reshape From 1-D to 3-D
# Convert the following 1-D array with 12 elements into a 3-D array: 
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements. 

import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)


# Returns Copy or View? 
# Check if the returned array is a copy or a view: 
import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)

# Unknown Dimension 
# You are allowed to have one "unknown" dimension
# Meaning that you do not have to specify an exact number for one the dimsnsions in the reshape method.
# Pas -1 as the value, and NumPy will calculate this numebr for you

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr) 

# Flattening the arrays 
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this 

import numpy as np 
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
newarr = arr.reshape(-1)
print(newarr)

