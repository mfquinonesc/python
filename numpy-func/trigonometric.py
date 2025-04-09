# Numpy Trigonometric Functions 
# Trignometric Functions
# NumPy provides the ufuncs sin(), cos(), and tan() that take values in radians and produce the corresponding sin, cos, and tan  values. 


import numpy as np 

x = np.sin(np.pi/2)
print(x)

# Find sine values for all of the values in arr: 
import numpy as np 

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

# Convert Degrees Into Radians
# By default all of the trigonometric functions take radians as parameters but we can convert radians to degreea and vice versa as well in Numpy. 

import numpy as np 

arr = np.deg2rad(arr)
x = np.deg2rad(arr)
print(x)


# Finding Angles 
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given. 

import numpy as np 

x = np.arcsin(1.0)
print(x)


# Angles of each value in arrays 
# Find the angle for all of the sine values in the array 

import numpy as np 

arr = np.array([1, -1 , 0.1])
x = np.arcsin(arr)
print(x)

# Hypotenues 
# Find hypotenues using pythagoras theorem in NumPy.
# NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

import numpy as np

base = 3 
perp = 4 

x = np.hypot(base, perp)
print(x)
