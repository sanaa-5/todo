#List items are ordered, changeable, and allow duplicate values.
lists = ["apple", "banana", "cherry"]
list1 = [1, 2 , 3, 4]
list2 = [True, False, False]
list3 = ["she", 34, True]

# lenght
print(len(lists))

# Type
print(type(list3), type(lists), type(list2), type(list1))

# using list() constrocter
thislist = list(("a", "b", "c"))
print(thislist)

#accessing the item
print(list1[3])

# negative index -1 refers to the last item, -2 refers to the second last item etc.
print(list3[-1], lists[-3])

# range of index including the first but not the end
print(list1[1:5], list1[1:3])
print(list3[:2], list1[2:])
print(lists[-2:-1])

# change the the item and the range
list3[0] = "Abed"
print(list3)
list3[1:4] = ["she", 40, "fat", True, "eating"]
print(list3)

# insert items 2 is the index and 3 is the number that going to add to the list
list1.insert(2, 3)
print(list1)
# we can use append it will add at the end of the list
list1.append(5)
print(list1)

# Extending the list liek joining 2 lists, updating the existing list
list1.extend(list2)
print(list1)

# remove, pop, delete, clear
list1.remove(4)
print(list1)
x = list1.pop(1)
print(x, list1)
del list2[0]
print(list2)
list2.clear()
print(list2)

# for loop
for x in list1:
    print(x)

list2 = ["she", "he"]
for y in range(len(list2)):
    print(list2[y])
    print(y)

# while loop
x = 0
while x < len(list2):
    print(list2[x])
    x = x + 1
    
#  loop using list comprehension
[print(x) for x in list2]

# loop condition
tempreture = [0.1, 0.5, 0.7, 0.3, 0.9, 3.0, 4.0]
new_list = [x for x in tempreture if x < 1]
print(new_list)

# loop
hights_in_cm = [168, 183, 160]
hight_in_m = [x/100 for x in hights_in_cm]
particepants = [ x > 1.65 for x in hight_in_m ]
print(particepants)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
# this one is sorting without considiring the alphabet
thislist.reverse()
print(thislist) 

# this one is reversing considiring the alphabet 
# note: normal sort will make the capital first 
thislist.sort(reverse = True)
print(thislist)

# Sort the list descending
thislist.sort(reverse = True)
print(thislist)

# sort the list 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# this will make a coppy where we have saperate lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
thislist.append("as")
print(mylist)

# this one is like a pointer whenever we change the thislist a will change 
a = thislist
thislist.append("d")
print(a)

# anothor way to make a coppy 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# JOIN 1 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# JOIN 2 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# JOIN 3 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)














