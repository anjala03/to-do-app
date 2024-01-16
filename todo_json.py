import json

def add_task(task):
    try:
        with open("jsondata.json", "r") as jsonf:
            tasks = json.load(jsonf)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        tasks = []

    tasks.append(task)
    
    with open("jsondata.json", "w") as jsonf:
        json.dump(tasks, jsonf)

    print("Task Added")

def read_the_task():
    try:
        with open("jsondata.json", "r") as jsonf:
            loaded_file = json.load(jsonf)
        return loaded_file
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("File not found. No tasks available.")
        return []

def mark_a_task_done():
    tasks = read_the_task()

    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks):
        print(f"{i + 1}. {'[Done]' if task.get('done', False) else '[Not Done]'} {task.get('task', 'Unknown')}")

    try:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        tasks[task_index]['done'] = True

        with open("jsondata.json", "w") as jsonf:
            json.dump(tasks, jsonf)

        print("Task marked as done.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid task number.")

if __name__ == "__main__":
    while True:
        print("1. Add Todo")
        print("2. Mark a task as done")
        print("3. Exit")
        user_choice = input("Please enter a number between 1 to 3: ")

        if user_choice == "1":
            task_text = input("Please enter what you want to add to your list: ")
            add_task({"task": task_text, "done": False})
        elif user_choice == "2":
            mark_a_task_done()
        elif user_choice == "3":
            print("Exiting the app.")
            break
