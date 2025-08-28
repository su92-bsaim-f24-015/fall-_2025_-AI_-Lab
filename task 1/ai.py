tasks = []  

def addTask():
    while True:
        task = input("Enter a new task (or write stop to go to menu) : ")
        if task.lower()== "stop":
            break
        
        elif task.strip() == "":
            print("Task cannot be empty!")
        else:
            tasks.append({"task": task, "done": False})
            print(f"Task '{task}' added to the list!")
            

def listTasks():
    if not tasks:
        print("No tasks in the list!")
    else:
        print("Current Tasks:")
        for index, t in enumerate(tasks):
            print(f"{index}. {t['task']} ]")

def deleteTask():
    listTasks()
    if not tasks:
        return
    try:
        taskToDelete = int(input("Enter the # of the task to delete: "))
        if 0 <= taskToDelete < len(tasks):
            removed = tasks.pop(taskToDelete)
            print(f"Task '{removed['task']}' has been removed.")
        else:
            print(f"Task #{taskToDelete} not found.")
    except ValueError:
        print("Invalid input! Enter a number.")

def completeTask():
    listTasks()
    if not tasks:
        return
    try:
        taskToComplete = int(input("Enter the # of the task to mark as done: "))
        if 0 <= taskToComplete < len(tasks):
            
            print(f"Task '{tasks[taskToComplete]['task']}' marked as done!")
        else:
            print(f"Task #{taskToComplete} not found.")
    except ValueError:
        print("Invalid input! Enter a number.")

if __name__ == "__main__":
    print("Welcome to the Dynamic To-Do List Game!")

    while True:
        print("\nSelect an option:")
        print("1. Add new tasks")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Mark task as done")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            completeTask()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input! Please try again.")
