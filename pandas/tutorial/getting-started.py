# Pandas Getting Started 

## Installation of Pandas 
# > pip install pandas

import pandas 

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)
print(myvar)


# Now the Pandas package can be referred to as pd instead of pandas. 

import pandas as pd 

myvar = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)

# Checking Pandas Version 
# The version string is stored under under __version__ attribute. 

import pandas as pd 

print(pd.__version__)