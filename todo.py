import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: Corrupted file. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task_name = input("Enter a task: ")
    task_obj = {"Task": task_name, "Done": False}
    tasks.append(task_obj)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["Done"] else "❌ Not Done"
        print(f"{i}. {task['Task']} - {status}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        d = int(input("\nEnter the task number to delete: "))
        if 1 <= d <= len(tasks):
            deleted = tasks.pop(d - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{deleted['Task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n---- Task Manager ----")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            print("Saving tasks... Goodbye 👋")
            save_tasks(tasks)
            break
        else:
            print("Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

