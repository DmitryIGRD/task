import pytz
from task_1 import calculate_pi, calculate_factorial, calculate_square, process_result
from celery import Celery, shared_task, Task

app = Celery('task_1', broker='amqp://guest@localhost//')
app.conf.result_backend = 'rpc://'

number_of_task = int(input('Выберите тип задания:\n 1 - выполнение фоновой задачи \n 2 - выполнение пакетной обработки задач(последовательно) \n 3- выполнение пакетной обработки задач(параллельно) \n 4 - выполнение периодических задач \n' ))

if number_of_task == 1:
    @shared_task
    def ExecuteTask():
        result_value = calculate_pi()
        print("Результат задачи:", result_value)
        process_result(result_value)

    ExecuteTask.apply_async()

elif number_of_task == 2:
    numbers = [5, 3, 7, 2]

    class ExecuteTask(Task):
        def run(self, number):
            result_value = calculate_factorial(number)
            print("Результат задачи:", result_value)
            process_result(result_value)

    for number in numbers:
        ExecuteTask().apply_async(args=(number,))

elif number_of_task == 3:
    numbers = [5, 3, 7, 2]
    results = []

    class ExecuteTask(Task):
        def run(self, number):
            result_value = calculate_square(number)
            print("Результат задачи:", result_value)
            process_result(result_value)

    for number in numbers:
        results.append(ExecuteTask().apply_async(args=(number,)))

    for result in results:
        result.get()

elif number_of_task == 4:
    app.conf.beat_schedule = {
        'periodic_task': {
            'task': 'task_1.periodic_task',
            'schedule': 60.0,  # Интервал выполнения задачи (60 секунд)
        }
    }
    app.conf.timezone = pytz.timezone('UTC')
    app.Beat().run()
