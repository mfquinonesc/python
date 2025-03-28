# Rayleigh Distribution

# Rayleigh distribution
# It has two parameters 
# scale = (standard deviation) decides how flat the distribution will be default 1.0
# size = the shape of the returned array

from numpy import random 

x = random.rayleigh(scale=2, size=(2, 3))
print(x)

# Visualization of Raylaeigh Distribution

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.displot(random.rayleigh(size=1000), kind='kde')
plt.show()