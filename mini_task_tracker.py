import json
import os

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
        except:
            tasks = []
    else:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['title']} [{status}]")

def complete_task():
    if not tasks:
        print("No tasks to complete.")
        return
    view_tasks()
    try:
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks()
            print("Task completed.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks()
            print(f"Deleted task: '{deleted['title']}'")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    load_tasks()
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add 2. View 3. Complete 4. Delete 5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice.")

if __name__ == "__main__":
    main()
