# Python Datetime
# Python Dates 
# A date in python is not a dat type of its own, but we can import a module named datatime to work with dats as date objects 

import datetime 

x = datetime.datetime.now()
print(x)

import datetime 
x = datetime.datetime.now() 

print(x.year)
print(x.strftime("%A"))

# Creating date objects 
# To create a date, we can use the datetime() class (constructor) of the datetime module

import datetime
x = datetime.datetime(2020,5,17) 
print(x)

# The strftime() Method 
# The datetime object has a method for formatting date objects into readable strings 
# The method is called strftime(), and takes one parameter,  format, to specify the format of the return string. 

import datetime 
x = datetime.datetime(2018, 6, 1)
print(x)

import datetime
x = datetime.date(2018, 6, 1)
print(x.strftime("%B"))


