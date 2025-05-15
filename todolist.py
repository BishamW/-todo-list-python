todo_list = []

def show_menu():
    print("\n===== TO-DO MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:    
        todo_list.append({"task": task, "done": False})
        print("Task added.")
    else:
        print("Empty task not added.")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, item in enumerate(todo_list):
            status = "✓" if item["done"] else "✗"
            print(f"{i + 1}. [{status}] {item['task']}")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid option. Try again.")