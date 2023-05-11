# To-Do List Application
#5/11/2023
#By: Adam Fulton

# Function to display the to-do list
def display_list():
    print("To-Do List:")
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully.")

# Function to remove a task from the list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found in the list.")

# Function to clear all tasks from the list
def clear_list():
    todo_list.clear()
    print("All tasks cleared from the list.")

# Main program
todo_list = []

while True:
    print("\n==== To-Do List Application ====")
    print("1. Display the to-do list")
    print("2. Add a task to the list")
    print("3. Remove a task from the list")
    print("4. Clear all tasks from the list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_list()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '4':
        clear_list()
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")