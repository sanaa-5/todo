# A set is a collection which is unordered, unchangeable*, and unindexed
# and do not allow duplicate values
# the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.
thisset = {"apple", "banana", "cherry"}
set1 = {"abc", 34, True, 40, "male"}
print(thisset, set1)

# if there is duplicate item it will remove it
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# The values True and 1 are considered the same value in sets
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# The values False and 0 are considered the same value in sets
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# lenght of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# accessing the item in set since there is no index we can use loop
x = {"apple", "banana", "Kiwi"}
for i in x:
    print(i)

# check if the item in the set or not
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

# we can't change the item but we can add
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# adding update() any iterable
thisset = {"apple", "banana", "cherry"}
tropical = ["pineapple", "mango", "papaya"]
thisset.update(tropical)
print(thisset)

# removing
thisset.remove("banana")
print(thisset)

# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print(thisset)

# You can also use the pop() method to remove an item,but this method will
# remove a random item, so you cannot be sure what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear the set
thisset.clear()
print(thisset)

# delete
del thisset
#print(thisset)

# for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# The union() and update() methods joins all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set4 = {9, 0, 8}
set3 = set1.union(set2, set4)
print(set3)

# You can use the | operator instead of the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set4 = {4, 6, 9}
set3 = set1 | set2 | set4
print(set3)

# The intersection() method will return a new set, that only
# contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# another way to write but only for set with set
set4 = set1 & set2
print(set4)

# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"shehab", "32", "wt"}
set2 = {"he is indian", "trying to make pay", "32"}
set1.intersection_update(set2)
print(set1)

# The difference() method will return a new set that will contain only 
# the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = ("google", "microsoft", "apple")
set3 = set1.difference(set2)
print(set3)

# the other way to do it only applies on set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# Use the difference_update() method to keep the items that are not present
# in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements
# that are NOT present in both sets.
set3 = set1.symmetric_difference(set2)

# You can use the ^ operator instead of the symmetric_difference() method,
# and you will get the same result. and it's only for set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


















































