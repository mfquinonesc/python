# Iterating Arrays 
# Iterating means going through elements one by one 
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

import numpy as np 
arr  = np.array([1,2,3])
for x in arr:  
    print(x) 

# Iterating 2-D Arrays 
# In a 2-D array it will go through al the rows

import numpy as np 
arr = np.array([[1,2,3],[4,5,6]])
for x in arr: 
    print(x)

# Iterating 2-D array
# To return the actual values, the scalars, we have to iterate the arrays in each dimension 
import numpy as np 
arr = np.array([[1,2,3],[4,5,6]])
for x in arr: 
    for y in x: 
        print(y)

# Iterating 3-D Arrays 
# In a 3-D array it will go throuhg all the 2-D arrays

import numpy as np 
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr: 
    print(x)

# To return the actual values,  the scalars, we have to iterate the arrays in each dimension. 

import numpy as np 
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr: 
    for y in x: 
        for z in y: 
            print(z)

# Iterating Arrays Usng nditer() 
# The function nditer() is a helping function that can be used from very advanced iterations. It solves some basic issues whcich we face in iteration, lets go through it eith examples

import numpy as np 
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types 
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating 
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other sace to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']

import numpy as np 
arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterating With Different Step Size
# We can use filtering 
import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:,::2]):
    print(x)

import numpy as np

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


# Enumerate on following 2D array's elements: 

import numpy as np 
arr = np.array([[1,2,3,4],[5,6,7,8]])
for idx, x in np.ndenumerate(arr): 
    print(idx,x)

