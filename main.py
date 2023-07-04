import pytz
from task_1 import calculate_pi
from celery import Celery, shared_task, Task

app = Celery('task_1', broker='amqp://guest@localhost//')
number_of_task = int(input('Выберите тип задания:\n 1 - выполнение фоновой задачи' ))

if number_of_task == 1:
    from task_1 import calculate_pi
    result = calculate_pi.delay()
    print("Task ID:", result.task_id)

else:
    print('0')