# Python Dictionaries

thisdict = {
    "brand": "Ford",
    "model":"Mustang",
    "year": 1964
}

# Dictionaries are used to store data values in key: value pairs 
# A dictionary is a collection which is ordered, changeable an do not allow duplicates 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)

# Dictionary Items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

thisdict = {
    "brand": "Ford", 
    "model": "Mustang",    
    "year": 2020
}

print(thisdict)
print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors":["red","white", "blue"]
}

print(type(thisdict))

thisdict = dict(name = "Jhon", age = 36, country = "Norway")
print(thisdict)

# Dictionary access items 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

car = {
    "brand": "Ford",
    "model":"Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

print(car)

x = thisdict.values()
print(x)

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

x = car.values()
print(x)
car["year"] = 2020
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year":1964
}

x = car.values()
print(x)
car["color"] = "red"
print(x)

x = thisdict.items()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)
car["year"] = 2020
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict: 
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"year": 2020})

print(thisdict)

# Adding Items 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964    
}
thisdict["colors"] = "red"

print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)

# Removing Items 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()
print(thisdict)

thisdict = {
    "brand":"Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)

# Loop Through a Dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict: 
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print(x,y)

# Copy dictionaries
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}

mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
myfamily = {
    "child1" : {
        "name": "Emil",
        "year": 2004
    },
    "Child2":{
        "name": "Tobias",
        "year": 2007,        
    },
    "Child3": {
        "name": "Linus",
        "year": 2011
    }
}

print(myfamily)

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year" : 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)

print(myfamily["child1"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in obj: 
        print(y + ':', obj[y])

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.copy()
print(x)

x = ('key1', 'key2', 'key3')
y = 0 
thisdict = dict.fromkeys(x,y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get('model')
print(x)

# Try to return the value of an item that do not exist
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# It returns a value that do not exist
x = car.get("price", 15000)
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)

car = {
    "brand": "Ford",
    "model":"Mustang",
    "year": 1964
}

x = car.items()
car['year'] = 2018
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
car['color'] = "white"
print(x)
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop('model')
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.pop('model')
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.popitem()
print(car)

car  = {
    "brand": "Ford",
    "model":"mustang",
    "year": 1964
}
 
x = car.popitem()
print(x)
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x)

print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("color", "white")
print(x)
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.update({'color': 'white'})
print(car)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)

car = {
    "barnd": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
car["year"] = 2018 
print(x)
