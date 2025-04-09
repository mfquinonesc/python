# Rounding Decimals 
# There are primarily five ways of rounding off decimals in NumPy
# truncation, fix, rounding, floor, ceil

# Truncation
# Remove the decimals, and return the float number closest to zero. use the trunc() and fix() functions.

import numpy as np 
arr = np.trunc([-3.1666, 3.6667])
print(arr)

# Rounding 
# The around() function increments preceding digit or decimal by 1 if >= 5 else do nothing
# E.g. round off to 1 decimal point, 3.166666 is 3.2 

import numpy as np 
arr = np.around(3.1666,2)
print(arr)


# Floor 
# The floo() function rounds off decimal to nearest lower integer. 
# E.g. floor of 3.1666 is 3

import numpy as np 
arr = np.floor([-3.1666, 3.6667])
print(arr)

# Ceil 
# The ceil() function rounds off decimal to nearest upper integer.
# E.g ceil of 3.166 is 4

import numpy as np
arr = np.ceil([-3.1666, 3.6667])
print(arr)


