# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and 
# do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier,
# dictionaries are unordered.
# Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# lenght
print(len(thisdict))

# type
print(type(thisdict))

# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# dic constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# to get the ket value 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
x = thisdict["model"]
print(x)

# we can use method
y = thisdict.get("model")

# return the list of all keys
x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list 
# gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# get the value
x = thisdict.values()
print(x)

# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

# checking if the keyword exist
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# change the value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# we can use update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# adding
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Removing Items with a specefic key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions 
# before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# 0r delete the dictionary comletly 
del thisdict

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# loop in dictinary will return all key names
thisdict = {
  "sanaa": "29",
  "Abed": "34",
  "shehab": "32"
}
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

# we can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)
    
# we can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
  
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

# COPPY : Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
mydict = dict(thisdict)
print(mydict)

# a dictionary can contain more dictionaries "Nested dictionaries"
# this is a main dictionary called my_family inside of it is keys
# shatha, shaima and saad are keys having values The values of these
# keys are dictionaries containing details
my_family = {
    "Shatha" : {
        "name" : "Basmah",
        "age" : 14
    },
    "Shaima" : {
        "name" : "Leenaa",
        "age" : 15
    },
    "Saad" : {
        "name" : "shahed",
        "age" : 10
    }
}
print(my_family)

# Create three dictionaries, then create one dictionary that will 
# contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

# accessing items in nested dictionary by using the name of the 
# dictionaries, starting with the outer dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

# to print may here 
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}

print(customers['c2']['name'])

# using loop
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


















