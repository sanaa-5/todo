# Test 1
square = lambda x: x * 2
print(square(5))

# Test 2
nums = [1, 2, 3, 4]
lamb = lambda x: x * 2
# map_object holds all the information needed for mappi
map_object = map(lamb, nums)
# Now we we want to execute this mapping/transformation
# We do this by creating a list
# We call the list constructor/init and pass the map_object (holding the mapping info) into the list contructor/init
doubled = list(map_object)
print(doubled)

# Test 3
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: True, nums))
print(doubled)
# The job of map is to create a new array which has values "which are mapped from the values" old array
[2, 4, 6, 8]

# Test 4
nums = [5, 12, 17, 9, 20]
# The output of the lamba in a filter must be a boolean
filter_operation = lambda x: x > 10
# The type for filter_operation lambda
filtered_nums = list(filter(filter_operation, nums))
print(filtered_nums)
[12, 17, 20]

# Test 5
heights = [168, 183, 50]
heights_in_m = list(map(lambda x: x / 100, heights))
list_of_tall_people = list(filter( lambda x: x > 0.5 , heights_in_m))
print(list_of_tall_people)

# Test 6
heights = [168, 183, 50]
heights_in_m = list(map(lambda x: x / 100, heights))
list_of_tall_people = list(filter( lambda x: 0, heights_in_m))
# 1 True
# 0 False
# -1 True
print(list_of_tall_people)

# Test 7
def add (a, b, opration):
# func add() returns the value that is returned by the lambda operation
    return opration(a,b)
# This lambda returns a value
lamb = lambda x, y: x + y
a = add(3, 5, lamb)
print(a)


# Test 7
def add(a, b, opration):
    return opration(a,b)

def lamb_func(x, y):
    return x + y

# Singature type for a lambda and a function is the same,
# Bot of them accepting two argumetns and both of them returning a value
# (Any, Any) -> (Any)

# BEFORE YOU PASSED A LAMBDA INTO A FUNC
# NOW YOU ARE PASSING A FUNC INTO A FUNC
# IM TRYING TO SAY LAMBDA AND A FUNCTION IS A THE SAME THING
a = add(3, 5, lamb_func)
print(a)




















