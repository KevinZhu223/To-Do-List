#To-Do List

def menu():
    print("\nTo-Do Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")


def main():
    tasks = []
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Viewing Tasks")
            if not tasks:
                print("No tasks here")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start = 1):
                    status = "✓" if task["completed"] else "X"
                    print(f"{i}. {task['task']} [{status}]")
        elif choice == "2":
            print("Adding a new task")
            task_name = input("Enter the task: ")
            tasks.append({"task": task_name, "completed": False})
            print(f"Task '{task_name}' added")
        elif choice == "3":
            print("Marking task as complete")
            if not tasks:
                print("No tasks to mark as complete")
            else:
                for i, task in enumerate(tasks, start = 1):
                    print(f"{i}. {task['task']}")
                try:
                    task_num =int(input("Enter the task number to mark as complete: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num -1]["completed"] = True
                        print(f"Task '{tasks[task_num - 1]['task']} marked as complete'")
                    else:
                        print("Not a valid task number")
                except ValueError:
                    print("Enter a valid number")
        elif choice == "4":
            print("Deleting a task")
            if not tasks: 
                print("No tasks to delete.")
            else:
                for i, task in enumerate(tasks, start = 1):
                    print(f"{i}. {task['task']}")
                try:
                    task_num = int(input("ENter the task number to delete"))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num -1)
                        print(f"Task '{removed_task['task']}' deleted")
                    else:
                        print("Not a valid task number")
                except ValueError:
                    print("Please enter a valid number")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()