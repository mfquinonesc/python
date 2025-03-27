# Python Arrays 
# Note: Python does not have built in support for Arrays, but Python Lists can b used instead 
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library 

# Python arrays 
cars = ["Ford", "Volvo", "BMW"]
print(cars)

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Access the Elements of an Array
x = cars[0]
print(x)

x = len(cars)

for x in cars: 
    print(x)

cars.append('Honda')
print(cars)

cars.pop(1)
print(cars)

# Remove an element 
cars  = ['Volvo', 'BMW', 'Ford']
cars.remove('Volvo')
print(cars)

# Array methods 

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

fruits = ['apple','banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

fruits = ['apple', 'banana', 'cherry']
x = fruits.count('cherry')
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
points = (1,4,5,9)
fruits.extend(points)
print(fruits)

fruits = ['apple', 'banana', 'cherry'] 
x = fruits.index('cherry')
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,'orange')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

fruits = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

