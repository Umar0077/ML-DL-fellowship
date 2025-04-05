import os

TASKS_FILE = "Task7/tasks.txt"

def read_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except Exception as e:
        print(f"Error reading tasks: {e}")
        return []

def write_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except Exception as e:
        print(f"Error writing tasks: {e}")

