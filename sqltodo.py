"""
To-do App: A simple command-line task manager using MySQL.
"""

import pymysql

def get_connection():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="2006",
        database="todo_app"
    )

def load_tasks():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT id, task, done FROM tasks")
    tasks = cursor.fetchall()
    db.close()
    return tasks

def add_task():
    task_name = input("Enter a task: ")

    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_name,))
    db.commit()
    db.close()

    print("✓ Task added!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour tasks:")
    for t in tasks:
        task_id, task_name, done = t
        status = "✓ Done" if done else "✗ Not Done"
        print(f"{task_id}. {task_name} - {status}")

def delete_task():
    view_tasks()
    tid = input("\nEnter the task ID to delete: ")

    db = get_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (tid,))
    db.commit()
    db.close()

    print("🗑 Task deleted!")

def main():
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
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Goodbye 👋")
            break
        else:
            print("Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
