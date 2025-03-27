#Python sets
myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry","apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0 }
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


set1 = {"apple","banana", "cherry"}
set2 = {1,5,7,9,3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset =  set(("apple","banana","cherry")) # note the double round-brackets 
print(thisset)

# Pyhton - Access Set Items
thisset = {"apple", "banana", "cherry"}

for  x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = { "apple", "banana", "cherry" }
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineaple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana","cherry"}
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana","cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana","cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)

# Loops in sets 
thisset = {"apple", "banana", "cherry"}
for x in thisset: 
    print(x)

# Pyhton Join Sets 
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# This is a join too
set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = {"Jhon", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2,set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1,2,3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4 
print(myset)

x = {"a", "b", "c"}
y = (1,2,3)
z = x.union(y)
print(z)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# This is the intersection of sets 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# Keep the items that exist in both set1 and set2 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Keep all items from set1 that are not in set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Symmetric Differences 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# python set Methods 

# Set add() method
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

fruits = {"apple", "banana", "cherry" }
x = fruits.copy()
print(x)

# Diference in sets 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
myset = a - b
print(myset)

# The difference method returns a set that contains the difference between two sets 
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a.difference(b,c)
print(myset)

# Join more than two sets with the - operator
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}
myset = a - b - c
print(myset)

# Reverse the example on the top of this page. Retrun a set that contains the items that only exist in set y,  and not in set x:
x = {"apple", "banana",  "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)

print(z)

# Remave an element from the set 
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# Return a set that contains the items that exist in both set x, and set y: 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x &= y
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x &= y & z
print(x)

# Return True if no items in set x is present in set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

# Returns False if one or more items are present in both sets 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x <= y
print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x >= y 
print(z)

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x ^ y
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x | y
print(z)

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y,z)
print(result)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x |= y
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "mcrosoft","apple"}
z = {"cherry", "micra", "bluebird"}
x.update(y,z)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = {"cherry", "micra", "bluebird"}
x |= y | z
print(x)
