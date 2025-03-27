# Python Inheritance

# Create a Parent Class
class Person:
    def __init__(self,fname, lname):
        self.firsname = fname 
        self.lastname = lname

    def printname(self): 
        print(self.firsname, self.lastname) 

# Create an object of the class Person, and then execute the printname method

x = Person("Jhon", "Doe")
x.printname() 


# Create the child class 

class Student(Person):
    pass

y = Student('Michael', 'Jackson')
y.printname()

# Add the init function 
class Student(Person):
    def __init__(self, fname, lname):
        pass
        #add properties.

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# Adding properties 
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019 

class Person: 
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname     

    def printname(self):
        print(self.fname + " " + self.lname)


class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x =  Student("Mike", "Olsen", 2019)
print(x.graduationyear,x.printname())

# Add methods 
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x =  Student('John', 'Doe', 1990)
x.printname()
x.welcome()
