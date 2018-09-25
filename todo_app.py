import functions
import redis_backend
# ToDo App is a terminal application that allows a user
#   to enter, view and delete tasks. It remembers previous tasks
#   even after the terminal is closed.

if redis_backend.check_if_redis_available():
    tasks = redis_backend.load_tasks_from_redis()
else:
    tasks = functions.load_tasks_from_file()

finished_tasks = []

user_reply = ''
functions.show_title()

# Loop through tasks allowing a user to enter a new task
while user_reply != 'q':

    user_reply = functions.get_user_reply()
    functions.show_title()

    if user_reply == "t":
        functions.show_tasks(tasks)
        functions.show_finished_tasks(finished_tasks)
    elif user_reply == "a":
        functions.add_task(tasks)
    elif user_reply == "r":
        removed_task = functions.remove_task(tasks)
        finished_tasks.append(removed_task)
    elif user_reply == "q":
        if redis_backend.check_if_redis_available():
            redis_backend.save_tasks_to_redis(tasks)
        else:
            functions.save_tasks_to_file(tasks)
    else:
        print("\n\t Please select a command from the Options")
    
    
    