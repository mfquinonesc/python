# NumPy Filter Array

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering 

import numpy as np 

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

# Creating the Filter Array 
# Creating a filter array that will return only values higher than 42:

import numpy as np 
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# Go through each element in arr 
for element in arr: 
    # if the element is higher than 42, set the value to True, otherwise False
    if element > 42: 
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


# Create a filter array that  will return only even elements from the original array:

import numpy as np 

arr = np.array([1,2,3,4,5,6,7])

# Create an empty list 
filter_arr = [] 

# Go through each element in arr 
for element in arr:
    # If the element is completely divisible by 2, set the vaue to True, otherwise False
    if element % 2 == 0:
        filter_arr.append(True)
    else: 
        filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating Filter Directly Form Array 

import numpy as np 

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


import numpy as np 
arr = np.array([1,2,3,4,5,6,7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
