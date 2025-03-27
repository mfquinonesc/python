# Parse Json - Convert from JSON to Python 
# If you have a JSON string, you can parse it by using the json.loads() method.
# 

import json 

# some JSON: 
x = '{ "name": "John", "age": 30, "city":"New York" }'

# parse x: 
y = json.loads(x)

# The result is a Python dictionary
print(y)

print(y['age'])

# Convert from python to JSON

import json 

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:  
y = json.dumps(x)

# The result is a JSON string: 
print(y)


# Convert python objects into JSON strings, and print the values: 

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json 

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars":[
        {"model": "BMW 230", "mpg": 27.5},
        {"model" : "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# Format the Result 
# The example above prints a JSON string,  but is not very easy to read, with no indentations and line breaks. 

# The json.dumps() moethod has parameters to make it easier to read the result: 

y = json.dumps(x , indent = 4, separators=(". ", " = "))
print(y)



