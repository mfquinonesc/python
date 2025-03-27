# Python Iterators 

# An iterator is an object that contains a countable number of values 

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

mystr = "banana"
for x in mystr:
    print(x)

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

mystr = "banana"
for x in mystr:
    print(x)

# Create an iterator 
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,etc) 

class MyNumbers: 
    
    def __iter__(self):
        self.a = 1 
        return self
    
    def __next__(self):
        x = self.a 
        self.a += 1
        return x 

myclass = MyNumbers()
myiter = iter(myclass)

for x in range(100):
    print(next(myiter))

# Stop Iteration 
# The example above would continue forever if you had enough nex() 
# To prevent the iteration from going on forever, we can use the StopIteration statement

class MyNumbers: 
    def __iter__(self):
        self.a  = 1 
        return self 
    
    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1 
            return x
        else: 
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)    

