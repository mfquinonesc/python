# Pandas Series 

# What is a Series? 
# A Pandas Series is like a column in a table
# It is one-dimensional array holding data of any type

import pandas as pd 

a = [1, 7, 2] 
myvar = pd.Series(a)
print(myvar)

# Labels 
# If nothing else is specified, the values are labeled with their index number. 
# First value has index 0, second value has index 1 etc . 
# This label can be used to access a specified value. 

print(myvar[0])

# Create Labels 
# With the index argument, you can name your own labels. 

import pandas as pd 

a = [1, 7, 2]
myvar = pd.Series(a, index= ['x', 'y', 'z'])
print(myvar)

print(myvar['y'])

# Key/Value Objects as Series 
# You can also ude a key/value object, like a dictionary, when creating a Series. 

import pandas as pd 

calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories)

print(myvar)

# Note: The keys of the dictionary become the labels. 
# To select only some of the items you want to include in the series 

import pandas as pd

calories = {'day1': 420, 'day2': 380, 'day3': 390}

myvar = pd.Series(calories, index=['day1', 'day2'])
print(myvar)

# Data Frames 

# Data sets in Pandas are usually multi-dimensional tables, called DataFrame.
# Series is like a colum, a DataFrame is the whole table.

import pandas as pd

data = {
    'calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

myvar = pd.DataFrame(data)
print(myvar)
