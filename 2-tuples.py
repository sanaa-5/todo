# Tuple items are ordered, unchangeable, and allow duplicate values.
# When we say that tuples are ordered, it means that the items have
# a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, \
# add or remove items after the tuple has been created.

# allow the dipliacate
thistuple = ("apple", 40, True, "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# you have to add a comma after the item, if it's only 1 item
# otherwise Python will not recognize it as a tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#This will return the items from position 2 to 5.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

# if statment
if "apple" in thistuple:
   print("Yes, 'apple' is in the fruits tuple")

# tuple is unchangeable , immmutable so to change it we can covert to list 
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "orange"
x = tuple(y)
print(x)

# add
z = list(x)
z.append("Kiwi")
x = tuple(z)
print(x)

# remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# adding tuple to a tuple 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# delete the tuple
del thistuple

# unpacking
# in Python, we are also allowed to extract the values back into variables.
this_tuple = ("red", "blue", "brown", "green", "yellow")
(one,two,*three) = this_tuple
print(one)
print(two)
print(three)
(one,*two,three) = this_tuple
print(one)
print(two)
print(three)

# for loop
a = ("apple", "banana", "Kiwi")
for x in a:
   print(x)
for x in range(len(a)):
   print(a[x])

# while loop 
x = 0
while x < len(a):
   print(a[x])
   x += 1

# multiply the tuple is like duplicate
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# tiple method .index()
# method finds the first occurrence of the specified value.
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# .count()
# Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)


