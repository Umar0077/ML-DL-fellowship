from Task7.task_operations import add_task, remove_task, update_task, view_tasks

def show_menu():
    print("\n=== Task Manager ===")
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Update a task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter task number to update: "))
                new_task = input("Enter the updated task: ")
                update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

