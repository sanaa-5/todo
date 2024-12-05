#adding the lib

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_number):
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' removed.")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")


#unpacking 

    fruits = ["apple", "banana", "cherry", "orange"]
    x = y = z = s = fruits
    print(x)
    print(y)
    print(z)


#concatination

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
x = 5
y = 6
z = 7
print(x + y + z)


#global

y = "ed"

def set_globals():
    global x
    x = "loves ab"

def execute_code():
    print("Shehab", x + y)

set_globals()
execute_code()


#tuple

my_tuple = [1, 2, 3]
my_tuple = [7, 6, 4]
my_tuple[0] = 3

print(my_tuple)



#random:

import random

print(random.randrange(1, 10))


#lenght - if statment

a = "Hello, World!"
print(len(a))
print("hello" in a)
if "," in a :
    print(", is there ")
if "hello" not in a :
    print(a[0], a[2:6], a[:3], a[7:], a[-1:-2])




x = 1995
y = f"date of birth is {x:.1f}"
print(y)


capitalize()
center()
count()
endswith()
format()
index()
isdecimal()
isupper()
join()
lower()
lstrip()
replace()
rfind()
split()
splitlines()
startswith()
strip()


# Original string
text = "hello, Python World! 123 Welcome to Python programming."

# 1. capitalize()
capitalized_text = text.capitalize()
print("capitalize():", capitalized_text)

# 2. center()
centered_text = text.center(2, "-")
print("center():", centered_text)

# 3. count()
count_python = text.count("Python")
print("count():", count_python)

# 4. endswith()
ends_with_world = text.endswith("World!")
print("endswith():", ends_with_world)

# 5. format()
formatted_text = "Hello, {}!".format("Pythonista")
print("format():", formatted_text)

# 6. index()
index_python = text.index("Python")
print("index():", index_python)

# 7. isdecimal()
numeric_string = "12345"
is_decimal = numeric_string.isdecimal()
print("isdecimal():", is_decimal)

# 8. isupper()
is_upper = text.isupper()
print("isupper():", is_upper)

# 9. join()
words = ["Python", "is", "awesome"]
joined_text = " ".join(words)
print("join():", joined_text)

# 10. lower()
lowercase_text = text.lower()
print("lower():", lowercase_text)

# 11. lstrip()
lstripped_text = text.lstrip()
print("lstrip():", lstripped_text)

# 12. replace()
replaced_text = text.replace("Python", "Coding")
print("replace():", replaced_text)

# 13. rfind()
last_occurrence = text.rfind("Python")
print("rfind():", last_occurrence)

# 14. split()
split_text = text.split()
print("split():", split_text)

# 15. splitlines()
split_lines = text.splitlines()
print("splitlines():", split_lines)

# 16. startswith()
starts_with_hello = text.startswith(" Hello")
print("startswith():", starts_with_hello)

# 17. strip()
stripped_text = text.strip()
print("strip():", stripped_text)





x = []
y = ""
if bool(x) == bool(y):
    print("s")
else:
    print("d")
x = 200
print(isinstance(x, int))



thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]
print(list1)





thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)



thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



# pop , delete , clear 

thislist = ["apple", "banana", "cherry"]
a = thislist.pop(0)
del thislist[0]
print(a , thislist)
thislists = ["apple", "banana", "cherry"]
thislists.clear()
print(thislists)










