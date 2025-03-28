# Uniform Distribution 
# Used to describe probability where every event has equal changes of occurring.
# It has three parameters 

# low - lower bound - default 0.0 
# high upper bound - defoult 1.0 
# size - the shape of the retrned array 

from numpy import random 

x = random.uniform(size=(2,3))
print(x)


# Visualization of UNiform Distribution 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.displot(random.uniform(size=1000), kind = "kde")
plt.show()

