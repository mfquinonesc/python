# NumPy Summations 

# Summations 
# What is the difference between summation and addition? 
# Addition is done between two arguments whereas summation happens over n elements 

import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)
print(newarr)


import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr)

# Summation Over an Axis
# If you specify axis = 1, NumPy will sum the numbers ineach array

import numpy as np 

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2],axis=1)
print(newarr)

# Cummulative Sum 
# Cummulative sum means partialy adding the elements in array.
import numpy as np 
arr = np.array([1, 2, 3, 4])
newarr = np.cumsum(arr)
print(newarr)


