import os
from colors import *
from sys import platform

def clear_screen():
    """Clear the terminal screen."""
    if platform == "win32":
        clear_screen_command = 'cls'
    else:
        clear_screen_command = 'clear'
    return os.system(clear_screen_command)

def show_title():
    """Print title to the screen"""
    clear_screen()
    
    print("\t*************************************************")
    print("\t***  ToDo App - Manage your tasks with ease!  ***")
    print("\t*************************************************")

def get_user_reply():
    """Display actions available for the user and get reply."""
    print(CVIOLET + "\n\t Options:" + CEND)
    print("\t ________")
    print(CVIOLET + "\t Enter [t] to show all your tasks" + CEND)
    print(CVIOLET + "\t Enter [a] to add a new task" + CEND)
    print(CVIOLET + "\t Enter [r] to remove a task" + CEND)
    print(CVIOLET + "\t Enter [q] to quit the program" + CEND)

    return input("\n\t What would you like to do next? ")

def show_tasks(tasks_list):
    """Print the tasks to the screen."""
    print(CBLUE + "\n\t Here are your scheduled tasks for today: " + CEND)
    print("\t ________________________________________ ")
    if tasks_list:
        count = 0 
        for task in tasks_list:
            count += 1
            print(CBLUE + f" \t{count}. {task}" + CEND)
    else:
        print(CRED + "\t You don't have any tasks yet. Print 'add' to add a new task!" + CEND)

def show_finished_tasks(finished_list):
    """Show tasks completed during the current session."""
    if finished_list:
        print(CBLUE + "\n\t Today you completed a lot! Keep it up!" + CEND)
        count = 0 
        for task in finished_list:
            count += 1
            print(CGREY + f" \t{count}. {(task)}" + " - Completed!" + CEND)

def add_task(tasks_list):
    """Adds new task to the list of tasks."""
    new_task = input("\t Enter a new task: ")
    
    if new_task and new_task not in tasks_list:
        tasks_list.append(new_task)
        print(CGREEN + "\n\t You have successfully added a new task! \n",
        "\t Hint: press [t] to see all the tasks." + CEND)
    else:
        print(CRED + "\t Please make sure that you entered the task \n",  
            "\t and that the task is not already in the list!" + CEND)
    
def remove_task(tasks_list):
    """Removes a task specified by user."""
    show_tasks(tasks_list)
    task_number = input("\n\t Enter a number of the task you want to remove: ")
    try:
        if int(task_number) >= 1:  
            removed_task = tasks_list.pop(int(task_number)-1)
            print(CGREEN + "\n\t Your task has been removed!" + CEND)
            return removed_task
        else:
            print(CRED + "\t You must enter a positive number!" + CEND)
    except IndexError:
        print(CRED + "\n\t There's no task with such number." + CEND)
    except ValueError:
        print(CRED + "\n\t Please enter a number." + CEND)
    
def load_tasks_from_file():
    """Load data from a file."""
    loaded_tasks = []
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                loaded_tasks.append(line.strip())
    except Exception as e:
        print(CRED + e + CEND)
    return loaded_tasks
    
def save_tasks_to_file(tasks_list):    
    """Save data from a file."""
    try:
        with open('tasks.txt', 'w') as file:
            for task in tasks_list:
                file.writelines(f"{task}\n")
        print(CGREEN + "\n\t All unfinished tasks have been saved.",
                        "See you next time!\n" + CEND)
    except Exception as e:
        print(e)
        print(CRED + "\n\t Couldn't save your tasks! Sorry! \n" + CEND)