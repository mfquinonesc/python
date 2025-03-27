import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray

# We can create a Numpy ndarray object by using the array() function.

import numpy as np 

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

import numpy as np 
arr = np.array((1,2,3,4,5))
print(arr)


# Dimensions in Arrays 
# 0-D Arrays, or Scalars, are the elements in an arry. Each value in an array is a = 0-D array 
import numpy as np 

arr = np.array(42)
print(arr)

# 1-D Arrays 
# An array that has 0-D arrays as its elements is called nui-dimentional or 1-D array
# These are the most common and basic arrays 

import numpy as np 
arr = np.array([1,2,3,4,5])
print(arr)

# 2-D Arrays 
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors 

# NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

import numpy as np 
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

# 3-D Arrays 
# An array that has 2-D arrays (matrices) as its elements is called 3-D array 
# These are often used to represent a 3rd order tensor 

import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print('tensor')
print(arr)


# Check Number of Dimensions? 
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have. 

import numpy as np 

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3,],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions 
# When the array is created, you can define the number of dimensions by using ndmin argument.

import numpy as np 
arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
