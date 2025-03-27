# Numpy Array Slicing 
# Slicing arrays 
# Slicing in python means taking elements from one given index to another given index.

import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

# We can slice instead of index like this: [start,end]
# We can also define the step, li this: [start,end,step]
# If we don't pass start its considerd 0 
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[4:])

import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[:4])

# Negative Slicing 
# Use the minus operator to refer to an index from the end:

import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

# STEP 
# use the step value to determine the step of the slicing:

import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])


import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
print(arr[::2])

# Slicing 2-D Arrays 
# From the second element, slice elements from index 1 to 4 (not included)
import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])

# From both elements, return index 2: 
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
import numpy as np 
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2, 1:4])
