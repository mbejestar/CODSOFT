# todo list CodSoFT

import random
import datetime

class ToDoListManager:
    def __init__(self):
        self.tasks = []
        self.greetings = ["Hey, buddy!", "What's up, friend!", "Howzit!", "Hey, partner!", "Yo, what's good!"]
        self.signoffs = ["Later, player!", "Catch you on the flip side!", "Peace out, homie!", "Laters, mate!", "Until next time, stay awesome!"]

    def add_task(self, task_name):
        """Add a new task to the to-do list"""
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added successfully!")

    def view_tasks(self):
        """View all tasks in the to-do list"""
        if not self.tasks:
            print("No tasks available!")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"Task {i}: {task['name']}")
                print(f"Status: {status}")
                print("-" * 30)

    def update_task(self, task_index, task_name=None):
        """Update an existing task in the to-do list"""
        if task_index > 0 and task_index <= len(self.tasks):
            if task_name:
                self.tasks[task_index - 1]["name"] = task_name
            print(f"Task {task_index} updated successfully!")
        else:
            print(f"Task {task_index} not found!")

    def delete_task(self, task_index):
        """Delete a task from the to-do list"""
        if task_index > 0 and task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print(f"Task {task_index} deleted successfully!")
        else:
            print(f"Task {task_index} not found!")

    def mark_task_completed(self, task_index):
        """Mark a task as completed"""
        if task_index > 0 and task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task {task_index} marked as completed!")
        else:
            print(f"Task {task_index} not found!")

    

    def greet_user(self):
        """Greet the user with a random message"""
        print(random.choice(self.greetings))

    def signoff_user(self):
        """Bid farewell to the user with a random message"""
        print(random.choice(self.signoffs))


def main():
    todo_manager = ToDoListManager()
    todo_manager.greet_user()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task/Event")
        print("2. View Tasks/Event")
        print("3. Update Task/Event")
        print("4. Delete Task/Event")
        print("5. Mark Task/Event Completed")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_manager.add_task(task_name)
        elif choice == "2":
            todo_manager.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task number: "))
            task_name = input("Enter new task name (optional): ")
            todo_manager.update_task(task_index, task_name if task_name else None)
        elif choice == "4":
            task_index = int(input("Enter task number: "))
            todo_manager.delete_task(task_index)
        elif choice == "5":
            task_index = int(input("Enter task number: "))
            todo_manager.mark_task_completed(task_index)
        
        elif choice == "6":
            todo_manager.signoff_user()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()