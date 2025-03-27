# Python String Formatting 

# F-Strings 

txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(price)

txt = f"The price i {95:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59 
tax = 0.25
txt = f"The price is { price + (price * tax)} dollars"
print(txt)


# You can perform if ... else statements inside the placeholders:

price = 49 
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

# You can execute functions inside the placeholder

fruits = 'apples'
txt = f"I love {fruits.upper()}"
print(txt)

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# Use a comma as a thousnd separator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)


price = 49 
txt = "The price is {} dollars"
print(txt.format(price))

# You can add parameters inside the curly brackets to specify how to convert the value: 
txt = "The price is {:.2f} dollars"
print(txt)

# Multile Values
# If you want to use more values, just add more values to the format() method: 
quantity = 3 
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers
# You can use index numbers (a numer inside the curly brackets {0}) to be sure the values are placed in the corret placeholders:

quantity = 3 
itemno = 567
price = 49 
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# Also, if you want to refer to the same value more than once, use the index number 
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age,name))

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))




