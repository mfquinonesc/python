# Random Data Distribution 
# A random distribution is a set of random numbers that follow a certain probability density function 

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3 , 0.6 , 0.0], size=(100))
print(x)

# Same example as above, but return a 2-D array with 3 rows, each containing 5 values

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print(x)