print('Hello')
print("Hello")

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a =  """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt: 
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' in NOT present")

# Slicing strings in python 

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello,  World!"
print(b[:2])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.replace("l", "x"))

# Split string 
a = "Hello, World!"
print(a.split(','))

print(a.split(',')[0])
print(a.split(',')[1])


# Concatenate strings 

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36 
txt = f"My name is john, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price i {price:.2f} dollars"
print(txt)

txt = f"The price i {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north"

# Escape Characters

txt = "It\'s alright"
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello \nWorld!"
print(txt)

txt = "Hello \rWorld!"
print(txt)

txt = "Hello \tWorld!"
print(txt)

txt = "Hello \bWorld!"
print(txt)

txt = "\f"
print(txt)

txt = "\110\145\154\154\157"
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# String Methods 

txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x =  txt.center(20)
print(x)

txt = "banana"
x = txt.center(20, "0")
print(x)

# This is searching from position  10 to 24
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "Hello,  welcome to my world."
x = txt.endswith('.')
print(x)

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

#Check if position 5 to 11 ends with the phrase "my world."
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) 
print(x)

#Check if the strings ends with either the phrase "world." or "castle."
txt = "Hello, welcome to my castle."
x = txt.endswith(("world.", "castle."))

#Set the tab size to 2 whitespaces 
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

# The expandtabs() method sets the tab size to th specified number of whitespaces
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#The find method finds the first occurrence of the specifid value.
txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?
txt = "Hello, welcome to my world."
x = txt.find("e", 5 ,10)
print(x)

txt = "Hello, welcome to my world."
print(txt.find("q"))
#print(txt.index("q")) #Thi function throws an exception 

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "Jhon", age = 36)
txt2 = "My name is {0}, I'm {1}".format("Jhon",36)
txt3 = "My name is {}, I'm {}".format("Jhon",36)

txt = "We have {:<} chickens."
print(txt.format(49))

txt = "We have {:>8} chickens."
print(txt.format(49))

txt = "We have {:^8} chickens."
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3,7))

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3,7))

txt = "The universe is {:,} years old."
print(txt.format(1380000000))

txt = "The universe is {:_} years old."
print(txt.format(1380000000))

txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

txt = "{:c}"
print(txt.format(64))

txt = "We have {:d} chickens."
print(txt.format(0b101))

txt = "We have {:e} chickens."
print(txt.format(5))

txt = "We have {:E} chickens."
print(txt.format(5))

txt = "The price is {:.2f} dollars."
print(txt.format(45))

txt = "The price is {:f} dollars."
print(txt.format(45))

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

txt = "The price is {:f} dollars."
print(txt.format(x))

txt = "The octal version of {0} is {0:o}"
print(txt.format(10))

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))

txt = "You scored {:%}"
print(txt.format(0.25))

txt = "You scored {:.0%}"
print(txt.format(0.25))

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Company123"
x = txt.isascii()
print(x)

txt = "1234"
x = txt.isdecimal()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "hello world!"
x = txt.islower()
print(x)

txt = "565543"
x = txt.isnumeric()
print(x)

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)

txt = "    " 
x = txt.isspace()
print(x)

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

myTuple = ("Jhon","Peter","Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorte fruit")

txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

txt = "    banana    "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "Hello Sam!"
mytable = str.maketrans("S","P")
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I like bananas"
x = txt.replace("bananas","apples")
print(x)

txt = "Mi casa, su casa"
x = txt.rfind("casa")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit")

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "      banana      "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "Thank you for the misic\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

txt = "Welcome to my world"
x = txt.title()
print(x)

mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))

txt = "Hello my friends"
x = txt.upper()
print(x)

txt = "50"
x = txt.zfill(10)
print(x)


#https://www.w3schools.com/python/python_strings_methods.asp