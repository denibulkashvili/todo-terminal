import redis
from colors import CEND, CGREEN, CRED

# redis connetion
r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)


def check_if_redis_available():
    """Check if there's an establish connection to redis"""
    try:
        r.ping()
        return True
    except Exception as e:
        print(e)
        return False


def save_tasks_to_redis(task_list):
    """Save task to redis."""
    try:
        r.delete("todo:task")
        for task in task_list:
            r.lpush("todo:task", task)
        print(CGREEN + "\n\t All unfinished tasks have been saved.",
                        "See you next time!\n" + CEND)
    except Exception as e:
        print(e)
        print(CRED + "\n\t Couldn't save your tasks! Sorry! \n" + CEND)

def load_tasks_from_redis():
    """Load data from redis."""
    loaded_tasks = []
    try:
        loaded_tasks = r.lrange("todo:task", 0, -1)
    except Exception as e:
        print(CRED + e + CEND)
    return loaded_tasks