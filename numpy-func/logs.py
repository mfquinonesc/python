# Logs 

# NumPy provides functions to perform log at the base 2, e and 10.
# We will also explore how we can take log for any base by creating a custom ufunc.
# All of the functions will place -inf or inf in the elements if the log can not be computed.

# Log at base 2 
# Use log at base 2 of all elements of following array: 

import numpy as np 
arr = np.arange(1, 10)
print(np.log2(arr))

# Log al base 10 
# Use the log10() function to perform log at the base 10.

import numpy as np 
arr = np.arange(1, 10)
print(np.log10(arr))

# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e. 

import numpy as np 
arr = np.arange(1, 10)
print(np.log(arr))

# Log at Any Base 
# NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter: 

from math import log 
import numpy as np 

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
