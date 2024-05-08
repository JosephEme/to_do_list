# Function to add a task to the list of tasks
def add_task(tasks, task):
    tasks.append(task)

# Function to delete a task from the list of tasks
def delete_task(tasks, task_index):
    del tasks[task_index]

# Function to mark a task as complete in the list of tasks
def mark_task_complete(tasks, task_index):
    tasks[task_index] += " - Completed"

# Function to display all tasks in the list
def display_tasks(tasks):
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks.")

# Main function to manage the application flow
def main():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task Complete")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            if tasks:
                display_tasks(tasks)
                task_index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, task_index)
            else:
                print("No tasks to delete.")
        elif choice == "3":
            if tasks:
                display_tasks(tasks)
                task_index = int(input("Enter task number to mark as complete: ")) - 1
                mark_task_complete(tasks, task_index)
            else:
                print("No tasks to mark as complete.")
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
