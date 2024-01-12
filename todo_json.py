import json

def add_task(task):
    tasks = []  
    try:
        with open("jsondata.json", "r") as jsonf:
            tasks = json.load(jsonf)
    except:
        with open("jsondata.json", "w") as jsonf:
            json.dump(tasks, jsonf)
    tasks.append(task)
    with open("jsondata.json", "w") as jsonf:
        json.dump(tasks, jsonf)

    print("Task Added")

def read_the_task():
    try:
        with open("jsondata.json", "r") as jsonf:
            loaded_file = json.load(jsonf)
        return ("Loaded data:", loaded_file)
    except FileNotFoundError:
        print("File not found. No tasks available.")

def mark_a_task_done():
     tasks = read_the_task()
     for task in tasks:
         task["done"] = True

     with open("jsondata.json", "w") as jsonf:
         json.dump(tasks, jsonf)

if __name__ == "__main__":
    while True: 
        user_choice = input("Please enter a number between 1 to 3: ")
        if user_choice == "1":
            task = input("Please enter what you want to add to your list: ")
            add_task({"task": task, "done": False})
        elif user_choice == "2":
            pass
        elif user_choice == "3":
            print("exit")
            break


