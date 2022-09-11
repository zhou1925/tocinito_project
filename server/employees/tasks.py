from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task


app = Celery()

logger = get_task_logger(__name__)

