from celery_demos.task1 import add


if __name__ == '__main__':
    for _ in range(10):
        add.delay(_, _)
