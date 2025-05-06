# Simple To-Do List Application

todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Done")
    print("4. View Tasks")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    todo_list.append({"task": task, "done": False})
    print("✅ Task added!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        removed = todo_list.pop(task_num)
        print(f"🗑️ Deleted: {removed['task']}")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        todo_list[task_num]["done"] = True
        print("✅ Task marked as done!")
    except (IndexError, ValueError):
        print("❌ Invalid task number.")

def view_tasks():
    if not todo_list:
        print("📭 No tasks added yet.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(todo_list, 1):
        status = "✅ Done" if task["done"] else "❌ Not done"
        print(f"{i}. {task['task']} [{status}]")

# Run the menu in a loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        view_tasks()
    elif choice == '5':
        print("👋 Exiting To-Do List App. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please enter a number from 1 to 5.")
