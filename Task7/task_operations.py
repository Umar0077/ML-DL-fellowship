from Task7.file_handler import read_tasks, write_tasks

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("Task added successfully.")

def remove_task(task_number):
    tasks = read_tasks()
    try:
        removed = tasks.pop(task_number - 1)
        write_tasks(tasks)
        print(f"Removed task: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def update_task(task_number, new_task):
    tasks = read_tasks()
    try:
        tasks[task_number - 1] = new_task
        write_tasks(tasks)
        print("Task updated successfully.")
    except IndexError:
        print("Invalid task number.")

