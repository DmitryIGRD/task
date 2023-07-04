from celery import Celery
import math

app = Celery('task_1', broker='amqp://guest@localhost//')
app.conf.result_backend = 'rpc://'

@app.task(name='task_1.calculate_pi')
def calculate_pi():
    return math.pi