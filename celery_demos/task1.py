import time

from celery import Celery


app = Celery('tasks', broker='amqp://guest@127.0.0.1//')


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
