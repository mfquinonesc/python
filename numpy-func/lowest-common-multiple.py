# LCM Lowest Common Multiple 
# The lowest Common Multiple is the smallest number that is a common multiple o two numbers 

import numpy as np 

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

# Finding LCM in Arrays 
# To find the lowest common multiple of all values in an array, you can use the reduce() method. 

import numpy as np 

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)


# Find the LCm of all values of an array  where the array contains all integers from 1 to 10

import numpy as np 

arr = np.arange(1, 11) 
x = np.lcm.reduce(arr)
print(x)
