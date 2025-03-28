# Normal Distribution 
# The normal Distribution is one of the most important distributions.
# It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss
# It fits the probability distributio of many events, eg IQ Sceores, Heartbeet etc.
# Use the random.normal() method to get a Normal Data Distribution
# It has three parameters

from numpy import random

x = random.normal(size=(2, 3))
print(x)

# Generate a random normal distribution of size 

from numpy import random
x = random.normal(loc=1, scale=2, size= (2, 3))

print(x)

# Visualization of Normal Distribution 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.displot(random.normal(size = 1000), kind= "kde")
plt.show()
