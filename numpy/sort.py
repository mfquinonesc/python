# Sorting Arrays 
# Sorting means putting alements in an ordered sequence.
# The NumPy ndarray object has a function called sort(), that will sort a specified array

import numpy as np 
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


import numpy as np 
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))


import numpy as np 
arr = np.array([True, False, True])
print(np.sort(arr))

# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted

import numpy as np 
arr = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))


