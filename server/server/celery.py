import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='America/Lima',
    enable_utc=True,
)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()