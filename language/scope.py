# Pyhton Scope 
# A variable is only available from inside the region  it is created. This is called scope 
# Local Scope 

def myfunc(): 
    x = 300
    print(x)

myfunc()

def myfunc(): 
    x = 300 
    def myinnerfunc():
        print(x)
    
    myinnerfunc() 

myfunc() 

# Global Scope 
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, globall and local

x = 300

def myfunc():
    print(x)

myfunc() 
print(x)


def myfunc(): 
    global x 
    x = 300 

myfunc()
print(x)

x = 300

# Nonlocal Keyword 
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunct1(): 
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    
    myfunc2()
    return x

print(myfunct1())

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()