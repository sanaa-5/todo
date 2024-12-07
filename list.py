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



















