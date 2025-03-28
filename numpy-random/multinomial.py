# Multinomial Distribution 
# Multinomial distribution is a generalization of binomial distribyution.
# It describes outcomes of multi-normal scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.

# It has three parameters 
# n = number of times to run the experiment 
# pvals = list of probabilities of outcomes (e.g [1/16, 1/16, 1/16, 1/16, 1/16]) for dice roll) 
# size the shape of the returned array

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)