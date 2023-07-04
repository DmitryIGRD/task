from datetime import timedelta
from celery import Celery

app = Celery('task_1', broker='amqp://localhost')

# Настройка результата выполнения задач
app.conf.result_backend = 'cache'  # Использование встроенного backend cache
app.conf.cache_backend = 'memory'  # Использование памяти в качестве хранилища
app.conf.worker_redirect_stdouts = False

# Определение периодической задачи
beat_schedule = {
    'periodic_task': {
        'task': 'tasks.periodic_task',
        'schedule': timedelta(seconds=60),  # интервал выполнения задачи - 60 секунд
    },
}

timezone = 'UTC'