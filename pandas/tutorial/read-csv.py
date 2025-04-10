# Pandas Read CSV

# Read CSV Files 
# 
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and id a well know format that can be read by everyone including Pandas.
# In our examples we  will be using aa csv file called 'data.csv'. 

import pandas as pd 
df = pd.read_csv('../files/data.csv')

# Use to_string() to print the entire DataFrame.
print(df.to_string())


# If you have a large DataFrame with many rows, Pandas wikk only return the first 5 rows, and the last 5 rows: 
import pandas as pd 
df = pd.read_csv('../files/data.csv')
print(df)

# max_rows 
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum  rows with the pd.option.display.max_rows statement 

import pandas as pd
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:

import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('../files/data.csv')
print(df)