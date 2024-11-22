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
