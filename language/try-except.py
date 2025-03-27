# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error
# The else block lets you execute code when there is no error 
# The finally block lets you execute code, regardless of the result o the try- and excet blocks. 


try:
    print(x)
except: 
    print('An exception ocurred')


try: 
    print(x)
except NameError: 
    print("Variable x is not defined")
except: 
    print("Something else went wrong")

# Using Else
try: 
    print('Hello')
except: 
    print('Something went wrong')
else:
    print('Nothing went wrong')


# Using Finally 

try: 
    print(x)
except: 
    print("Something went wrong")
finally: 
    print("The 'try except' is finished")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1

if x < 0: 
    raise Exception('Sorry, no numbers below zero')
