from celery import Celery

app = Celery('hello_celery', broker='amqp://localhost')

@app.task
def add(x, y):
    return x + y

