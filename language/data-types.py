#data types in python  

x = 5 
print(type(x))

x = "Hello world"
print(type(x))

x = 20
print(type(x))

# pyhton has complex numbers 
x = 1j
print(type(x))

y = 2 + 3j
print(type(y))

x = ["apple", "banana", "cherry"] 
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name": "John", "age": 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(type(x))

# Setting the specific data type

x = str("Hello Word")
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(type(x))

x = tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = dict(name="jhon", age=36)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(type(x))

x = bool(5)
print(type(x))

x = bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))