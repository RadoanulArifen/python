tasks = []

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully.")
    elif choice == "2":
        print("Todo List:")
        if not tasks:
            print("No tasks found.")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {status} {task['task']}")
    elif choice == "3":
        print("Todo List:")
        if not tasks:
            print("No tasks found.")
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {status} {task['task']}")
        task_index = int(input("Enter task number to mark as complete: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print(f"Task {task_index} marked as complete.")
        else:
            print("Invalid task index.")
    elif choice == "4":
        print("Exiting the todo list program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
