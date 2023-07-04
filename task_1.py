from celery import Celery
import math

app = Celery('task_1', broker='amqp://guest@localhost//')
app.conf.result_backend = 'rpc://'

@app.task(name='task_1.calculate_pi')
def calculate_pi():
    result = math.pi
    from task_1 import process_result
    process_result(result)
    return result

@app.task(name='task_1.calculate_factorial')
def calculate_factorial(number):
    factorial = math.factorial(number)
    print(f"Факториал числа {number} равен {factorial}")
    return factorial

@app.task(name='task_1.calculate_square')
def calculate_square(number):
    square = number ** 2
    print(f"Квадрат числа {number} равен {square}")
    return square

@app.task(name='task_1.periodic_task')
def periodic_task():
    print("Это периодическая задача, которая выполняется каждые 60 секунд.")

@app.task(name='task_1.process_result')
def process_result(result):
    print("Результат задачи:", result)
