# Create Your Own ufuunc 

# How to create your own ufunc

# To create your own ufunc, you have to define a function, like you do with normal functions in python, then you add it to your NUmPy ufunc library with the frompyfunc() method.
# The frompyfunc() method takes the following arguments: 
# 1. function - the name of the function 
# 2. inputs - the number of input arguments (arrays)
# 3. outputs - the number of output arrays

import numpy as np 

def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Check if a Function is a ufunc
# Check the type of a function to check if it is a ufunc or not 
# A ufunc should return <class 'numpy.ufunc'>

import numpy as np 
print(type(np.add))

# If it is not ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays: 

import numpy as np 
print(type(np.concatenate))

# Use an if statement to check if the fu ction is a ufunc or not:

import numpy as np

if type(np.add) == np.ufunc:
    print('add is ufunc')
else: 
    print('add is not ufunc')

