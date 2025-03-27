def my_function():
    print('Hello from a function')

my_function()
 
def my_function(fname):
    print(fname + " refsnes")

my_function('two')
my_function('three')

def my_function(fname, lname):
    print(fname+ ' '+ lname)

my_function('Emily', 'Refsnes')

def my_function(*kids):
    print("The youngest child is "+ kids[2])

my_function('Emil','Tobias', "Linus")

def my_function(child1, child2, child3):
    print("The youngest child is "+ child3)

my_function(child1='Emil', child2="Tobias", child3="Linus")

def my_function(**kid):
    print('His last name i '+ kid['lname'])

my_function(fname = "tobias", lname = "Refsnes")

def my_function(country = "Norway"):
    print('I am from '+ country)

my_function('Sweden')
my_function('India')
my_function()
my_function('Brazil')

# Passing a list as an argument
def my_function(food):
    for x in food: 
        print(x) 
    
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
    return 5 * x 

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The paas statement 
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error 
def myfunction():
    pass 

# Positional - Only Arguments 
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments 

def my_function(x, /):
    print(x)


my_function(3)

def my_function(x):
    print(x)

my_function(x = 3)

def my_function(x):
    print(x)

my_function(x = 3)

# Keyword Only Arguments 
# To specify that a function can have only keyword arguments, add *, before the arguments 
def my_fucntion(*, x):
    print(x)

my_fucntion(x = 3)

def my_function(x):
    print(x)

my_function(3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

# Recursion 
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else: 
        result = 0
    return result

print('Recursion Example Results:')
tri_recursion(6)

