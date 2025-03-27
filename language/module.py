# What is a Module?
# Consider a module to be the same as a code library
# A file containing a set of functions you want to include in your application

# Create a module
# To create a module just save the code you want in a file with the extension .py

# Here is defined the folder name 
from modules import mymodule 

mymodule.greeting('Jonathan')

# Varibles in modules 
# The module can contain functions, as already decribed, but also variables of all types (arrays, dictionaries, objects, etc)

a = mymodule.person1['age']
print(a)

# Naming a module

from modules import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like 

import platform

x = platform.system()
print(x)

# Using the dir Function 
# There is a built-in function to list all the function names (or variables names) in a module. The dir() function. 

import platform

x = dir(platform)
print(x)

# Import from a module 
# You can choose to import only parts from a module,  by using the from keyword 

from modules.mymodule import person1

print(person1)
