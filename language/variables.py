x = 5
y = 'John'

print(x)
print(y)

# Variables can change their type of data after been declared

x = 4 
x = "Sally"

print(x)

# This can be done if you want to specify the type of data 

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# Get the variable type of data 

x = 5
y = "john"

print(type(x))
print(type(y))


# Variable names are Case-Sensitive

a = 4
A = "Sally"

# A will not overwrite a 

print(a)
print(A)


# Variable names 

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Camel Case

myVariableName = "John"
MyVariableName = "Jhon"
my_variable_name = "Jhon"

print(myVariableName)
print(MyVariableName)
print(my_variable_name)

# Many values to multiple variables 

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection 

fruits = ["apple", "banana", "cherry"] 
x, y, z = fruits; 

print(x)
print(y)
print(z)


x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"

print(x,y,z)

x = "Pyhton "
y = "is "
z = "awesome"

print(x + y + z)

x = 5 
y = 10
print(x + y)

x = 5
y = "John"
print(x,y)

x = 5 
y = "John"
print(x, y)

# Pyhton global variables 

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# The global keyword 


def myfunc():
    global x 
    x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc(): 
    global x 
    x = "fantastic"

myfunc()

print("Python is " + x)

# Pyhton - Variable Exercises 

