# Python Classes / Objects 
# Pyhton is an object oriented programming language 
# Almost everything in Pyhton is an object,  with its properties and methods 
# A class is like an object contructor, or a 'blueprint' for creating objects 

class MyClass: 
    x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function 
# Create a class named Person, use the __init__() function to assign values for name and age
class Person: 

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('John', 36)
print(p1.name)
print(p1.age)


class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)

class Person: 

    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def myfunc(self):
        print('Hello my name is '+ self.name) 

p1 = Person('John', 36) 
p1.myfunc()

# The self Parameter 
# The self parameter is a reference to the current instance of the class, and is used to access varibles that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the firs parameter of any function in the class 

class Person:
    def __init__(obj,name, age):
        obj.name = name
        obj.age = age
    
    def myfucn(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfucn()

# Delete Object Properties
# You can delete properties on objects by using the del keyword
del p1.age 
print(p1)

# Delete Objects 
# You can delete objects by using the del keyword
del p1 

# The pass Statement 
class Person: 
    pass 

