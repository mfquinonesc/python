# NumPy Data Types
# Data Types in Python 
# By default Python have these data types: 

# strings, integer, float, boolean, complex

# Data Types in NumPy 
import numpy as np 
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# Create Arrays With a Defined Data Type
import numpy as np 
arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)


# Create an array with data type 4 bytes integer:
import numpy as np 
arr = np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)


# Create data type from float to integer by using 'i' as parameter value: 
import numpy as np 
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print('arr', arr)
print('newarr',newarr)
print(newarr.dtype)


# Change data type from float to integer by using int as parameter value: 
import numpy as np

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean 

import numpy as np 
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
