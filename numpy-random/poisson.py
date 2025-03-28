# Poisson Distribution

# Poisson Distribution is a Discrete Distribution
# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is th e probability he will eat thrice? 
# 
# It has two parameters 
# lam = rate or known number of occurrences e.g. 2 for above problem.
# size = The shape of the returned array 
# 

from numpy import random

x = random.poisson(lam=2, size=10)
print(x)

# Visualization of Poisson Distribution

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.displot(random.poisson(lam=2, size=1000))
plt.show()

# Difference Between Normal and Poisson Distribution 
# Normal distribution is continuos whereas poisson is discrete
# But we can see that similar to binomial for large enough possion distribution it will become similar to normal distribution with certain std dev and mean. 
# 

from numpy  import random
import matplotlib.pyplot as plt 
import seaborn as sns 

data = {
    "normal" : random.normal(loc=50, scale=7, size=1000),
    "poisson": random.poisson(lam=50, size=1000) 
}

sns.displot(data, kind='kde')
plt.show()

# Difference Between Binomial and Poisson Distribution 
# Binomial distribution only has possible outcomes, whereas poisson distribution can have unlimited possible outcomes.
# But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is near equal to lam

from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sns 

data = {
    "binomial": random.binomial(n= 1000, p=0.01, size= 1000),
    "poisson": random.poisson(lam=10, size= 1000)
}

sns.displot(data, kind="kde")
plt.show() 