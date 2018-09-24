import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def save_tasks_to_redis(task):
    pass