# Finding GCD (Great Common Devisor)
# The GDC, also known as highest common factor is the biggest number that is a common factor of both of the numbers

import numpy as np

num1 = 6 
num2 = 9 

x = np.gcd(num1, num2) 
print(x)

# Finding GCD in arrays 
# To find the highest common factor of all values in an array, you can use the reduce() method. 

import numpy as np 

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x) 