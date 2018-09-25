# A Terminal To-Do App in Python

A ToDo application that lets the user view, add and remove tasks. On removal it will show tasks completed during the current session. And will store all the unfinished tasks in Redis datastore and retirieve it on the next session!
The app uses Redis as a backend, but if for some reason it cannot establish a connection with Redis, it will use a txt file.

## Installation 

* Copy to your machine
```
$ git clone https://github.com/denibulkashvili/todo-terminal.git
$ cd todo-terminal
```
* [Download](https://redis.io/download) and install Redis

* Install [redis-py](https://github.com/andymccurdy/redis-py) package for Python
```
$ pip install redis
```
* Run the app in the terminal
```
$ python todo_app.py
```

## Controls

Press [t] to show all your tasks  
Press [a] to add a new task  
Press [r] to remove a task  
Press [q] to quit the program  

##  Disclaimer

This is a free app. Feel free to use it or parts of it as you wish :)
