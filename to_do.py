import csv

# todo list aplication

tasks = [
    {"name": "visit hamada", "completed": False},
    {"name": "go to gyme", "completed": True},
    {"name": "visit ali", "completed": False},
]


# run the programe
def main():
    # showing user choices
    message = (
        ("=" * 30)
        + """\n1- add tasks
2- mark task as complete
3- view tasks
4- quit"""
    )

    while True:
        print(message)
        choice = input("pick a choice between 1 and 4 please: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("please chose a valid choice: ")


# add taskb
def add_task():
    tsk = input("write your task please: ")
    task_info = {"name": tsk, "completed": False}
    tasks.append(task_info)
    print("task aded successfully!")


# mark task as complete
def mark_complete():
    incompleted_tasks = [task for task in tasks if not task["completed"]]
    if not incompleted_tasks:
        print("no task to mark as complete")
        return
    for i, task in enumerate(incompleted_tasks):
        print(f"{i+1}- {task['name']}")
    print("-" * 30)
    try:
        user_choice = int(input("choose task to mark as complete: "))
        if user_choice < 1 or user_choice > len(incompleted_tasks):
            print("invalid task number ")
            return

        incompleted_tasks[user_choice - 1]["completed"] = True
        print("task  marked as complete successfuly! ")
    except ValueError:
        print("invalid choice please enter a number")


# view tasks
def view_tasks():
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{i + 1}. {task['name']} {status}")


main()
