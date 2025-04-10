# Pandas DataFrames

# What is a DataFrame? 
# A Pandas DataFrame is a 2 dimendional data structure, like a 2 dimensional array, or table with rows and columns. 

import pandas as pd 

data = {
    'calories':[420, 380, 390],
    'durations': [50, 40, 45]
}

# load data into a DataFrame object: 
df = pd.DataFrame(data)

print(df)

# Locate Row 

# As you can see from the result above, the DataFrame is like a table with rows and columns. 
# Pandas use the loc attribute to return one or more specified row(s) 

# refer to the row index: 
print(df.loc[0])

# use a list of indexes: 
print(df.loc[[0, 1]])


# Named Indexes
import pandas as pd 

data = {
    'Calories': [420, 380, 390],
    'duration': [50, 40, 45]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])
print(df)

# refer to the named index: 
print(df.loc['day2'])

# Load Files Into a DataFrame 
# If your data sets se stored in a file, Pandas can load them into a DataFrame

import pandas as pd 

df = pd.read_csv('files/data.csv')
print(df)